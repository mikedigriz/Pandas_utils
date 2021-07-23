import pandas as pd
import os
# папка с файлами
folder = 'C:/Users/admin/Downloads/Merge' 
# формируем список путей к файлам
files = os.listdir(folder) 
# сюда будем добавлять прочитанную таблицу
all_file_frames = []
for f in files:
    print('Reading %s'%(folder+'/'+f))
    tab = pd.read_excel(folder+'/'+f)
    tab = pd.DataFrame(tab)
    filtered_df = tab.query('Данные > 2000')
    filtered_df.sort_values(by='Данные', ascending=False)
    all_file_frames.append(filtered_df)
 # axis=0 если нужно добавить таблицу снизу и axis=1 если нужно слева   
all_frame = pd.concat(all_file_frames, axis=0) 
# print(all_frame)
# получим файл final_file.xlsx в os.getcwd()
all_frame.to_excel('C:/Users/admin/Downloads/Merge/final_file.xlsx', index=False) 
