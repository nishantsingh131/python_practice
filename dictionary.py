person={

    "person":"Nish",
    "Age":25,
    "Place":"India"
}

print(person.keys())
print(person.values())
print(person.items())
person.update({"Place" :"patna"})
print(person.get("Placse")) # Print None as error 
print(person["Placess"]) # Print keyerror as error 