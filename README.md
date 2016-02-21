bottle Whois API
==================
------------------

#### Whois ####

基于pythonwhois模块(稍微做部分变动)，由于本地可能失败，所以搭建该接口作为备用选项。

可以搭建到openshift上。


### Requires ###

* bottle (pip install bottle)
* redis-py (pip install redis)


### Use ###
redis-cli:
``` shell 
set "TOKEN:token" 0
```

python code:
``` python
from pythonwhois.parse import parse_raw_whois

req = requests.get('http://localhost/whois/token/domain.com') 
resp = parse_raw_whois([req.content])

```

### Tip ###

编译出现：
```
/var/lib/openshift/{{ directory_hash }}/python//bin/install: line 10: version: unbound variable
make: *** [install-whois] Error 1
```
解决办法，临时把PATH变量中关于python的内容删除。
