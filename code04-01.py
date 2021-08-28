class Node() :
    def __init__(self):         #생성자로 그냥 쓰는거 
        self.data = None        #처음이니까 none
        self.link = None

node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

# 쯔위, 사나, 지효 
node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# print(node1.data, end=' ')
# print(node1.link.data, end=' ')
# print(node1.link.link.data, end=' ')
# print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')

# 위의 내용을 반복문으로 처리 
current = node1
print(current.data, end=' ')
while (current.link != None):       #current link가 없으면 끝나 
    current = current.link
    print(current.data, end=' ')
