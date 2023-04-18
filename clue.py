#--------
#Clue
#-------
#Aiden Krahn
#--------

import random
#lists&variables
adolfhand = []
phand = []
evahand = []
killer = []

o = False
x = True
n = o
void = o

green = ['green', o]
mustard = ['mustard', o]
white = ['white', o]
peacock = ['peacock', o]
plum = ['plum', o]
scarlett = ['scarlett', o]

billiard = ['billiard', o, 100]
study = ['study', o, 100]
entrance = ['entrance', o, 100]
music = ['music', o, 100]
lounge = ['lounge', o, 100]
dining = ['dining', o, 100]
greenhouse = ['greenhouse', o, 100]
library = ['library', o, 100]
kitchen = ['kitchen', o, 100]

void = ['void', o, 0]

gun = ['gun', o]
candlestick = ['candlestick', o]
rope = ['rope', o]
dagger = ['dagger', o]
pipe = ['pipe', o]
wrench = ['wrench', o]


people = [green, mustard, white, peacock, plum, scarlett]
places = [billiard, study, entrance, music, lounge, dining,
          greenhouse, library, kitchen]
things = [gun, candlestick, rope, dagger, pipe, wrench]
sus = []
fulllist = [green, mustard, white, peacock, plum, scarlett,
            billiard, study, entrance, music, lounge, dining,
          greenhouse, library, kitchen, gun, candlestick, rope,
            dagger, pipe, wrench]

loc = [billiard, study, entrance, music, lounge, dining,
          greenhouse, library, kitchen]

pope = [green, mustard, white, peacock, plum, scarlett]

varsol = [gun, candlestick, rope, dagger, pipe, wrench]

imhere = loc[random.randint(0, len(loc)-1)]
imhere[2] = 0
who = green
what = gun
proms = billiard
finala = []

#defenitions
def dst():
    global imhere
    if billiard[2] == 0:
        study[2] = 15
        entrance[2] = 15
        music[2] = 5
        lounge[2] = 22
        dining[2] = 14
        greenhouse[2] = 6
        library[2] = 3
        kitchen[2] = 16
        imhere = loc[0]
        
    elif study[2] == 0:
        billiard[2] = 15
        entrance[2] = 10
        music[2] = 16
        lounge[2] = 16
        dining[2] = 18
        greenhouse[2] = 18
        library[2] = 6
        kitchen[2] = 1
        imhere = loc[1]
        
    elif entrance[2] == 0:
        billiard[2] = 15
        study[2] = 9
        music[2] = 12
        lounge[2] = 7
        dining[2] = 7
        greenhouse[2] = 18
        library[2] = 6
        kitchen[2] = 18
        imhere = loc[2]
        
    elif music[2] == 0:
        billiard[2] = 5
        study[2] = 16
        entrance[2] = 12
        lounge[2] = 14
        dining[2] = 6
        greenhouse[2] = 4
        library[2] = 11
        kitchen[2] = 6
        imhere = loc[3]
        
    elif lounge[2] == 0:
        billiard[2] = 21
        study[2] = 16
        entrance[2] = 7
        music[2] = 14
        dining[2] = 3
        greenhouse[2] = 1
        library[2] = 13
        kitchen[2] = 18
        imhere = loc[4]
        
    elif dining[2] == 0:
        billiard[2] = 13
        study[2] = 18
        entrance[2] = 7
        music[2] = 6
        lounge[2] = 3
        greenhouse[2] = 17
        library[2] = 13
        kitchen[2] = 10
        imhere = loc[5]
        
    elif greenhouse[2] == 0:
        billiard[2] = 5
        study[2] = 18
        entrance[2] = 18
        music[2] = 4
        lounge[2] = 1
        dining[2] = 17
        library[2] = 13
        kitchen[2] = 18
        imhere = loc[6]
        
    elif library[2] == 0:
        billiard[2] = 3
        study[2] = 6
        entrance[2] = 6
        music[2] = 11
        lounge[2] = 13
        dining[2] = 15
        greenhouse[2] = 13
        kitchen[2] = 21
        imhere = loc[7]
        
    elif kitchen[2] == 0:
        billiard[2] = 16
        study[2] = 1
        entrance[2] = 18
        music[2] = 6
        lounge[2] = 18
        dining[2] = 10
        greenhouse[2] = 18
        library[2] = 20
        imhere = loc[8]
    
    return imhere

