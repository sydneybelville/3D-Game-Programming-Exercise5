from pubsub import pub
from view_object import ViewObject

class WorldView:
    def __init__(self, game_logic):
        self.game_logic = game_logic
        self.view_objects = {}

        pub.subscribe(self.new_game_object, 'create')

    def new_game_object(self, game_object):
        #if game_object.kind == 'player':
            #return

        view_object = ViewObject(game_object)
        self.view_objects[game_object.id] = view_object

    def tick(self):
        for key in self.view_objects:
            self.view_objects[key].tick()
