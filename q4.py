'''
Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old. 

'''

 
file=open("table.txt","w")

for i in range(1,11):
    file.write(2*i)
    file.close()

    