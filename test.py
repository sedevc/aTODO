"""
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
"""

a = [(14, 1, u'Easasdnter yourAdsA todo..'), (19, 1, u'open tasks'), (21, 1, u'Fix this completely atrocious code before anyone sees it'), (22, 1, u'Implement foobar'), (23, 1, u'Add this functionality.'), (24, 1, u'FIXME: DB name should be configurable')]

item_id = 19

for item in a:
	if item[0] == item_id:
		print item[0]
		print item[1]
		print item[2]