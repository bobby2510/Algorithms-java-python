# stack node ( we are likely using doubly linked list here )
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
# stack
class Stack:
    def __init__(self):
        self.root=None
        self.top=None
    def push(self,data):
        temp=Node(data)
        if self.root == None:
            self.root=temp
            self.top=temp
        else:
            temp.left=self.top
            self.top.right=temp
            self.top=temp
        print(data, 'is pushed successfully!')
    def peek(self):
        if self.root == None:
            return -1
        else:
            return self.top.data
    def pop(self):
        if self.root == None:
            print('stack is empty!')
        else:
            if self.root == self.top:
                p=self.root
                self.root=None
                self.top=None
                del p
            else:
                self.top=self.top.left
                p=self.top.right
                self.top.right=None
                p.left=None
                del p
            print('Element is poped successfully!')
    def print_stack(self):
        if self.root == None:
            print('stack is empty!')
        else:
            print('stack data : ',end='')
            p=self.root
            while p != None:
                print(p.data,end=' ')
                p=p.right
            print('')
 def main():
    stack=Stack()
    stack.print_stack()
    stack.pop()
    print(stack.peek())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    print(stack.peek())
if __name__ == '__main__':
    main()
