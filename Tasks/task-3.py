#NODE CLASS
class Node:
    def __init__(self, data=None, link=None): # Constructor
        self.data = data
        self.link = link

    # Accessing/Modifying object's attribute
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

#LINKED LIST CLASS
class LL:
    def __init__(self):
        self.head = None

    def push(self,data):
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode

    #POP DATA FROM THE LIST - returns 'popped' value
    def pop(self):
        tempNode = self.head
        self.head = tempNode.getNext()
        return tempNode.getData()
    
    #ENQUEUE DATA INTO LIST (to tail)
    def enqueue(self,data):
        current = self.head
        if current is None:
            tempNode = Node(data)
            tempNode.setLink(self.head)
            self.head = tempNode
            del tempNode
        else:
            tempNode = Node(data)
            while current.getNext():
                current = current.getNext()
            current.setLink(tempNode)
            del tempNode
        del current

    #DEQUEUE DATA FROM THE LIST (at head)
    def dequeue(self):
        return self.pop() # dequeuing returns a value

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

    #Returns the number of element(s) in the LL
    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count

# Using stack data structure
def convertToArray(linked_list):
    array = [] # create an empty array
    while linked_list.count() > 0:
        array.append(linked_list.pop()) # Take LL element and put inside array
    return array

# Using queue data structure 
# Head of LL is the start of the queue 
def reverseList(nonempty_list, empty_list):
    while nonempty_list.count() > 0:
        tempNode = nonempty_list.dequeue()
        empty_list.push(tempNode) # Using push instead of enqueue to insert it at the head
        del tempNode
    return None


# Test
''' Passed
listA = LL()
listA.push('P')
listA.push('Y')
listA.enqueue('T')
listA.enqueue('H')
listA.push('O')
listA.enqueue('N')
listA.displayList()
print(listA.count())
'''

''' Passed
listA = LL()
listA.push('I')
listA.enqueue('L')
listA.enqueue('O')
listA.enqueue('V')
listA.enqueue('E')
listA.push('C')
listA.push('O')
listA.push('D')
listA.push('I')
listA.push('N')
listA.push('G')
listA.displayList()

arrayA = convertToArray(listA)
listA.displayList()
print(arrayA)
'''

''' Passed
listA = LL()
listB = LL()
listA.push('I')
listA.enqueue('A')
listA.enqueue('M')
listA.push('A')
listA.enqueue('M')
listA.enqueue('U')
listA.enqueue('S')
listA.enqueue('L')
listA.enqueue('I')
listA.enqueue('M')
listA.displayList()

reverseList(listA,listB)
listA.displayList()
listB.displayList()
'''
