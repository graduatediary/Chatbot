import os

#print(os.listdir('.'))

os.chdir(r'C:\Users\student\chatbot\day1\list')

#print(os.getcwd())

#print(os.listdir('.'))

List=os.listdir('.')

for i in List:
    os.rename(i,"SSAFY"+i)