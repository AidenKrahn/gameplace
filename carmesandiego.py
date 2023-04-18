

#---------------------
#Carmen Sandiego
#Aiden Krahn
#Started February 28th
#made in 3 days
#----------------------
import random
#lists of countries-
#DO NOT LOOK AT CODE BEFORE PLAYING
#IT WILL SPOIL HINTS THAT YOU GET THROUGHOUT THE GAME
bolivia = [1, 1, "stripes, a crest", "paraguay", "natural gas", "12 million", "Valle de La Luna"]
chile = [3, 2 ,"star(s), French colours", 'argentina', "copper and fish", "19.5 million", "Easter Island"]
peru = [3, 3, "stripes, a crest", 'ecuador', 'coffee', "33.7 million", "Machu Picchu"]
brazil = [0, 4, "star(s), blue", 'venezuela', 'soy beans and sugar', "214.3 million", "Christ the Redeemer"]
argentina = [2, 5, "stripes, blue", 'chile', 'soy beans and corn', "45.8 million", "Bariloche"]
uruguay = [2, 6, "stripes, blue", 'paraguay', 'meat and pharmaceuticals', "3.4 million", "Fingers of Punta del Este"]
paraguay = [1, 7, "stripes, a crest", 'uruguay', 'soy beans, soy oil', "6.7 million", "Monday Falls"]
venezuela = [1, 8, "stars, a crest", 'bolivia', 'steel, aluminum', "28.2 million", "Angel Falls"]
colombia = [1, 9, "stripes, blue", 'venezuela', 'natural gas, coffee', "51.5 million", "Salt Cathedral"]
ecuador = [2, 10, "stripes, a crest", 'peru', 'shrimp, bananas', "17.8 million", "Middle of the World City"]
guyana = [1, 11, "triangles, green", 'colombia', 'oil, gold', ".8 million", "Kaieteur Falls"]
frenchguiana = [1, 12, "star(s), triangles", 'guyana', 'shrimp, gold', ".3 million", "Devil's Island"]
suriname = [1, 13, "star(s), stripes", 'guyana', 'rice, bananas', ".6 million", "Jodensavanne"]
listofcountries = ["bolivia", "chile", "peru", "brazil", "argentina", "uruguay",
                   "paraguay", "venezuela", "colombia", "ecuador", "guyana", "frenchguiana", "suriname"]
fakecountry = [17]
listofcountriespart2 = [bolivia, chile, peru, brazil, argentina, uruguay,
                   paraguay, venezuela, colombia, ecuador, guyana, frenchguiana, suriname]

#definitions
def hint(country):
    que = random.randint(1, 6)
    if que == 1:
        print("This countries flag contains--",country[2])
        #more hints will be added in the future: corresponding list elements will also be added
    elif que == 2:
        print("This country is near--", country[3])
        
    elif que == 3:
        print("This country exports--", country[4])
        
    elif que == 4:
        print("This country has this many people--", country[5])
        
    elif que == 5:
        antihint()
        
    elif que == 6:
        print("The countries landmark is--", country[6])
        
    else:
        antihint()

    
def antihint():
    global witwics
    crazy = random.randint(1, 13)
    if crazy == witwics[1]:
        antihint()
    
    elif crazy == 1:
        print("Carmen Sandiego is not in Bolivia")
        
    elif crazy == 2:
        print("Carmen Sandiego is not in Chile")
        
    elif crazy == 3:
        print("Carmen Sandiego is not in Peru")
        
    elif crazy == 4:
        print("Carmen Sandiego is not in Brazil")
        
    elif crazy == 5:
        print("Carmen Sandiego is not in Argentina")
        
    elif crazy == 6:
        print("Carmen Sandiego is not in Uruguay")
        
    elif crazy == 7:
        print("Carmen Sandiego is not in Paraguay")
        
    elif crazy == 8:
        print("Carmen Sandiego is not in Venezuela")
        
    elif crazy == 9:
        print("Carmen Sandiego is not in Colombia")
        
    elif crazy == 10:
        print("Carmen Sandiego is not in Ecuador")
        
    elif crazy == 11:
        print("Carmen Sandiego is not in Guyana")
        
    elif crazy == 12:
        print("Carmen Sandiego is not in French Guiana")
        
    elif crazy == 13:
        print("Carmen Sandiego is not in Suriname")
    
    
def event():
    global location
    global witwics
    if location == witwics:
        print("After searching around, you managed to track down a criminal hiding in an abandoned building...")
        print("It was Carmen Sandiego!")
        print("Now that you caught her, you can go home and eat cake*.")
        print("*cake not provided")
        play = False
        #whether or not you catch Carmen Sandiego
    elif location != witwics:
        print("After searching around, you managed to track down a criminal hiding in an abandoned building...")
        print("It was an impostor! (sus)")
        print("You caught the impostor, and now they agreed to give you a hint to Carmen's whereabouts...")
        hint(witwics)
        print("Keep searching!")
    #if I wanted to be accurate, I could've added more here
