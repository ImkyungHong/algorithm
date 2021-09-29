# stack이든 queue든 배열로 잡는 것. 
# 초기화된 상태 
size = 5
queue = [None for _ in range(size)]
front = rear = -1

rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'

print('<--', queue, '<--')

front += 1
data = queue[front]
queue[front] = None
print('입장손님:', data)
front += 1
data = queue[front]
queue[front] = None
print('입장손님:', data)
front += 1
data = queue[front]
queue[front] = None
print('입장손님:', data)

print('<--', queue, '<--')
