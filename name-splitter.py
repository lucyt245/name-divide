fullName= input("What is your full name? ")
lengthOfFullName= len(fullName)
posOfSpace= fullName.find(" ")
initial = fullName[0:1]
surname = fullName[posOfSpace+1:lengthOfFullName]
print (initial, surname)
