import pandas as pd

df = pd.read_excel('mask_extratoIMZCOS.xlsx')

old_name = ['Rev  CC  ', 'Numero Caderno','Status']
new_name = ['REV_CC','NUMERO_CADERNO','STATUS']

for i in range(len(old_name)):
    print(old_name[i], new_name[i])
    #read.append([old_name[i], new_name[i]])
    df.rename(columns={old_name[i]:new_name[i]}, inplace=True)

print(df.head())