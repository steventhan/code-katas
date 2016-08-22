from stack import Stack


def check_parentheses(string):
    """Check string for proper parenthetics"""
    my_stack = Stack()
    for char in string:
        if char == '(':
            my_stack.push(char)
        elif char == ')':
            try:
                my_stack.pop()
            except IndexError:
                return -1
    if len(my_stack) == 0:
        return 0
    else:
        return 1
