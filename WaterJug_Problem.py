#AUTHOR#SUDHANVA PATURKAR
#DFS_WATER_JUG_AI_PRACTICAL2
def get_states(state,CP):
    states=[]
    if([0,state[1]] not in CP):
        states.append([0,state[1]])
    if([state[0],0] not in CP):
        states.append([state[0],0])
    if([size_jug1,state[1]] not in CP):
        states.append([size_jug1,state[1]])
    if([state[0],size_jug2] not in CP):
        states.append([state[0],size_jug2])
    if(state[0]+state[1]>3):
        if([state[0]+state[1]-3,3] not in CP):
            states.append([state[0]+state[1]-3,3])
    else:
        if([0,state[0]+state[1]] not in CP):
            states.append([0,state[0]+state[1]])
    if(state[0]+state[1]>4):
        if([4,state[0]+state[1]-4] not in CP):
            states.append([4,state[0]+state[1]-4])
    else:
        if([state[0]+state[1],0] not in CP):
            states.append([state[0]+state[1],0])
    
    return states

def state_dfs(CP,AS,CS):
    for i in AS:
        CP.append(i)
        new_AS=get_states(i,CP)
        if(len(new_AS)!=0):
            if(i != [goal_jug1,goal_jug2]):
                
                state_dfs(CP,new_AS,i)
            else:
                paths.append(CP.copy())
                CP.remove(i)
                continue
        CP.remove(i) 
        
        
size_jug1,size_jug2=4,3
print('Enter goal state')
goal_jug1,goal_jug2=map(int,(input().split()))
paths=[]
current_path=[[0,0]]
current_state=[0,0]
available_states=get_states([0,0],current_path)
state_dfs(current_path,available_states,current_state)
min1=9999999
minP=[]
print('All paths are:')
for i in paths:
    print(i)
    if len(i)<min1:
        min1=len(i)
        minP=i
print('Shortest Path is:')
print(minP)
print('Length of path :'+str(min1))
