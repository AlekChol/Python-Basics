''' a program that prompts the user for the answer
 of 5+5 if the answer is 10,the program shuld display the message correct you got it 5+5 is 10
 otherwise the progrma should diplay 5+5 is not what the user input as
 answer but it should ouput the correct answer for the user

'''
print("what is 5+5")
answer=int(input())
if answer==10:
    print("Got it 5+5 is 10")
else:
    print("No 5+5 is not {} but the correct answer is 10".format(answer))
    

