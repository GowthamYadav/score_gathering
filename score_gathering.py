
#Node class
class Node(object):
    def __init__(self, value,count=None):
        '''value to store data of the node.
           count is to count the same values ,if added to the tree.
           left and right to indicate children if any'''
        self.value = value
        if count:
            self.count=count
        else:
            self.count=1
        self.left = None
        self.right = None


#BST class    
class BST(object):
    '''first inserted value will be root.'''
    def __init__(self, root):
        self.root = Node(root)

    
    def insert(self, new_val):
        '''Insert node to the tree.'''
        return self.insert_helper(self.root,new_val)
        
        
    def insert_helper(self,current,new_val):
        '''Helper method - use to create a 
        binary tree.'''
        #if value to be added is already in tree.
        #increment count.
        if current.value==new_val:
            current.count+=1
        #check for the right place for the new value in the tree.
        elif current.value<new_val:
            if current.right:
                return self.insert_helper(current.right,new_val)
            else:
                current.right=Node(new_val)

        elif current.value>new_val:
            if current.left:
                return self.insert_helper(current.left,new_val)
            else:
                current.left=Node(new_val)
        
    def print(self):
        '''Print out all tree nodes
        as they are visited in
        a level-order traversal.'''
        return self.print_helper(self.root)

    def print_helper(self, start):
        '''Helper method - use this to create a 
        print solution.'''
        if start is None:
            return
        #queue to store the address of the nodes
        #queue first in first out
        queue=[]
        #adding root to queue as first element
        queue.append(start)
        string=""   
        while True:
            count1=len(queue)

            if count1==0:
                break

            while count1>0 :
                #address of the queue is assigned to start
                start=queue[0]
                #pop after printing
                queue.pop(0)
                if start:
                    #print value of queue top
                    #print("{}:{}".format(start.value,start.count),end='')
                    string+=(str(start.value)+':'+str(start.count))
                    #if queue top has any left or right node add its address to queue(append at end) 
                    if start.left!=None or start.right!=None:
                        queue.append(start.left)
                        queue.append(start.right)
                    #if queue has some values print ','    
                    if queue:
                        #print(',',end='')
                        string+=','
                    
                else:
                    #print(",",end='')
                    string+=","
                count1-=1
        
        return string
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(5)
tree.insert(5)
tree.insert(6)
tree.insert(1)
tree.insert(4)

#print tree
print(tree.print())
#should print 4:2,2:1,5:2,1:1,,,6:1
