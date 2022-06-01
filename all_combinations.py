import itertools
import json

# Poker Tracker

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


def decompose_cards(which):
    n_which = []
    suits_which = []
    
    for i in range(0, len(which)):
        n_which.append(which[i][:-1])
        suits_which.append(which[i][0])
        
    return n_which, suits_which

        
def all_combinations(deck):
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
    
    n_deck = list(range(2, 15))
    suits_deck = ['h', 's', 'c', 'd']
    
    # High Card
    for k in n_deck:
        outs['high_card'].append([k])
    
    
    # Pairs
    for k in n_deck:
        outs['pair'].append([k, k])
    
    # Two pairs
    for k in n_deck:
        remain_n_deck = n_deck.copy()
        remain_n_deck.remove(k)
        for j in remain_n_deck:
            outs['two_pairs'].append([k, k, j, j])
            
    # Three of a kind
    for k in n_deck:
        outs['t_o_k'].append([k, k, k])
        
    # Straight
    i = min(n_deck)
    maxi = max(n_deck)
    while i + 5 <= maxi + 1:
       outs['straight'].append(list(range(i, i + 5)))
       i += 1
    
    # Flush
    for k in suits_deck:
        outs['flush'].append([k, k, k, k, k])
        
    # Full
    for k in n_deck:
        remain_n_deck = n_deck.copy()
        remain_n_deck.remove(k)
        for j in remain_n_deck:
            outs['full'].append([k, k, k, j, j])
            
    # Four of a kind
    for k in n_deck:
        outs['f_o_k'].append([k, k, k, k])
        
    # Straight flush
    for j in suits_deck:
        i = min(n_deck)
        maxi = max(n_deck)
        while i + 5 <= maxi:
            straight = list(range(i, i + 5))
            for item in range(0, len(straight)):
                straight[item] = str(straight[item]) + j
            outs['straight_flush'].append(straight)
            i += 1
            
    # Royal Flush
    for j in suits_deck:
        outs['royal_flush'].append(['10' + j, '11' + j, '12' + j, '13' + j, '14' + j])
        
        
    return outs

deck = create_deck()

dic_to_export = all_combinations(deck)

json_file = json.dumps(dic_to_export)

path = r'/Users/lucasA/Desktop/PokerTracker/Poker_Tracker/Combinations/combinations.json'

with open(path, "w") as outfile:
    outfile.write(json_file)


    
    