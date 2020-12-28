'''
this module defines a data structure used a pipeline
to send information to be written to the writer 
'''
from dataclasses import dataclass

@dataclass
class DataClassExcelFields:
	datetime_of_search: str = ''
	date_and_time: str = ''
	keyword: str = ''
	publisher: str = ''
	result_title: str = ''