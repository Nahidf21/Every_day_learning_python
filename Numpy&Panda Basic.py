import numpy as np
a=np.array([[1,2,3,4,5,6,7],[1,2,3,4,5,3,2]])
a[1,0:3]

from pandas import Series
import pandas as pd

gool= Series(["Nahid FErdous",30,"United State", "Texas Tech University"],
             index=["Name :","Age :","Country :","University :"])
gool

lists= np.array(["a","b","c","d","e","f"])

dec= {"Name":["nahid","ferdous","MARZIA","khan","abid","khan"], "Age": [28,27,28,29,33,
                                                                        30]}
df= pd.DataFrame(dec, index= lists)
df

### lets change the columns name :

df.columns=["nam","ag"]
df

### lets change the index name :

df.index=(1,2,3,4,5,6)
df

df.rename(columns={"ag":"Age","nam":"Name"},index={1:"a",2:"b"},inplace=True)
df1=df.copy()
df1.drop("Name", axis=1)
df1.drop(["a","b"], axis=0, inplace=True)
df1 

df.iloc[1,]
df.loc["a",]


