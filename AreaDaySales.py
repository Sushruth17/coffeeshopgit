import pandas as pd
data_root_folder = 'res\\data\\'
data = pd.read_csv(data_root_folder+'sales.csv', encoding="cp1252")
MON_VIJ = list(data['Mon.Vijayangar'])
TUE_VIJ = list(data['Tue.Vijayangar'])
WED_VIJ = list(data['Wed.Vijayangar'])
THU_VIJ = list(data['Thu.Vijayangar'])
FRI_VIJ = list(data['Fri.Vijayangar'])
SAT_VIJ = list(data['Sat.Vijayangar'])
SUN_VIJ = list(data['Sun.Vijayangar'])
MON_MGR = list(data['Mon.MG Road'])
TUE_MGR = list(data['Tue.MG Road'])
WED_MGR = list(data['Wed.MG Road'])
THU_MGR = list(data['Thu.MG Road'])
FRI_MGR = list(data['Fri.MG Road'])
SAT_MGR = list(data['Sat.MG Road'])
SUN_MGR = list(data['Sun.MG Road'])
data