from random import randint
import sys
import time

class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
    
    def delay_print(self, s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.01)


class FailedKingdom(Scene):
    
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Yuo've failed yourself, your family, your kingdom, you deserve nothing but to die.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You are a joke of a warrior"
    ]
    def enter(self):
        print FailedKingdom.quips[randint(0, len(self.quips) - 1)]
        print "\n"
        exit(1)
    

class CentralKingdom(Scene):
    
    def enter(self):
        verbiage = [
            "You are the bravest warrior living in Central Kingdom",
            "together with North, South, East and West, your Central Kingdom",
            "would become a global super power able to influence what happens",
            "in virtually any single place on planet earth.",
            "\n",
            "But to achieve this level of power you have to first convince",
            "and come into terms with your neighbors from the North, South, East, and West.",
            "Without all of their supports, the Kingdom will weaken via internal",
            "disputes, to the point that the rest of the world will notice",
            "and will decide to nuke-bomb each of the 5 main cities in the Kingdom",
            "and the Kingdom will be doomed and you yourself will be the first one to",
            "burn into flames and die upon the foreing shellings.",
            "\n",
            "Your mission is to in a record time; go and conquer or convince the other",
            "4 four kingdoms in the kinghood to unite and become The One and Only:",
            "UNITED KINGDOM",
            "\n",
            "Otherwise, you misserably fail Yourself, your Family, your Kingdom, and",
            "the planet Earth, Die"
        ]
        a_scene = Scene()
        for i in verbiage:
            a_scene.delay_print(i)
            print ""
        
        action = raw_input("Which kingdom would you approach first? > ")
        
        if action == "North":
            print "\n"
            print "Good choice. The Northners are about to get attacked at the"
            print "North Wall by the Wildlings. If you go there now and help them"
            print "defeat the imminent threat, they will most likely join you in the"
            print "Quest to unite the rest of the kinghood"
            return 'north'
        
        elif action == "South":
            print "\n"
            print "I'm sorry. The people in the Highlands from the South won't"
            print "even receive your courier if you haven't secured at least"
            print "the support from another king."
            print "Your kingdom is doomed from inception."
            return 'doomed'
            
        elif action == "East":
            print "\n"
            print "I'm sorry. The people in the Wetlands from the East won't"
            print "even receive your courier if you haven't secured at least"
            print "the support from other 2 kings."
            print "Your kingdom is doomed from inception."
            return 'doomed'
        
        elif action == "West":
            print "\n"
            print "I'm sorry. The people of Westeros won't even"
            print "receive your courier if you haven't secured the support"
            print "from the 3 other kings in the kinghood."
            print "Your kingdom is doomed from inception."
            return 'doomed'
        
        else:
            print "\n"
            print "DOES NOT COMPUTE"
            return 'central_kingdom'

class NorthWall(Scene):
    
    def enter(self):
        verbiage = [
            "Uppon arriving at the North Wall, you and your army are warmly received.",
            "The Northners are preparing for winter and the imminent attack from the",
            "Wildlings.",
            "\n",
            "The keeper of the wall asks for your help on this deadly feat"
        ]
        
        a_scene = Scene()
        for i in verbiage:
            a_scene.delay_print(i)
            print ""        
        
        action = raw_input("Would you join forces with the gate keeper? > ")
        
        if action == 'yes':
            print "\n"
            print "Great. I knew I could count on you my brother"
            print "Let's slay a few of these crapy frozen beasts and then we will join"
            print "your forces to go and convince the South, the East, and the West"
        
            action1 = raw_input("Which kingdom would you approach next? > ")
        
            if action1 == "South":
                print "\n"
                print "You naughty warrior! You are becoming a chees master. The Highlanders"
                print "will more likely join your unifying efforts if they see you already gained"
                print "support from the North kingdom. Even if they don't, you are know a stronger"
                print "force, capable of coercing any of the other three kingdoms ...."
                print "unless they already joined forces among them"
                return 'south'
                        
            elif action1 == "East":
                print "\n"
                print "I'm sorry. The people in the Wetlands from the East won't"
                print "even receive your couriers if you haven't secured at least"
                print "the support from 2 other kings first."
                print "Your kingdom became doomed at a very ealy stage."
                return 'doomed'
            
            elif action1 == "West":
                print "\n"
                print "I'm sorry. The people of Westeros won't even"
                print "receive your couriers if you haven't secured the support"
                print "from the 3 other kings in the kinghood first."
                print "Your kingdom became doomed at a very ealy stage."
                return 'doomed'
            
            else:
                print "\n"
                print "DOES NOT COMPUTE"
                return 'north'
        
        else:
            print "\n"
            print "Worst error you could ever have commited. The Northners had long been"
            print "preparing for war. And now instead of helping your unification efforts"
            print "they decide to fight your army and quickly take back control, before"
            print "news about this dispute slips out of the border and foreing forces decide"
            print "to intervene."
            print "Your kingdom became doomed at a very ealy stage."
            return 'doomed'            

