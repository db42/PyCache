# PyCache

Object cache implementation in python

### Dependency

All you need is python installed on your system and you are ready to go. However, you will need to install one python module - nose for testing.


```
easy_install nose
```

### Running

```
from cache import Cache

#cache of entries size = 10
cache = Cache(size = 10)

#basic write operation
cache.write(key = "key1",value = "value1")
cache.write("key2", "value2")

#basic read operation
value =  cache.beginRead("key1")
print value

#doesn not return anything
cache.endRead("key1")

return
```
Or, just run
```
python cache.py
```

### Testing

```
cd path/to/PyCache
nosetests
```
