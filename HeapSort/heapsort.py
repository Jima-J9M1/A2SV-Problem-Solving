class Solution:
    #Function that return the min val
    def heappop(self,heap):
        min_val = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        n = len(heap)
        self.heap_down(heap, 0, n)
        
        return [min_val, heap]
    
    #Function that to build heap from down
    def heap_down(self, heap, current, n):
        right = self.right_child(current)
        left = self.left_child(current)
        
        small_child = current
        
        if left < n and heap[left] < heap[small_child]:
            small_child = left
            
        if right < n and heap[right] < heap[small_child]:
            small_child = right
            
        if small_child != current:
            self.swap(heap, current, small_child)
            self.heap_down(heap, small_child, n)
            
    #return parent position       
    def parent(self,current):
        return (current - 1) // 2
      
    #return left child position  
    def left_child(self,parent):
        return (2*parent + 2)
        
    #return right child position
    def right_child(self,parent):
        return (2*parent + 1)
        
    #swap two elements
    def swap(self,heap,current, node):
        heap[current], heap[node] = heap[node], heap[current]
        
    def heap_up(self,heap, current):
        prnt = self.parent(current)
        
        if current > 0 and heap[current] < heap[prnt]:
            self.swap(heap, current, prnt)
            self.heap_up(heap, prnt)
    
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        heap = []
        
        for ele in arr:
            heap.append(ele)
            current = len(heap) - 1
            self.heap_up(heap, current)
            
        return heap
        # code here
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        heap = self.buildHeap(arr, n)
        # print(heap)
        right = 0
        
        while heap:
            min_val, build_heap = self.heappop(heap)
            arr[right] = min_val
            right += 1
            heap = build_heap
        
            
        
