### Reverse a string
#### "adam is cool" "looc si mada"

from stack import Stack

reverse = 'adam is cool'
rev_stack = Stack()

for i in range(len(reverse)):
    rev_stack.push(reverse[i])

res = ''
while rev_stack.size() > 0:
    res += rev_stack.pop()


