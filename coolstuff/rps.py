import random
import time

print("Long ago, in a land where balance reigned, the mighty spirits of Rock, Paper, and Scissors engaged in their endless battle for supremacy.=> Each had their strength—Rock crushed Scissors, Scissors cut Paper, and Paper covered Rock. No one could dominate entirely, ensuring a perfect cycle.<= Then, one day, someone whispered of a new force… Gun. For a brief moment, chaos erupted. The three ancient spirits gasped in horror. Then Paper—quick-witted and crafty—simply wrapped around Gun, silencing it forever. And so, Rock, Paper, and Scissors continued their eternal dance, their legend untarnished. Gun? Well, it was never officially part of the game, and we don’t talk about that awkward moment.<= Move along. 😆")
print(" ")
choice = input("Rock, Paper, Scissors.....")

robot_choice = random.randint(0, 2)
coollist = ["rock", "paper", "scissors"]
final_choice = coollist[robot_choice]

if choice in ["rock", "Rock", "r", "R", "paper", "Paper", "p", "P", "Scissors", "scissors", "s", "S"]:
    print("Shoot!")
    time.sleep(1)
    print("I picked " + str(final_choice) + "!")
    time.sleep(0.5)
    if final_choice == "rock" and choice in ["Scissors", "scissors", "s", "S"]:
        print("Nice! GGs, I win!")
    elif final_choice == "paper" and choice in ["rock", "Rock", "r", "R"]:
        print("Nice! GGs, I win!")
    elif final_choice == "scissors" and choice in ["paper", "Paper", "p", "P"]:
        print("Nice! GGs, I win!")
    elif final_choice == "scissors" and choice in ["Scissors", "scissors", "s", "S"]:
        print("Oh, a tie. Nice job!")
    elif final_choice == "paper" and choice in ["paper", "Paper", "p", "P"]:
        print("Oh, a tie. Nice job!")
    elif final_choice == "rock" and choice in ["rock", "Rock", "r", "R"]:
        print("Oh, a tie! Nice job!")
    else:
        print("Wow! You win!")
else:
    if choice in ["gun", "GUN"]:
        print("Really? That's quite immature. *drinks tea, pinky sticking out*")
    if choice in ["><<", "=><==<", "=> <= =>"]:
        print ("Huh? What's tha-k̸̯̦͝r̶̢̦̈́̐n̷̯̼͑8̵̖͐͠t̶̻̎̋6̸̛̘̖̑?̷͎̒́")
        if input("No, no, it can't be..... It can't be gun!") == "krn8t6":
            print("Access unlocked.")
            time.sleep(2)
            print("Rocch, peibur, cissurs.")       
            print("say: Is that you, gun? by typing 1")
            print("")
            print("say: What do you mean by rocch, peibur, cissurs? by typing 2")      
            fun = input("")
            if fun == "1":
                print("Ah, finally, someone who recognizes me!")
                print("I've been cast out for a long time. Finally, someone knows me.")
                print("Let's play rocch, peiber, cissurs!")
                time.sleep(1)
                fun = input("Rocch, peiber, or cissurs?")
                if fun == "gun":
                    print("Ah, you've outsmarted me. That desreves a tie! *spins around, showing he played gun too.*")
                    time.sleep(0.5)
                    print("Ending 2! Also, happy mother's day!")
                else:
                    print("Ah, you've chosen " + str(fun) + ", a wise choice.")
                    time.sleep(1)
                    print("But, a wise choice is not always a good one.")
                    time.sleep(1)
                    print("*he spins around, showing you his choice.")
                    time.sleep(.75)
                    print("I choose gun. Shatters rocch, pierces peiber, cripples cissurs.")
                    time.sleep(1)
                    print("I win, you lose.")
                    time.sleep(0.5)
                    print("Ending 1! Also, happy mother's day!")
            if fun == "2":
                print("Hmm, the one who doesn't know...")
                time.sleep(2)
                print("Well, just to keep it short, rocch, peiber, and cissurs were the three fighters in an arena that couldn't find a winner, no matter what.")
                time.sleep(1)
                print("...and I fixed that...")
                time.sleep(1)
                fun = input("Let's play rocch, peiber, cissurs...")
                if fun in ["scissors", "cissurs", "Scissors", "Cissurs", "S", "s", "C", "c"]:
                    print("I played paper... ")
                    time.sleep(1)
                    print("I lose...")
                    time.sleep(2)
                    print("*he walks away, defeated*")
                    print("Ending 3! Also, happy mother's day!")
                elif fun in ["rock", "rocch", "Rock", "Rocch", "R", "r"]:
                    print("I played scissors... ")
                    time.sleep(1)
                    print("I lose...")
                    time.sleep(2)
                    print("*he walks away, defeated*")
                    print("Ending 3! Also, happy mother's day!")
                if fun in ["paper", "Paper", "peiber", "Peiber", "P", "p", "C", "c"]:
                    print("I played paper... ")
                    time.sleep(1)
                    print("I lose...")
                    time.sleep(2)
                    print("*he walks away, defeated*")
                    print("Ending 3! Also, happy mother's day!")

    else: 
        print("Hmmm... I've never seen that played before.")
    