from pandas import DataFrame
import os
current_dir = os.getcwd()


Cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]
        }

df = DataFrame(Cars, columns= ['Brand', 'Price'])


export_csv = df.to_csv (str(current_dir)+'/vin.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path


print (df)