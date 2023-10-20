# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.flattened_list = [] 
        self.index = 0  
        self.flatten(nestedList) 

  
    def flatten(self, nested_list):
        for nested_int in nested_list:
            if nested_int.isInteger():
                self.flattened_list.append(nested_int.getInteger())  # If it's an integer, add it to the list.
            else:
                self.flatten(nested_int.getList())  

    def next(self):
        value = self.flattened_list[self.index] 
        self.index += 1  
        return value

    def hasNext(self):
        return self.index < len(self.flattened_list) 
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())