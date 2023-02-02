class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_begining(self,data):
        new_node = Node(data, self.head)
        self.head = new_node
    
    def print(self):
        if self.head is None:
            print("Empty list")
            return
        ptr = self.head
        while(ptr):
            print(ptr.data, end=" ")
            ptr = ptr.next
    
    def insert_at_end(self, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            return
        new_node = Node(data)
        itr = self.head

        while(itr.next):
            itr = itr.next
        itr.next = new_node
    def insert_values(self,val_list):

        for data in val_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head

        while(itr):
            count += 1
            itr = itr.next
        return count

    def remove_at_index(self, index):
        if index <0 or index >= self.get_length():
            raise Exception("Index Out of Bounds")

        count = 0
        itr = self.head
        while(itr):
            if count == index -1 :
                itr.next = itr.next.next
            count += 1 
            itr = itr.next


    def insert_at_index(self,index, data):
        if index <0 or index>self.get_length():
            raise Exception("Index out of bounds")
        
        if index == 0:
            self.insert_at_begining(data)
        else:
            count = 0
            itr = self.head
            while(itr):
                if count == index-1:
                    new_node = Node(data, itr.next)
                    itr.next = new_node
                count +=1
                itr = itr.next


if __name__ == '__main__':
    ll = linkedlist()
    ll.insert_at_end(3)
    ll.insert_at_end(7)
    #ll.print()

    ll1 = linkedlist()
    ll1.insert_values(["cat", "dog", "rat"])
    #ll1.print()
    ctr = ll1.get_length()
    ##print(ctr)

    ll2 = linkedlist()
    ll2.insert_values([1,3,4,5,67,8,2,32,54,2,7])
    print("Before Elements")
    ll2.print()
    ll2.remove_at_index(7)
    print("/n After Elements")
    ll2.print()
    print("Now doing for new ll \n")

    ll3 = linkedlist()
    ll3.insert_values([3,5,7])
    ll3.print()
    print("\n")
    ll3.insert_at_index(3, 66)
    ll3.print()





    