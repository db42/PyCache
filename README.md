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
### Notes

#### 1. GIL in CPython
Though dictionary accesses are thread-safe in CPython due to Global Interpreter Lock, I have used a lock to protect dict to make this code implementation independent. 
http://effbot.org/pyfaq/what-kinds-of-global-value-mutation-are-thread-safe.htm


```
""" Write (key,value) into the cache """
with self.hash_db_lock:
	self.hash_db[key] = Elem(value)
```

#### 2. Assumption of correct usage of endRead() function
Here, I have assumed that the application using this object cache will make a single call to endRead() corresponding to every beginRead() call.

Usage:
```
self.cache.write("test_key", "test_value")

print self.cache.beginRead("test_key")

self.cache.endRead("test_key")
self.cache.endRead("test_key") #Not allowed
```
