from sys import path
from os.path import dirname as dir
from Flask_Project.model import draw
path.append(dir(path[0]))

#Apparnelty don't need to do it for each
def test_draw(): # check to see if it works when people already exist
    sample_friends = ["person1:email1,person2:email2,person3:email3"]
    actual_results = parseRowFriends(sample_friends)
    assert actual_results['friends'] == ['person1', 'person2', 'person3']
