
from random import randint

SPLIT = '|'
LABEL_PRE = 'V'


class Graph:
    
    
    def __init__(self):
        self.vertices = {}
        self.edges = {}
        
    def addEdge(self, vertex_pair):
        
        #Assume no parallel edge
        vertex_pair.sort()
        
        #No self loop
        vert1,vert2 = vertex_pair
        if vert1 == vert2:
            print('self Loop for :',vert1,' not adding..')
            return
        
        
        edge_label = str(vert1)+SPLIT+str(vert2)
        
        if edge_label not in self.edges:
            self.edges[edge_label] = 1
        else:
            self.edges[edge_label] +=1
            
        if vert1 not in self.vertices:
            self.vertices[vert1] = []
            
        if vert2 not in self.vertices:
            self.vertices[vert2] = []            
            
        if vert2 not in self.vertices[vert1]:
            self.vertices[vert1].append(vert2)
            
        if vert1 not in self.vertices[vert2]:
            self.vertices[vert2].append(vert1) 
            
    
    def normEdges(self):  
        for i in self.edges.keys():
            self.edges[i] = 1
              
    def doContract(self):    
        for i in range(198):
            ledges = list(self.edges.keys())   
            ind = randint(0,len(ledges)-1)   
            self.contractEdge(ledges[ind])
        
    def contractEdge(self,edge_label):
        
        print('contracting edge',edge_label)
        vert1,vert2 = [int(item) for item in edge_label.split(SPLIT)]
        
        # for each edge in vert2 add an edge to vert1
        
        #self.deleteEdge([vert1,vert2])
        
        n = len(self.vertices[vert2])
        for i in range(n):
            vert = self.vertices[vert2][0]
            self.addEdge([vert1,vert])
            self.deleteEdge([vert,vert2])
            
        self.vertices.pop(vert2,None)
            
        
        
    def deleteEdge(self,vertex_pair):
        
        vertex_pair.sort()
        
        vert1,vert2 = vertex_pair
        
        edge_label = str(vert1)+SPLIT+str(vert2)
        
        self.edges[edge_label] -= 1
        
        if self.edges[edge_label] == 0:
            self.edges.pop(edge_label,None)
        
            if vert1 in self.vertices and vert2 in self.vertices[vert1]:
                self.vertices[vert1].remove(vert2)
            
            if vert2 in self.vertices and vert1 in self.vertices[vert2]:
                self.vertices[vert2].remove(vert1)        
        
        
        
    
    def parseList(self, vertex_list):  
        
        cur_vertex = int(vertex_list[0])
        adj_vertices = [int(i) for i in vertex_list[1:]]
            
        for vertex in adj_vertices:    
            # Add new edge if not already present
            self.addEdge([cur_vertex,vertex])
            
    def display(self):
        
        for vertex in self.vertices:
            print('Vertex : ',vertex,'Edges : ',self.vertices[vertex])
         
        return
        k = 1  
        for edge in self.edges:
            print('seq : ',k,'Edge : ',edge,'Vert : ',self.edges[edge])
            k+=1
            

     



if __name__ == '__main__':
    

    
    
    lines = [line.rstrip('\n') for line in open('kargerMinCut.txt')]  
    #lines = [5,3,6,9,8,2,1,4,7]
    print ('length = ',len(lines))

    g = Graph()
    
    for line in lines:
        #print(line.strip().split('\t'))
        g.parseList(line.strip().split('\t'))
        
    g.normEdges()
        
    g.display()
    
    
   # print(g.edges)
    #print('len : ',len(g.edges))
   # exit(0)
    print('\n\n')
    g.doContract()
    print('\n\n')
    g.display()
    print('len : ',len(g.vertices))
    print ('vertices', g.vertices)
    print('edges',g.edges)
    #print (l)
  #  listObj = quicksort(lines)  
      
    #exit(0)
   # c = listObj.sortWrap()
   # print("comparisons : ",c)
   # listObj.display(100)
    #print (listObj.list[1:100])