class Stack:


    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, add_element):
        self.stack.append(add_element)

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def stack():
    print(f'{Stack().is_empty()}\n')
    Stack().push(input('Enter new element: '))
    print(f'Last element is: {Stack().pop()}')
    print(f'Last element is: {Stack().peek()}')
    print(f'Total elements: {Stack().size()}')




