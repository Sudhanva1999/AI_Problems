#AUTHOR#SUDHANVA PATURKAR
#BFS_CANNIBALS AND MISSIONARIES PROBLEM
class parentTracker:
    def __init__ (self,node,parent):
        self.key=node
        self.parent=parent

def get_states(state):
    children=[]
    m=[]
    c=[]
    if state[2]==1:
        m.append(state[0]-2)
        m.append(state[0])
        m.append(state[0]-1)
        m.append(state[0]-1)
        m.append(state[0])
        c.append(state[1])
        c.append(state[1]-2)
        c.append(state[1]-1)
        c.append(state[1])
        c.append(state[1]-1)
        for i in range(5):
            if (m[i]>=c[i] or m[i]==0) and m[i]>=0 and c[i]>=0 and ((3-m[i])>=(3-c[i]) or (3-m[i]==0)):
                if [m[i],c[i],0] not in visited and [m[i],c[i],0] not in bfs_q:
                    children.append([m[i],c[i],0])
    else:
        m.append(state[0]+2)
        m.append(state[0])
        m.append(state[0]+1)
        m.append(state[0]+1)
        m.append(state[0])
        c.append(state[1])
        c.append(state[1]+2)
        c.append(state[1]+1)
        c.append(state[1])
        c.append(state[1]+1)
        for i in range(5):
            if (m[i]>=c[i] or m[i]==0) and m[i]<4 and c[i]<4 and ((3-m[i])>=(3-c[i]) or (3-m[i]==0)) :
                if [m[i],c[i],1] not in visited and [m[i],c[i],1] not in bfs_q:
                    children.append([m[i],c[i],1])
        
    return children

def get_Parent(node):
    for i in parentObj:
        if(i.key== node):
            return i.parent
    else:
         return 0

visited=[]
parentObj=[]
flag=0
gs=[0,0,0]
parent_path=[]
initial_state=[3,3,1]

bfs_q=[[3,3,1]]
while flag!=1:
    node=bfs_q.pop(0)
    visited.append(node.copy())
    if(node == gs):
        flag2=0
        parent_path.append([0,0,0])
        while flag2!=1:
          
            node_p=get_Parent(node)
            if node_p ==[3,3,1]:
                l=node_p.copy()
                parent_path.append(l)
                flag2=1
            else:
                l=node_p.copy()
                print('found parent-->',l)
                parent_path.append(l)
                print(parent_path)
            node=node_p
        print('The path to solve problem found by BFS traversal => ')
        for j in reversed(range(len(parent_path))):
            print(parent_path[j], end=" ")
        flag=1
    else:  
        children=get_states(node)
        for i in children:
            parentObj.append(parentTracker(i,node))
            bfs_q.append(i)
