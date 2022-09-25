class SnapshotArray:

    def __init__(self, length: int):
        self.array = [{} for _ in range(length)]
        self.id = 0
        self.length = length
        

    def set(self, index: int, val: int) -> None:
        self.array[index][self.id] = val
    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.array[index]:
            return self.array[index][snap_id]
        timelist = list(self.array[index].keys())
        snap_id = bisect.bisect_left(timelist,snap_id) - 1
        if snap_id == -1:
            return 0
        return self.array[index][timelist[snap_id]]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)