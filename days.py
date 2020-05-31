import pandas as pd
data_root_folder = 'res\\data\\'
data = pd.read_csv(data_root_folder+'data_source.csv', encoding="cp1252")
MON = list(data['MON'])
TUE = list(data['TUE'])
WED = list(data['WED'])
THU = list(data['THU'])
FRI = list(data['FRI'])
SAT = list(data['SAT'])
SUN = list(data['SUN'])