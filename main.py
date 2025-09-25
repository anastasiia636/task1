import pandas as pd
import os

# читаем csv и берем только нужные столбцы
df = pd.read_csv("data.csv", usecols=[0, 1, 3])

# имя выходного файла
output_file = "output.csv"

# сохраняем результат в новый csv
df.to_csv(output_file, index=False)

# открываем файл (Windows)
os.startfile(output_file)



print("Результат выборки столбцов:")
print(df)