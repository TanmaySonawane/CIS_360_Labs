# Tanmay Sonawane CIS 360 Lab 06
# 10/29/24

import random

class Heap:
    def __init__(self):
        self.S = [None]
        self.heapsize = 0
        
    def siftdown (self, i):
        spotfound = False
        siftkey = self.S[i]
        parent = i
        largerchild = 0
        
        while 2*parent <=self.heapsize and not spotfound:
            if 2*parent < self.heapsize and self.S[2*parent] < self.S[2*parent + 1]:
                largerchild = 2*parent + 1
            else:
                largerchild = 2*parent
            if siftkey < self.S[largerchild]:
                self.S[parent] = self.S[largerchild]
                parent = largerchild
            else:
                spotfound = True
                
        self.S[parent] = siftkey
        
    def makeheap (self, elements):
        n = len(elements)
        self.S = [None] + elements
        self.heapsize = n
        for i in range(n//2, 0, -1):
            self.siftdown(i)
            
    def removekeys(self, elements):
        sorted_elements = []
        for _ in range(len(elements)):
            sorted_elements.append(self.root())
        
        return sorted_elements[::-1]
            
    def root (self):
        if self.heapsize < 1:
            raise IndexError("Heap is empty")

        keyout = self.S[1]
        self.S[1] = self.S[self.heapsize]
        self.heapsize -= 1
        self.siftdown(1)
        
        return keyout
    
    def heapsort(self, elements):
        self.makeheap(elements)
        return self.removekeys(elements)

def main():
    
    heap = Heap()
    heap.makeheap([random.randint(0,20) for _ in range(20)])
    print(heap.S[1:heap.heapsize+1])
    
    elements = [random.randint(0, 200) for _ in range(200)]
    elements2 = [random.randint(0, 500) for _ in range(500)]
    
    sorted_elements = heap.heapsort(elements)
    print("Sorted elements:", sorted_elements)
    print("\n")
    sorted_elements2 = heap.heapsort(elements2)
    print("Sorted elements2:", sorted_elements2)
    
if __name__ == "__main__":
    main()