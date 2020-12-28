'''
this is our timekeeper, it returns a formatted datetime str
'''

import datetime

class TimeKeeper:
	def __init__(self, datetime_format='%d-%b-%Y T%I:%M'):
		self.datetime_format = datetime_format
		self.keep_search_datetime()

	def __repr__(self):
		return self._datetime_of_search

	def keep_search_datetime(self):
		'''
		return the current correct date and time using the format specified
		'''
		datetime_of_search_object = datetime.datetime.now()
		self._datetime_of_search = datetime_of_search_object.strftime(self.datetime_format)
		return self._datetime_of_search