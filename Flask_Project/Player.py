
'''
Future Goals:
Have a constructur method that specifies the virus they want
'''


class Player():
    def __init__(self, player, virus):
        """ Initialize a Player object

        :param player: integer of 1 or 2 representing if the player is player 1 or player 2
        :type player: int
        :param virus: The name of the virus in lowercase
        :type virus: str
        """
        self.hand = []
        self.stage = 0
        self.atp = 0
        self.player = player
        self.virus = virus
        self.virusImage = self.findVirusImage(virus)
        self.stageNumberList = self.setStageCount()
        self.stageImageList = [
            "/static/images/stage/stage_1.png",
            "/static/images/stage/stage_2.png",
            "/static/images/stage/stage_3.png",
            "/static/images/stage/stage_4.png",
            "/static/images/stage/stage_5.png",
            "/static/images/stage/stage_6.png"]
        self.stageImage = self.stageImageList[0]

    def advanceStage(self, data):
        """ Given the new updated data, the player updates the data and tests if the stage can be updated. It needs enough atp to be updated. This is checked based on the
        stage limits of the individual virus.

        :param data: A dictonary showing the state of the player
        :type data: dict
        :return: A boolean indicating if the player's virus' stage was increased
        :rtype: bool
        """
        self.update(data)
        if self.stage == 5:
            return False
        elif self.atp >= self.stageNumberList[self.stage]:
            self.update(data)
            self.stage += 1
            self.atp = 0
            self.stageImage = self.stageImageList[self.stage]
            return True
        else:
            return False

    def findVirusImage(self, virus):
        """ Returns the file location of the png image of the virus

        :param virus: Name of virus in lowercase
        :type virus: str
        :return: File location of virus image file
        :rtype: str
        """
        if self.virus == "flu":
            return "/static/images/virus/flu.png"
        elif virus == "ebola":
            return "/static/images/virus/ebola.png"

    def setStageCount(self):
        """ Returns the stage threshold limits for player's virus

        :return: List of threshold limits per stage of virus
        :rtype: list
        """
        if self.virus == "flu":
            return [6, 12, 18, 44, 50]
        elif self.virus == "ebola":
            return [40, 12, 16, 34, 28]

    def update(self, data):
        """ Changes player's stats with that of input data parameter.

        :param data: A dictionary representing the updated stats of the player
        :type data: dict
        """
        self.hand = data["hand"]
        self.stage = int(data["stage"])
        self.atp = int(data['atp'])
        self.stageImage = data["stageImage"]

    def quaranine(self, data):
        """ Used when quarantine card is played. If the player is in a stage greater than 2 they go back one stage. If stage 2 or lower, card gets reshuffled into deck.
        :param data: A dictionary representing the updated stats of the player
        :type data: dict
        :return: Boolean indicating if player's stage was reduced
        :rtype: bool
        """
        if self.stage <= 1:
            return False
        self.stage -= 1
        self.stageImage = self.stageImageList[self.stage]
        return True
