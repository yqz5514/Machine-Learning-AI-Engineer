# 创建动态数组
# 不用显式指定数组大小，它会根据实际存储的元素数量自动扩缩容
arr = []

for i in range(10):
    # 在末尾追加元素，时间复杂度 O(1)
    arr.append(i)

# 在中间插入元素，时间复杂度 O(N)
# 在索引 2 的位置插入元素 666
arr.insert(2, 666)

# 在头部插入元素，时间复杂度 O(N)
arr.insert(0, -1)

# 删除末尾元素，时间复杂度 O(1)
arr.pop()

# 删除中间元素，时间复杂度 O(N)
# 删除索引 2 的元素
arr.pop(2)

# 根据索引查询元素，时间复杂度 O(1)
a = arr[0]

# 根据索引修改元素，时间复杂度 O(1)
arr[0] = 100

# 根据元素值查找索引，时间复杂度 O(N)
index = arr.index(666)


# dynamic array 
class MyArrayList:
    # 默认初始容量
    INIT_CAP = 1

    def __init__(self, init_capacity=None):
        self.data = [None] * (init_capacity if init_capacity is not None else self.__class__.INIT_CAP)
        self.size = 0
    
    # 增
    def add_last(self, e):
        cap = len(self.data)
        # 看 data 数组容量够不够
        if self.size == cap:
            self._resize(2 * cap)
        # 在尾部插入元素
        self.data[self.size] = e
        self.size += 1

    def add(self, index, e):
        # 检查索引越界
        self._check_position_index(index)

        cap = len(self.data)
        # 看 data 数组容量够不够
        if self.size == cap:
            self._resize(2 * cap)

        # 搬移数据 data[index..] -> data[index+1..]
        # 给新元素腾出位置
        for i in range(self.size-1, index-1, -1):
            self.data[i+1] = self.data[i]
        
        # 插入新元素
        self.data[index] = e

        self.size += 1

    def add_first(self, e):
        self.add(0, e)

    # 删
    def remove_last(self):
        if self.size == 0:
            raise NoSuchElementException
        cap = len(self.data)
        # 可以缩容，节约空间
        if self.size == cap // 4:
            self._resize(cap // 2)

        deleted_val = self.data[self.size - 1]
        # 删除最后一个元素
        self.data[self.size - 1] = None
        self.size -= 1

        return deleted_val

    def remove(self, index):
        # 检查索引越界
        self._check_element_index(index)

        cap = len(self.data)
        # 可以缩容，节约空间
        if self.size == cap // 4:
            self._resize(cap // 2)

        deleted_val = self.data[index]

        # 搬移数据 data[index+1..] -> data[index..]
        for i in range(index + 1, self.size):
            self.data[i - 1] = self.data[i]

        self.data[self.size - 1] = None
        self.size -= 1

        return deleted_val

    def remove_first(self):
        return self.remove(0)

    # 查
    def get(self, index):
        # 检查索引越界
        self._check_element_index(index)

        return self.data[index]

    # 改
    def set(self, index, element):
        # 检查索引越界
        self._check_element_index(index)
        # 修改数据
        old_val = self.data[index]
        self.data[index] = element
        return old_val

    # 工具方法
    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # 将 data 的容量改为 newCap
    def _resize(self, new_cap):
        temp = [None] * new_cap
        for i in range(self.size):
            temp[i] = self.data[i]
        self.data = temp

    def _is_element_index(self, index):
        return 0 <= index < self.size

    def _is_position_index(self, index):
        return 0 <= index <= self.size

    def _check_element_index(self, index):
        if not self._is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def _check_position_index(self, index):
        if not self._is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def display(self):
        print(f"size = {self.size}, cap = {len(self.data)}")
        print(self.data)


# Usage example
if __name__ == "__main__":
    arr = MyArrayList(init_capacity=3)

    # 添加 5 个元素
    for i in range(1, 6):
        arr.add_last(i)

    arr.remove(3)
    arr.add(1, 9)
    arr.add_first(100)
    val = arr.remove_last()

    # 100 1 9 2 3
    for i in range(arr.size):
        print(arr.get(i))