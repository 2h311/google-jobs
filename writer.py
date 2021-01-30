# This is our base writer which will be extended for other writers
# TODO: define some methods and properties for all writers

class Writer:
	def __init__(self, filename):
		self.filename = filename