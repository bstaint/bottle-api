import redis
from bottle import route, default_app

from settings import *
from libs.pythonwhois.net import get_whois_raw
from libs.pythonwhois.shared import WhoisException


pool = redis.ConnectionPool(**DB_CONF)
r = redis.StrictRedis(connection_pool=pool)

def required_token(func):
    def check_token(**kwargs):
        if r.exists(DB_PRE_TOKEN % kwargs['token']):
            return func(**kwargs)
        else:
            return 'Unauthenticated!'
    return check_token


@route('/whois/<token>/<domain>')
@required_token
def whois(token, domain):
    raw = r.get(DB_PRE_WHOIS % domain)
    if raw: return raw

    try:
        raw = get_whois_raw(domain)[0]
        r.setex(DB_PRE_WHOIS % domain, WHOIS_EXPIRE, raw)
        r.incr(DB_PRE_TOKEN % token)
        return raw
    except WhoisException, e:
        return e


application=default_app()
