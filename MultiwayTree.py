#  File: MultiwayTree.py
#  Description: Implement multiway trees with n number of children and see if
#               two trees are isomorphic to each other
#  Student's Name: Amy Fang
#  Student's UT EID: af27947
#  Course Name: CS 313E 
#  Unique Number: 86940
#
#  Date Created: 08/07/17
#  Date Last Modified: 08/08/17

class MultiwayTree:
     
    def __init__(self, pyTree):
        self.parent = None
        self.root = None
        self.children = []
        
        self.setRootVal(pyTree[0])
        for i in range(len(pyTree[1])):
            # make a new tree for each child
            child = MultiwayTree(pyTree[1][i])
            child.parent = self
            self.children.append(child)
                                                    
    def getChild(self, n):
        return self.children[n]

    def setRootVal(self, value):
        self.root = value

    def getRootVal(self):
        return self.root

    def preOrder(self):
        # print out the node-and-pointer representation of a tree using preorder.
        print(self.root, end = " ")
        for child in self.children:
            child.preOrder()

    def isIsomorphicTo(self, other):
        # return True if the tree "self" has the same structure as the
        # tree "other", "False" otherwise.
        status = True
        if len(self.children) == len(other.children):
            for i in range(len(self.children)):
                # compares each child to the other child
                result = self.getChild(i).isIsomorphicTo(other.getChild(i))
                status = result
        else:
            status = False

        # Returns the status
        return status


def main():
    infile = open("MultiwayTreeInput.txt", "r")

    firstLine = True
    count = 1 # keeps count of trees
    for line in infile:
        line = line.strip()
        print("Tree " + str(count) + ": " + line)
        line = eval(line)
        
        if firstLine:
            # if first tree
            firstLine = False
            tree1 = MultiwayTree(line)
            print("Tree " + str(count) + " preorder: ", end = "")
            tree1.preOrder()
            print()
            print()
            
        else:
            # if second tree
            firstLine = True
            tree2 = MultiwayTree(line)
            print("Tree " + str(count) + " preorder: ", end = "")
            tree2.preOrder()
            print()
            print()

            # See if the two are isomorphic
            if tree1.isIsomorphicTo(tree2):
                # isomorphic
                print("Tree", count - 1, "is isomorphic to Tree", count)
            else:
                # NOT isomorphic
                print("Tree", count - 1, "is not isomorphic to Tree", count)

            print()
            print()
        
        count += 1

    infile.close()

main()
