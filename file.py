print("File Operation.....")
'''
file=open("l1.py","r")
text=file.read()
print(text)
file.close()



#write 
# Open the file in write mode 
f = open("this.txt", "w") 
# Write a string to the file 
f.write("this is nice") 
# Close the file 
f.close() 

# We can also use f.readline() function to read one full line at a time. 
#read 
#readline 

r – open for reading 
w - open for writing  
a - open for appending 
+  - open for updating. 
‘rb’ will open for read in binary mode. 
‘rt’ will open for read in text mode.

'''

#we can also use wih to open  read write file operation
with open("this.txt","r") as f:
    read=f.read()
print(read)    



