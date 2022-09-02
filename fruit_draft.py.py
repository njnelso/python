

#Two teams lists of fruit stored in these variables
teamA = []
teamB = []

#Intro
print('\n')
print("Today we have two teams taking part in the 2022 Fruit Draft: User1 picking for Team A and User2 picking for Team B.")
print('\n')

#First Round
oneA = input("User1 will have first draft pick: What fruit are you picking? ")
teamA.append(oneA)
print("\n")

oneB = input("User2 will have the second draft pick: What fruit are you picking? ")
teamB.append(oneB)
print("\n")

#Second Round
twoA = input("Round 2: User1, what fruit are you picking? ")
teamA.append(twoA)
print("\n")

twoB = input("User2, what fruit are you picking? ")
teamB.append(twoB)
print("\n")

#Third Round
threeA = input("Round 3: User1, what fruit are you picking? ")
teamA.append(threeA)
print("\n")

threeB = input("User2, what fruit are you picking? ")
teamB.append(threeB)
print("\n")

#Fourth Round
fourA = input("Round 4: User1, what fruit are you picking? ")
teamA.append(fourA)
print("\n")

fourB = input("User2, what fruit are you picking? ")
teamB.append(fourB)
print("\n")

#Fifth Round
fiveA = input("Round 5 and Final Round: User1, what fruit are you picking? ")
teamA.append(fiveA)
print("\n")

fiveB = input("User2, what fruit are you picking? ")
teamB.append(fiveB)
print("\n")

#Draft Results
print("Team A" + "\n")
print(*teamA, sep='\n')
print("\n" + "vs." + "\n")
print("Team B" + "\n")
print(*teamB, sep='\n')
print("\n")

#Who is the winner of this match? The audience will decide.
winner = input("Now to the audience, which team is the winner, A or B? ")

if winner == "A":
    print("Team A is the winner!!!")

elif winner == "B":
    print("Team B is the winner!!!")

else:
    print("Please select either \'A\' or \'B\': ")

print("\n")