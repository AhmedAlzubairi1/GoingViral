import copy
import json
import random
from Player import Player
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from model import draw
app = Flask(__name__)
mark_as_deleted={

}
#Descriptions are foucsed on in the js side
cards=[
    {
    "name":"Hospitalization",
    "atp":3,
    "immediate":False,
    "hold":False,
    "treatment":True,
    "image":"/static/images/card/treatement_ebola.png"

}
,
{
    "name":"Bed Rest",
    "atp":3,
    "immediate":False,
    "hold":False,
    "treatment":True,
    "image":"/static/images/card/treatement_flu.png"

},

{
    "name":"Resistance",
    "atp":8,
    "immediate":False,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/resistance.png"

}
,
{
    "name":"Rapid Growth",
    "atp":10,
    "immediate":True,
    "hold":True,
    "treatment":False,
    "image":"/static/images/card/rapidgrowth.png"

}
,
    {
    "name":"Quarantine",
    "atp":0,
    "immediate":True,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/quaranine.png"

}
,
{
    "name":"No Vaccine",
    "atp":5,
    "immediate":True,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/novaccine.png"

}
,
{
    "name":"Gene Exchange",
    "atp":0,
    "immediate":False,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/geneexchange.png"

}
,
{
    "name":"Antibiotic",
    "atp":0,
    "immediate":True,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/antibiotic.png"

}
,
{
    "name":"Antiviral",
    "atp":0,
    "immediate":False,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/antiviral.png"

}
,
{
    "name":"2 ATP",
    "atp":2,
    "immediate":False,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/atp_2.png"

}
,
{
    "name":"4 ATP",
    "atp":4,
    "immediate":False,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/atp_4.png"

}
,
{
    "name":"5 ATP",
    "atp":5,
    "immediate":False,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/atp_5.png"

}
,
{
    "name":"10 ATP",
    "atp":10,
    "immediate":False,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/atp_10.png"

}
,
{
    "name":"12 ATP",
    "atp":12,
    "immediate":False,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/atp_12.png"

}
,
{
    "name":"15 ATP",
    "atp":15,
    "immediate":False,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/atp_15.png"

}
,
{
    "name":"Coinfection",
    "atp":0,
    "immediate":True,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/coinfection.png"

}
,
{
    "name":"Fever",
    "atp":0,
    "immediate":True,
    "hold":False,
    "treatment":False,
    "image":"/static/images/card/fever.png"

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
deck=None
playerOne=None
playerTwo=None


@app.route('/')
def homeScreen():
    return render_template('Home.html') 
#    return render_template('home.html', cards=animeInfo[-9:]) 
@app.route('/game')
def newGame():
    global deck, playerOne, playerTwo
    deck=copy.deepcopy(cards)
    playerOne=Player(1,"flu")
    playerTwo=Player(2,"ebola")
    return render_template('Game.html', deck=deck, playerOne=json.loads(json.dumps(playerOne.__dict__)), playerTwo=json.loads(json.dumps(playerTwo.__dict__)))
@app.route('/howToPlay')
def howToPlay():
    return render_template('HowToPlay.html')  
@app.route('/settings')
def settings():
    return render_template('Settings.html')  

@app.route('/draw', methods=['GET', 'POST'])
def drawCard():
    global deck
    return jsonify(drawnCard=draw(deck,cards))
@app.route('/draw2', methods=['GET', 'POST'])
def draw2Card():
    global deck
    twoCards=[]
    twoCards.append(draw(deck,cards))
    twoCards.append(draw(deck,cards))
    return jsonify(cards=twoCards) #we can now do ["data"] in js to reference data, or ["bob"] to reference 1


@app.route('/update', methods=['GET', 'POST'])
def update():
    data=request.get_json()
    if data["number"]==1:
        playerOne.update(data["player"])
        return jsonify(player=json.loads(json.dumps(playerOne.__dict__)))
    else:
        playerTwo.update(data["player"])
        return jsonify(player=json.loads(json.dumps(playerTwo.__dict__)))
@app.route('/nextStage', methods=['GET', 'POST'])
def nextStage():
    data=request.get_json()
    print(data)
    print(type(data))
    print('--------------------------------------')
    if data["number"]==1:
        upGraded = playerOne.advanceStage(data["player"])
        return jsonify(player=json.loads(json.dumps(playerOne.__dict__)), upGraded=upGraded)
    else:
        upGraded= playerTwo.advanceStage(data["player"])
        return jsonify(player=json.loads(json.dumps(playerTwo.__dict__)), upGraded=upGraded)
@app.route('/quarantine', methods=['GET', 'POST'])
def quarantine():
    data=request.get_json()
    print(data)
    print(type(data))
    print('----------------------------------------------------')
    if data["player"]==1:
        downGraded = playerOne.quaranine(data)
        if not downGraded:
            deck.append({"name":"Quarantine","atp":0,"immediate":True,"hold":False,"treatment":False,"image":"/static/images/card/quaranine.png"})
        print(deck)
        return jsonify(player=json.loads(json.dumps(playerOne.__dict__)), downGraded=downGraded)
    else:
        downGraded = playerTwo.quaranine(data)
        if not downGraded:
            deck.append({"name":"Quarantine","atp":0,"immediate":True,"hold":False,"treatment":False,"image":"/static/images/card/quaranine.png"})
        print(deck) 
        return jsonify(player=json.loads(json.dumps(playerTwo.__dict__)), downGraded=downGraded)


if __name__ == '__main__':
   app.run(debug = True)



