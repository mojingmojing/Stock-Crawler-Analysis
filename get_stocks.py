# This program reads the stock numbers from .xlsx file and turn them into a list
# Run this program in the Terminal and copy the result into the web browser console
import xlrd


if __name__ == "__main__":
	xl_workbook = xlrd.open_workbook("A.xlsx")
	sh_sheet = xl_workbook.sheet_by_name("SH")
	sz_sheet = xl_workbook.sheet_by_name("SZ")

	sh_list = []
	sz_list = []
	for row_idx in range(1, sh_sheet.nrows):
		sh_list.append(str(sh_sheet.cell_value(row_idx, 0)).split(".")[0])

	for row_idx in range(1, sz_sheet.nrows):
		sz_list.append(str(sz_sheet.cell_value(row_idx, 0)).split(".")[0])

	print(sh_list)
	print(sz_list)


