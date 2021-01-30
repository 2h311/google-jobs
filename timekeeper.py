# '''
# this is our timekeeper, it returns a formatted datetime str
# '''

import datetime

# class TimeKeeper:
# 	@property
# 	def now(self):
# 		'''
# 		return the current correct date and time using the format specified
# 		'''
# 		return f'{datetime.datetime.now():%d-%b-%Y T%I:%M}'


def now():
	'''
	return the current correct date and time using the format specified
	'''
	print(f'{datetime.datetime.now():%d-%b-%Y T%I:%M}')

now()