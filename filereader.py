'''
accepts filename, return content of file if it exists
else returns an error.
'''
from pathlib import Path

class FileReader:	
	# @staticmethod
	# def accept_filename():
		# filename = input("Enter a valid filename: ")
		# return filename

	def grab_content_of_file(self):
		filename = 'keywords.txt'
		path_object = Path(filename)
		if path_object.exists():
			print(f"{filename} found...")
			with path_object.open() as file_handler:
				return [ line.strip() for line in file_handler.readlines() ]
		else:
			print("You might have to check the file name.")