import sys
from math import ceil,log2
  
INT_MAX = sys.maxsize

class RMQSegment():

    def __init__(self, vector):
        self.vector = vector
        self.n = len(vector)

    def minVal(self, x, y) : 
        return x if (x < y) else y 

    def getMid(self, s, e) : 
        return s + (e - s) // 2

    def RMQUtil(self, start_seg, end_seg, x, y, index) : 
        # part of the given range 
        if (x <= start_seg and y >= end_seg) : 
            return self.seg_tree[index]    
        # outside of the given range  
        if (end_seg < x or start_seg > y) : 
            return INT_MAX 
        # overlap with the given range  
        mid = self.getMid(start_seg, end_seg)  
        return self.minVal(self.RMQUtil(start_seg, mid, x, y, 2 * index + 1),
            self.RMQUtil(mid + 1, end_seg, x, y, 2 * index + 2))

    def constructSTUtil(self, start_seg, end_seg, current) : 
        if (start_seg == end_seg) : 
      
            self.seg_tree[current] = self.vector[start_seg]  
            return self.vector[start_seg]  
  
        mid = self.getMid(start_seg, end_seg)  
        self.seg_tree[current] = self.minVal(self.constructSTUtil(start_seg, mid, current * 2 + 1),
                        self.constructSTUtil(mid + 1, end_seg, current * 2 + 2))  
        return self.seg_tree[current] 

    def constructST(self) : 
      
        # Allocate memory for segment tree  
      
        # Height of segment tree  
        x = (int)(ceil(log2(self.n)))  
      
        # Maximum size of segment tree  
        max_size = 2 * (int)(2**x) - 1  
       
        self.seg_tree = [0] * (max_size)  
      
        # Fill the allocated memory st  
        self.constructSTUtil(0, self.n - 1, 0)  
      
        # Return the constructed segment tree  
        return self.seg_tree
    
    def preprocess(self):
        self.seg_tree = self.constructST()
    
    def RMQ(self, x, y):
        return self.RMQUtil(0, self.n - 1, x, y, 0) 
