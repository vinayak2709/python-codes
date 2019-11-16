import csv
import os
from datetime import date
def csv_folder_creation():
    current_dir = os.getcwd()
    today = date.today()
    excel_path = current_dir + '\\' + str(today) + '\\'
    # fname2=r'sample.csv'

    row = [None,None]

    row[0] = "ID Number"
    row[1] = "Time"

    def write_to_csv(row_value_1,row_value_2):
        if os.path.isfile(excel_path + str(today) + '.csv'):
            print('old file')
            with open(excel_path + str(today) + '.csv', 'a') as writeFile:

                # writer.writerows(row)

                # for i in range(5):
                row[0] = row_value_1
                row[1] = row_value_2
                writer = csv.writer(writeFile)
                writer.writerow(row)

        else:
            print('new file')
            with open(excel_path + str(today) + '.csv', 'w') as writeFile:
                writer = csv.writer(writeFile)
                # writer.writerows(row)
                writer.writerow(row)
                row[0] = row_value_1
                row[1] = row_value_2
                writer.writerow(row)

            writeFile.close()

    if not os.path.exists(str(today)):
        os.mkdir(str(today))
        # write_to_csv()
    else:
        print("Folder Already Exsist")

    write_to_csv("0", "25")