import pandas as pd
import numpy as np

def main():
    path = './data_sources/'
    rpta_file = ['RPTA1.xlsx', 'RPTA2.xlsx', 'RPTA3.xlsx']
    array_elements = []
    for filex in rpta_file:
        excel = pd.ExcelFile(path+filex)
        for sheet_name in excel.sheet_names:
            excel_sheet = excel.parse(sheet_name=sheet_name)

            excel_sheet.replace(to_replace=np.nan, value='null', inplace=True)


            for index, row in excel_sheet.iterrows():
                txt_msg = row[0]
                label = row[1]
                modified = row[2]

                if modified != 'null':
                    label = modified
                
                array_elements.append([txt_msg, label])

    df = pd.DataFrame(array_elements, columns=['message', 'label'])
    df.to_csv('./uwu.csv', index=False)

main()




    


