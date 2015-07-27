
SPLIT = '|'
LABEL_PRE = 'V'


class Graph:
    
    
    def __init__(self):
        self.vertices = {}
        self.edges = {}
    
    def addEdges(self, vertex_list):  
        
        cur_vertex = vertex_list[0]
        adj_vertices = vertex_list[1:]  
            
        for vertex in adj_vertices:
            
            # Add new edge if not already present
            vertex_label = LABEL_PRE+str(vertex)
            cur_vertex_label = LABEL_PRE+str(cur_vertex)
                        
            label1 = str(cur_vertex_label)+SPLIT+str(vertex_label)
            label2 = str(vertex_label)+SPLIT+str(cur_vertex_label)

            
            if label1 not in self.edges and label2 not in self.edges:
                self.edges[label1] = [cur_vertex_label, vertex_label]
                
                if cur_vertex_label not in self.vertices:
                    self.vertices[cur_vertex_label] = []
                    
                if vertex_label not in self.vertices:
                    self.vertices[vertex_label] = []
                    
                self.vertices[cur_vertex_label].append(label1) 
                self.vertices[vertex_label].append(label1)                   
            
            
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
        g.addEdges(line.strip().split('\t'))
        
    g.display()
  #  listObj = quicksort(lines)  
      
    #exit(0)
   # c = listObj.sortWrap()
   # print("comparisons : ",c)
   # listObj.display(100)
    #print (listObj.list[1:100])