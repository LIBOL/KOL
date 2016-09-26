import sys
import os

data='a9a'
train=data+'_train'
test=data+'_test'
train_set=[train,'train0','train1','train2','train3','train4','train5','train6','train7','train8','train9','train10']
for i in range(0,10):
    cmd='rand.py '+ train_set[i]+' '+ train_set[i+1]
    os.system(cmd)
    cmd='KOL.exe -i '+ train_set[i]+" -t "+test+'  -opt kernel-ogd >>"reslut_project.txt'
    os.system(cmd)


f0 = open("reslut_project.txt")
raw=f0.read()
sum=0
for i in range(0,10):
    indexleft=raw.find('Test acuracy:')
    indexright=indexleft+20
    sss=raw[indexleft+13:indexright]
    raw=raw[indexright+10:]
    accu=float(sss)
    sum=sum+accu
    print(accu)
    
accurate=sum/10
print("\n")
print("test accuracy")
print(accurate)
print("\n")


f0 = open("reslut_project.txt")
raw=f0.read()
sum=0
for i in range(0,10):
    indexleft=raw.find('Learning time: ')
    indexright=indexleft+22
    sss=raw[indexleft+15:indexright]
    raw=raw[indexright+10:]
    accu=float(sss)
    sum=sum+accu

accurate=sum/10
print("\n")
print("learning time:")
print(accurate)
print("\n")

f0 = open("reslut_project.txt")
raw=f0.read()
sum=0
for i in range(0,10):
    indexleft=raw.find('Test time: ')
    indexright=indexleft+18
    sss=raw[indexleft+11:indexright]
    raw=raw[indexright+10:]
    accu=float(sss)
    sum=sum+accu
    
accurate=sum/10
print("\n")
print("Test time")
print(accurate)
print("\n")
f0.close()
#os.remove('reslut1.txt')


