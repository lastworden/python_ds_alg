



class mergesort:
    
    def __init__(self, list):
        self.list = list
        
    def display(self):
        print('List is : ',self.list)
        
    def sortWrap(self):
        return mergesort.sort(self,0,len(self.list)-1)
        
    def sort(self, start, end):
               
        if (start >= end):
            return 0
        mid = (start+end)//2
        
        c =0
        c += mergesort.sort(self,start,mid)
        c += mergesort.sort(self,mid+1,end)
        
        i = start
        j = mid+1
       
        
        temp = []
        
        while (i<=mid and j<=end):
            if self.list[i] <= self.list[j]:
                temp.append(self.list[i])
                i+=1
            else:
                c += (mid-i+1)
                temp.append(self.list[j])
                j+=1
                
        temp = temp + self.list[i:mid+1] + self.list[j:end+1]

        self.list[start:end+1] = temp
        return c
 
        
                
            
            




if __name__ == '__main__':
    

    
    
    lines = [int(line.rstrip('\n')) for line in open('IntegerArray.txt')]  
    print ('length = ',len(lines))




    listObj = mergesort(lines)  
    #listObj.display()  
    inv = listObj.sortWrap()
    print("inversions : ",inv)
    print (listObj.list[1:100])