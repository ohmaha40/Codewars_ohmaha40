#? https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

# Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.
#Example

#create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
#The returned format must be correct in order to complete this challenge.

#Don't forget the space after the closing parentheses!
#! Eigene Lösung
n = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
def create_phone_number(n):
    antwort = ""
    for i in range(len(n)):
        if i == 0:
            antwort += "("+ str(n[i])
        elif i == 3:
            antwort += ") "
            antwort += str(n[i])
        elif i == 6:
            antwort += "-"
            antwort += str(n[i])
        else: 
            antwort += str(n[i])
    return antwort
print(create_phone_number(n))

#! perfekte Lösung durch Format
def create_phone_number_analyse1(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
print(create_phone_number_analyse1(n))

#! noch eine sinnvolle Lösung
def create_phone_number_analyse2(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
print(create_phone_number_analyse2(n))


        
    

