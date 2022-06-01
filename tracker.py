import json

def create_deck():
    suits = ['c', 'd', 'h', 's']

    cards = []

    for i in range(1, 14):
        cards.append(i)

    deck = []

    for card in cards:
        for suit in suits:
            create_card = str(card) + suit
            deck.append(create_card)
            
    return deck

def update_deck(deck, hand, table):
    for card in hand:
        if card in deck:
            deck.remove(card)
    if table != None:
        for card in table:
            if card in deck:
                deck.remove(card)
                
def decompose_cards(which):
    n_which = []
    suits_which = []
    
    for i in range(0, len(which)):
        n_which.append(which[i][:-1])
        suits_which.append(which[i][0])
        
    return n_which, suits_which 
    
 
def outs_probabilities(table, hand, combinations, remaining_turns, deck):
    outs = {'high_card' : [],
            'pair' : [],
            'two_pairs' : [],
            't_o_k' : [],
            'straight' : [],
            'flush' : [],
            'full' : [],
            'f_o_k' : [],
            'straight_flush' : [],
            'royal_flush' : []}
    
    available_cards = hand + table
    
    # decompose cards into (value / suit)
    n_available, suits_available = decompose_cards(available_cards)
    n_deck, suits_deck = decompose_cards(deck)
    n_hand, suits_hand = decompose_cards(hand)
    
    # convert cards values to integers
    for i in range(0, len(n_deck)):
        n_deck[i] = int(n_deck[i])
        
    for i in range(0, len(n_hand)):
        n_hand[i] = int(n_hand[i])
        
    for i in range(0, len(n_available)):
        n_available[i] = int(n_available[i])

    # for all figures
    for out in outs.keys():
        # execpt for high card
        if out == 'high_card':
            outs[out] = f'{round(max(n_hand) / 14, 2) * 100} %'
        else:
            # for all combinations
            for item in combinations[out]:
                # check if we have required cards
                required_nb_cards = []
                n_available_copy = n_available.copy()

                for i in item:
                    if i not in n_available_copy:
                        required_nb_cards.append(i)
                    else:
                        n_available_copy.remove(i)
                
                required_nb_cards = len(required_nb_cards)
                
                # if we do -> probability of combination is 100%
                if required_nb_cards == 0:
                    outs[out] = '100 %'
                    break
                # if not then...  
                # impossible darws
                if required_nb_cards > remaining_turns:
                    outs[out].append(0)
                # possible draws
                else:
                    # which cards are missing ?
                    print(out, item, required_nb_cards)  
                    required_values = list(set(item) - set(available_cards))
                    # probability of drawing missing cards given state of game
                    for value in required_values:
                        nb_in_deck = n_deck.count(value)
                        p = nb_in_deck / len(deck)
                    
                    outs[out].append(p)
            # total probabilities
            if len(outs[out]) == len(combinations[out]):
                proba = round(sum(outs[out]), 2)
                outs[out] = f'{proba * 100} %'
            else:
                pass
            
    return outs

path = r'/Users/lucasA/Desktop/PokerTracker/Poker_Tracker/Combinations/combinations.json'

with open(path, 'r') as openfile:
    combinations = json.load(openfile)

state = int(input('state : ?'))

if type(state) != int:
    print('erreur')
    state = int(input('state : ?'))
elif state < 1 or state > 5:
    print('erreur')
    state = int(input('state : ?'))
else:
    pass

remaining_turns = 5 - state

hand = ['10s', '4c']
table  = ['4d', '3s', '9s']

deck = create_deck()

outs = outs_probabilities(table, hand, combinations, remaining_turns, deck)



