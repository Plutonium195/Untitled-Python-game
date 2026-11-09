import random

# Define the deck of cards
deck = [
    "Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades",
    "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades",
    "Jack of Spades", "Queen of Spades", "King of Spades",
    "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts",
    "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts",
    "Jack of Hearts", "Queen of Hearts", "King of Hearts",
    "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs",
    "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs",
    "Jack of Clubs", "Queen of Clubs", "King of Clubs",
    "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds",
    "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds",
    "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds",
    "Queen of Diamonds", "King of Diamonds"
]

# Define the values for each card
card_values = {
    "Ace": 14, 
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "10": 10, 
    "Jack": 11, 
    "Queen": 12, 
    "King": 13
}

# Define the initial amount for each player
player_money = 1000
npc_money = 1000

# Define the bet amount for each round
bet = 100

# Shuffle the deck
random.shuffle(deck)

# Deal the cards
player_hand = [deck.pop(), deck.pop()]
npc_hand = [deck.pop(), deck.pop()]

# Define the flop
flop = [deck.pop(), deck.pop(), deck.pop()]

# Define the turn
turn = deck.pop()

# Define the river
river = deck.pop()

# Define the function to determine the winner
def determine_winner(player_hand, npc_hand, board):
    player_score = calculate_score(player_hand, board)
    npc_score = calculate_score(npc_hand, board)
    
    if player_score > npc_score:
        return 'player'
    elif npc_score > player_score:
        return 'npc'
    else:
        return 'tie'

# Define the function to calculate a hand's score
def calculate_score(hand, board):
    # Combine the hand and board
    all_cards = hand + board
    
    # Sort the cards by value
    all_cards.sort(key=lambda x: card_values[x.split()[0]])
    
    # Check for a straight flush
    straight_flush = check_straight_flush(all_cards)
    
    if straight_flush:
        return 100 + straight_flush
    
    # Check for four-of-a-kind
    four_of_a_kind = check_four_of_a_kind(all_cards)
    
    if four_of_a_kind:
        return 80 + four_of_a_kind
    
    # Check for a full house
    full_house = check_full_house(all_cards)
    
    if full_house:
        return 60 + full_house
    
    # Check for a flush
    flush = check_flush(all_cards)
    
    if flush:
        return 40 + flush
    
    # Check for a straight
    straight = check_straight(all_cards)
    
    if straight:
        return 20 + straight
    
    # Check for three-of-a-kind
    three_of_a_kind = check_three_of_a_kind(all_cards)
    
    if three_of_a_kind:
        return 10 + three_of_a_kind
    
    # Check for two pairs
    two_pairs = check_two_pairs(all_cards)
    
    if two_pairs:
        return 5 + two_pairs
    
    # Check for one pair
    one_pair = check_one_pair(all_cards)
    
    if one_pair:
        return one_pair
    
    # If no other hands are present, return high card
    return card_values[all_cards[-1].split()[0]]

# Define the function to check for a straight flush
def check_straight_flush(cards):
    suits = {}
    
    for card in cards:
        suit = card.split()[2]
        
        if suit not in suits:
            suits[suit] = []
        
        suits[suit].append(card)
        
        if len(suits[suit]) >= 5:
            straight_flush = check_straight(suits[suit])
            
            if straight_flush:
                return straight_flush
    
    return False

# Define the function to check for four-of-a-kind
def check_four_of_a_kind(cards):
    values = {}
    
    for card in cards:
        value = card.split()[0]
        
        if value not in values:
            values[value] = []
        
        values[value].append(card)
        
        if len(values[value]) == 4:
            return card_values[value]
    
    return False

# Define the function to check for a full house
def check_full_house(cards):
    values = {}
    
    for card in cards:
        value = card.split()[0]
        
        if value not in values:
            values[value] = []
        
        values[value].append(card)
    
    three_of_a_kind_value = False
    two_of_a_kind_value = False
    
    for value in values:
        if len(values[value]) == 3:
            three_of_a_kind_value = value
        
        if len(values[value]) == 2:
            two_of_a_kind_value = value
    
    if three_of_a_kind_value and two_of_a_kind_value:
        return card_values[three_of_a_kind_value]
    
    return False

# Define the function to check for a flush
def check_flush(cards):
    suits = {}
    
    for card in cards:
        suit = card.split()[2]
        
        if suit not in suits:
            suits[suit] = []
        
        suits[suit].append(card)
        
        if len(suits[suit]) >= 5:
            return card_values[suits[suit][-1].split()[0]]
    
    return False

