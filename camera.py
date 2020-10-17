import rayPoint, math

class Camera:
    def __init__(self, pos):
        self.pos = pos

    def _view(self, world):
        view = [[(0, 0, 0) for i in range(120)] for j in range(120)]
        for i in range(120):
            for j in range(120):
                vector = ((60 - i)/59, (60 - j)/59, 0.25)
                rp = rayPoint.RayPoint(self.pos, vector)
                object = 0
                while object == 0:
                    object = rp.update(world)
                if object == 1:
                    view[j][i] = (255, 255, 255)
                elif object == 2:
                    view[j][i] = (3, 123, 252)
                elif object == 3:
                    view[j][i] = (3, 252, 36)
                elif object == 4:
                    view[j][i] = (235, 64, 52)
        return view

    def setPos(self, pos):
        self.pos = pos[:]
    def setX(self, x):
        self.pos[1] = x
    def setZ(self, z):
        self.pos[2] = z
    def setY(self, y):
        self.pos[0] = y
