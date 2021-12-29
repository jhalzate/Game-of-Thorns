# This class along with Map(object) class handle the transition between
# scenes in the Game of Thorns game. It will keep on looping scene 
# after scene until an exception or an exit() is found.
#
# scene_map will be an instance of Map(object) and its opening_scene
# method will return the intial scene in the game.

class Engine(object):
    """In charge of handling the scene sequence of Thy Game."""
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        """Play the game."""
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n-----------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
