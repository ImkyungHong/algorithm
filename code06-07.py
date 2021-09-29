##함수 선언
def isStackFull():
    global size, stack, top 
    if (top == size -1):
        return True
    else:
        return False

def isStackEmpty():
    global size, stack, top 
    if (top == -1):
        return True
    else:
        return False

def push(data):
    global size, stack, top 
    if (isStackFull()):
        return
    top += 1
    stack[top] = data

def pop():
    global size, stack, top 
    if (isStackEmpty()):
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

## 전역 변수
# 초기값(빈 스택)
size = 5
stack = [None for _ in range(size)]
top = -1

## 메인코드 
# 데이터 6건 입력, 확인 / 빼기, 확인 
