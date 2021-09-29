##함수 
# def isQueueFull():
#     global size, queue, front, rear
#     if (rear >= size -1):
#         return True
#     else:
#         return False
## 24페이지
def isQueueFull():
    global size, queue, front, rear
    if(rear != size-1):
         return False
    elif(rear == size-1) and (front == -1):
        return True
    else:
        for i in range(front+1, size):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False


def isQueueEmpty():
    global size, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

def enQueue(data):
    global size, queue, front, rear
    if (isQueueFull()) :
        print('Queueisfull')
        return
    rear += 1
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data
    
## 전역
size = 5
queue = [None for _ in range(size)]
front = rear = -1

## 메인 
# queue = ['커피', '녹차', '꿀물', '환타', '콜라']
# front = -1
# rear = 4

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('<--', queue, '<--')

data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)
print('<--', queue, '<--')

enQueue('재남')
enQueue('강아지')
print('<--', queue, '<--')