def move():
    global varsol
    global imhere
    global loc
    mvm = random.randint(2,12)
    print(f'You can move- {loc}')
    print(f"You can move {mvm} spaces.")
    where = input("Where would you like to go?  ")
    if where == 'billiard':
        wwhere = loc[0]
        
    elif where == 'study':
        wwhere = loc[1]
        
    elif where == 'entrance':
        wwhere = loc[2]
        
    elif where == 'music':
        wwhere = loc[3]
        
    elif where == 'lounge':
        wwhere = loc[4]
        
    elif where == 'dining':
        wwhere =  loc[5]
        
    elif where == 'greenhouse':
        wwhere = loc[6]
        
    elif where == 'library':
        wwhere = loc[7]
        
    elif where == 'kitchen':
        wwhere = loc[8]
        
    else:
        wwhere = loc[random.randint(0,8)]
        if wwhere == imhere:
            wwhere = loc[random.randint(0,8)]
            if wwhere == imhere:
                wwhere = loc[random.randint(0,8)]
                if wwhere == imhere:
                    wwhere = loc[random.randint(0,8)]
        
        
    loc[0][2] -= mvm
    loc[1][2] -= mvm
    loc[2][2] -= mvm
    loc[3][2] -= mvm
    loc[4][2] -= mvm
    loc[5][2] -= mvm
    loc[6][2] -= mvm
    loc[7][2] -= mvm
    loc[8][2] -= mvm
    if wwhere[2] <= 0:
        loc[0][2] += 100
        loc[1][2] += 100
        loc[2][2] += 100
        loc[3][2] += 100
        loc[4][2] += 100
        loc[5][2] += 100
        loc[6][2] += 100
        loc[7][2] += 100
        loc[8][2] += 100
        wwhere[2] -= 100
        wwhere[2] = 0
        dst()
        print(f"You are in {imhere}.\n")
        return wwhere
        
    else:
        imhere = void
        return imhere


def accuse():
    print(pope)
    whom = input("Who are you guessing?  ")
    if whom == 'green':
        who = green
        
    elif whom == 'mustard':
        who = mustard
        
    elif whom == 'white':
        who = white
        
    elif whom == 'peacock':
        who = peacock
        
    elif whom == 'plum':
        who = plum
        
    elif whom == 'scarlett':
        who = scarlett
        
    print(loc)
    prom = input("Where were they?  ")
    
    if prom == 'billiard':
        proms = billiard
        
    elif prom == 'study':
        proms = study
        
    elif prom == 'entrance':
        proms = entrance
        
    elif prom == 'music':
        proms = music
        
    elif prom == 'lounge':
        proms = lounge
        
    elif prom == 'dining':
        proms = dining
        
    elif prom == 'greenhouse':
        proms = greenhouse
        
    elif prom == 'library':
        proms = library
        
    elif prom == 'kitchen':
        proms = kitchen
        
    print(varsol)
    withwhat = input("What did they use?  ")
    
    if withwhat == 'gun':
        what = gun
        
    elif withwhat == 'candlestick':
        what = candlestick
        
    elif withwhat == 'rope':
        what = rope
        
    elif withwhat == 'dagger':
        what = dagger
        
    elif withwhat == 'pipe':
        what = pipe
        
    elif withwhat == 'wrench':
        what = wrench
        
    print(f"You are guessing {who} did it in the {imhere} room with a {what}.")
    finala.append(who)
    finala.append(proms)
    finala.append(what)
    if finala == killer:
        print("So... you figured it out.")
        print("The culprit was arrested, and you went home safe.")
        print("Congratulations!!")
        play = o
        return play
        
    else:
        print("That is incorrect.")
        print("All of a sudden, the lights in the room went out!")
        print("In the darkness, you were killed, and the murderer went on to see another day of murder...")
        print("Solution-", killer)
        play = o
        return play
    

def elim():
    doors = x
    while doors == x:
        print(f'{pope}\n')
        print(f'{loc}\n')
        print(f'{varsol}\n')
        chg = input('Which one do you want to change?(n to exit)  ')
        
        if chg == 'n':
            doors = o
            break
        
        elif chg == 'green':
            if green[1] == o:
                green[1] = x
                
            elif green[1] == x:
                green[1] = o
                
        elif chg == 'mustard':
            if mustard[1] == o:
                mustard[1] = x
                
            elif mustard[1] == x:
                mustard[1] = o
            
        elif chg == 'white':
            if white[1] == o:
                white[1] = x
                
            elif white[1] == x:
                white[1] = o
                
        elif chg == 'peacock':
            if peacock[1] == o:
                peacock[1] = x
                
            elif peacock[1] == x:
                peacock[1] = o
                
        elif chg == 'plum':
            if plum[1] == o:
                plum[1] = x
                
            elif plum[1] == x:
                plum[1] = o
                
        elif chg == 'scarlett':
            if scarlett[1] == o:
                scarlett[1] = x
                
            elif scarlett[1] == x:
                scarlett[1] = o
                
        elif chg == 'billiard':
            if billiard[1] == o:
                billiard[1] = x
                
            elif billiard[1] == x:
                billiard[1] = o
                
        elif chg == 'study':
            if study[1] == o:
                study[1] = x
                
            elif study[1] == x:
                study[1] = o
                
        elif chg == 'entrance':
            if entrance[1] == o:
                entrance[1] = x
                
            elif entrance[1] == x:
                entrance[1] = o
                
        elif chg == 'music':
            if music[1] == o:
                music[1] = x
                
            elif music[1] == x:
                music[1] = o
                
        elif chg == 'lounge':
            if lounge[1] == o:
                lounge[1] = x
                
            elif lounge[1] == x:
                lounge[1] = o
                
        elif chg == 'dining':
            if dining[1] == o:
                dining[1] = x
                
            elif dining[1] == x:
                dining[1] = o
                
        elif chg == 'greenhouse':
            if greenhouse[1] == o:
                greenhouse[1] = x
                
            elif greenhouse[1] == x:
                greenhouse[1] = o
                
        elif chg == 'library':
            if library[1] == o:
                library[1] = x
                
            elif library[1] == x:
                library[1] = o
                
        elif chg == 'kitchen':
            if kitchen[1] == o:
                kitchen[1] = x
                
            elif kitchen[1] == x:
                kitchen[1] = o
                
        elif chg == 'gun':
            if gun[1] == o:
                gun[1] = x
                
            elif gun[1] == x:
                gun[1] = o
                
        elif chg == 'candlestick':
            if candlestick[1] == o:
                candlestick[1] = x
                
            elif candlestick[1] == x:
                candlestick[1] = o
                
        elif chg == 'rope':
            if rope[1] == o:
                rope[1] = x
                
            elif rope[1] == x:
                rope[1] = o
                
        elif chg == 'dagger':
            if dagger[1] == o:
                dagger[1] = x
                
            elif dagger[1] == x:
                dagger[1] = o
                
        elif chg == 'pipe':
            if pipe[1] == o:
                pipe[1] = x
                
            elif pipe[1] == x:
                pipe[1] = o
                
        elif chg == 'wrench':
            if wrench[1] == o:
                wrench[1] = x
                
            elif wrench[1] == x:
                wrench[1] = o


