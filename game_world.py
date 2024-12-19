from pubsub import pub
from game_object import GameObject
from player import Player

class GameWorld:
    def __init__(self):
        self.properties = {}
        self.game_objects = {}

        self.next_id = 0

    def create_object(self, position, kind, size):
        # TODO: we'll need to create the right subclass here
        # We need to work out how to know which one to use

        if kind == "player":
            obj = Player(position, kind, self.next_id, size)
        else:
            obj = GameObject(position, kind, self.next_id, size)

        self.next_id += 1
        self.game_objects[obj.id] = obj

        pub.sendMessage('create', game_object=obj)
        return obj

    def tick(self):
        for id in self.game_objects:
            self.game_objects[id].tick()

        # TODO: let the physics world get a tick in

    def load_world(self):
        self.create_object([0, 0, 0], "crate", (5,2,1))
        self.create_object([0, -20, 0], "player", (1,1,1))

    def get_property(self, key):
        if key in self.properties:
            return self.properties[key]

        return None

    def set_property(self, key, value):
        self.properties[key] = value
