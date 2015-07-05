



class mergesort:
    
    def __init__(self, list):
        self.list = list
        
    def display(self):
        print('List is : ',self.list)
        
    def sortWrap(self):
        mergesort.sort(self,0,len(self.list)-1)
        
    def sort(self, start, end):
               
        if (start >= end):
            return
        mid = (start+end)//2
        
        mergesort.sort(self,start,mid)
        mergesort.sort(self,mid+1,end)
        
        i = start
        j = mid+1
        
        temp = []
        
        while (i<=mid and j<=end):
            if self.list[i] <= self.list[j]:
                temp.append(self.list[i])
                i+=1
            else:
                temp.append(self.list[j])
                j+=1
                
        temp = temp + self.list[i:mid+1] + self.list[j:end+1]

        self.list[start:end+1] = temp
 
        
                
            
            




if __name__ == '__main__':
    
    listObj = mergesort([4,3,9,8,1,2,6,5,7])  
    listObj.display()  
    listObj.sortWrap()
    listObj.display()