#!/usr/bin/python

# redis db config
DB_CONF = {
    'host': '',
    'port': 6379,
    'db': 0
}

# redis key namespace
DB_PRE_WHOIS = 'WHOIS:%s'
DB_PRE_TOKEN = 'TOKEN:%s'

# WHOIS data expried
WHOIS_EXPIRE = 2592000
