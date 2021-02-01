''' write a program to prompt for a scrore between 0.0 to 1.0 . If the score is out of
range, print an error message. IF the score is between 0.0 to 1.0, print a grade. '''

answer = "y"
while (answer == "y"):
    try : 
            score  = float(input("Enter score: "))
            if (score == 10.0): print("Bad score")
            elif (score >= 0.9): print("A")
            elif(score >= 0.8): print("B")
            elif(score >= 0.7): print("C")
            elif(score >= 0.6): print("D")
            elif (score < 0.6): print("F")
    except :
        print("Bad score")

    answer = (str(input("Do you want to keep going ? type y for yes and n for no : " )))
