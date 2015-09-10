from Queue import Queue
import random

class Printer:
	"""docstring for Printer"""
	def __init__(self, ppm): #ppm page per minute
		self.pageRate = ppm
		self.currentTask = None
		self.timeRemaining = 0


	def tick(self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining - 1
			if self.timeRemaining <= 0:
				self.currentTask = None

	def busy(self):

		if self.currentTask != None:
			return True
		else:
			return False

	def pickNextTask(self, newTask):
		self.currentTask = newTask
		self.timeRemaining = newTask.getPages() * 60/self.pageRate

class Task:
	"""docstring for ClassName"""
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1, 21)

	def getTimestamps(self):
		return self.timestamp

	def getPages(self):
		return self.pages

	def waitTime(self, currenttime):
		return  currenttime - self.timestamp

def simulation(numseconds, pageperminute):
	labprinter = Printer(pageperminute)
	printerQueue = Queue()
	waitingtimes = []

	for currentseconds in range(numseconds):
		
		if newPrintTask():
			task = Task(currentseconds)
			printerQueue.enqueue(task)

		if (not labprinter.busy()) and (not printerQueue.isEmpty()):
			nextTask = printerQueue.dequeue()
			waitingtimes.append(nextTask.waitTime(currentseconds))
			labprinter.pickNextTask(nextTask)

		labprinter.tick()

	averageWait = sum(waitingtimes)/len(waitingtimes)
	print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printerQueue.size()))

def newPrintTask():
	num = random.randrange(1, 181)

	if num == 180:
		return True
	else:
		return False

for i in range(10):
	simulation(3600, 5)