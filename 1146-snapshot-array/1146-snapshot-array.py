class SnapshotArray:

    def __init__(self, length: int):
        self.s_id = 0
        self.snap_arr = [[[0,0]] for _ in range(length)]
    def set(self, index: int, val: int) -> None:
        self.snap_arr[index].append([self.s_id, val])

    def snap(self) -> int:
        self.s_id += 1
        return self.s_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.snap_arr[index], [snap_id, 10**9])
        return self.snap_arr[index][snap_index - 1][1]
            
                         
# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)