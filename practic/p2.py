'''
Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.
'''


sub1=int(input("Enter 1 Number : "))
sub2=int(input("Enter 2 Number : "))
sub3=int(input("Enter 3 Number : "))

result=sub1+sub2+sub3
per=(result/300)*100



if(per>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("pass")
else:
    print("Pass")  