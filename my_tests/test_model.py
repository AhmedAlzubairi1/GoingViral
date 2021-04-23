from sys import path
import copy
from os.path import dirname as dir
from Flask_Project.model import draw, newDeck
path.append(dir(path[0]))

# Apparnelty don't need to do it for each


def test_drawOneCard():  # check to see if it works when people already exist
    """ Tests if user can draw one card
    """
    deck = [10, 20, 30]
    cards = [10, 20, 30]
    returnedCard = draw(deck, cards)
    assert returnedCard in cards
    assert len(deck) == 2


def test_drawOneCardEmpty():  # check to see if it works when people already exist
    """ Tests if the draw method resets an empty deck
    """
    deck = [10]
    cards = [10, 20, 30]
    returnedCard = draw(deck, cards)
    assert returnedCard in cards
    # print("hello")
    assert len(deck) == 3


def test_newDeck():
    """Tests if you can reset a deck
    """
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
    # tempCard
    returnedDeck = []
    returnedDeck.append(cards[0])
    for _ in range(3):
        returnedDeck.append(cards[1])
    for _ in range(3):
        returnedDeck.append(cards[2])
    for _ in range(4):
        returnedDeck.append(cards[3])
    returnedDeck.append(cards[4])
    for _ in range(5):
        returnedDeck.append(cards[5])
    for _ in range(2):
        returnedDeck.append(cards[6])
    for _ in range(2):
        returnedDeck.append(cards[7])
    returnedDeck.append(cards[8])
    for _ in range(18):
        returnedDeck.append(cards[9])
    for _ in range(23):
        returnedDeck.append(cards[10])
    for _ in range(14):
        returnedDeck.append(cards[11])
    for _ in range(8):
        returnedDeck.append(cards[12])
    for _ in range(5):
        returnedDeck.append(cards[13])
    returnedDeck.append(cards[14])
    returnedDeck.append(cards[14])
    returnedDeck.append(cards[15])

    assert newDeck() == copy.deepcopy(returnedDeck)
