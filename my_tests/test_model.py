from sys import path
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
    tempCards = [
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
            "name": "Quarantine",
            "atp": 0,
            "immediate": True,
            "hold": False,
            "treatment": False,
            "image": "/static/images/card/quaranine.png"

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
            "name": "2 ATP",
            "atp": 2,
            "immediate": False,
            "hold": False,
            "treatment": False,
            "image": "/static/images/card/atp_2.png"

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
    assert newDeck() == tempCards
