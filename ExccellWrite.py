#Writing to an excel
# sheet using Python
import xlwt

from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Excell_example')       #sheet1 = wb.add_sheet('Excell_sheet_name')


sheet1.write(0, 0, 'INTERN    ')
sheet1.write(0, 1, 'INTERN ID ')
sheet1.write(0, 2, 'GENDER    ')
sheet1.write(0, 3, 'COLLEGE   ')


sheet1.write(1, 0, 'Vinayak')       # sheet1.write(row , column, 'data')
sheet1.write(2, 0, 'Nishi')
sheet1.write(6, 0, 'Swarali')
sheet1.write(3, 0, 'Shubham K.')
sheet1.write(4, 0, 'Shubham')
sheet1.write(5, 0, 'Siddharth')


sheet1.write(1, 1, 'abcd 1')
sheet1.write(2, 1, 'abcd 2')
sheet1.write(3, 1, 'abcd 3')
sheet1.write(4, 1, 'abcd 4')
sheet1.write(5, 1, 'abcd 5')
sheet1.write(6, 1, 'abcd 5')


sheet1.write(1, 2, 'male')
sheet1.write(2, 2, 'female')
sheet1.write(3, 2, 'male')
sheet1.write(4, 2, 'male')
sheet1.write(5, 2, 'male')
sheet1.write(6, 2, 'female')

sheet1.write(1, 3, 'VJTI')
sheet1.write(2, 3, 'D J Sanghavi')
sheet1.write(3, 3, 'COLLEGE')
sheet1.write(4, 3, 'K J Somaiya')
sheet1.write(5, 3, 'K J Somaiya')
sheet1.write(6, 3, 'D J Sanghavi')





#  # Specifying style
# style = xlwt.easyxf('font: bold 1')
#
#  # Specifying column
# sheet1.write(1, 6, 'SAMPLE', style)
# wb.save("styleee.xls")
#
#  # Applying multiple styles
# style = xlwt.easyxf('font: bold 1, color red;')
#
#  # Writting on specified sheet
# sheet1.write(1, 5, 'SAMPLE', style)



wb.save('Excell_Implenetation3.xls')           #wb.save('Excel_sheet_name.xls')