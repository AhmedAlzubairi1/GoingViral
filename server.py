import re
import copy
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
mark_as_deleted={

}
animeInfo=[
{
    "id":30,
    "title":"Dragon Ball Z",
    "image": "https://cdn.myanimelist.net/images/anime/6/20936.jpg",
    "info": "Five years after winning the World Martial Arts tournament, Gokuu is now living a peaceful life with his wife and son. This changes, however, with the arrival of a mysterious enemy named Raditz who presents himself as Gokuu's long-lost brother. He reveals that Gokuu is a warrior from the once powerful but now virtually extinct Saiyan race, whose homeworld was completely annihilated. When he was sent to Earth as a baby, Gokuu's sole purpose was to conquer and destroy the planet; but after suffering amnesia from a head injury, his violent and savage nature changed, and instead was raised as a kind and well-mannered boy, now fighting to protect others. With his failed attempt at forcibly recruiting Gokuu as an ally, Raditz warns Gokuu's friends of a new threat that's rapidly approaching Earth—one that could plunge Earth into an intergalactic conflict and cause the heavens themselves to shake. A war will be fought over the seven mystical dragon balls, and only the strongest will survive in Dragon Ball Z."
    ,"year": 1989,
    "reviews": []
},
    {
    "id":31,
    "title": "Naruto",
    "image": "https://cdn.myanimelist.net/images/anime/13/17405.jpg",
    "info": "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the village, the Fourth Hokage, sacrificed his life and sealed the monstrous beast inside the newborn Naruto.Now, Naruto is a hyperactive and knuckle-headed ninja still living in Konohagakure. Shunned because of the Kyuubi inside him, Naruto struggles to find his place in the village, while his burning desire to become the Hokage of Konohagakure leads him not only to some great new friends, but also some deadly foes.",
    "year": 2002,
    "reviews": [["I loved Naruto",False], ["Naruto was okay",False], ["wasn't the biggest fan",False], ["Yah are bugging, naruto is amazing",False]]
}
]

#animeList=['Naruto', 'Hunter x Hunter', 'Fullmetal Alchemist: Brotherhood', 'Bleach', 'Suzumiya Haruhi no Shoushitsu', 'Yakusoku no Neverland', 'One Punch Man', 'Ashita no Joe 2', 'Mushishi Zoku Shou: Suzu no Shizuku', 'Kizumonogatari II: Nekketsu-hen', 'Chihayafuru 3', 'Bakuman. 3rd Season', 'Death Note', 'Fate/Zero Season 2', 'Kimi no Na wa.', 'Gintama: Enchousen', 'A Silent Voice', 'Haikyu!! 3rd Season', 'Clannad: After Story', 'Owarimonogatari Second Season', 'Code Geass: Lelouch of the Rebellion R2', 'Mob Psycho 100 II', 'Spirited Away', 'Demon Slayer: Kimetsu no Yaiba', 'Your Lie in April', 'Made in Abyss', 'Cowboy Bebop', 'Vinland Saga', 'Princess Mononoke', 'Dragon Ball Z']



@app.route('/')
def homeScreen():
    return render_template('Home.html') 
#    return render_template('home.html', cards=animeInfo[-9:]) 
@app.route('/newGame')
def newGame():
    return render_template('NewGame.html')
@app.route('/howToPlay')
def howToPlay():
    return render_template('HowToPlay.html')  
@app.route('/settings')
def settings():
    return render_template('Settings.html')  
@app.route('/Game')
def playGame():
    return render_template('Game.html')  


@app.route('/view/<id>')
def view(id=None):
    print(f'Look id is {id}')
    look=int(id)
    temp={
    "id":look,
    "title":     "",
    "image": "",
    "info":""
    ,"year": 0,
    "reviews": ["Error"]
}
    for i in animeInfo:
        if i["id"]==look:
            temp["title"]=i["title"]
            temp["image"]=i["image"]
            temp["info"]=i["info"]
            temp["year"]=i["year"]
            temp["reviews"]=i["reviews"]
    
    return render_template('view.html',id=look,currentAnime=temp) 

