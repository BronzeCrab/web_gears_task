class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev

    def __str__(self):
        """ Return description of the node """
        if self.getPrev() == None and self.getNext():
            return "{0} <-- || this node: {1} || --> {2}".format(
                self.getPrev(),
                self.getData(),
                self.getNext().getData())
        elif self.getNext() == None and self.getPrev():
            return "{0} <-- || this node: {1} || --> {2}".format(
                self.getPrev().getData(),
                self.getData(),
                self.getNext())
        elif self.getNext() == None and self.getPrev() == None:
            return "{0} <-- || this node: {1} || --> {2}".format(
                self.getPrev(),
                self.getData(),
                self.getNext())
        else:
            return "{0} <-- || this node: {1} || --> {2}".format(
                self.getPrev().getData(),
                self.getData(),
                self.getNext().getData())


class DoublyLinkedList(object):

    def __init__(self):
        self.firstNode = None
        self.lastNode = None

    def getFirstNode(self):
        return self.firstNode

    def getLastNode(self):
        return self.lastNode

    def setFirstNode(self, firstNode):
        self.firstNode = firstNode

    def setLastNode(self, lastNode):
        self.lastNode = lastNode


def insertAfter(dlist, node, newNode):
    """Inserting newNode after node"""
    newNode.setPrev(node)
    newNode.setNext(node.getNext())
    # if node was last set new last node
    if node.getNext() == None:
        dlist.setLastNode(newNode)
    # else i should renew before-link of the node after "node"
    else:
        node.getNext().setPrev(newNode)
    node.setNext(newNode)


def removeNode(dlist, node):
    """Deleting node"""
    if node.getNext() == None:
        dlist.setLastNode(node.getPrev())
    else:
        node.getNext().setPrev(node.getPrev())
    if node.getPrev() == None:
        dlist.setFirstNode(node.getNext())
    else:
        node.getPrev().setNext(node.getNext())
    node.setNext(None)
    node.setPrev(None)


def iterate(dlist, startnode):
    "Iterates forward from startnode till the end"
    node = startnode
    while node:
        yield node
        node = node.getNext()

# creating dummy nodes for test:
node1 = Node(1)
node2 = Node(2)
# setting links
node1.setNext(node2)
node2.setPrev(node1)
# creating dummy dllist:
dlist = DoublyLinkedList()
# setting up first last nodes
dlist.setFirstNode(node1)
dlist.setLastNode(node2)
# inserting node number 3 between 1 and 2 nodes, so schema
# will be like  None <-- 1 --> <-- 3 --> <-- 2 --> None
# to test insert function
print "after inserting node number 3 after node 1:"
node3 = Node(3)
insertAfter(dlist, node1, node3)
print node1
print node3
print node2
print "after deleting node number 3:"
removeNode(dlist, node3)
print "Node 1:"
print node1
print "Nide 2:"
print node2
print "Iterating trought dlist of 2 nodes:"
for x in iterate(dlist, dlist.getFirstNode()):
    print x
