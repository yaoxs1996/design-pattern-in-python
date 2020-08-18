class Rectangle:
    def draw(self):
        print("Inside Rectangle::draw() method.")

class Square:
    def draw(self):
        print("Inside Square::draw() method.")

class Circle:
    def draw(self):
        print("Inside Circle::draw() method.")

class ShapeFactory:

    def getShape(self, shapeType: str):
        if shapeType == None:
            return None
        
        if shapeType.upper() == "CIRCLE":
            return Circle()
        elif shapeType.upper() == "RECTANGLE":
            return Rectangle()
        elif shapeType.upper() == "SQUARE":
            return Square()

        return None

def main():
    shapeFactory = ShapeFactory()

    s1 = shapeFactory.getShape("CIRCLE")
    s1.draw()

    s2 = shapeFactory.getShape("RECTANGLE")
    s2.draw()

    s3 = shapeFactory.getShape("SQUARE")
    s3.draw()

if __name__ == "__main__":
    main()
    