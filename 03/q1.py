def sum_part_nums(data):
    row, col = len(data), len(data[0])
    x,sum_all =0, 0

    while(x<row):
        y=0
        while(y<col):
            if data[x][y].isdigit():
                num = ""
                neighbor_symbol = False
                while y<col and data[x][y].isdigit():
                    num += data[x][y]
                    if check_symbol(data, x, y, row, col):
                        neighbor_symbol = True
                    y += 1

                if neighbor_symbol:
                    sum_all += int(num)  
            y += 1            
        x += 1

    return sum_all

def check_symbol(data, x, y, row, col):
    for m in [x+1, x, x-1]:
        for n in [y+1, y, y-1]:
            if 0 <= m < row and 0 <= n < col:
                if data[m][n] != "." and not data[m][n].isdigit():
                    return True
    return False