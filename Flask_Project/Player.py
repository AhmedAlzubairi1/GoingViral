
'''
Future Goals:
Have a constructur method that specifies the virus they want
'''

class Player():
    def __init__(self, player, virus):
        self.hand=[]
        self.stage=0
        self.atp=0
        self.player=player
        self.virus=virus
        self.virusImage=self.findVirusImage(virus)
        self.stageNumberList=self.setStageCount()
        self.stageImageList=["/static/images/stage/stage_1.png","/static/images/stage/stage_2.png","/static/images/stage/stage_3.png","/static/images/stage/stage_4.png","/static/images/stage/stage_5.png","/static/images/stage/stage_6.png"]
        self.stageImage=self.stageImageList[0]
        
    def advanceStage(self,data):
        self.update(data)
        if self.stage == 5:
            return False
        elif self.atp>=self.stageNumberList[self.stage]:
            self.update(data)
            self.stage+=1
            self.atp=0
            self.stageImage=self.stageImageList[self.stage]
            return True
        else:
            return False
    def findVirusImage(self,virus):
        if self.virus == "flu":
            return "/static/images/virus/flu.png"
        elif virus == "ebola":
            return "/static/images/virus/ebola.png"
    def setStageCount(self):
        if self.virus=="flu":
            return [6,12,18,44,50]
        elif self.virus=="ebola":
            return [40,12,16,34,28]
    def update(self,data):
        self.hand=data["hand"]
        self.stage=int(data["stage"])
        self.atp=int(data['atp'])
        self.stageImage=data["stageImage"]
        print(self.stage)
    def quaranine(self,data):
        if self.stage<=1:
            return False
        self.update(data)
        self.stage-=1
        self.stageImage=self.stageImageList[self.stage]
        return True
        

    
    

