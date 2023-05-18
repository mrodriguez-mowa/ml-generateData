import pandas as pd

def main():
    csv = pd.read_csv('./uwu.csv')

    df = pd.DataFrame(csv, columns=['message', 'label'])

    # valid_labels = ['NO DESEADO', 'VERIFICAR NÚMERO', 'POSITIVO', 'NEGATIVO', 'NO APLICA']

    parsed_data = []
    
    for row in df.itertuples():
        message = row.message
        label = row.label.upper()
        new_label = label
        if label.__contains__('POSI'):
            new_label = 'POSITIVO'
            parsed_data.append([message, new_label])
        elif label.__contains__('NEGA'):
            new_label = 'NEGATIVO'
            parsed_data.append([message, new_label])
        elif label.__contains__('VERI'):
            new_label = 'VERIFICAR NÚMERO'
            parsed_data.append([message, new_label])
        elif label.__contains__('DESEA'):
            new_label = 'NO DESEADO'
            parsed_data.append([message, new_label])
        elif label.__contains__('APLIC') or label.__contains__('VA'):
            new_label = 'NO APLICA'
            parsed_data.append([message, new_label])
        else:
            print('No se reconoce el label: ', label)
    
    df = pd.DataFrame(parsed_data, columns=['message', 'label'])
    df.to_csv('./uwu_parsed.csv', index=False)
    


main()