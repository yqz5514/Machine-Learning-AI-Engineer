# arr with 4 items
arr = [0]*10
for i in range(4):
    arr[i] = i

# 1. add an item at the end
arr[4] = 4

# add another item to the end
arr[5] = 5

# 2. insert item in the middle of arr
# insert item 666 at index 2, need to move all items after index2 one position after 
# attention: 注意要倒着遍历数组中已有元素避免覆盖
#在数组中间插入元素的时间复杂度是 O(N)因为涉及到数据搬移，给新元素腾地方
# for i in range(6,2,-1):
#     print(i)
    #arr[i] = arr[i-1]
#arr[2] = 666
#print(arr)
# for i in range(6,2,-1): #6,5,4,3
#     # range(6,2,-1) 是倒着从数字6到2但不包含2， range（6）是 0-5.
#     print(i)


# 3. full array

# 大小为 10 的数组已经装满了
# arr = [i for i in range(10)]

# # 现在想在数组末尾追加一个元素 10
# # 需要先扩容数组
# newArr = [0] * 20

# # 把原来的 10 个元素复制过去
# for i in range(10):
#     newArr[i] = arr[i]

# # 释放旧数组的内存空间
# # ...

# # 在新的大数组中追加新元素
# newArr[10] = 10

# 4. delete last item
# 大小为 10 的数组已经装了 5 个元素
# arr = [0] * 10
# for i in range(5):
#     arr[i] = i

# # 删除末尾元素，暂时用 -1 代表元素已删除
# arr[4] = -1

# 5. delete middle item
# 大小为 10 的数组已经装了 5 个元素
# arr = [0] * 10
# for i in range(5):
#     arr[i] = i

# # 删除 arr[1]
# # 需要把 arr[1] 之后的元素都往前移动一位
# # 注意要正着遍历数组中已有元素避免覆盖，不懂的话请看下方可视化面板
# for i in range(1, 4):
#     arr[i] = arr[i + 1]

# # 最后一个元素置为 -1 代表已删除
# arr[4] = -1