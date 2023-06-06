def check(string: str):
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    stack = []
    for i in string:
        if i in brackets_open:
            stack.append(i)
        if i in brackets_closed:
            if len(stack) == 0:
                return False
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else: return False
    return (not stack)

while True:
    el = input('Enter symbol: ')
    if not el:
        exit()
    print(check(el))
