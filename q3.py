#Write a program to read the text from a given file ‘poems.txt’ and find out 
#whether it contains the word ‘twinkle’. 


file=open("p.txt","r")
read=file.read()
if 'this' in read:
    print("Found : ")
else:
    print("Not Found :")    
