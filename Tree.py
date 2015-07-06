import sys

class Node:
    def __init__(self,value = None):
        self.left = self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insertNode(self, node):
        if self.root == None:
            self.root = node
        else:
            curr = self.root
            while True:
                #print("Searching to insert")
                if curr.value >= node.value:
                    if curr.left == None:
                        curr.left = node
                        return
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = node
                        return
                    else:
                        curr = curr.right
                        
    def displayTree(self):
        self.__class__.doDisplay(self.root)
    
    @staticmethod    
    def doDisplay(root):
        if root == None:
            return
        else:
            BinarySearchTree.doDisplay(root.left)
            print(root.value, end=" ")
            BinarySearchTree.doDisplay(root.right)
            
        
                
            

            
if __name__ == '__main__':

    bst1 = BinarySearchTree()
    while True:
        choice = input("Press q to quit or enter a number :")
        if choice == 'q':
            break
        else:
            bst1.insertNode(Node(int(choice)))
            
    print ("The binary search tree is")
    bst1.displayTree()   
        
        
    """
    
    bst1.insertNode(Node(6))
    bst1.insertNode(Node(4))
    bst1.insertNode(Node(3))
    bst1.insertNode(Node(5))
    bst1.insertNode(Node(7))
    bst1.insertNode(Node(9))
    bst1.insertNode(Node(8))
    bst1.insertNode(Node(10))
    print ("The binary search tree is")
    bst1.displayTree()"""