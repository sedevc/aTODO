class Ticker(object):
	def __init__(self):
		self.count = 0
	def tick(self):
		self.count += 1
		return self.count
class PrintingTicker(Ticker):
	def printMe(self):
		print "Ticker is",self.count

t = Ticker()
p = PrintingTicker()
print t.tick()
print p.tick()
print p.tick()
p.printMe()