
from random import randint
import copy

SPLIT = '|'
LABEL_PRE = 'V'


class Graph:
    
    
    def __init__(self):
        self.vertices = {}
        self.edges = {}
        
    def addEdge(self, vertex_pair, weight=1):

        vertex_pair.sort()
        vert1,vert2 = vertex_pair

        #No self loop allowed.
        if vert1 == vert2:
            #print('self Loop for :',vert1,' not adding..')
            return
        
        
        edge_label = self.getEdgeLabel(vertex_pair)
        
        if edge_label not in self.edges:
            self.edges[edge_label] = weight
        else:
            self.edges[edge_label] += weight
            
        if vert1 not in self.vertices:
            self.vertices[vert1] = []
            
        if vert2 not in self.vertices:
            self.vertices[vert2] = []            
            
        if vert2 not in self.vertices[vert1]:
            self.vertices[vert1].append(vert2)
            
        if vert1 not in self.vertices[vert2]:
            self.vertices[vert2].append(vert1) 


    def deleteEdge(self,vertex_pair):

        vertex_pair.sort()

        vert1,vert2 = vertex_pair

        edge_label = self.getEdgeLabel(vertex_pair)

        self.edges.pop(edge_label,None)


        if vert1 in self.vertices and vert2 in self.vertices[vert1]:
            self.vertices[vert1].remove(vert2)

        if vert2 in self.vertices and vert1 in self.vertices[vert2]:
            self.vertices[vert2].remove(vert1)

    def getEdgeLabel(self,vertex_pair):

        vertex_pair.sort()
        vert1,vert2 = vertex_pair

        edge_label = str(vert1)+SPLIT+str(vert2)
        return edge_label

    def contractEdge(self,edge_label):

        #print('contracting edge',edge_label)
        vert1,vert2 = [int(item) for item in edge_label.split(SPLIT)]

        n = len(self.vertices[vert2])
        for i in range(n):
            vert = self.vertices[vert2][0]

            cur_edge_label = self.getEdgeLabel([vert,vert2])
            edge_weight = self.edges[cur_edge_label]
            self.addEdge([vert1,vert],edge_weight)
            self.deleteEdge([vert,vert2])

        self.vertices.pop(vert2)


    def doContract(self):

        m = len(self.vertices)

        numVertToContract = m-2

        for i in range(numVertToContract):
            ledges = list(self.edges.keys())
            ind = randint(0,len(ledges)-1)
            self.contractEdge(ledges[ind])

        for i in self.edges.keys():
            l = self.edges[i]
        return l


    def normEdges(self):
        '''
        Since the initial graph construction contains symetric edges, we need to subtract 1 from edge count
        :return:
        '''

        for i in self.edges.keys():
            self.edges[i] = 1

    
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

    print ('length = ',len(lines))

    g = Graph()
    
    for line in lines:
        g.parseList(line.strip().split('\t'))
        
    g.normEdges()
        
    g.display()


    n = len(g.vertices)
    n = 4000

    min_cut_len = None



    for i in range(n):
        g1 = copy.deepcopy(g)
        l = g1.doContract()
        if min_cut_len is None or l<min_cut_len:
            min_cut_len = l

        print('min_curr:',l, 'min till now : ',min_cut_len, 'iter',i)



    print('len : ',min_cut_len)
    #print ('vertices', g.vertices)
    #print('edges',g.edges)
    #print (l)
  #  listObj = quicksort(lines)  
      
    #exit(0)
   # c = listObj.sortWrap()
   # print("comparisons : ",c)
   # listObj.display(100)
    #print (listObj.list[1:100])


