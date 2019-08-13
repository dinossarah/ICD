#!/usr/bin/env python
# coding: utf-8

# In[10]:


from pandas.io import sql
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('SEMARHFILE.xlsx') #Reads, index_col = 'ANO PORTARIA'

df.sort_values('ANO PORTARIA',ascending=False)

mean_val = pd.to_numeric(df['VZ CONC. (m3/s)'], errors='coerce').mean() #update

df['VZ CONC. (m3/s)'] = pd.to_numeric(df['VZ CONC. (m3/s)'], errors='coerce') #update

df['COMPARATIVO'] = df.apply(lambda x: 'MENOR QUE A MÉDIA' if x['VZ CONC. (m3/s)'] <= mean_val else 'MAIOR QUE A MÉDIA', axis=1)

print(df.iloc[:,[10,28,29,6,15,9,33]])
print('Média de vazões:', mean_val, 'm³/s')


# In[24]:


import pandas as pd
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
df1 = pysqldf("SELECT * FROM df LIMIT 15")

print(pysqldf('SELECT * FROM df1'))
print("_______________________")

print(pysqldf("""SELECT DATA EXTRATO, count(*) as 'TotalNo'
              FROM df
              GROUP BY county
              HAVING COUNT(*) > 1000
              ORDER BY 1
              """))


# In[6]:


df.to_sql(name=database, con=conn, if_exists = 'replace', index=False, flavor = 'mysql')


# In[ ]:


DataFrame.to_sql(name, con, flavor='sqlite', schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None)

