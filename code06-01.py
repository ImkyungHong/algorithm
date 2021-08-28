#stack 초기화
stack = [None, None, None, None, None]
top = -1

# push
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'

print(stack)

# pop한 뒤 사용해야 하는거 = data
data = stack[top]
stack[top] = None
top -= 1
print('Pop--->', data)

data = stack[top]
stack[top] = None
top -= 1
print('Pop--->', data)

data = stack[top]
stack[top] = None
top -= 1
print('Pop--->', data)

print(stack)