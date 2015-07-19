



class quicksort:
    
    def __init__(self, list):
        self.list = list
        
    def display(self,len):
        print('List is : ',self.list[:len])
        
    def sortWrap(self):
        return self.sort(0,len(self.list)-1)
        
    def sort(self, start, end):
               
        if (start >= end):
            return 0
        
        c = end-start
        
        pivot_ind = self.partition(start,end)
        
        c += self.sort(start,pivot_ind-1)
        c += self.sort(pivot_ind+1,end)
        return c
        
    def get_pivot(self,start,end):
        
        
        #print("ar ",self.list[start:end+1])
        mid = (start+end)//2
        a = (start, self.list[start])
        b = (mid, self.list[mid]) 
        c = (end, self.list[end])
        #print("li bef ",[a,b,c])
        l = sorted([a,b,c], key = lambda item:item[1])
        
        #print("st,end,mid ",start,mid,end)
        
        #print("list ", l)
        return l[1][0]
        
        
        
        
                
        

    def partition(self,start,end):   

        
        #pivot_pos = start
        #pivot_pos = end
        
        pivot_pos = self.get_pivot(start, end)
    
        pivot = self.list[pivot_pos]     
    
        self.list[pivot_pos] = self.list[start]
        self.list[start] = pivot     
    
        i=j=start+1

    
        while j<=end:
            if self.list[j] <= pivot:
                self.list[j],self.list[i] = self.list[i],self.list[j]
                i+=1
            j+=1
            
    
        self.list[start],self.list[i-1] = self.list[i-1],self.list[start]
        
        return i-1
     



if __name__ == '__main__':
    

    
    
    lines = [int(line.rstrip('\n')) for line in open('QuickSort.txt')]  
    #lines = [5,3,6,9,8,2,1,4,7]
    print ('length = ',len(lines))


    listObj = quicksort(lines)  
      
    #exit(0)
    c = listObj.sortWrap()
    print("comparisons : ",c)
    listObj.display(100)
    #print (listObj.list[1:100])