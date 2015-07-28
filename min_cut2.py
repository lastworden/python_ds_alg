
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
        
        
        edge_label = str(vert1)+LABEL_PRE+str(vert2)
        
        if edge_label not in self.edges:
            self.edges[edge_label] = 1
            
        if vert1 not in self.vertices:
            self.vertices[vert1] = []
            
        if vert2 not in self.vertices:
            self.vertices[vert2] = []            
            
        if vert2 not in self.vertices[vert1]:
            self.vertices[vert1].append(vert2)
            
        if vert1 not in self.vertices[vert2]:
            self.vertices[vert2].append(vert1)            
        
    def contractEdge(self,edge_label):
        
    def deleteEdge(self,vertex_pair):
        
        vertex_pair.sort()
        
        vert1,vert2 = vertex_pair
        
        edge_label = str(vert1)+LABEL_PRE+str(vert2)
        
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
        print(line.strip().split('\t'))
        g.parseList(line.strip().split('\t'))
        
    g.display()
  #  listObj = quicksort(lines)  
      
    #exit(0)
   # c = listObj.sortWrap()
   # print("comparisons : ",c)
   # listObj.display(100)
    #print (listObj.list[1:100])