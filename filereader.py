'''
accepts filename, return content of file if it exists
else returns an error.
'''
from pathlib import Path

class FileReader:	
	@staticmethod
	def accept_filename():
		filename = input("\aEnter a valid filename: ")
		return filename

	@property
	def file_content(self):
		filename = self.accept_filename()
		path_object = Path(filename)
		if path_object.exists():
			print(f"{filename} found...")
			with path_object.open() as file_handler:
				content = [ line.strip() for line in file_handler.readlines() ]
				if content:
					return content
				else:
					print("\aNo keywords in the file specified")
		else:
			print("\aYou might have to check the file name.")