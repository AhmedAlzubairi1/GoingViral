import copy
import random
cards = [
    {
        "name": "Quarantine",
        "atp": 0,
        "immediate": True,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/quaranine.png"

    },
    {
        "name": "Hospitalization",
        "atp": 3,
        "immediate": False,
        "hold": False,
        "treatment": True,
        "image": "/static/images/card/treatement_ebola.png"

    },
    {
        "name": "Bed Rest",
        "atp": 3,
        "immediate": False,
        "hold": False,
        "treatment": True,
        "image": "/static/images/card/treatement_flu.png"

    },

    {
        "name": "Resistance",
        "atp": 8,
        "immediate": False,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/resistance.png"

    },
    {
        "name": "Rapid Growth",
        "atp": 10,
        "immediate": True,
        "hold": True,
        "treatment": False,
        "image": "/static/images/card/rapidgrowth.png"

    },
    {
        "name": "No Vaccine",
        "atp": 5,
        "immediate": True,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/novaccine.png"

    },
    {
        "name": "Gene Exchange",
        "atp": 0,
        "immediate": False,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/geneexchange.png"

    },
    {
        "name": "Antibiotic",
        "atp": 0,
        "immediate": True,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/antibiotic.png"

    },
    {
        "name": "Antiviral",
        "atp": 0,
        "immediate": False,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/antiviral.png"

    },
    {
        "name": "4 ATP",
        "atp": 4,
        "immediate": False,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/atp_4.png"

    },
    {
        "name": "5 ATP",
        "atp": 5,
        "immediate": False,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/atp_5.png"

    },
    {
        "name": "10 ATP",
        "atp": 10,
        "immediate": False,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/atp_10.png"

    },
    {
        "name": "12 ATP",
        "atp": 12,
        "immediate": False,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/atp_12.png"

    },
    {
        "name": "15 ATP",
        "atp": 15,
        "immediate": False,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/atp_15.png"

    },
    {
        "name": "Coinfection",
        "atp": 0,
        "immediate": True,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/coinfection.png"

    },
    {
        "name": "Fever",
        "atp": 0,
        "immediate": True,
        "hold": False,
        "treatment": False,
        "image": "/static/images/card/fever.png"

    }

]
'''
This is stuff for rest of the virus

{
    "name":"Vaccination",
    "atp":3,
    "immediate":False,
    "hold":False,
    "treatment":True,
    "image":"/static/images/card/treatement_rabies.png"

}
,
{
    "name":"Anti-Retroviral",
    "atp":3,
    "immediate":False,
    "hold":False,
    "treatment":True,
    "image":"/static/images/card/treatement_hiv.png"

}
,
{
    "name":"Acetominophen",
    "atp":3,
    "immediate":False,
    "hold":False,
    "treatment":True,
    "image":"/static/images/card/treatement_zika.png"

}
'''


def newDeck():
    """ Returns an original copy of the deck of cards

    :return: Resetted deck of cads
    :rtype: list[dict]
    """
    print(f'new deck is returning type {type(copy.deepcopy(cards))}')
    returnedDeck = []
    # Set the current weights, index of weights should be:
    '''
    0 -> 1
    1 -> 3
    2 -> 3
    3 -> 4
    4 -> 1
    5 -> 5
    6 -> 2
    7 -> 2
    8 -> 1
    9 -> 18
    10 -> 23
    11 -> 14
    12 -> 8
    13 -> 5
    14 -> 2
    15 -> 1
    '''
    returnedDeck.append(cards[0])
    for i in range(3):
        returnedDeck.append(cards[1])
    for i in range(3):
        returnedDeck.append(cards[2])
    for i in range(4):
        returnedDeck.append(cards[3])
    returnedDeck.append(cards[4])
    for i in range(5):
        returnedDeck.append(cards[5])
    for i in range(2):
        returnedDeck.append(cards[6])
    for i in range(2):
        returnedDeck.append(cards[7])
    returnedDeck.append(cards[8])
    for i in range(18):
        returnedDeck.append(cards[9])
    for i in range(23):
        returnedDeck.append(cards[10])
    for i in range(14):
        returnedDeck.append(cards[11])
    for i in range(8):
        returnedDeck.append(cards[12])
    for i in range(5):
        returnedDeck.append(cards[13])
    returnedDeck.append(cards[14])
    returnedDeck.append(cards[14])
    returnedDeck.append(cards[15])
    return copy.deepcopy(returnedDeck)


def draw(deck, cardSet):
    """ Given a deck and cardset, a random card is popped from the deck and returned to user. It also resets the deck if it then becomes empty

    :param deck: Current deck
    :type deck: list[dict]
    :param cardSet: Original deck
    :type cardSet: list[dict]
    :return: Drawn card
    :rtype: dict
    """
    # Should take random card then remove it.
    cardLocation = random.randint(0, len(deck) - 1)
    newCard = deck[cardLocation]
    deck.pop(cardLocation)
    # After getting the card, i remove it from deck then reset the deck if
    # needed
    if len(deck) == 0:
        deck[:] = copy.deepcopy(cardSet)
    return newCard
