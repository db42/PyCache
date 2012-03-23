'''
Created on 15-Mar-2012

@author: dushyant
'''
import threading

class Elem(object):
    """ This class corresponds to element of Cache. Can be further modified to extend this cache """
    
    def __init__(self, value):
        self.value = value
        self.readers_count = 0 #Ready to evict
        self.count_lock = threading.Lock()

    def getValue(self):
        return self.value
    
    def beginRead(self):
        with self.count_lock:
            self.readers_count += 1
    
    def endRead(self):
        with self.count_lock:
            self.readers_count -= 1
            assert self.readers_count >= 0
                    
    def getEvictStatus(self):
        if self.readers_count == 0:
            return True
        else:
            return False
    
class Cache(object):
    """ Base class for Cache object """
    def __init__(self, size):
        self.hash_db = {}
        self.size = size
        self.hash_db_lock = threading.Lock()
        
    def beginRead(self, key):
        """ Return the value corresponding to key from the cache. If key is not present, throws exception"""
        with self.hash_db_lock:
            if self.hash_db.has_key(key):
                elem = self.hash_db[key]
            else:
                raise LookupError
        elem.beginRead()
        return elem.getValue()
    
    def endRead(self, key):
        """ Return None. If key is not present, throws exception. Now, entry corresponding to key can be evicted from the cache """
        with self.hash_db_lock:
            if self.hash_db.has_key(key):
                self.hash_db[key].endRead()
            else:
                raise LookupError
        return
    
    def write(self, key, value):
        """ Write (key,value) into the cache """
        with self.hash_db_lock:
            self.hash_db[key] = Elem(value)
        
            #if size exceeds cache_size
            if (len(self.hash_db) > self.size):
                self.__evictEntry()
    
    def __evictEntry(self):
        keys = [key for key in self.hash_db.keys() if self.hash_db[key].getEvictStatus()]
        key = Cache.__findEntryToEvict(keys)

        #evict
        del self.hash_db[key]

        
    @staticmethod
    def __findEntryToEvict(keys):
        """ Eviction Strategy: Currently, just return the first entry """
        return keys[0]
    
def main():
    #cache of entries size = 10
    cache = Cache(size = 10)
    
    #basic write operation
    cache.write(key = "key1",value = "value1")
    cache.write("key2", "value2")
    
    #basic read operation
    value =  cache.beginRead("key1")
    print value
    
    #doesn't return anything
    cache.endRead("key1")
    
    return


if __name__ == "__main__":
    main()