@app.route('/search', methods=['GET', 'POST'])
def update():
    global animeInfo
    json_data = request.get_json() 
    #print(json_data)
    #print(f'Searching for {json_data} and of type {type(json_data)}') 
    requestList=[]
    pat=json_data
    for i in animeInfo:
        if re.search(pat.lower(),i["title"].lower())!=None:
            result = re.sub('('+pat.lower()+')', r'<b>\1</b>', i["title"],flags=re.IGNORECASE)  
            bob={
               "id":i["id"],
                "title":     result,
                "image": i["image"],
                "info":i["info"]
                ,"year": i["year"],
                "reviews": i["reviews"]
            }
            requestList.append(bob)
        elif re.search(pat.lower(),i["info"].lower())!=None:
            #result = re.sub('('+pat.lower()+')', r'<b>\1</b>', i["info"],flags=re.IGNORECASE)  
            requestList.append(i)            
    return jsonify(requestList=requestList) #we can now do ["data"] in js to reference data, or ["bob"] to reference 1

@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    global animeInfo
    #0 means none, 1 means review only, 2 means dateONLY, 3 means both
    json_data=request.get_json() 
    print(f'-----------{json_data}')
    if json_data["combo"]==1:
        look = json_data["id"]
        review = json_data["review"]
        lookIndex=0
        for i in range(len(animeInfo)):
            if animeInfo[i]["id"]==look:
                lookIndex=i
                break
        animeInfo[lookIndex]["reviews"].append([review,False])
        return jsonify(id=look) #we can now do ["data"] in js to reference data, or ["bob"] to reference 1
    elif json_data["combo"]==2:
        look = json_data["id"]
        date = json_data["year"]
        lookIndex=0
        for i in range(len(animeInfo)):
            if animeInfo[i]["id"]==look:
                lookIndex=i
                break
        animeInfo[lookIndex]["year"]=int(date)
        return jsonify(id=look) #we can now do ["data"] in js to reference data, or ["bob"] to reference 1
    elif json_data["combo"]==3:
        look = json_data["id"]
        review = json_data["review"]
        date = json_data["year"]
        lookIndex=0
        for i in range(len(animeInfo)):
            if animeInfo[i]["id"]==look:
                lookIndex=i
                break
        animeInfo[lookIndex]["reviews"].append([review,False])
        animeInfo[lookIndex]["year"]=int(date)

        return jsonify(id=look) #we can now do ["data"] in js to reference data, or ["bob"] to reference 1

    else:
        return jsonify(id="look")
@app.route('/undo', methods=['GET', 'POST'])
def undo():
    global animeInfo
#   global animeList
    json_data = request.get_json() #Usually json_data would be just an int, now it is a list where first is int and second is location of review to mark as true 
    reviewList=[]
    print(json_data)
    #Found possible Issue: It is i am not deleting
    for i in range(len(animeInfo)):
        if animeInfo[i]["id"]==json_data[0]:
            for k in range(len(animeInfo[i]["reviews"])):
                if k == json_data[1]:
                    animeInfo[i]["reviews"][k][1]=False
                    reviewList=animeInfo[i]["reviews"]
                    break
            break
    return jsonify(reviewList=reviewList)



@app.route('/delete_review', methods=['GET', 'POST'])
def delete_review():
    global animeInfo
#   global animeList
    json_data = request.get_json() #Usually json_data would be just an int, now it is a list where first is int and second is location of review to mark as true 
    reviewList=[]
    print(json_data)
    #Found possible Issue: It is i am not deleting
    for i in range(len(animeInfo)):
        if animeInfo[i]["id"]==json_data[0]:
            for k in range(len(animeInfo[i]["reviews"])):
                if k == json_data[1]:
                    animeInfo[i]["reviews"][k][1]=True
                    reviewList=animeInfo[i]["reviews"]
                    break
            break
    return jsonify(reviewList=reviewList) 
@app.route('/create')
def create():
    return render_template('create.html',current_id=current_id) 

@app.route('/add_anime', methods=['GET', 'POST'])
def add_anime():
    global animeInfo
    global current_id
    json_data = request.get_json()
    print(f"Requesting {json_data}")
    animeInfo.append(json_data)
    current_id+=1
    return jsonify(lastID=(current_id-1)) 
if __name__ == '__main__':
   app.run(debug = True)



