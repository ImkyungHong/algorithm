##함수 선언부 
class Node() :
    def __init__(self):         #생성자로 그냥 쓰는거 
        self.data = None        #처음이니까 none
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while (current.link != None):       #current link가 없으면 끝나 
        current = current.link
        print(current.data, end=' ')
    print()
def insertNode(findData, insertData) :
    global memory, head, current, pre
    if head.data == findData: # 첫번째 노드 앞에 삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node 
            memory.append(node)
            return
    node = Node()   #마지막 노드에 삽입 
    node.data = insertData
    current.link = node
    memory.append(node)

def deleteNode(deleteData):
    global memory, head, current, pre
    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return
    current = head
    while current.link != None:
        pre = current 
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def findNode(findData):
    global memory, head, current, pre


## 전역 변수부
memory = []         # 노드를 저장할 공간 
head, current, pre = None, None, None        #초기화 
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부 

node = Node()       #첫번째 노드 
node.data = dataArray[0]
head = node
memory.append(node)

# 두번째 부터는 반복문으로 
for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
printNodes(head)

# insertNode('다현', '화사')
# printNodes(head)
# insertNode('사나', '솔라')
# printNodes(head)
# insertNode('재남', '문별')
# printNodes(head)

deleteNode('다현')
printNodes(head)
deleteNode('쯔위')
printNodes(head)
deleteNode('재남')
printNodes(head)

