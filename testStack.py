from pythond.basic.stack.Stack import Stack

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())


def revstring(mystr):
    s1 = Stack()
    reversStr = ''
    for i in mystr:
    	s1.push(i)

    while not s1.isEmpty():
    	reversStr+=s1.pop()
    
    return reversStr
    #print(s1.items)

print(revstring("apple"))