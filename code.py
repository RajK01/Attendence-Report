import csv
import os
import glob
import csv
import codecs

path = os.getcwd()
csv_files =glob.glob(os.path.join(path, "*.csv"))

temp = []
S_name = []
is_Present = []
is_Absent = []
percentage = []
final_Attendancece = []

n = 0 # total no of working days

for file in csv_files:
    csv_reader = csv.reader(codecs.open(file, 'r', 'utf-16'))

    next(csv_reader)  # next will redirect to next line
    
    for line in csv_reader:
        row = line[0].split("\t")[0]
        
        if('Guest' not in line[0] and row != 'Domnic S'):
            temp.append(row)
    
    #creating dictionary to remove redundant names
    temp = list(dict.fromkeys(temp))
    temp.sort()

    for x in temp:
        if (x in S_name):
            ind = S_name.index(x)
            is_Present[ind] = is_Present[ind] + 1
        
        else:
            S_name.append(x)
            is_Present.append(1)
            is_Absent.append(0)
            percentage.append(0)
    
    n = n + 1
    temp.clear() 


for i in range(len(is_Present)):
    is_Absent[i] = n - is_Present[i]
    percentage[i] = round((is_Present[i]/n)*100,2)

for i in range(len(S_name)):
    S_name[i] = S_name[i].upper()

for i in range(len(S_name)):
    final_Attendancece.append([S_name[i],is_Present[i],is_Absent[i],percentage[i]])

dict={}
for i in range (len(final_Attendancece)):
    dict[final_Attendancece[i][0]]=[]
    dict[final_Attendancece[i][0]].append(final_Attendancece[i][1])
    dict[final_Attendancece[i][0]].append(final_Attendancece[i][2])
    dict[final_Attendancece[i][0]].append(final_Attendancece[i][3])
