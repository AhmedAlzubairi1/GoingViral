import json
from Player import Player
from flask import Flask
from flask import render_template
from flask import request, jsonify
from model import draw, newDeck
app = Flask(__name__)
mark_as_deleted = {

}
# Descriptions are foucsed on in the js side
cards = newDeck()
deck = None
playerOne = None
playerTwo = None


@app.route('/')
def homeScreen():
    """Generate the homescreen page of the website

    :return: the rendered home.html page
    :rtype: str
    """
    return render_template('Home.html')


@app.route('/game')
def newGame():
    """ Resets the deck list, and the profiles for player one and player two. After that it renders the Game.html file

    :return: Game.html
    :rtype: str
    """
    global deck, playerOne, playerTwo
    deck = newDeck()
    playerOne = Player(1, "flu")
    playerTwo = Player(2, "ebola")
    return render_template(
        'Game.html', deck=deck, playerOne=json.loads(
            json.dumps(
                playerOne.__dict__)), playerTwo=json.loads(
            json.dumps(
                playerTwo.__dict__)))


@app.route('/howToPlay')
def howToPlay():
    """Renders the howtoplay.html

    :return: howtoplay.html
    :rtype: str
    """
    return render_template('HowToPlay.html')


@app.route('/draw', methods=['GET', 'POST'])
def drawCard():
    """On the /draw endpoint, it returns a random drawn card from the deck

    :return: JSON version of a card
    :rtype: dict
    """
    global deck
    t=draw(deck, cards)
    return jsonify(drawnCard=t)


@app.route('/draw2', methods=['GET', 'POST'])
def draw2Card():
    """ on the /draw2 endpoint it returns 2 random cards from thed deck.

    :return: List of 2 random cards
    :rtype: list
    """
    global deck
    twoCards = []
    twoCards.append(draw(deck, cards))
    twoCards.append(draw(deck, cards))
    return jsonify(cards=twoCards)


@app.route('/update', methods=['GET', 'POST'])
def update():
    """ On the /update endpoint, it updates the player one or player two data in the backend side and then returns the json version
    of them to be updated in the front end side

    :return: JSON format of player data
    :rtype: dict
    """
    data = request.get_json()
    if data["number"] == 1:
        playerOne.update(data["player"])
        return jsonify(player=json.loads(json.dumps(playerOne.__dict__)))
    else:
        playerTwo.update(data["player"])
        return jsonify(player=json.loads(json.dumps(playerTwo.__dict__)))


@app.route('/nextStage', methods=['GET', 'POST'])
def nextStage():
    """ On the /nextStage end point, it tests to see if the current player's virus can be advacned. If it can, it goes to the next stage and updates the virus stage. If not,
    It lets the user know and doesnt't update the stage.

    :return: JSON formate of player data
    :rtype: dict
    """
    data = request.get_json()
    if data["number"] == 1:
        upGraded = playerOne.advanceStage(data["player"])
        return jsonify(
            player=json.loads(
                json.dumps(
                    playerOne.__dict__)),
            upGraded=upGraded)
    else:
        upGraded = playerTwo.advanceStage(data["player"])
        return jsonify(
            player=json.loads(
                json.dumps(
                    playerTwo.__dict__)),
            upGraded=upGraded)


@app.route('/quarantine', methods=['GET', 'POST'])
def quarantine():
    """ On the /quarantine endpoint it is expected that the quarantine card has been activated by the player. If the player is downgraded a stage,
    it lowers the players stage.  if they werent downgraded, quarantine gets reshuffled back into the deck. Regardless, updated player profile is sent back

    :return: JSON format of player's updated state
    :rtype: dict
    """
    data = request.get_json()
    if data["player"] == 1:
        # If im playerOne and I have to downgrade, I just give back to the deck the quarantine card.
        playerOne.update(data)
        downGraded = playerOne.quaranine(data)
        if not downGraded:
            deck.append({"name": "Quarantine",
                         "atp": 0,
                         "immediate": True,
                         "hold": False,
                         "treatment": False,
                         "image": "/static/images/card/quaranine.png"})
        return jsonify(
            player=json.loads(
                json.dumps(
                    playerOne.__dict__)),
            downGraded=downGraded)
    else:
        playerTwo.update(data)
        downGraded = playerTwo.quaranine(data)
        if not downGraded:
            deck.append({"name": "Quarantine",
                         "atp": 0,
                         "immediate": True,
                         "hold": False,
                         "treatment": False,
                         "image": "/static/images/card/quaranine.png"})
        return jsonify(
            player=json.loads(
                json.dumps(
                    playerTwo.__dict__)),
            downGraded=downGraded)


if __name__ == '__main__':
    app.run(debug=True)
