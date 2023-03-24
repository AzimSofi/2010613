'''
# Create a function that swaps 2 elements in the list using their index number. (3m)
'''

# region NODE CLASS <fold this class>
class Node:
    #CONSTUCTOR
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    #BASIC USER-DEFINED OPERATIONS OF NODE

    def updateData(self,data):
        self.data = data

    def setLink(self,link):
        self.link = link

    def removeLink(self):
        self.link = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.link
# endregion

# region LINKED LIST CLASS <fold this class>
class LL:
    #LL CONSTRUCTOR
    def __init__(self):
        self.head = None

    
    #ADD A NODE TO THE START OF THE LIST
    def addToStart(self,data):
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    #ADD A NODE TO THE END OF THE LIST
    def addToEnd(self,data):
        current = self.head
        if current is None:
            self.addToStart(data)
        else:
            tempNode = Node(data)
            while current.getNext():
                current = current.getNext()
            current.setLink(tempNode)
            del tempNode
        del current

    #CLEARING THE LIST
    def clearList(self):
        self.head = None

    #GET THE LENGTH
    def length(self):
        current = self.head
        if current is None:
            return 0
        else:
            count = 0
            while current:
                count += 1
                current = current.getNext()
            return count
        del current

    #PUSH DATA INTO LIST
    def push(self,data):
        self.addToStart(data)
        #WHAT IT DOES
        # tempNode = Node(data)
        # tempNode.setLink(self.head)
        # self.head = tempNode
        # del tempNode

    #POP DATA FROM THE LIST
    def pop(self):
        tempNode = self.head
        self.head = tempNode.getNext()
        del tempNode

    #ENQUEUE DATA INTO LIST
    def enqueue(self,data):
        self.addToEnd(data)
        #WHAT IT DOES
        # current = self.head
        # if current is None:
        #     self.addToStart(data)
        # else:
        #     tempNode = Node(data)
        #     while current.getNext():
        #         current = current.getNext()
        #     current.setLink(tempNode)
        #     del tempNode
        # del current

    #DEQUEUE DATA FROM THE LIST
    def dequeue(self):
        self.pop()
        #WHAT IT DOES
        # tempNode = self.head
        # self.head = tempNode.getNext()
        # del tempNode

    #DISPLAY THE LINKED LIST
    def displayList(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                print(current.getData(),end=" ")
                current = current.getNext()
                if current:
                    print("-->", end=" ")
        print()
        del current

    #GET THE MAX VALUE
    def max(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            max = current.getData()
            while current.getNext():
                current = current.getNext()
                if current.getData() > max:
                    max = current.getData()
            return max
        del current

    # GET THE MAX VALUE
    def min(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            min = current.getData()
            while current.getNext():
                current = current.getNext()
                if current.getData() < min:
                    min = current.getData()
            return min
        del current

    #CALCULATE THE RANGE
    def rangeOptimized(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            max = current.getData()
            min = current.getData()
            while current.getNext():
                current = current.getNext()
                if current.getData() < min:
                    min = current.getData()
                if current.getData() > max:
                    max = current.getData()
            return max - min
        del current

    def range(self):
        if self.head is None:
            print("List is empty")
        else:
            return self.max() - self.min()

    #CALCULATE THE TOTAL
    def total(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            sum = current.getData()
            while current.getNext():
                current = current.getNext()
                sum += current.getData()
            return sum
        del current

    #CALCULATE THE AVERAGE
    def average(self):
        if self.head is None:
            print("List is empty")
        else:
            return self.total() / self.length()

    #CHECK THE ORDER OF THE LIST
    def checkSort(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            increase = False
            decrease = False
            k = current.getData()
            while current.getNext():
                current = current.getNext()
                if current.getData() > k:
                    increase = True
                elif current.getData() < k:
                    decrease = True
                k = current.getData()
            if (increase and decrease or (not increase and not decrease)):
                print ("Neither")
            elif (increase):
                print ("Increase")
            else:
                print("Decrease")
        del current

    # SORT IN INCREASING ORDER
    def sortIncrease(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                tempNode = current.getNext()
                while tempNode:
                    if tempNode.getData() < current.getData():
                        tempValue = current.getData()
                        current.updateData(tempNode.getData())
                        tempNode.updateData(tempValue)
                    tempNode = tempNode.getNext()
                current = current.getNext()
            print ("The list is sorted in increasing order.")

    #SORT IN DECREASING ORDER
    def sortDecrease(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                tempNode = current.getNext()
                while tempNode:
                    if tempNode.getData() > current.getData():
                        tempValue = current.getData()
                        current.updateData(tempNode.getData())
                        tempNode.updateData(tempValue)
                    tempNode = tempNode.getNext()
                current = current.getNext()
            print ("The list is sorted in decreasing order.")

    #FIND THE DATA IN THE LIST
    def findData(self,data):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            k = 1
            while current:
                if current.getData() == data:
                    print("The data is found in the list at index", k)
                    return k
                current = current.getNext()
                k += 1
            print("The data is not found in the list.")

    #HOW TO GET DATA USING THE INDEX
    def getData(self,index):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            k = 1
            while current:
                if k == index:
                    print("The data at index", k, "is", current.getData())
                    return current.getData()
                current = current.getNext()
                k += 1
            print("The index desired in not within the size of the list")

    #REMOVE THE DATA BY FINDING IT'S INDEX
    def removebyIndex(self,index):
        current = self.head
        prev = None
        if current is None:
            print("List is empty")
        else:
            k = 1
            while current:
                if k == index:
                    print("Data", current.getData(),"at index", k,"will be removed")
                    if prev is None:
                        self.head = current.getNext()
                    else:
                        prev.setLink(current.getNext())

                    return
                else:
                    prev = current
                    current = current.getNext()
                    k += 1
            print("The index desired in not within the size of the list")
# endregion

# LL Class with addition swap_elements_by_index() method
class LL_forTask(LL):
    def __init__(self):
        super().__init__() # Inherits LL's constructor

    def swap_elements_by_index(self, first_index, second_index):
        if self.head is None:
            print("List is empty")
            return

        if first_index == second_index: # 何これ? = No swap
            return

        # Initialize node, prev node and counters
        current = self.head
        node_before_node1 = None
        node_before_node2 = None
        node1 = None
        node2 = None
        index = 0 # Index of head is 0 です

        # Traverse the linked list and find the nodes to swap
        while current:
            if index == first_index - 2: # Node that points to node1
                node_before_node1 = current
            elif index == first_index -1: # Node 1
                node1 = current

            if index == second_index - 2: # Node that points to node2
                node_before_node2 = current
            elif index == second_index -1: # Node2
                node2 = current

            if node1 and node2:
                break

            current = current.getNext()
            index += 1

        # Check if the nodes are valid (debug) eg. Index is out of bound
        if not (node1 and node2):
            return

        # Update the Node that points to node1/2's pointers to 2/1
        if node_before_node1:
            node_before_node1.setLink(node2)
        else:
            self.head = node2

        if node_before_node2:
            node_before_node2.setLink(node1)
        else:
            self.head = node1

        # Update the next node pointers
        # Pointer of node 1 = pointer of node 2 //At the same time
        # Pointer of node 2 = pointer of ndoe 1 //At the same time
        temp = node1.getNext()
        node1.setLink(node2.getNext())
        node2.setLink(temp)

# region test
'''
a = LL_forTask()
a.addToEnd(1)
a.addToEnd(2)
a.addToEnd(3)
a.addToEnd(4)
a.addToEnd(5)
a.displayList()
a.swap_elements_by_index(1,8)
a.displayList()
print(" ")

str_list = LL_forTask()
str_list.addToEnd("apple")
str_list.addToEnd("banana")
str_list.addToEnd("cherry")
str_list.addToEnd("date")
str_list.displayList()
str_list.swap_elements_by_index(1,3)
str_list.displayList()
print(" ")

mixed_list = LL_forTask()
mixed_list.addToEnd(1)
mixed_list.addToEnd("apple")
mixed_list.addToEnd(True)
mixed_list.addToEnd(3.14)
mixed_list.addToEnd(False)
mixed_list.displayList()
mixed_list.swap_elements_by_index(1,3)
mixed_list.displayList()
print(" ")

empty_list = LL_forTask()
empty_list.displayList()
empty_list.swap_elements_by_index(1,3)
empty_list.displayList()
print(" ")

duplicate_list = LL_forTask()
duplicate_list.addToEnd(1)
duplicate_list.addToEnd(2)
duplicate_list.addToEnd(3)
duplicate_list.addToEnd(2)
duplicate_list.addToEnd(5)
duplicate_list.displayList()
duplicate_list.swap_elements_by_index(1,3)
duplicate_list.displayList()
print(" ")
'''

# endregion
