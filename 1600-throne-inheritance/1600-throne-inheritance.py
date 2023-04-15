class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.inheritance = defaultdict(list)
        self.dead = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = [[]]
        self.dfs(self.kingName, res)
        
        return res[0]
    
    def dfs(self,name, res):
        if name not in self.dead:
            res[0].append(name)
        
        for child in self.inheritance[name]:
            self.dfs(child,res)
                
        return
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()