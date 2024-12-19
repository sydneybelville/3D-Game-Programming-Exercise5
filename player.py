from panda3d.core import Quat, lookAt, Vec3
from game_object import GameObject
from pubsub import pub

class Player(GameObject):
    def __init__(self, position, kind, id, size):
        super().__init__(position, kind, id, size)

        self.speed = 0.1

        pub.subscribe(self.input_event, 'input')

    def input_event(self, events=None):
        # TODO: this needs to interact with the physics object
        # to move the player in the right direction.  We cannot
        # just teleport the player to the new position like we
        # did before.
        if events:
            if 'moveForward' in events:
                pass

            if 'moveBackward' in events:
                pass

            if 'moveLeft' in events:
                pass

            if 'moveRight' in events:
                pass


    def collision(self, other):
        # TODO: the physics engine needs to detect the
        # collision and call this function
        pass

