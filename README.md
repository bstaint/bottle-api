bottle 自建API
==================
------------------

#### Whois: ####

基于pythonwhois模块(稍微做部分变动)，由于本地可能失败，所以搭建该接口作为备用选项。

可以搭建到openshift上。


### Requires ###

* redis-py (pip install redis)


### Use ###
redis-cli:
``` shell 
set "TOKEN:token"
```

python code:
``` python
from pythonwhois.parse import parse_raw_whois

req = requests.get('http://localhost/whois/token/domain.com') 
resp = parse_raw_whois([req.content])

```
