# csv(Comma Seperated Value : 쉼표로 구분된 값)
import csv

# f = open('sspy1.csv','w',encoding='utf-8',newline='')
# sspy1 = csv.writer(f)
# sspy1.writerow(["name","cell","email","01029394293","sspy1","CS"])
# f.close()   

# f= open('sspy1.csv','r',encoding='utf-8')
# sspy1 = csv.reader(f)
# for line in sspy1:
#     for d in line:
#         print(d)
# f.close()   

f = open('sspy1_impsy.csv','a',encoding='utf-8',newline='')
sspy1 = csv.writer(f)
sspy1.writerow(["name","cell","email","01029394293"])
f.close()   

