class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
point1.z = 30
point1.draw()
point1.move()
print(point1.x)
