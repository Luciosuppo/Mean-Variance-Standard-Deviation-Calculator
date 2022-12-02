import numpy as np
import pandas as pd 

def calculate(list):
    if (len(list)==9):
        calculations={}                         #create dict
        colmean=[]
        rowmean=[]
        colvar=[]
        rowvar=[]
        colstddev=[]
        rowstddev=[]
        colmax=[]
        rowmax=[]
        colmin=[]
        rowmin=[]                           #create lists for rows and columns
        colsum=[]
        rowsum=[]
        array=np.asarray(list)                  #convert list to array
        matrix=np.reshape(array,(3,3))          #create matrix
        matrix2=matrix.transpose()              #transpos matrix for columns values
        for i in range(0,(len(matrix2))):
            a=matrix2[i].mean()
            colmean.append(a)
        for i in range(0,(len(matrix))):
            a=matrix[i].mean()                  #append mean values 
            rowmean.append(a)
        m=array.mean()
        calculations['mean']=[colmean,rowmean,m]
        for i in range(0,(len(matrix2))):
            a=matrix2[i].var()
            colvar.append(a)
        for i in range(0,(len(matrix))):
            a=matrix[i].var()                  #append variance values 
            rowvar.append(a)
        v=np.var(array)
        calculations['variance']=[colvar,rowvar,v]
        for i in range(0,(len(matrix2))):
            a=matrix2[i].std()
            colstddev.append(a)
        for i in range(0,(len(matrix))):
            a=matrix[i].std()                  #append std dev values 
            rowstddev.append(a)
        s=np.std(array)
        calculations['standard deviation']=[colstddev,rowstddev,s]
        colmax=[]
        rowmax=[]
        for i in range(0,(len(matrix2))):
            a=matrix2[i].max()
            colmax.append(a)
        for i in range(0,(len(matrix))):
            a=matrix[i].max()                  #append max values 
            rowmax.append(a)
        max=array.max()
        calculations['max']=[colmax,rowmax,max]
        colmin=[]
        rowmin=[]
        for i in range(0,(len(matrix2))):
            a=matrix2[i].min()
            colmin.append(a)
        for i in range(0,(len(matrix))):
            a=matrix[i].min()                  #append min values 
            rowmin.append(a)
        min=array.min()
        calculations['min']=[colmin,rowmin,min]
        colsum=[]
        rowsum=[]
        for i in range(0,(len(matrix2))):
            a=matrix2[i].sum()
            colsum.append(a)
        for i in range(0,(len(matrix))):
            a=matrix[i].sum()                  #append sum values 
            rowsum.append(a)
        sum=array.sum()
        calculations['sum']=[colsum,rowsum,sum]
    else:
        raise ValueError('List must contain nine numbers.')

    return calculations