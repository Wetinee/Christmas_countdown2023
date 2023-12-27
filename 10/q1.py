from collections import deque


class array2D:
    def __init__(self, data):
        self.data = data
        self.row = len(data)
        self.col = len(data[0])
        self.start_point = self.find_start_point()

    def get_neighbors(self, x, y):
        result = []
        for dx, dy in self.get_dneighbors(x, y):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < self.row and 0 <= ny < self.col):
                continue
            result.append((nx, ny))
        return result

    def get_dneighbors(self, x, y):
        res = []

        if self.data[x][y] == "S":
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < self.row and 0 <= ny < self.col):
                    continue
                if (x, y) in self.get_neighbors(nx, ny):
                    res.append((dx, dy))
            return res

        result = {
            "|": [(-1, 0), (1, 0)],
            "-": [(0, -1), (0, 1)],
            "L": [(-1, 0), (0, 1)],
            "J": [(-1, 0), (0, -1)],
            "7": [(0, -1), (1, 0)],
            "F": [(0, 1), (1, 0)],
            ".": []
        }[self.data[x][y]]

        return result

    def find_start_point(self):
        for x in range(self.row):
            for y in range(self.col):
                if self.data[x][y] == "S":
                    return (x, y)

    def find_max_distance(self):
        visited = set()
        distances = {}
        q = deque([(self.start_point, 0)])
        while q:
            top, dist = q.popleft()
            if top in visited:
                continue

            visited.add(top)
            distances[top] = dist

            for nbr in list(self.get_neighbors(*top)):
                if nbr in visited:
                    continue
                q.append((nbr, dist + 1))

        return max(distances.values())
