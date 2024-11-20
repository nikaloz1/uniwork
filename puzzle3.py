import random

def setup_deck():
    """Creates a standard deck of 52 cards."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    return [(rank, suit) for suit in suits for rank in cards]

def find_relative_position(rank1, rank2):
    """Finds the relative position of rank2 with respect to rank1 using modular arithmetic."""
    rank_order = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    pos1 = rank_order.index(rank1)
    pos2 = rank_order.index(rank2)
    return (pos2 - pos1) % 13

def magictrick():
    """Simulates the card trick."""
    # making the deck and shuffling it
    deck = setup_deck()
    random.shuffle(deck)
    
    # selection of the 5 cards
    chosen_cards = random.sample(deck, 5)
    print("The chosen cards are:")
    for card in chosen_cards:
        print(card)
    
    # classification of cads by suits
    suits = {}
    for card in chosen_cards:
        rank, suit = card
        if suit not in suits:
            suits[suit] = []
        suits[suit].append(rank)
    
    # two suits of one card
    secret_suit = None
    for suit, cards in suits.items():
        if len(cards) >= 2:
            secret_suit = suit
            break
    
    # secret and key cards
    secret_rank, key_rank = suits[secret_suit][:2]
    secret_card = (secret_rank, secret_suit)
    key_card = (key_rank, secret_suit)
    
    # position of the secret card
    relative_position = find_relative_position(key_rank, secret_rank)
    
    # sorting remaininh cards
    remaining_cards = [card for card in chosen_cards if card != secret_card]
    random.shuffle(remaining_cards)
    
    # output key and the rest three cards
    print("\nAssistant shows these cards to the Magician:")
    shown_cards = [key_card] + remaining_cards[:3]
    for card in shown_cards:
        print(card)
    
    # the secret card
    print("\nMagician determines the secret card is:")
    print(secret_card)


magictrick()