# Define the function to check for a straight
def check_straight(cards):
    values = []
    
    for card in cards:
        value = card.split()[0]
        
        if value not in values:
            values.append(value)
        
        if len(values) >= 5:
            straight_values = sorted(values, key=lambda x: card_values[x])
            
            if (card_values[straight_values[-1]] - card_values[straight_values[0]]) == 4:
                return card_values[straight_values[-1]]
            
            values.pop(0)
    
    return False

# Define the function to check for three-of-a-kind
def check_three_of_a_kind(cards):
    values = {}
    
    for card in cards:
        value = card.split()[0]
        
        if value not in values:
            values[value] = []
        
        values[value].append(card)
        
        if len(values[value]) == 3:
            return card_values[value]
    
    return False

# Define the function to check for two pairs
def check_two_pairs(cards):
    values = {}
    
    for card in cards:
        value = card.split()[0]
        
        if value not in values:
            values[value] = []
        
        values[value].append(card)
    
    pairs = []
    
    for value in values:
        if len(values[value]) == 2:
            pairs.append(value)
    
    if len(pairs) == 2:
        pair_values = sorted(pairs, key=lambda x: card_values[x])
        
        return card_values[pair_values[-1]]
    
    return False

# Define the function to check for one pair
def check_one_pair(cards):
    values = {}
    
    for card in cards:
        value = card.split()[0]
        
        if value not in values:
            values[value] = []
        
        values[value].append(card)
        
        if len(values[value]) == 2:
            return card_values[value]
    
    return False

# Play the game
while True:
    
    # Print the player's hand and ask for their action
    print(f"Your hand: {player_hand}")
    
    action = input("Do you want to fold, call or raise? ")
    
    # If the player folds, end the game and award the NPC the pot
    if action.lower() == 'fold':
        print("You fold.")
        npc_money += bet * 2
        break
    
     # If the player calls, deal the rest of the board and determine the winner
     # based on each player's hand and the board
     elif action.lower() == 'call':
         print(f"The flop: {flop}")
         
         action_2 = input("Do you want to fold or call? ")
         
         if action_2.lower() == 'fold':
             print("You fold.")
             npc_money += bet * 2
             break
         
         elif action_2.lower() == 'call':
             print(f"The turn: {turn}")
             
             action_3 = input("Do you want to fold or call? ")
             
             if action_3.lower() == 'fold':
                 print("You fold.")
                 npc_money += bet * 2
                 break
             
             elif action_3.lower() == 'call':
                 print(f"The river: {river}")
                 
                 winner = determine_winner(player_hand, npc_hand, flop + [turn] + [river])
                 
                 if winner == 'player':
                     print("You win!")
                     player_money += bet * 2
                     break
                 
                 elif winner == 'npc':
                     print("You lose.")
                     npc_money += bet * 2
                     break
                 
                 else:
                     print("It's a tie!")
                     player_money += bet
                     npc_money += bet
                     break
     
     # If the player raises, ask them how much they want to raise and deal the rest
     # of the board and determine the winner based on each player's hand and the board     
     elif action.lower() == 'raise':
         raise_amount_str = input("How much do you want to raise? ")
         raise_amount_int = int(raise_amount_str)
         
         player_money -= raise_amount_int
         bet += raise_amount_int
         
         print(f"You raise by {raise_amount_int}.")
         
         print(f"The flop: {flop}")
         
         action_2 = input("Do you want to fold, call or raise? ")
         
         # If the player folds, end the game and award the NPC the pot plus their raise amount
         if action_2.lower() == 'fold':
             print("You fold.")
             npc_money += bet * 2
             break
        
         # If the player calls, deal the rest of the board and determine the winner based on each player's hand and the board
         elif action_2.lower() == 'call':
             print(f"The turn: {turn}")
             
             action_3 = input("Do you want to fold, call or raise? ")
             
             # If the player folds, end the game and award the NPC the pot plus their raise amount times two
             if action_3.lower() == 'fold':
                 print("You fold.")
                 npc_money += bet * 2
                 break
            
             # If the player calls, deal the rest of the board and determine the winner based on each player's hand and the board   
             elif action_3.lower() == 'call':
                 print(f"The river: {river}")
                 
                 winner = determine_winner(player_hand, npc_hand, flop + [turn] + [river])
                 
                 # If the player wins, award them with both pots plus their raise amount times two; otherwise award NPC with both pots plus their raise amount times two.
                 if winner == 'player':
                     print("You win!")
                     player_money += bet * 2 + raise_amount_int * 2
                     break
                
                 elif winner == 'npc':
                     print("You lose.")
                     npc_money += bet * 2 + raise_amount_int * 2
                     break
                
                 else:
                     print("It's a tie!")
                     player_money += bet + raise_amount_int
                     npc_money += bet + raise_amount_int
                     break
     
     # If an invalid action is given, ask again     
     else:
         print("Invalid input. Please try again.")
