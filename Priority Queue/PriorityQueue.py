from abc import ABC, abstractmethod

# from queue import PriorityQueue  
# q = PriorityQueue()
# q.put()
# q.get()

class PatientStucture(ABC):
    @abstractmethod
    def insert(self):
        pass
    
    @abstractmethod
    def view(self):
        pass

    @abstractmethod
    def count(self):
        pass

class Helper():
    pass

class Patient(Helper, PatientStucture):
    def __init__(self):
        self.ls = [None]
    
    def swap(self, i, j):
        self.ls[i], self.ls[j] = self.ls[j], self.ls[i]
    
    def shiftDown(self, i):
        if 2**i+1 >= len(self.ls):   
            return
        
        maxIndex = -1
        if self.ls[2**i]['p']>self.ls[2**i + 1]['p']:
            maxIndex = 2**i
        else:
            maxIndex = 2**i + 1
        self.swap(i, maxIndex)
        self.shiftDown(maxIndex)
        
    def shiftUp(self, i):
        # print(i)
        while (i > 1 and (self.ls[i]['p'] > self.ls[i//2]['p'])):
            self.swap(i//2, i) # Swap parent and current node
            i = i//2 # Update i to parent of i
    
    def insert(self, p):
        if len(self.ls)>1 and p['p'] == 0:
            p['p'] = self.ls[-1]['p']-1
        self.ls.append(p)
        self.shiftUp(len(self.ls)-1)
    
    def view(self):
        for i in range(1, len(self.ls)):
            print(self.ls[i])
    
    def count(self):
        print(len(self.ls)-1)
    
    def peek(self):
        print(self.ls[1])
        
    def pop(self):
        self.swap(1, len(self.ls)-1)
        print(self.ls.pop())
        self.shiftDown(1)

if __name__=='__main__':
    P = Patient()
    # X = PatientStucture()
    
    #Note: 'p' non-emergency should be 0
    #Note: 'p' emergenecy should be 1  (no other value is allowed!!!)
    p1= {'Name': 'Seeta',
         'Gender': 'F',
         'p': 0}
    p2 = {'Name': 'Ram',
          'Gender': 'M',
          'p': 0}
    p3 = {'Name': 'Karan',
          'Gender': 'M',
          'p': 1}
    
    P.insert(p1)
    P.insert(p2)
    P.insert(p3)
    # P.view()
    P.count()
    P.pop()
    P.pop()
    