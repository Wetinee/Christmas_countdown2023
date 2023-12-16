def find_asterik(data):
    row, col = len(data), len(data[0])
    sum_all, x = 0, 0
    while x < row:
        y=0
        while y < col:
            if data[x][y] == "*":
                sum_all += check_adjacent(data, x, y, row, col)
            y+=1
        x += 1    
    return sum_all

def check_adjacent(data, x, y, row, col):
    adjacent_nums = []
    for m in [x+1, x, x-1]:
        for n in [y+1, y, y-1]:
            if 0 <= m < row and 0 <= n < col:
                if data[m][n].isdigit():
                    adjacent_nums.append([m, n])
    nums = set()
    for a, b in adjacent_nums:
        nums.add(get_nums(data, a, b, col))
    
    if len(nums) == 2:
        tmp = 1
        for s in nums:
            tmp *= int(s)
        return tmp
    return 0

def get_nums(data, x, y, col):
    num = ""
    tmp_y = y
    while tmp_y < col:
        if data[x][tmp_y].isdigit():
            num += data[x][tmp_y]
            tmp_y += 1
        else: 
            break
    
    tmp_y = y-1
    while tmp_y >= 0:
        if data[x][tmp_y].isdigit():
            num = data[x][tmp_y] + num
            tmp_y -= 1
        else: 
            break
    return num