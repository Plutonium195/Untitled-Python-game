import random

# Initialize variables
luck = 5
luckxp = 0
gold = 100


# Define a function to play blackjack
def playblackjack():
    global gold, luck, luckxp

    # Define a function to calculate the value of a hand
    def handvalue(hand):
        value = 0
        numaces = 0
        for card in hand:
            if card == 'A':
                numaces += 1
                value += 11
            elif card in ['K', 'Q', 'J']:
                value += 10
            else:
                value += int(card)
        while value > 21 and num_aces > 0:
            value -= 10
            numaces -= 1
        return value

    
    # Initialize variables for the game
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    #removing cards from deck and putting them in players hand
    playerhand = [deck.pop(), deck.pop()]
    dealerhand = [deck.pop(), deck.pop()]
    
    # Check if the player has blackjack
    if handvalue(playerhand) == 21:
        print("You have blackjack! You win!")
        gold += amount * 2
        return
    
    # Player's turn
    while True:
        print("Your hand:", playerhand)
        print("Dealer's faceup card:", dealerhand[0])
        action = input("Do you want to hit or stand? ")
        if action.lower() == 'hit':
            playerhand.append(deck.pop())
            if handvalue(playerhand) > 21:
                print("Bust! You lose.")
                gold -= amount * 2
                return
        elif action.lower() == 'stand':
            break
    
    # Dealer's turn
    while handvalue(dealerhand) < 17:
        dealerhand.append(deck.pop())
    print("Dealer's hand:", dealerhand)
    
    # Determine the winner
    if handvalue(dealerhand) > 21:
        print("Dealer busts! You win!")
        gold += amount * 2
    elif handvalue(playerhand) > handvalue(dealerhand):
        print("You win!")
        gold += amount * 2
    elif handvalue(playerhand) == handvalue(dealerhand):
        print("Push.")
    else:
        print("You lose.")
        gold -= amount * 2

# Call the play_blackjack function
playblackjack()
