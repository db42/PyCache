'''
Created on 15-Mar-2012

@author: dushyant
'''

class Elem(object):
    """ This class corresponds to element of Cache. Can be further modified to extend this cache """
    
    def __init__(self, value):
        self.value = value
        self.evict_status = True #Ready to evict

    def getValue(self):
        return self.value
    
    def setEvictStatus(self, status):
        self.evict_status = status
    
    def getEvictStatus(self):
        return self.evict_status
    
class Cache(object):
    """ Base class for Cache object """
    def __init__(self, size):
        self.hash_db = {}
        self.size = size
        
    def beginRead(self, key):
        """ Return the value corresponding to key from the cache. If key is not present, throws exception"""
        if self.hash_db.has_key(key):
            elem = self.hash_db[key]
        else:
            raise LookupError
        elem.setEvictStatus(False)
        return elem.getValue()
    
    def endRead(self, key):
        """ Return None. If key is not present, throws exception. Now, entry corresponding to key can be evicted from the cache """
        if self.hash_db.has_key(key):
            self.hash_db[key].setEvictStatus(True)
        else:
            raise LookupError
        return
    
    def write(self, key, value):
        """ Write (key,value) into the cache """
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
