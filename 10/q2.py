class Array2D:
    def __init__(self, input_file_path):
        with open(input_file_path) as fin:
            self.lines = fin.read().strip().splitlines()
        self.n, self.m = len(self.lines), len(self.lines[0])
        self.dirs = {
            "|": [(1, 0), (-1, 0)],
            "-": [(0, 1), (0, -1)],
            "L": [(-1, 0), (0, 1)],
            "J": [(-1, 0), (0, -1)],
            "7": [(1, 0), (0, -1)],
            "F": [(1, 0), (0, 1)],
            ".": [],
        }

    def get_nbrs(self, i, j):
        res = []
        for di, dj in self.get_dnbrs(i, j):
            ii, jj = i + di, j + dj
            if 0 <= ii < self.n and 0 <= jj < self.m:
                res.append((ii, jj))
        return res

    def get_dnbrs(self, i, j):
        return self.dirs[self.lines[i][j]] if self.lines[i][j] != "S" else self._get_start_dnbrs(i, j)

    def _get_start_dnbrs(self, i, j):
        res = []
        didjs = []
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ii, jj = i + di, j + dj
            if 0 <= ii < self.n and 0 <= jj < self.m:
                if (i, j) in self.get_nbrs(ii, jj):
                    didjs.append((i, j))
                    res.append((di, dj))

        for char, ds in self.dirs.items():
            if sorted(ds) == sorted(didjs):
                break

        self.lines[i] = self.lines[i].replace("S", char)

        return res

    def find_start_position(self):
        for i, line in enumerate(self.lines):
            if "S" in line:
                return i, line.index("S")

    def get_polygon_bfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            top = stack.pop()
            if top in visited:
                continue
            visited.add(top)

            for nbr in self.get_nbrs(*top):
                if nbr not in visited:
                    stack.append(nbr)

        return visited

    def count_inversions(self, i, j, visited):
        count = 0
        for x, y in zip(range(i), range(j)):
            if (i - x, j - y) in visited:
                if self.lines[i - x][j - y] in {"|", "-", "J", "F"}:
                    count += 1
        return count

    def analyze_graph(self):
        start_position = self.find_start_position()
        visited_nodes = self.get_polygon_bfs(start_position)

        cnt = 0
        for i, line in enumerate(self.lines):
            for j in range(self.m):
                if (i, j) not in visited_nodes:
                    invs = self.count_inversions(i, j, visited_nodes)
                    cnt += (invs % 2 == 1)

        return cnt
