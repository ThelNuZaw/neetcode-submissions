class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)#{key:0}
        self.p = []

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.p.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.p:
            if(abs(px - x) != abs(py - y) or x == px or y == py):
                continue
            res += self.points[(x, py)] * self.points[(px, y)]
        return res
