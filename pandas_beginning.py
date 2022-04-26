#pandas is widely used for data analyzing and manipulation

#mostly used for Panel data. financial works

#pandas's datatype is not fixed like numpy's datatype

import pandas as pd
import numpy as np




#DataType----------------------------------------

#series
series=pd.Series([10,22,33,41,35])
print("Seires")
print(series)
print("Type of series: ",type(series))
print("Information about index: ",series.axes )
print("Type of: ",series.dtype)
print("Size of: ",series.size)
print("Dimesnion of: ",series.ndim)

print("Values :")
print(series.values)
print(series.head(2))

#naming the index-------------------------------------

dif_series=pd.Series([554,2232,12,665,222,32,2345,7878])
print(dif_series.axes)

indexed_series=pd.Series([554,2232,12,665,222,32,2345,7878], index=['f',"s",'t','f','f1','s','n','e'])

#print(indexed_series["s":"s"])# will not happen because not unique

#print(indexed_series["f":"t"])#again


#-------------------------------------------------------

diction={"name":"Nurhan","age":20,"place":"Sum"}
print(pd.Series(diction))
b=pd.Series(diction)
a=pd.concat([b,b])
print(a)

#-------------------------------------------------------

#create series from np array

arr=np.arange(0,10,3)

ser=pd.Series(arr)
print(ser)

print(ser[0])
print(ser[0:3])

#--------------------------------------------------------

print(b.index)
print("Values: ",b.values)
print(b.keys)
print(list(b.items()))
print("name" in b)

print(b[["name","place"]])
print(b["name":"place"])

#--------------------------------------------------------------------------------------------------------------------
#DATAFRAME

print("----------------------------------------------------------------------------")

arr2=[1995,2004,2013,2002]
fourology=pd.DataFrame(arr2,columns=["years of before fourology"])
print(fourology)


m=np.arange(1,10).reshape((3,3))
new_triology=pd.DataFrame(m,columns=["var1","var2","var3"])
print(new_triology)

print("type of ",type(new_triology))
print("type of ",new_triology.axes)

#new_triology["var1"]="x1"# it doesn't change column name to x1. it just changes all values to x1

print(new_triology.shape)
print(new_triology.ndim)
print(new_triology.values)#numpy array
print(type(new_triology.values))

#---------------------------------------------

s1=np.random.randint(10,size=5)
s2=np.random.randint(10,size=5)
s3=np.random.randint(10,size=5)
diction={"s1":s1,"s2":s2,"s3":s3}
df=pd.DataFrame(diction)

#df=pd.DataFrame([s1,s2,s3],columns=["s1","s2","s3"])# doesn't work why?????
print(df)
df.index=["a","b","c","d","e"]
print(df)
print(df["c":"e"])


#delete
df.drop("a",axis=0,inplace=True)#axis 0-->row 1-->column
print(df)

#fancy delete
l=["c","e"]

print(df.drop(l,axis=0))

# column

l=["s1","s2","var1","var2"]
for i in l:
    print(i in df.columns)

#create new column
df["s4"]=df["s1"]*df["s2"]
print(df)

#delete column
df.drop("s4",axis=1,inplace=True)
print(df)

l=["s2","s3"]
print(df.drop(l,axis=1))