def ask():
    global imhere
    if imhere == void:
        print("You can't guess because you aren't in a room.\n")
        
    else:
        print(pope)
        whom = input("Who are you guessing?  ")
        if whom == 'green':
            who = green
            
        elif whom == 'mustard':
            who = mustard
            
        elif whom == 'white':
            who = white
            
        elif whom == 'peacock':
            who = peacock
            
        elif whom == 'plum':
            who = plum
            
        elif whom == 'scarlett':
            who = scarlett
            
        print(varsol)
        withwhat = input("What did they use?  ")
        
        if withwhat == 'gun':
            what = gun
            
        elif withwhat == 'candlestick':
            what = candlestick
            
        elif withwhat == 'rope':
            what = rope
            
        elif withwhat == 'dagger':
            what = dagger
            
        elif withwhat == 'pipe':
            what = pipe
            
        elif withwhat == 'wrench':
            what = wrench
            
        print(f"You are guessing {who} did it in the {imhere} room with a {what}.")
        
        if imhere in adolfhand:
            print(f'Adolf Hitler has {imhere}.')
            
        elif what in adolfhand:
            print(f'Adolf Hitler has {what}.')
            
        elif who in adolfhand:
            print(f'Adolf Hitler has {who}.')
            
        elif imhere in evahand:
            print(f'Eva Braun has {imhere}')
            
        elif what in evahand:
            print(f'Eva Braun has {imhere}')
            
        elif who in evahand:
            print(f'Eva Braun has {who}')
            
        else:
            print('None of that is in anybodies hand...')
        

def main():
    killer.append(people.pop(random.randint(0, len(people)-1)))
    killer.append(places.pop(random.randint(0, len(places)-1)))
    killer.append(things.pop(random.randint(0, len(things)-1)))
    while len(people) > 0:
        sus.append(people.pop(random.randint(0, len(people)-1)))
        
    while len(places) > 0:
        sus.append(places.pop(random.randint(0, len(places)-1)))
        
    while len(things) > 0:
        sus.append(things.pop(random.randint(0, len(things)-1)))
        
    while len(sus) > 0:
        phand.append(sus.pop(random.randint(0, len(sus)-1)))
        if len(sus) > 0:
            pass
        
        else:
            break
        
        adolfhand.append(sus.pop(random.randint(0, len(sus)-1)))
        if len(sus) > 0:
            pass
        
        else:
            break
        
        evahand.append(sus.pop(random.randint(0, len(sus)-1)))
        if len(sus) > 0:
            pass
        
        else:
            break
     
    dst()
    print('You were at a dinner party when the host, Mr. Bohdy, was found murdered!')
    print("It's now your job to find out who did it.")
    print("If you don't know the rules of Clue, learn them.")
    print("Use sheet to eliminate suspects.")
    print("Use ask to gather information from other people.")
    print("Use move to go to different rooms.")
    print("And once you've reached a conclusion: use ACCUSE to find out who did it.")
    print(f"You are in- {imhere}")
    print(f'Your hand is- {phand}')
    
    while play == x:
        action = input("What would you like to do?(ask, move, sheet, accuse)  ")
        if action == 'move':
            move()
            
        elif action == 'ask':
            ask()
            
        elif action == 'sheet':
            elim()
            
        elif action == 'accuse':
            accuse()
            break
                
        else:
            print("I don't understand")
            

#main
play = x
main()