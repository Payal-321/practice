class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into the stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"{item} popped from the stack.")
            return item
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def size(self):
        return len(self.stack)

# Testing the Stack class
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(50)
    my_stack.push(60)
    my_stack.push(70)
    print(f"Top of the stack: {my_stack.peek()}")
    print(f"Size of the stack: {my_stack.size()}")
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()  # Attempt to pop from an empty stack
