list=[
    
    "Make a lot of money "
    "buy now"
    "subscribe this"
    "click this"
]
user=input("Enert youe Comment")
for word in list:
    if(word.lower() in user.lower()):
        print("SPAM !")
        break
    else:
        print("Not Spam")    