# single 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None # only have next pointer for single linked-list


# 输入一个数组，转换为一条单链表
def createLinkedList(arr: 'List[int]') -> 'ListNode':
    if arr is None or len(arr) == 0:
        return None

    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head

# look up / edit
# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 遍历单链表
p = head
while p is not None:
    print(p.val)
    p = p.next

## add
## add item at begining 
# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 在单链表头部插入一个新节点 0 
newHead = ListNode(0)
newHead.next = head
head = newHead
# 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5

## add item at the end
# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 在单链表尾部插入一个新节点 6
p = head
# 先走到链表的最后一个节点
while p.next is not None:
    p = p.next
# 现在 p 就是链表的最后一个节点
# 在 p 后面插入新节点
p.next = ListNode(6)

# 现在链表变成了 1 -> 2 -> 3 -> 4 -> 5 -> 6

## insert item in the middle
# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 在第 3 个节点后面插入一个新节点 66
# 先要找到前驱节点，即第 3 个节点
p = head
for _ in range(2):
    p = p.next
# 此时 p 指向第 3 个节点
# 组装新节点的后驱指针
new_node = ListNode(66)
new_node.next = p.next

# 插入新节点
p.next = new_node

# 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5

## delete
## delete a item
# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 在第 3 个节点后面插入一个新节点 66
# 先要找到前驱节点，即第 3 个节点
p = head
for _ in range(2):
    p = p.next
# 此时 p 指向第 3 个节点
# 组装新节点的后驱指针
new_node = ListNode(66)
new_node.next = p.next

# 插入新节点
p.next = new_node

# 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5

## delete last item
# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 删除尾节点
p = head
# 找到倒数第二个节点
while p.next.next is not None:
    p = p.next

# 此时 p 指向倒数第二个节点
# 把尾节点从链表中摘除
p.next = None

# 现在链表变成了 1 -> 2 -> 3 -> 4

## delete first item
# 创建一条单链表
head = createLinkedList([1, 2, 3, 4, 5])

# 删除头结点
#直接把 head 移动到下一个节点就行了
head = head.next

# 现在链表变成了 2 -> 3 -> 4 -> 5