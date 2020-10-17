import camera

class Player:
    def __init__(self):
        self.pos = [0, 5, 5]
        self.camera = camera.Camera([1, 5, 5])

    def view(self, world):
        return self.camera._view(world)

    def move(self, direction, world):
        if 0 <= self.pos[0]+direction[0] < world.getSize()[0] and 0 <= self.pos[1]+direction[1] < world.getSize()[1] and 0 <= self.pos[2]+direction[2] < world.getSize()[2]:
            self.pos[0] += direction[0]
            self.pos[1] += direction[1]
            self.pos[2] += direction[2]
        self.camera.setPos(self.pos)
        self.camera.setY(self.pos[0]+1)

    def turn(self, orientation):
        self.camera.turn(orientation)