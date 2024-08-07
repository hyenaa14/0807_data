import numpy as np
my_index=['A','B','C']
my_columns=['이름','나이','성별']
my_data=numpy.array([['Alice,'Bob','홍길동'],[25,30,26],['남','여','남']])

df=pd.DataFrame(my_data, index=)
print(my_data)
df=pd.DataFrame(my_data,index=my_index,columns=my_columns)
#print(df)
