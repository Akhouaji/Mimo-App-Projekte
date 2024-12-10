import random

def create_deck():
  
  suits = ["♥", "♦", "♣", "♠"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

  deck = []

  for s in suits :
    for r in ranks :
      deck.append((s, r))

  random.shuffle(deck)
  
  return deck

def draw_card(deck, cardn):
  hand = []
  for n in range(cardn):
    hand.append(deck.pop())
  return hand, deck

deck = create_deck()

def show_card(card):
  space = " "
  if len(card[1]) == 2:
    space = ""
  print (f"""
  +-------+
  |{card[1]}     {space}|
  |       |
  |   {card[0]}   |
  |       |
  |{space}     {card[1]}|
  +-------+
  """)


while len(deck) > 0:
  num_cards = int(input(f"There are {len(deck)} cards left, how many cards do you want? "))
  if num_cards > len(deck) :
    print(f"There are only {len(deck)} cards left, drawing {len(deck)} cards")
    num_cards = len(deck)
  else: 
    print(f"drawing {num_cards} cards")

  hand, deck = draw_card(deck, num_cards)
  for card in hand:
    show_card(card)

print("We are out of cards")