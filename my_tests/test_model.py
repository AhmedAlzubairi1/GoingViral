from sys import path
from os.path import dirname as dir
from Flask_Project.model import draw
path.append(dir(path[0]))

#Apparnelty don't need to do it for each
def test_drawOneCard(): # check to see if it works when people already exist
    deck = [10,20,30]
    cards=[10,20,30]
    returnedCard=draw(deck,cards)
    assert returnedCard in cards
    assert len(deck)==2
def test_drawOneCardEmpty(): # check to see if it works when people already exist
    deck = [10]
    cards=[10,20,30]
    returnedCard=draw(deck,cards)
    assert returnedCard in cards
    #print("hello")
    assert len(deck)==3

