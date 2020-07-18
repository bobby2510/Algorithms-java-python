# creation of the node
class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

# creation of the single linked list 
class SingleLinkedList:
    def __init__(self):
        self.root=None
    def add(self,data):
        temp_node=Node(data)
        if self.root == None:
            self.root=temp_node
        else:
            p=self.root
            while p.link != None:
                p=p.link
            p.link=temp_node
        print(data,' is inserted successfully!')
    def print_list(self):
        if self.root == None:
            print('list is empty!')
        else:
            p=self.root
            print('List : ',end='')
            while p != None:
                print(p.data,end=" ")
                p=p.link
            print('')       
    def remove(self,data):
        # this function basically removes the first valid node(i mean if value of the node is eqaul to the data arguement)
        if self.root == None:
            print(data,' is already not existed!')
        else:
            p=self.root
            q=p
            while p != None:
                if p.data == data:
                    break
                q=p
                p=p.link
            if p == None:
                print(data,' is already not existed!')
            elif p == self.root:
                self.root=p.link
                p.link=None
                del p
                print(data,' is removed successfully!')
            else:
                q.link=p.link
                p.link=None
                del p
                print(data,' is removed successfully!')
    def reverse_single_linked_list(self):
        if self.root == None:
            print('list is empty!')
        else:
            p=None
            q=self.root
            r=q.link
            while r != None:
                q.link=p
                p=q
                q=r
                r=q.link
            q.link=p
            self.root=q
            print('list is reversed successfully!')
def main():
    s_list=SingleLinkedList()
    s_list.add(1)
    s_list.add(2)
    s_list.add(3)
    s_list.add(4)
    s_list.add(5)
    s_list.print_list()
    s_list.remove(1)
    s_list.print_list()
    s_list.reverse_single_linked_list()
    s_list.print_list()
    s_list.add(6)
    s_list.add(7)
    s_list.print_list()
    s_list.reverse_single_linked_list()
    s_list.print_list()
    s_list.remove(6)
    s_list.print_list()
# starting of the main function
main()
