#rockpaperscissors
#Aiden Krahn

import random

def rockwin():
    while True:
        fist = input("Rock, Paper, or Scissors?(r to see record) ")
        fool = random.randint(1,3)
        if fool == 1:
            foul = 'rock'
            
        elif fool == 2:
            foul = 'paper'
            
        elif fool == 3:
            foul = 'scissors'
            
        record = open('record.txt', 'a')
        if fist == 'r':
            record.close()
            cwc = open('record.txt', 'r')
            sonichu = cwc.read()
            print(sonichu)
            cwc.close()
             
        elif fist == 'rock':
            if foul == 'rock':
                print("Tie")
                record.write('Tie, rock/rock\n')
                
            elif foul == 'paper':
                print("You Lost")
                record.write("Loss, rock/paper\n")
                
            elif foul == 'scissors':
                print("You Won")
                record.write("Win, rock/scissors\n")
                
        elif fist == 'paper':
            if foul == 'rock':
                print("You Won")
                record.write("Win, paper/rock\n")
                
            elif foul == 'paper':
                print("Tie")
                record.write("Tie, paper/paper\n")
                
            elif foul == 'scissors':
                print("You Lost")
                record.write("Loss, paper/scissors\n")
                
        elif fist == 'scissors':
            if foul == 'rock':
                print("You Lost")
                record.write('Loss, scissors/rock\n')
                
            elif foul == 'paper':
                print("You Won")
                record.write('Win, scissors/paper\n')
                
            elif foul == 'scissors':
                print("Tie")
                record.write('Tie, scissors/scissors\n')
                
        record.close()
        brek = input('Quit? (y/n)  ')
        if brek == 'y':
            break
        
        elif brek == 'n':
            pass
        
rockwin()
            
        
            