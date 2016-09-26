import sys
import os
import platform


train_file ='german'####training file name
eta=['1','0.1','0.01','0.001','0.0001']#####
gamma=['1','0.1','0.01','0.001','0.0001']#####



fold_num=5
count_cmd = 'wc -l %s' %train_file
count_handler = os.popen(count_cmd)
line_num = int(count_handler.read().split()[0])
count_handler.close()

split_line_num = int(line_num / fold_num)

split_list = []
for k in range(0,fold_num):
    file_name = train_file + '_cva' + chr(ord('a') + k)
    os.system('rm -f %s' %file_name)
    split_list.append(file_name)

split_cmd = 'split -l {0} {1} {2}_cv'\
            .format(split_line_num,train_file, train_file) 

os.system(split_cmd)
    
f0 = open(split_list[0])
raw0=f0.read()
f0.close()
f1 = open(split_list[1])
raw1=f1.read()
f1.close()
f2 = open(split_list[2])
raw2=f2.read()
f2.close()
f3 = open(split_list[3])
raw3=f3.read()
f3.close()
f4 = open(split_list[4])
raw4=f4.read()
f4.close()
train_list=['train0','train1','train2','train3','train4']
output_file = open(train_list[0], 'w')
output_file.write(raw1+raw2+raw3+raw4)
output_file.close()

output_file = open(train_list[1], 'w')
output_file.write(raw0+raw2+raw3+raw4)
output_file.close()

output_file = open(train_list[2], 'w')
output_file.write(raw0+raw1+raw3+raw4)
output_file.close()

output_file = open(train_list[3], 'w')
output_file.write(raw0+raw1+raw2+raw4)
output_file.close()

output_file = open(train_list[4], 'w')
output_file.write(raw0+raw1+raw2+raw3)
output_file.close()

del raw0
del raw1
del raw2
del raw3
del raw4


for k in range(len(gamma)):
    for j in range(len(eta)):
        for i in range(0,5):
            command="KOL -i "+train_list[i]+" -opt kernel-ogd -t "+split_list[i]+" -eta "+eta[j]+' -gamma '+gamma[k]+' >>result.txt'####
            os.system(command)
    
        f0 = open("result.txt")
        raw=f0.read()

        sum=0
        for i in range(0,5):
            indexleft=raw.find('Test acuracy:')
            indexright=indexleft+20
            sss=raw[indexleft+13:indexright]
            raw=raw[indexright+10:]
            accu=float(sss)
            sum=sum+accu

        accurate=sum/5
        print(gamma[k]+'\t'+eta[j]+"\t"+str(accurate))
        f0.close()
        os.remove("result.txt")

for i in range(0,5):   
    os.remove(train_list[i])
    os.remove(split_list[i])
