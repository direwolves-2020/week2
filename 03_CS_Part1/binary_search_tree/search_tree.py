




class Node:

    def __init__(self, data=None, right_child=None, left_child=None):
        self.data = data
        self.right_child = right_child
        self.left_child = left_child
        self.size = 0


class Tree:

    """ insert node, find node, find size beginning with parent """

    def __init__(self, root=None):
        self.root = Node(root)

    # def get_parent(self):
    #     return self.parent


    def insert(self, item):

        print ('\nentered item: ', item)

        if self.root == None:  # if no parent exists
            self.root = Node(item) # then make passed item a node and set it as the parent
            print ('item is parent ' + str(item))
            return True

        else:
            parent_num = self.root # create integer variable from attribute
            print ('parent num', parent_num.data)  

            while parent_num != None:  # if parent exists

                if item > parent_num.data:
                    if parent_num.right_child != None:   # if a right child exists
                        parent_num = parent_num.right_child   # make the right child the parent
                    else:
                        parent_num.right_child = Node(item) # if no right child exists set item as right child
                        print (str(item) + ' is right child of ' + str(parent_num.data))
                        return True

                elif item < parent_num.data:
                    if parent_num.left_child != None:   # if a left child exists
                        parent_num = parent_num.left_child  # set parent as the left child
                    else:
                        parent_num.left_child = Node(item)  # if no left child exists set item as left child
                        print (str(item) + ' is left child of ' + str(parent_num.data))
                        return True

                else:
                    print ('duplicate node', parent_num.data)  # return None for if item already exists as node
                    return False



    def search(self, item):
        """ check for item matches with tree parent and children. Based on comparison, 
        replace parent with left/right children as new parent """

        def inner_search(number, parent):
            if parent == None:
                return False

            else:
                if item == parent.data: # check if item matches original parent
                    return True
                elif item > parent.data: 
                    return inner_search(item, parent.right_child)
                elif item < parent.data:
                    return inner_search(item, parent.left_child)
                else:
                    return False

        return inner_search(item, self.root)



    def size(self, node):

        if node == None:
            print (zero)
            return 0
        else: 
            children = size(self.right_child + self.left_child)
            size = 1 + children
            return size() + 1

        print ('size: ', size)





test1 = Tree(26)


assert test1.insert(15) == True
assert test1.insert(36) == True
assert test1.insert(4) == True
assert test1.insert(7) == True


assert test1.search(13) == False
assert test1.search(26) == True
assert test1.search(15) == True
assert test1.search(36) == True
assert test1.search(4) == True
assert test1.search(7) == True


