
from random import randint

reg = 'f'
rev = 'r'


gstack = []

gstack2 = []

NUM_NODES = 10#875714

cnt = 0
k = 0


        


class Graph:
    

    
    def __init__(self):
        
        self.vertices = []
        self.rev_vertices = []
        self.leaders = []
        self.top = []
        for i in range(NUM_NODES):
            self.vertices.append({reg:[],rev:[]})
        self.visited = [False]*NUM_NODES
        
    def setVisited(self):
        self.visited = [False]*NUM_NODES
 
    def addEdge(self, vertex_pair):
        
        vert1,vert2 = vertex_pair
        if vert1 == vert2:
            print('self Loop for :',vert1,' not adding..')
            return

        if vert2 not in self.vertices[vert1][reg]:
            self.vertices[vert1][reg].append(vert2)
            
        if vert1 not in self.vertices[vert2][rev]:
            self.vertices[vert2][rev].append(vert1)            
                   

        
    def revDFS(self):
        

        for vertex in range(NUM_NODES):
            if not self.visited[vertex]:
                
                self.doRevDFS(vertex)
        

    def doRevDFS(self, vertex):
        

        self.visited[vertex] = True
        gstack.append(vertex)
  
      
        while gstack:
            
            current = gstack[-1]
            
            flag = True

            for vert in self.vertices[current][rev]:
                if not self.visited[vert]:
                    self.visited[vert] = True
                    gstack.append(vert)
                    flag = False
                    break
 
            if flag:
                gstack.pop()
                self.rev_vertices.append(current)
                    
        

                
    def regDFS(self):
        
        global cnt
        cnt = 0
        for vertex in reversed(self.rev_vertices):
            if not self.visited[vertex]:
                cnt += 1
                self.leaders.append(vertex)
                self.doRegDFS(vertex)    
        
                
    def doRegDFS(self, vertex):
        
        self.visited[vertex] = True
        gstack2.append(vertex)
        k = 1
        
        while gstack2:
            
            current = gstack2[-1]
            flag = True
            for vert in self.vertices[current][reg]:
                if not self.visited[vert]:
                    self.visited[vert] = True
                    flag = False
                    k += 1
                    gstack2.append(vert)
                    break
            
            
            if flag:
                gstack2.pop()      
        self.top.append(k)

                
   # def topFive    
        

if __name__ == '__main__':
    
    
    g = Graph()
    
    g.addEdge([0,1])
    g.addEdge([1,3])
    g.addEdge([3,2])
    g.addEdge([2,0])
    g.addEdge([3,4])
    
    
    g.addEdge([7,8])
    g.addEdge([8,9])
    g.addEdge([9,7])
    g.addEdge([4,7])
    g.addEdge([8,3])
   # 
    
    print(g.visited)
    print(g.vertices)
    

    g.setVisited()
    g.regDFS()    
    
    g.setVisited()
    g.revDFS()
    
    print('Rev:',g.rev_vertices)
    g.setVisited()
    g.regDFS()
    
    print ('numCom :',cnt)
    print ('leaders : ',g.leaders )
    print ('tops : ',g.top )
    
    
    exit()    
    g = Graph()
    print('Graph construction started ...')
    with open('SCC.txt') as f:
        for line in f:
            vert1, vert2 = [int(i)-1 for i in line.rstrip().split(' ')]
            g.addEdge([vert1,vert2])
            k +=1
            if k%100000 == 0:
                print(k)
            
    
    print('Graph construction finished ...')
    g.setVisited()
    g.revDFS()
     
    print('Rev DFS finished ...')
    g.setVisited()
    print('DFS Starting ...')
    g.regDFS()
    
    print ('numCom :',cnt)
    print ('leaders : ',g.leaders.sort() )
    
