

NUM_NODES = 5#200
MAX_WEIGHT = 1000000


        


class Graph:
    

    
    def __init__(self):
        
        self.vertices = []
        self.min_dist = [MAX_WEIGHT]*NUM_NODES
        self.dij_score = {}
        self.visited = []
    
        for i in range(NUM_NODES):
            self.vertices.append({})
    
            self.dij_score[i] = MAX_WEIGHT
      
        
        
    def setVisited(self):
        self.visited = [False]*NUM_NODES
 
    def addEdge(self, vertex_list):
        
        vert1,vert2,weight = vertex_list

        if vert2 not in self.vertices[vert1]:
            self.vertices[vert1][vert2]=weight
        else :
            print('Error: source :',vert1,'dest:',vert2)
                      
    
    def updateHeap(self,vertex):   
        
        for item in self.vertices[vertex].keys():
            if item not in self.visited:
                cur_score = self.min_dist[vertex]+self.vertices[vertex][item]
                org_score = self.dij_score[item]
                
                if cur_score < org_score:
                    self.dij_score[item] = cur_score
     
     
    def getMinDijVert(self):     
        
        min_val = None
        min_key = None
        
        for item in self.dij_score.keys():
            
            if min_val is None:
                min_val = self.dij_score[item]
                min_key = item
            elif min_val > self.dij_score[item]:
                min_val = self.dij_score[item]
                min_key = item
                
        
        return [min_key,min_val]
                
            
                 

    def doDijkstra(self):  
        
        self.min_dist[0] = 0
        self.dij_score.pop(0)
        self.visited.append(0)
        self.updateHeap(0)
        
        while len(self.visited) < NUM_NODES:
            
            [min_key,min_val] = self.getMinDijVert()
            self.min_dist[min_key] = min_val
            self.dij_score.pop(min_key)
            self.visited.append(min_key)
            self.updateHeap(min_key)
            
            
        
        
        



                
   # def topFive    
def getEdgeWeight(line):
    
    dest,weight = line.split(',')
    dest,weight = int(dest)-1,int(weight)
    return [dest,weight]
            

if __name__ == '__main__':
    
    

    g = Graph()
   
    print('Graph construction started ...')
    
    g.addEdge([0,1,1])
    g.addEdge([1,2,2])
    g.addEdge([0,2,4])
    g.addEdge([1,3,6])
    g.addEdge([2,3,3])
    g.addEdge([3,4,2])
    g.addEdge([1,4,2])
    

                   
            
            
    print('Graph construction finished ...')   
    print ('vertex 0',g.vertices)    
    g.doDijkstra()
    print('Dist ',g.min_dist)

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
           # vert1, vert2 = [int(i)-1 for i in line.rstrip().split(' ')]
            #g.addEdge([vert1,vert2])

    
