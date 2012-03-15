'''
Created on 15-Mar-2012

@author: dushyant
'''

class Elem(object):
    """ This class corresponds to element of Cache """
    NOT_READY = 0
    READY_EVICT = 1
    
    def __init__(self, value):
        self.value = value
        self.evict_status = Elem.READY_EVICT

class Cache(object):
    """ Base class for Cache object """
    def __init__(self, size):
        self.hash_db = {}
        self.size = size
        
    def beginRead(self, key):
        """ Return the value corresponding to key from the cache. If key is not present, throws exception"""
        try:
            elem = self.hash_db[key]
        except KeyError:
            raise Exception("KeyNotFoundError")
        elem.evict_status = Elem.NOT_READY
        return elem.value
    
    def endRead(self, key):
        """ Return None. If key is not present, throws exception. Now, entry corresponding to key can be evicted from the cache """
        try:
            self.hash_db[key].evict_status = Elem.READY_EVICT
        except KeyError:
            raise Exception("KeyNotFoundError")
        return
    
    def write(self, key, value):
        """ Write (key,value) into the cache """
        self.hash_db[key] = Elem(value)
        
        #if size exceeds cache_size
        if (len(self.hash_db) > self.size):
            self.__evictEntry()
    
    def __evictEntry(self):
        keys = [key for key in self.hash_db.keys() if self.hash_db[key].evict_status]
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
    cache.endRead("key2")
    
    return


if __name__ == "__main__":
    main()