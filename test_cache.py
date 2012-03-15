'''
Created on 15-Mar-2012

@author: dushyant
'''
from cache import Cache

SIZE = 10
TEST_SIZE = 15

class TestCache():
    
    def __init__(self):
        self.cache = Cache(SIZE)

    def test_read_write(self):
        #basic write and read
        self.cache.write("test_key", "test_value")
        assert 'test_value' == self.cache.beginRead("test_key")
        
        #beginRead: read key not present
        try:
            self.cache.beginRead("key_not_found")
            assert False
        except:
            assert True
            
        #endRead: read key not present
        try:
            self.cache.endRead("key_not_found")
            assert False
        except:
            assert True
        
    
    def test_eviction(self):
        """ To check an entry is never evicted once beginRead is called """
        self.cache.write("test_key", "test_value")
        value = self.cache.beginRead("test_key")
        
        for i in range(TEST_SIZE):
            self.cache.write(i, i)
        
        try:
            #if evicted, endRead should throw and exception
            self.cache.endRead("test_key")
            assert True
        except:
            assert False
        
        
    def test_size(self):
        #size
        for i in range(TEST_SIZE):
            self.cache.write(i, i)
            
        assert len(self.cache.hash_db) <= SIZE