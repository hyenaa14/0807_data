import pandas as pd

data= pd.read_csv('./new/pima-indians-diabetes.data.csv')
col_names=['preg','plas','pres','skin','test','mass','pedi','age','class']

print(data['preg'])