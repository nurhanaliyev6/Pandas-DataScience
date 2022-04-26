#selecting column names     Loc and Iloc

import pandas as pd
import numpy as np

m=np.random.randint(1,30,size=(10,3))
df=pd.DataFrame(m,columns=["var1","var2","var3"])

print(df)

#loc

print(df.loc[0:3])#based on dataframe's index

#iloc
print(df.iloc[0:3])#based on idex. Like in list,numpy

#-----------------------------------------------------
print("loc\n",df.loc[0:3,"var3"])

print("ILoc\n",df.iloc[0:3]["var3"])

#----------------------------------------------------------
#using if statement

#print(df[0:2]["var1","var2"])
#df[0:2]["var1","var2"]--->calismaz

print(df[0:2][["var1","var2"]])

#so let's if var1's values >5 or not
print("Values of var1")
print(df[df.var1>5]["var1"])

#---------------------------------------
df2=df[(df.var1>10) & (df.var2>7)].copy()
print("New df")
print(df2)
df2["var1"][1]=23
print("DF2")
print(df2)
print("DF")
print(df[(df.var1>10) & (df.var2>7)])
#--------------------------------------
print(df[df.var1>15][["var1","var2"]])#should be using fancy index

#----------------------------------------

#Join's
m=np.random.randint(1,30,size=(5,3))
df3=pd.DataFrame(m,columns=["var1","var2","var3"])
print(df3)

df4=df3+1
print(df4)

#df5=pd.concat([df3,df4])
#print(df5) #look at indexes. they are not in correct way

df5=pd.concat([df3,df4],ignore_index=True)
print(df5)#now, indexes are correct order:)

print(df4.columns)
print(df3.columns)
df3.columns=["var1","deg2","deg3"]
print(pd.concat([df4,df3])) #with nan
print(pd.concat([df4,df3],join="inner"))


#----------------------------------------------------

#more complex joins

dfa1=pd.DataFrame({'workers':["Nurhan","Anar","Rashad","Denzel"],
                   "group":["IT","Electronik","Chemistry","Acting"]})

dfa2=pd.DataFrame({'workers':["Rashad","Anar","Nurhan","Denzel"],
                   "start_date":[2018,2019,2019,1990]})


print(dfa1)
print(dfa2)

print("Join by autamatically without saying the column name")

print(pd.merge(dfa1,dfa2))
print(pd.merge(dfa1,dfa2,on="workers"))

print("-------------------------------------------")

dfa3=pd.merge(dfa1,dfa2)
print(dfa3)

dfa4=pd.DataFrame({"group":["IT","Electronik","Chemistry","Acting"],
                   "director":["Hafiz","Nizami","Abel","Wall"]})


print(pd.merge(dfa3,dfa4))


#------------------------------------------------

print("Aggregate and Grouping functions")
import seaborn as sns

data=sns.load_dataset("planets")
print(data.tail(5))
print(data.shape)
print(data["mass"].mean())
print(data["mass"].std())


print("Mean of Planets'method")
print(data.groupby("method")["orbital_period"].mean())

#ALL OF Explanatory STATISTICAL FUNCTIONS
print("ALL OF Explanatory STATISTICAL FUNCTIONS")
print(data.describe().T)

#-----------------------------------------------
print("Grouping")
print("-------------")
print("-------------")
print("-------------")

data=pd.DataFrame({"groups":["A","B","C","A","B","C"],
                   'data':[10,11,52,23,43,55]},columns=['groups',"data"])

print(data)

print(data.groupby("groups").mean())
print(data.groupby("groups").sum())









































