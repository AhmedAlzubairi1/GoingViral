from sys import path
from os.path import dirname as dir
from Flask_Project.Player import Player
path.append(dir(path[0]))


# Apparnelty don't need to do it for each
def test_Update():  # check to see if it works when people already exist
    """Tests if you can update all the member variables of a player object
    """
    player = Player(1, "flu")
    data = {"hand": [], "stage": "1", "atp": "2", "stageImage": "/testImage"}
    player.update(data)
    assert player.hand == []
    assert player.stage == 1
    assert player.atp == 2
    assert player.stageImage == "/testImage"


def test_AdvanceStageMax():
    """Tests that user can't advance past stage 5
    """
    player = Player(1, "flu")
    player.stage = 5
    assert player.advanceStage(
        data={
            "hand": [],
            "stage": "1",
            "atp": "2",
            "stageImage": "/testImage"}) == False


def test_AdvanceStageValid():
    """Tests that player's virus can advance its stage
    """
    player = Player(1, "flu")
    player.advanceStage(
        data={
            "hand": [],
            "stage": "0",
            "atp": "200",
            "stageImage": "/testImage"})
    assert player.stage == 1
    assert player.stageImage == "/static/images/stage/stage_2.png"


def test_AdvanceStageInvalid():
    """Tests that player can't advance their virius' stage if they dont have enough ATP
    """
    player = Player(1, "flu")
    assert player.advanceStage(
        data={
            "hand": [],
            "stage": "0",
            "atp": "0",
            "stageImage": "/testImage"}) == False


def test_findVirusImageFlu():
    """ TEsts if correct image path of virus is given for the flu
    """
    player = Player(1, "flu")
    assert player.findVirusImage(
        player.virus) == "/static/images/virus/flu.png"


def test_findVirusImageEbola():
    """TEsts if correct image path of virus is given for ebola
    """
    player = Player(1, "ebola")
    assert player.findVirusImage(
        player.virus) == "/static/images/virus/ebola.png"


def test_setStageCountEbola():
    """Tests if the correct stage thershold limits for ebola is provided
    """
    player = Player(1, "ebola")
    assert player.setStageCount() == [40, 12, 16, 34, 28]


def test_setStageCountFlu():
    """Tests if the correct stage thershold limits for the flu is provided
    """
    player = Player(1, "flu")
    assert player.setStageCount() == [6, 12, 18, 44, 50]


def test_quarantineInvalid():
    """ Tests if quaraninte can't work if player isn't at stage higher than 3
    """
    player = Player(1, "flu")
    assert player.quaranine([]) == False


def test_quarantineValid():
    """Tests that quaranine lowers stage if user is at a stage greater than 2
    """
    player = Player(1, "flu")
    player.stage = 2
    player.quaranine(
        data={
            "hand": [],
            "stage": "2",
            "atp": "200",
            "stageImage": "/testImage"})
    assert player.stage == 1
    assert player.stageImage == "/static/images/stage/stage_2.png"
