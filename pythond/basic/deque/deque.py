class Deque:
    
    def __init__(self):
        self.items = []
    
    def addFront(self, item):
        self.items.append(item);
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    

def main():
        d = Deque()
        print(d.isEmpty()) #True
        d.addRear(4)
        d.addFront(6)
        d.addRear('Cat')
        d.addFront("Deepak")
        d.addFront("Singh")

        d.addFront(8)

        print(d) #['Cat', 4, 6, 'Deepak', 'Singh', 8]

        print(d.removeFront()) #8
        print(d.removeRear()) #Cat

        print(d) #[4, 6, 'Deepak', 'Singh']

if __name__ == '__main__':
       main()

