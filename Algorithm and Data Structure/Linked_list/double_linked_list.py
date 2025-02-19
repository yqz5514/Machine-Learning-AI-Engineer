class DoublyListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
        
def createDoublyLinkedList(arr: List[int]) -> Optional[DoublyListNode]:
    if not arr:
        return None
    
    head = DoublyListNode(arr[0])
    cur = head
    
    # for 循环迭代创建双链表
    for val in arr[1:]:
        new_node = DoublyListNode(val)
        cur.next = new_node
        new_node.prev = cur
        cur = cur.next
    
    return head



## search / change
# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])
tail = None

# 从头节点向后遍历双链表
p = head
while p:
    print(p.val)
    tail = p
    p = p.next

# 从尾节点向前遍历双链表
p = tail
while p:
    print(p.val)
    p = p.prev


## add

## 在双链表头部插入元素，需要调整新节点和原头节点的指针：

# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])

# 在双链表头部插入新节点 0
new_head = DoublyListNode(0)
new_head.next = head
head.prev = new_head
head = new_head
# 现在链表变成了 0 -> 1 -> 2 -> 3 -> 4 -> 5


## 在双链表尾部插入元素时，如果我们持有尾节点的引用
# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])

tail = head
# 先走到链表的最后一个节点
while tail.next is not None:
    tail = tail.next

# 在双链表尾部插入新节点 6
newNode = DoublyListNode(6)
tail.next = newNode
newNode.prev = tail
# 更新尾节点引用
tail = newNode

# 现在链表变成了 1 -> 2 -> 3 -> 4 -> 5 -> 6


## 在双链表尾部插入元素时，如果我们持有尾节点的引用
# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])

# 在第 3 个节点后面插入新节点 66
# 找到第 3 个节点
p = head
for _ in range(2):
    p = p.next

# 组装新节点
newNode = DoublyListNode(66)
newNode.next = p.next
newNode.prev = p

# 插入新节点
p.next.prev = newNode
p.next = newNode

# 现在链表变成了 1 -> 2 -> 3 -> 66 -> 4 -> 5

## delete

## 在双链表中删除节点时，需要调整前驱节点和后继节点的指针来摘除目标节点：
# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])

# 删除第 4 个节点
# 先找到第 3 个节点
p = head
for i in range(2):
    p = p.next

# 现在 p 指向第 3 个节点，我们将它后面的那个节点摘除出去
toDelete = p.next

# 把 toDelete 从链表中摘除
p.next = toDelete.next
toDelete.next.prev = p

# 把 toDelete 的前后指针都置为 null 是个好习惯（可选）
toDelete.next = None
toDelete.prev = None

# 现在链表变成了 1 -> 2 -> 3 -> 5

## 在双链表头部删除元素需要调整头节点的指针：
# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])

# 删除头结点
toDelete = head
head = head.next
head.prev = None

# 清理已删除节点的指针
toDelete.next = None

# 现在链表变成了 2 -> 3 -> 4 -> 5

## 在双链表尾部删除元素
# 创建一条双链表
head = createDoublyLinkedList([1, 2, 3, 4, 5])

# 删除尾节点
p = head
# 找到尾结点
while p.next is not None:
    p = p.next

# 现在 p 指向尾节点
# 把尾节点从链表中摘除
p.prev.next = None

# 把被删结点的指针都断开是个好习惯（可选）
p.prev = None

# 现在链表变成了 1 -> 2 -> 3 -> 4