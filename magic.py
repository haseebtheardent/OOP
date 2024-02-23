class point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point({self.x},{self.y})')

    def __str__(self) -> str:
        return f'Point({self.x},{self.y})'

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y   

    def __gt__(self, other) -> bool:
        return self.x > other.x and self.y > other.y        

    def __add__(self ,other) -> any:
        return self.x + other.x and self.y + other.y    
p1 = point(1, 2)
p2 = point(4, 7)
p3 = point(10, 20)
p4 = point(1, 2)
# print(p1 == p2)
# print(p2 > p1)
print(p1 + p2)
