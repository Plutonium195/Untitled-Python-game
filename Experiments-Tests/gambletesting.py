import random

    # Play the game
    gold -= bet
    print("Spinning the reels...")
    reel1 = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar", "seven"])
    reel2 = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar", "seven"])
    reel3 = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar", "seven"])
    print(f"The reels stop on: {reel1} {reel2} {reel3}")

    # Determine the outcome
    if reel1 == reel2 == reel3 == "seven":
        win = amount * 10
        print("JACKPOT! You win" ,+ win + , 'gold!")
        gold += amount * 10
        luck += 1
    elif reel1 == reel2 == reel3:
        if reel1 == "cherry":
            win = amount * 3
            luckxp += 2
            print("Three cherries! You win" ,+ win + , 'gold!')
        else:
            luckxp += 2
            print(f"Three {reel1}s! You win {amount*3} gold!")
            gold += amount * 3
    elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
        print("Two of a kind! You win $10!")
        gold += amount * 2
        luckxp += 1
    else:
        print("Sorry, you didn't win anything this time.")
