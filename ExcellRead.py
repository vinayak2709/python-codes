# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ('Excell_Implenetation3.xls')

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 1 and column 0
print(sheet.cell_value(1, 0))               # displays the data element in specified location in sheet

print(sheet.cell_value(1, 1))
print(sheet.cell_value(1, 2))



print(sheet.nrows)                                # Extracting total number of rows
print(sheet.ncols)                                #total no of columns

i=0
for i in range(sheet.ncols):
    print("column_Title  ",i)
    print(sheet.cell_value(0, i),"\n")

i=0
for i in range(sheet.nrows):
    print(sheet.row_values(i))


i=0
for i in range(sheet.ncols):
    print(sheet.col_values(i))

print("\n\n if you want to serach by emp_data enter the data it will show all the details of person  =  ")
print(" enter data_string ")
search_string = input()

i=0
for i in range(sheet.nrows) :
    j=0
    for j in range(sheet.ncols):
        if(sheet.cell_value(i, j)==search_string):
            found_location1 =i
            found_location2 = j
            print("found1 location","row= ",i,"col= ",j,"\n")
            break

i= found_location1
j=0
for j in range(sheet.ncols) :

    print(sheet.cell_value(0, j),"          " ,sheet.cell_value(i, j))
