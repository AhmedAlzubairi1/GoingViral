import copy
import random
def draw(deck,cardSet):
    # Should take random card then remove it.
    cardLocation = random.randint(0,len(deck)-1)
    newCard=deck[cardLocation]
    deck.pop(cardLocation)
    #After getting the card, i remove it from deck then reset the deck if needed
    if len(deck)==0:
        deck[:]=copy.deepcopy(cardSet)
    return newCard
