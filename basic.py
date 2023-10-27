import time
import random

no=random.randrange(1,10)
name=input("Enter Your Name: ")
print("Hello",name,"!")
print("Welcome to Guessing Game")
print("Guess a number in range 1-10 only: ")
sol=0
move=1
chances=4
while True:
    while chances>0:
        n=int(input())
        chances-=1
        if no==n:
            print("Hurayyyyy",name,)
            print("you guessed it in",move,"move!")
            sol=1
            time.sleep(2)
            break
        else:
            if no>n:
                print("you guessed it lower.")
                time.sleep(1)
            else:
                print("you guessed it higher.")
                time.sleep(1)
            print("you still have",chances," more chances")
        print("Guess Again")
        move+=1
    if sol==0:
        print("Sorry",name)
        print("you don't have more chances")
        print("you loose the game!") 
        time.sleep(2)
        print("DO you want to play it again?")
        print("if yes SELECT '1' else SELECT '0' ")
        time.sleep(1)
        play_again=int(input())
    else:
        print("DO you want to play it again?")
        print("if yes SELECT '1' else SELECT '0' ")
        time.sleep(1)
        play_again=int(input())
    if play_again==0:
        print("THANKS FOR PLAYING")
        break
    else:
        chances=4
        move=1 
        time.sleep(1)
        print("Guess a number in range 1-10 only")