## Stock Crawler & Analysis

### Introduction
In this project, you will be able to download stock data from Yahoo Finance and then visualize the data you get through making different plots. Although you may not be able to come up with precise predictions of how the stock will behave from the plots made in this project, but it's fun to make these plots yourself to compare with plots we see from finance websites and get a general feeling of how the stock behaved in the days passed.  

Ok, let's get started!

## Getting Started
There are a number of steps in this project you need to do before you get the final step of making batches of plots for stocks that you are interested. But first thing first, clone all the files in this project to a local folder. 

## Get List of Stock Numbers
Next we need to get the list of stock numbers from the internet so the program will know which stock you will need to download. A "A_stocklist.xlsx" file is included in this project and it includes the stock numbers for stocks listed on Shanghai Stock Exchange (SH) and for stocks listed on Shenzhen Stock Exchange (SZ). 

To read all these stock numbers and turn them into a readable list in web browser, we need to first run a python program "get_stocks.py". Here is how the code in this python program looks like:

```python
import xlrd

if __name__ == "__main__":
	xl_workbook = xlrd.open_workbook("A_stocklist.xlsx")
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
```

Make sure you have Python 3 installed on your computer and if not, just get rid of the round brackets behind the last two lines with "print" command and you should be fine to run this program on Python 2. This program uses a python library called "xlrd" so if you don't have this library installed, try to input in your command line

```
pip install xlrd
```

Ok, everything is set up and 




In a candlestick chart, a green candlestick means the closing price is higher than the open price and a red candlestick means the closing price is higher than the open price. This presentation method of using red as gain and green as loss is commonly used in stock markets in China. 