def country_choose():
    global country
    global witwics
    roll = random.randint(0, 12)
    vcountry = listofcountries[roll]#v. stands for varsol
    if vcountry == "bolivia":
        witwics == bolivia
    
    elif vcountry == "chile":
        witwics = chile
        
    elif vcountry == "peru":
        witwics = peru
        
    elif vcountry == "brazil":
        witwics = brazil
        
    elif vcountry == "argentina":
        witwics = argentina
        
    elif vcountry == "uruguay":
        witwics = uruguay
        
    elif vcountry == "paraguay":
        witwics = paraguay
        
    elif vcountry == "venezuela":
        witwics = venezuela
        
    elif vcountry == "colombia":
        witwics = colombia
        
    elif vcountry == "ecuador":
        witwics = ecuador
        
    elif vcountry == "guyana":
        witwics = guyana
        
    elif vcountry == "frenchguiana":
        witwics = frenchguiana
        
    elif vcountry == "suriname":
        witwics = suriname
        
    if witwics == location:
        country_choose()
        
    return witwics

    
def fly(coward):
    global days
    global location
    location = coward
    days += coward[0]
    return location
    return days
    
def geographygarble(lratio):#determines how long it takes 
    if lratio[1] == 1:#you to fly based on where you are and where you go
        brazil[0] = 1
        paraguay[0] = 1
        argentina[0] = 1
        chile[0] = 1
        peru[0] = 1
        ecuador[0] = 2
        colombia[0] = 3
        venezuela[0] = 2
        guyana[0] = 3
        suriname[0] = 2
        frenchguiana[0] = 2
        uruguay[0] = 2
        bolivia[0] = 0
        
    elif lratio[1] == 2:
        argentina[0] = 1
        bolivia[0] = 1
        peru[0] = 1
        ecuador[0] = 2
        colombia[0] = 3
        venezuela[0] = 3
        guyana[0] = 3
        suriname[0] = 3
        frenchguiana[0] = 3
        paraguay[0] = 2
        brazil[0] = 3
        uruguay[0] = 2
        chile[0] = 0
        
    elif lratio[1] == 3:
        ecuador[0] = 1
        colombia[0] = 1
        venezuela[0] = 2
        guyana[0] = 2
        suriname[0] = 3
        frenchguiana[0] = 3
        brazil[0] = 1
        bolivia[0] = 1
        chile[0] = 1
        argentina[0] = 2
        uruguay[0] = 3
        paraguay[0] = 2
        peru[0] = 0
        
    elif lratio[1] == 4:
        frenchguiana[0] = 1
        guyana[0] = 1
        suriname[0] = 1
        venezuela[0] = 1
        colombia[0] = 1
        ecuador[0] = 2
        peru[0] = 1
        bolivia[0] = 1
        paraguay[0] = 1
        uruguay[0] = 1
        argentina[0] = 1
        chile[0] = 2
        brazil[0] = 0
        
    elif lratio[1] == 5:
        chile[0] = 1
        bolivia[0] = 1
        paraguay[0] = 1
        uruguay[0] = 1
        peru[0] = 2
        brazil[0] = 1
        ecuador[0] = 3
        colombia[0] = 3
        venezuela[0] = 3
        guyana[0] = 3
        frenchguiana[0] = 3
        suriname[0] = 3
        argentina[0] = 0
        
    elif lratio[1] == 6:
        argentina[0] = 1
        brazil[0] = 1
        chile[0]= 2
        bolivia[0] = 2
        peru[0] = 3
        ecuador[0] = 3
        colombia[0] = 3
        venezuela[0] = 3
        guyana[0] = 3
        frenchguiana[0]  = 3
        suriname[0] = 3
        paraguay[0] = 2
        uruguay[0] = 0
        
    elif lratio[1] == 7:
        bolivia[0] = 1
        argentina[0] = 1
        brazil[0] = 1
        uruguay[0] = 2
        chile[0] = 2
        peru[0] = 3
        ecuador[0] = 3
        colombia[0] = 3
        venezuela[0] = 3
        guyana[0] = 3
        frenchguiana[0] = 3
        suriname[0] = 3
        paraguay[0] = 0
        
    elif lratio[1] == 8:
        guyana[0] = 1
        brazil[0] = 1
        colombia[0] = 1
        suriname[0] = 2
        frenchguiana[0] = 2
        ecuador[0] = 2
        peru[0] = 2
        bolivia[0] = 3
        paraguay[0] = 3
        uruguay[0] = 3
        argentina[0] = 3
        chile[0] = 3
        venezuela[0] = 0
        
    elif lratio[1] == 9:
        venezuela[0] = 1
        ecuador[0] = 1
        peru[0] = 1
        brazil[0] = 1
        guyana[0] = 2
        suriname[0] = 2
        frenchguiana[0] = 3
        bolivia[0] = 2
        chile[0] = 3
        argentina[0] = 3
        paraguay[0] = 3
        uruguay[0] = 3
        colombia[0] = 0
        
    elif lratio[1] == 10:
        peru[0] = 1
        colombia[0] = 1
        venezuela[0] = 1
        guyana[0] = 2
        suriname[0] = 2
        frenchguiana[0] = 3
        brazil[0] = 2
        bolivia[0] = 2
        chile[0] = 2
        argentina[0] = 3
        paraguay[0] = 3
        uruguay[0] = 3
        ecuador[0] = 0
        
    elif lratio[1] == 11:
        suriname[0] = 1
        frenchguiana[0] = 1
        venezuela[0] = 1
        colombia[0] = 1
        ecuador[0] = 2
        brazil[0] = 1
        bolivia[0] = 2
        peru[0] = 2
        paraguay[0] = 2
        uruguay[0] = 3
        argentina[0] = 3
        chile[0] = 3
        guyana[0] = 0
        
    elif lratio[1] == 12:
        guyana[0] = 1
        suriname[0] = 1
        brazil[0] = 1
        venezuela[0] = 1
        colombia[0] = 2
        ecuador[0] = 2
        peru[0] = 3
        bolivia[0] = 2
        paraguay[0] = 2
        uruguay[0] = 3
        argentina[0] = 3
        chile[0] = 3
        frenchguiana[0]
        
    elif lratio[1] == 13:
        guyana[0] = 1
        frenchguiana[0] = 1
        brazil[0] = 1
        venezuela[0] = 1
        colombia[0] = 2
        ecuador[0] = 3
        peru[0] = 3
        bolivia[0] = 2
        paraguay[0] = 2
        uruguay[0] = 3
        argentina[0] = 3
        chile[0] = 3
        suriname[0] = 0
        
        
