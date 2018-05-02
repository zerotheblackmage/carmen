
import random
import csv


curLoc = "California USA"
thiLoc = ""

hops = 4
time = 24
traveltime = 3

locations = []
criminals = []
eyes = ["eye colour"]
hair = ["hair colour"]
gender = ["gender"]
vehicle = ["vehicle"]
trait =  ["trait"]
food = ["food"]
hobby = ["hobby"]
accuse = []
suspect = ""
locroll = []


with open ('locations.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        locations.append({'name': row[0], 'desc':row[1], 'hint':row[2]})



with open ('criminals.csv', 'r') as g:
    reader2 = csv.reader(g)
    for row in reader2:
        criminals.append({'name': row[0], 'eyes':row[1], 'hair':row[2], 'gender':row[3], 'vehicle':row[4], 'food':row[5], 'trait':row[6], 'hobby':row[7]})
        if row[1] not in eyes:
            eyes.append(row[1])
        if row[2] not in hair:
            hair.append(row[2])
        if row[3] not in gender:
            gender.append(row[3])
        if row[4] not in vehicle:
            vehicle.append(row[4])
        if row[5] not in food:
            food.append(row[5])
        if row[6] not in trait:
            trait.append(row[6])
        if row[7] not in hobby:
            hobby.append(row[7])

item = "Holy Grail"
crimin = random.choice(criminals)
crim = crimin['name']

def getOpt(arr):
    arr2 = arr[:]
    question = []
    answer = 0
    num = 1
    ty = arr2.pop(0)
    for a in arr2:
        question.append("{} - {}".format(num, a))
        num += 1
    question.append("{} - Don't know".format(num))

    while answer <= num and not answer >= 1:
        print("what do you know of the suspect's {}?\n".format(ty))
        for q in question:
            print(q)
        print("\n")
        try:
            answer = int(input(""))
        except:
            print("try again")
    if answer < num:
        return(arr2[int(answer)-1])
    else:
        return(None)

def initLoc():
    global locroll
    del locroll[:]
    locroll = locations[:]

def getLoc():
    global locroll
    x = random.choice(locroll)
    y = x['name']
    locroll.remove(x)
    return y

def warrant():
    global suspect
    accuse = {}
    accuse['gender'] = getOpt(gender)
    accuse['hair'] = getOpt(hair)
    accuse['hobby'] = getOpt(hobby)
    accuse['eyes'] = getOpt(eyes)
    accuse['food'] = getOpt(food)
    accuse['vehicle'] = getOpt(vehicle)
    accuse['trait'] = getOpt(trait)

    asses = criminals[:]
    print(asses)

    for key, val in accuse.items():
        if val is None:
            continue
        else:
            for a in criminals:
                print(a)
                print(a[key] + " <= compared to => " + val)
                if a[key] == val:
                    print("True")
                else:
                    try:
                        print("eliminating {}".format(a['name']))
                        asses.remove(a)
                    except Exception as e:
                        print("could not remove " + str(a) + " because " + str(e))

    print("your suspects are:")
    if len(asses) == 0:
        print("Sorry, no suspects match that description. Try again")

    else:
        for a in asses:
            print(a['name'])
            print(len(asses))
        if len(asses) == 1:
            suspect = a['name']
            print("congrats, you have a suspect! You now have a warrant for {}".format(suspect))
        else:
            print("Sorry, too many matches. You'll need to try again.")


def investigate():
    global crimin
    global thiLoc
    which = random.randint(0,1)
    if which == 1:
        hint = random.choice(list(crimin.keys()))
        while hint == crimin['name']
            hint = random.choice(list(crimin.keys()))
        print(crimin[hint] + "\n")
    if which == 0:
        for i in locations:
            if i['name'] == thiLoc:
                print(i['hint'] + "\n")
        # print(thiLoc + "\n")

def main():
    global time
    global hops
    global locroll
    global thiLoc
    global curLoc

    initLoc()
    thiLoc = getLoc()
    d1Loc = getLoc()
    d2Loc = getLoc()
    initLoc()


    while time > 0:
        x = [thiLoc, d1Loc, d2Loc]

        random.shuffle(x)

        print("You have {} hours left to find the missing {}. \nYou are in {}".format(time, item, curLoc))
        for d in locations:
            if d['name'] == curLoc:
                print( "\n \n {} \n \n".format(d['desc']))
        answer = ""

        while str(answer) not in ["3","2","1"]:

            print( "The criminal has fled with to one of the following locations. where do you think they went? \n")
            print("1 - {} \n2 - {} \n3 - {}".format(x[0],x[1],x[2]))
            print("\nw - warrant \ni - investigate \n")

            if answer == "w":
                warrant()
                answer = "10"
                time -= 1

            elif answer == "i":
                investigate()
                answer = "10"
                time -= 1
            else:
                answer = input("What do you do?\n")
        move = x[int(answer)-1]

        if thiLoc == move:
            hops -= 1
            time -= traveltime
            if hops == 0:
                print("You caught up to the theif!")
                if suspect != crim:
                    print("Unfortunately, you don't have the right warrant to arrest {}. Due to a legal oversight, "
                          "they walk away with the {}".format(crim, item))
                    exit(0)
                else:
                    print("Got-em! You arrested {} and recovered the {}! Well done Gumshoe.".format(crim, item))
                    exit(0)
            else:
                initLoc()
                curLoc = thiLoc
                thiLoc = getLoc()
                d1Loc = getLoc()
                d2Loc = getLoc()
                while curLoc == thiLoc or curLoc == d1Loc or curLoc == d2Loc:
                    thiLoc = getLoc()
                    d1Loc = getLoc()
                    d2Loc = getLoc()

                print( "you arrive in {} after a {} hour flight.".format(curLoc, traveltime))
                print( "You seem to be on the right track based on a recent attack by a V.I.L.E. agent")
                print(" ")
        else:

            # curLoc = move
            print( "you arrive in {} after a {} hour flight.".format(move, traveltime))
            print( "However, after an extensive search, find nothing. A return flight later, "
                   "you return to {}".format(curLoc))
            time -= traveltime
            print(" ")


    print("Sorry, you failed. {} got away".format(crim))
    exit(0)


main()
