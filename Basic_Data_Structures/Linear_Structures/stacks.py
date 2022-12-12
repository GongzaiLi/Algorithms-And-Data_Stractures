"""
- Stacks some time called a "push-down stack"
- an ordered collection
- add and remove always takes place at the same end.
- LIFO last-in first-out
- In a cafeteria has a stack of trays or plates
"""
"""
Application:
- web browser has Back button. As you from web page to web page, those pages are placed on a stack.
- keep website history
"""

"""
Stack Abstract Data Type
- Stack()
- push(item)
- pop()
- peek()
- is_empty()
- size()
"""


class Stack:
    """
    Stack Bottom
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # O(1)

    def pop(self):
        return self.items.pop()  # O(1)

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class StackTop:
    """
    Stack Top
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)  # O(n)

    def pop(self):
        return self.items.pop(0)  # O(n)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def revstring(mystr):
    s: Stack = Stack()
    for i in mystr:
        s.push(i)

    rev = []
    for i in range(s.size()):
        rev.append(s.pop())

    return ''.join(rev)


from helper.utils import testEqual
if __name__ == '__main__':
    s = StackTop()

    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    testEqual(revstring('apple'), 'elppa')
    testEqual(revstring('x'), 'x')
    testEqual(revstring('1234567890'), '0987654321')