#main code---
coolerdaniel = random.randint(0, 12)
location = listofcountriespart2[coolerdaniel]
#determine starting location
print("Carmen Sandiego is somewhere in South America!")
print("It is your job as a detective to find clues about Carmen Sandiego's whereabouts.")
print("She could be hiding in", listofcountries)
print("We have a few clues as to where Carmen Sandiego is hiding.")
print(f"You are currently in {listofcountries[coolerdaniel]}")
print("You have 7 days to find her.")
print("If you find her, there will be cake.")

#clues are split up into types:
#how much information they give(lots, not much, and cannonball)
#what kind of information they give(so I don't have to write 5000 sentences, just 100.
#flag hints, location based, political specifics, population
def main():
    witwics = fakecountry
    country_choose()#chooses where Carmen is
    play = True
    days = 0
    geographygarble(location)
    hint(witwics)
    while play == True:
        if location == witwics:
            break
        
        geographygarble(location)#calculate distances between your current location and other countries
        action = input("Where do you think she is?  ")
        
        if days < 7:
            #flying to different countries
            if action == "bolivia":
                print("You flew to Bolivia")
                fly(bolivia)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'argentina':
                print("You flew to Argentina")
                fly(argentina)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'ecuador':
                print("You flew to Ecuador")
                fly(ecuador)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'brazil':
                print("You flew to Brazil")
                fly(brazil)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'suriname':
                print("You flew to Suriname")
                fly(suriname)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'frenchguiana':
                print("You flew to French Guiana")
                fly(frenchguiana)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'guyana':
                print("You flew to Guyana")
                fly(guyana)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'chile':
                print("You flew to Chile")
                fly(chile)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'peru':
                print("You flew to Peru")
                fly(peru)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'paraguay':
                print("You flew to Paraguay")
                fly(paraguay)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'uruguay':
                print("You flew to Uruguay")
                fly(uruguay)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'venezuela':
                print("You flew to Venezuela")
                fly(venezuela)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
            elif action == 'colombia':
                print("You flew to Colombia")
                fly(colombia)
                geographygarble(location)
                print(f"Days Left =", 7 - days)
                event()
                
        elif days >= 7:#lose condition
            print("You ran out of time.")
            print("You failed, Carmen got away, and you're bad at geography.")
            print("You got fired, your wife left you.")
            print("You're homeless. A dog peed on you.")
            print("Better luck next time!")
            play = False

main()