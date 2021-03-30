import copy
import random
cards = [
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
    return copy.deepcopy(cards)


def draw(deck, cardSet):
    # Should take random card then remove it.
    cardLocation = random.randint(0, len(deck) - 1)
    newCard = deck[cardLocation]
    deck.pop(cardLocation)
    # After getting the card, i remove it from deck then reset the deck if
    # needed
    if len(deck) == 0:
        deck[:] = copy.deepcopy(cardSet)
    return newCard
