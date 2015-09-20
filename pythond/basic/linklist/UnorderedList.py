
class Node:
	"""docstring for ClassName"""
	def __init__(self, item):
		self.data = item
		self.next = None

	def getNext(self):
		return self.next

	def getData(self):
		return self.data

	def __str__(self):
		return self.data

	def setNext(self, newNext):
		self.next = newNext

	def setData(self, newData):
		self.data = newData

class UnorderdList:
	"""docstring for UnorderdList"""
	def __init__(self):
		self.head = None

	def add(self, data):
		tempItem = Node(data)
		tempItem.setNext(self.head)
		self.head = tempItem

	def isEmpty(self):
		return self.head == None


	def size(self):
		current = self.head
		count = 0
		while current != None:
			current = current.getNext()
			count = count + 1

		return count

	def remove(self, data):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == data:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def search(self, data):
		current = self.head
		found = False
		index = 0

		while current != None and not found:
			if current.getData() == data:
				found = True
			else:
				index = index + 1
				#print(found)
				current = current.getNext()

		if found:
			return index
		else:
			return -1


	def __str__(self):
		current = self.head
		dataStr = '['
		while current != None:
			if current.getNext() != None:
				dataStr += str(current.getData())+' '
			else:
				dataStr += str(current.getData())

			current = current.getNext()

		dataStr += ']'

		return dataStr

def main():
	unOrdlist = UnorderdList()

	unOrdlist.add(12)
	unOrdlist.add(15)
	unOrdlist.add(69)
	unOrdlist.add(10)
	unOrdlist.add(20)

	print(unOrdlist)
	print(unOrdlist.size())
	unOrdlist.remove(15)
	print(unOrdlist)
	print(unOrdlist.size())
	print(unOrdlist.search(20))
	print(unOrdlist.search(14))



main()


		


		