'''
COS 121
Homework #3
By Tristin Friend
Due 09/30/2024
'''

numCorrect = 0
numQuestion = 0


# Begining of quiz
print("Welcome to your history quiz! This quiz will consist of 15 questions. Are you ready? ")


print("Question 1: What is the shorest war in recorded history?")
# The Anglo-Zanibar War of 1896, lasting only 30 minutes

u = input(":") 
u = u.upper()
u = u.strip()

if u == "ANGLO-ZANIBAR WAR":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 2: What was the first living creature to enter space?")
# It was a dog named Laika. 

u = input(":") 
u = u.upper()
u = u.strip()

if u == "LAIKA":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 3: Who was the longest ruling monarch in Enlish history?")
# Queen Elizabeth II, ruling for 66 years. 


u = input(":") 
u = u.upper()
u = u.strip()

if u == "QUEEN ELIZABETH II":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 4: Which famous Egyptian leader was actually Greek?")
# Cleopatra

u = input(":") 
u = u.upper()
u = u.strip()

if u == "CLEOPATRA":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 5: In the British colony of Jamestown, what was the their greatest cashcrop?")
# tabacco 

u = input(":") 
u = u.upper()
u = u.strip()

if u == "TABACCO":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 6: The Declaration of Independence was sign on _________.")
# July 4, 1776
print("A: October 4, 1786")
print("B: July 4, 1776")
print("C: Febuary 6, 1779") 
print("D: March 8, 1772") 

u = input(":") 
u = u.upper()
u = u.strip()

if u == "B":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 7: __________ is the strong sense of loyalty to a state or section instead of a country.")
# Sectionalism
print("A: Popular Sovereignty")
print("B: Manifest Destiny")
print("C: Unalienable Rights")
print("D: Sectionalism")


u = input(":") 
u = u.upper()
u = u.strip()

if u == "D":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 8: _____________ were people who opposed the Constitution.")
# Antifederalists
print("A: Federalists")
print("B: Republicans")
print("C: Antifederalists")
print("D: Tories") 


u = input(":") 
u = u.upper()
u = u.strip()

if u == "C":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 9: The ___________ was one of the biggest influences on the Constitution.")
# Magna Carta
print("A: Declaration of Independence")
print("B: Magna Carta")
print("C: Articles of Confederation")
print("D: Monroe Docterine") 


u = input(":") 
u = u.upper()
u = u.strip()

if u == "B":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 10: After King ____________ refused the Olive Branch Petition, the colonies finally broke away from England.")
# George III
print("A: George III")
print("B: George Washington") 
print("C: Alfred")
print("D: Peter") 

u = input(":") 
u = u.upper()
u = u.strip()

if u == "A":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 11: Famous philospher __________ personally taught Alexander the Great.")
# Aristotle

u = input(":") 
u = u.upper()
u = u.strip()

if u == "ARISTOTLE":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 12: __________ cities were named after Alexander the Great.")
# 70

u = input(":") 
u = u.upper()
u = u.strip()

if u == "70":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 13: The __________ dynasty in China outlawed sea trade.")
# Ming Dynasty


u = input(":") 
u = u.upper()
u = u.strip()

if u == "MING DYNASTY":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 14: _________ founded the Akkadian Empire.")
# Sargon the Great


u = input(":") 
u = u.upper()
u = u.strip()

if u == "SARGON THE GREAT":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1



print("Question 15: The Kingdom of _________ gave early rise to the Abrahamic religion.")
# Israel


u = input(":") 
u = u.upper()
u = u.strip()

if u == "ISRAEL":
    print("Correct")
    numCorrect = numCorrect + 1
numQuestion = numQuestion +1

print(f"Number correct = {numCorrect}")


# End of quiz

print(f"The number you got correct was: {numCorrect}")

score = numCorrect/numQuestion * 100

print(f"Your score is: {numCorrect}/{numQuestion} ({score:.0f}%)")


if (score >= 90):
    print("A")
elif (score >= 80):
    print("B")
elif (score >= 70): 
    print("C") 
elif (score >= 60): 
    print("D") 
else: 
    print("F") 