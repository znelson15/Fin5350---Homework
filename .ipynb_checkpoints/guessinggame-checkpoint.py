answer = 'yes'
print ("Please, think of a number between 1 and 100. I am about to try to guess it in as few attempts as possible.")
while answer == "yes":
    NumOfTry = 1
    NumToGuess = 50
    LimitLow = 1
    LimitHigh = 100
    while NumOfTry != 0:
        try:
            print ("I try: ",NumToGuess)
            print ("Please type: 1 for my try is too high")
            print ("             2 for my try is too low")
            print ("             3 I guessed your number")
            HumanAnswer  = int (input("So did I guess right?" ))
            if 1 < HumanAnswer > 3:
                print ("Please enter a valid answer. 1, 2 and 3 are the valid choice")
                NumOfTry = NumOfTry + 1
            if HumanAnswer == 1:
                LimitHigh = NumToGuess
                print ("Hmm, so your number is between ",LimitLow, "and ", LimitHigh)
                NumOfTry = NumOfTry + 1
                print (NumOfTry, "attempt(s)")
                NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                if NumToGuess <= LimitLow:
                    NumToGuess = NumToGuess + 1
                if LimitHigh - LimitLow == 2:
                    NumToGuess = LimitLow + 1
            elif HumanAnswer == 2:
                LimitLow = NumToGuess
                print ("Hmm, so your number is between ",LimitLow, "and ", LimitHigh)
                NumOfTry = NumOfTry + 1
                print (NumOfTry, "attempt(s)")
                NumToGuess = int (((LimitHigh - LimitLow)/2) + LimitLow)
                if NumToGuess <= LimitLow:
                    NumToGuess = NumToGuess + 1
                if LimitHigh - LimitLow == 2:
                    NumToGuess = LimitLow + 1
            elif HumanAnswer == 3:
                print ("Woo hoo! I won")
                print("I guessed it in:", NumOfTry, "attempts.")
                NumOfTry = 0
        except:
            break
    else:
        answer = input ('Do you want to play again? (yes/no)')

else:
    print ("Thank you for playing. Goodbye")

