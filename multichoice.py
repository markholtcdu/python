#Tests questions for Python week 1
#by Mark Holt
Score=0
questions=["What is the correct order for a program?","end"]
number=0
choiceA=["comments,initialise constants,request inputs, compute answer, display answer"]
choiceB=["comments,request inputs, initialise constants, compute answer, display answer"]
choiceC=["request inputs, initialise constants, compute answer, display answer,comments,"]
choiceD=["request inputs,  compute answer, initialise constants, display answer,comments,"]
correctAnswer=['A']
while questions[number]!="end":
    print(number+1," ",questions[number])
    print("A ",choiceA[number])
    print("B ",choiceB[number])
    print("C ",choiceC[number])
    print("D ",choiceD[number])
    answer=input ("enter your answer ")
    number +=1
