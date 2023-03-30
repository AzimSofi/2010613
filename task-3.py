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
    
    #ENQUEUE DATA INTO LIST
    def enqueue(self,data):
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

    #DEQUEUE DATA FROM THE LIST
    def dequeue(self):
        self.pop()

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

def convertToArray(linked_list):
    array = [] # create an empty array
    while linked_list.count() > 0:
        array.append(linked_list.pop()) # Take LL element and put inside array
    return array

def reverseList(listA, listB):
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
