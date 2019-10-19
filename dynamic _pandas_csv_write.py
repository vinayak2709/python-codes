from pandas import DataFrame
import os
current_dir = os.getcwd()

column1=[]
column2=[]


def panda_csv_write(j):

    while(j<5):
        i=0
        while(i<5):

            column1.append('vmm_' + str(i))
            column2.append(i)
            i+=1

        csv_output = {'column_name': column1,
                    'column_name2': column2
                    }

        ########### any data #########
        column2.append('vinaaaa'+str(j))
        column1.append('v_' + str(i)+'ashvik'+str(j))

        j+=1
    return csv_output


csv_output=panda_csv_write(0)
df = DataFrame(csv_output, columns= ['column_name', 'column_name2'])


# name by and in specified folder with name
export_csv = df.to_csv (str(current_dir)+'/file.csv', index = None, header=True,mode='w') # to over write


csv_output=panda_csv_write(3)

df = DataFrame(csv_output, columns= ['column_name', 'column_name2'])




print (df)