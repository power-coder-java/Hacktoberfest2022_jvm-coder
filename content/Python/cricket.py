import random

def score():
    outputs = [0,1,2,3,4,5,6,7,8]
    return random.choice(outputs)

def match():
    balls = 0
    wickets = 0
    runs = 0
    while balls<30 :
        if wickets<5 :
            run = score()
            if run==0 :
                wickets += 1
                balls += 1
                print("You are OUT")
            elif run==7 :
                runs += 1
                print("WIDE Ball")
                print("You got 1 extra run in this ball")
            elif run==8 :
                run = random.choice([1,2,3,4,5,6])
                runs += (run+1)
                print("No Ball --FREE HIT--")
                print("You got ",run,"runs and 1 extra run in this ball")
            else:
                runs += run
                balls += 1
                print("You got ",run," runs in this ball")

            print("Runs : ",runs)
            print("Wickets : ",wickets)
            print("Balls : ",balls)
            print()
        else:
            break
            

    return runs

print("Total BALLS = 30")
print("Total WICKETS = 5\n\n")

print("Team A")
print("------\n")

scoreTeamA = match()
print("1st INNING OVER !!!!!!")
print("=======================================================================================\n\n")

print("Team B")
print("------\n")

scoreTeamB = match()
print("2nd INNING OVER !!!!!!\n\n")

print("Team A score : ",scoreTeamA)
print("Team B score : ",scoreTeamB)

print("Team A won !!!!!") if scoreTeamA>scoreTeamB else print("Team B won !!!!!")
