# This is our writer for xlsxwriter

from openpyxl import Workbook

from writer import Writer 

class XlsxWriter(Writer):
	def __init__(self, filename='output'):
		super().__init__(filename)
		self.file_type = '.xlsx'
		self.fields = [
						"Date & time of search",
						"Keyword",
						"Publisher",
						"Result_Title",
						"Date/Time",
					]
		self.check_filename()
		self.open_an_active_sheet()
		self.write_sheet_headers()

	def __repr__(self):
		return self.filename

	def check_filename(self):
		if self.file_type not in self.filename:
			self.filename += self.file_type
	
	def open_an_active_sheet(self):
		self.workbook = Workbook()
		self.sheet = self.workbook.active

	def close_workbook(self):
		self.workbook.save(filename=self.filename)

	def write_sheet_headers(self):
		self.sheet['A1'].value = self.fields[0]
		self.sheet['B1'].value = self.fields[1]
		self.sheet['C1'].value = self.fields[2]
		self.sheet['D1'].value = self.fields[3]
		self.sheet['E1'].value = self.fields[4]

	def write_to_sheet(self, dictionary):
		try:
			value = self.sheet.max_row + 1
			self.sheet[f'A{value}'].value = dictionary.get("Date & time of search")
			self.sheet[f'B{value}'].value = dictionary.get("Keyword")
			self.sheet[f'C{value}'].value = dictionary.get("Publisher")
			self.sheet[f'D{value}'].value = dictionary.get("Result_Title")
			self.sheet[f'E{value}'].value = dictionary.get("Date/Time")
		finally:
			self.close_workbook()