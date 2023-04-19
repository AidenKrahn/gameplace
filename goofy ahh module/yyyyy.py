import random
import cardyugioh
import groceryapocalypse
import rps
import clue
import carmesandiego


print("Welcome to the Game Place!")
print("I'm Michael Snyder, if you want to play something, just let me know.")

def main():
    while True:
        print('''yugioh
grocery
rps
clue
carmen
        ''')
        choose = input("What to play?(n to stop, idk for random)  ")
        
        if choose == 'yugioh':
            cardyugioh.maintrue()
            
        elif choose == 'grocery':
            groceryapocalypse.main()

        elif choose == 'rps':
            rps.rockwin()
            
        elif choose == 'clue':
            clue.main()
            
        elif choose == 'carmen':
            carmensandiego.main()
            
        elif choose == 'n':
            break
        
        elif choose == 'idk':
            spock = random.randint(1, 5)
            if spock == 1:
                cardyugioh.maintrue()
                    
            elif spock == 2:
                groceryapocalypse.main()
                
            elif spock == 3:
                rps.rockwin()
                
            elif spock == 4:
                clue.main()
                
            elif spock == 5:
                carmensandiego.main()

main()