class SouthLands(Scene):
    
    def enter(self):
        verbiage = [
            "After three long weeks ridding their horses from the North all the way",
            "to the South. The highlanders are surprised by the number of caballiers and",
            "soldiers on foot. The cold and the food scarcity had made a dent on the",
            "augmented army's morale. They urgently needed some rest and quality meals.",
            "The Highlanders are peaceful people and always willing to help in Unifying",
            "campains.",
            "\n",
            "After a few days of resting; Central, North, and South form the largest",
            "Army ever seen according the Kinghood History Books",
            "The Large mass heads towards the Wetlands of the East."
        ]
        
        a_scene = Scene()
        for i in verbiage:
            a_scene.delay_print(i)
            print ""
        
        return 'east'
    
class Westeros(Scene):
    
    def enter(self):
        verbiage = [
            "After three long weeks ridding their horses from the North all the way",
            "to the South. The highlanders are surprised by the number of caballiers, knights,",
            "and soldiers on foot. The cold and the food scarcity had made a dent on the",
            "augmented army's morale. They urgently needed some rest and quality meals.",
            "The Highlanders are peaceful people and always willing to help in Unifying",
            "campains.",
            "\n",
            "After a few days of resting; Central, North, and South form the largest",
            "Army ever seen according the Kinghood History Books",
            "God Bless the Queen!."
        ]
        
        a_scene = Scene()
        for i in verbiage:
            a_scene.delay_print(i)
            print ""
        
        return 'united'
    
class Wetlands(Scene):
    
    def enter(self):
        verbiage = [
            "After three long weeks ridding their horses from the North all the way",
            "to the South. The highlanders are surprised by the number of caballies and",
            "soldiers on foot. The cold and the food scarcity had made a dent on the",
            "augmented army's morale. They urgently needed some rest and quality meals.",
            "The Highlanders are peaceful people and always willing to help in Unifying" ,
            "campains.",
            "\n",
            "After a few days of resting; Central, North, and South form the largest",
            "The Large mass heads towards Westeros in thier last effort to",
            "becoming a truly Great United Kingdom."
        ]
        
        a_scene = Scene()
        for i in verbiage:
            a_scene.delay_print(i)
            print ""
        
        return 'west'
    
class Won(Scene):
    
    def enter(self):
        print "Individually we are Amazing"
        print "Together WE ARE UNSTOPPABLE"
        print "You Won! You became the Greates Kingdom on Earth!!!"
        print "Now is time to go out and conquer the WORLD"
        print "\n"
        exit(1)

class Map(object):
    
    scenes = {
        'central_kingdom': CentralKingdom(),
        'north': NorthWall(),
        'south': SouthLands(),
        'west': Westeros(),
        'east': Wetlands(),
        'doomed': FailedKingdom(),
        'united': Won()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        

# a_map = Map('central_kingdom')
# a_game = Engine(a_map)
# a_game.play()
