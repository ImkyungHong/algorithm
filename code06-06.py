## 함수 선언부 
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    #스택이 꽉 찾으면 꽉 찼다는 메시지 출력하고 종료
    if (isStackFull()):
        print('스택 꽉!')
        return
    #아니라면 스택에 데이터 넣기 
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1):
        return True
    else:
        return False

        
def pop():
    global SIZE, stack, top
    #스택이 비었는지 확인. 메시지 출력 후 끝
    if (isStackEmpty()):
        print('스택 텅!')
        return None
    #안비었으면 데이터추출해서 반환 
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

## 전역 변수부
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 


## 메인코드부
# stack = ['커피', '녹차', '꿀물', '콜라', '환타']
# top = 4
# print('스택 꽉?', isStackFull())

push('커피1')
push('커피2')
print(stack)

data = pop()
print(data)
data = pop()
print(data)
data = pop()
print(data)
print(stack)