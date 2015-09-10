from pythond.basic.queue.Queue import Queue

def hotPotato(nameList, num):
	simQueue = Queue()
	for name in nameList:
		simQueue.enqueue(name)

	while simQueue.size() > 1:
		for i in range(num):
			simQueue.enqueue(simQueue.dequeue())

		simQueue.dequeue()

	return simQueue.dequeue()

print(hotPotato(["Atul","Sanjiv","Deepak","Raju","Digivijay","Nihal"],7))