#AUTHOR#SUDHANVA PATURKAR
#Travelling Salesman Problem Using Best First Search 

from queue import PriorityQueue
import matplotlib.pyplot as plt

##generating graph for user

x = [1,11,6,1,6,6,11,6] 
y = [2,2,9,2,5,9,2,5]    
plt.plot(x, y, color='yellow', linestyle='solid', linewidth = 3, 
         marker='o', markerfacecolor='red', markersize=12)  
plt.annotate('A', xy=(6 ,9))
plt.annotate('B', xy=(1, 2))
plt.annotate('C', xy=(11, 2))
plt.annotate('D', xy=(6, 5))
plt.ylim(0,14) 
plt.xlim(0,16) 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('Travelling Salesman Problem') 
plt.show() 

nodes=['A','B','C','D']
link_dict={
    'A':{'B':10,'C':15,'D':20},
    'B':{'A':10,'C':35,'D':25},
    'C':{'B':35,'A':15,'D':30},
    'D':{'B':25,'C':30,'A':20},
}
print('Enter the start city.')
start_node=input()
q = PriorityQueue()
path=[]
cost=0
path.append(start_node)
for j in link_dict[start_node].keys():
    q.put((link_dict[start_node][j],j))
while not q.empty():
    next_item = q.get()
    path.append(next_item[1])
    cost=cost+int(next_item[0])
    while not q.empty():
        temp = q.get()
    for j in link_dict[next_item[1]].keys():
        if j in path:   
            continue
        q.put((link_dict[next_item[1]][j],j))
cost=cost+link_dict[path[-1]][start_node]
print(path) 
print(cost)
