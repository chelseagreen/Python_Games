import simplegui
import random

num_range = 100

def range100():
    print ""
    print "New game! The number is between 0 and 100."
    global secret_number
    secret_number = random.randrange(0, 100)
    global num_range
    global count 
    count = 0 
    num_range = 100
    return secret_number 

def range1000():   
    print ""
    print "New game! The number is between 0 and 1000."
    global secret_number
    secret_number = random.randrange(0, 1000)
    global count 
    count = 0 
    global num_range
    num_range = 1000
    
def input_guess(guess):
    print ""
    guess = int(guess)
    print "Your guess was ", guess,"."
    global count
    count +=1
    
    if (num_range == 100):
        print "You have", 7-count, "remaining guesses."
    else:
        print "You have", 10-count, "remaining guesses."
    
    if (secret_number > guess) and (count < 7):
        print "Guess higher, please."
    elif (secret_number < guess) and (count < 7):
        print "Guess lower, please."
    elif(secret_number == guess) and (count <= 7) and (num_range == 100):
        print "You are correct!! My number was ", secret_number,"."
        return range100()
    elif (secret_number > guess) and (count < 10) and (num_range == 1000):
        print "Guess higher, please."
    elif (secret_number < guess) and (count < 10) and (num_range == 1000):
        print "Guess lower, please."
    elif(secret_number == guess) and (count <= 10) and (num_range == 1000):
        print "You are correct!! My number was ", secret_number,"."
        return range1000()
    elif(count == 7):
        print "You have run out of guesses! Number was ", secret_number,"."
        return range100()
    elif(count == 10) and (num_range == 1000):
        print "You have run out of guesses! Number was ", secret_number,"."
        return range1000() 
    else:
        print "You guessed something not in range."

        
frame = simplegui.create_frame("Guess the Number", 200, 200)

frame.add_button("Range is [0,100)", range100)
frame.add_button("Range is [0, 1000)", range1000)

frame.add_input("Enter a guess:", input_guess, 50)

frame.start

range100()