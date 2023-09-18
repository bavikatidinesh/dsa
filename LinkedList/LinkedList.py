class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        current = Node(data, self.head)
        self.head = current

    def insert_last(self, data):
        current = Node(data)
        if self.head is None:
            self.head = current
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = current

    def print(self):
        if self.head is None:
            print("No Data in the LL")
            return

        iterator = self.head
        itr_str = ""
        while iterator:
            itr_str = itr_str + "======>" + iterator.data
            iterator = iterator.next

        print(itr_str)

    def insert_after(self, element_after, new_element):
        if self.head is None:
            print("no element in the LL")
            return
        iterator = self.head
        flag = False
        while iterator:
            if iterator.data == element_after:
                iterator.next = Node(new_element, iterator.next)
                flag = True
                break
            iterator = iterator.next

        if flag:
            print("new element inserted")
        else:
            print("element not found in the LL")


l = LinkedList()
l.insert_last("dyne")
l.insert_last("raj")
l.insert_last("jhon")
l.insert_last("chris")
l.insert_last("jo")
l.insert_last("ramu")
l.print() # ======>dyne======>raj======>jhon======>chris======>jo======>ramu
l.insert_start("sam")
l.insert_start("tom")
l.print() # ======>tom======>sam======>dyne======>raj======>jhon======>chris======>jo======>ramu
l.insert_after("dyne", "dyne2")
l.print() # ======>tom======>sam======>dyne======>dyne2======>raj======>jhon======>chris======>jo======>ramu