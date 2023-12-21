def parse(data):
    new_data = []
    for line in data:
        new_data.append([int(n) for n in line.split(" ")])
    return new_data

def get_new_nums_list(line):
    new_list = [line]
    tmp = []
    while len(set(tmp)) != 1:
        nums = new_list[-1]
        tmp = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
        new_list.append(tmp)
    return new_list
                  
def predict_next_number(line):
    new_list = get_new_nums_list(line)
    return sum([new_list[i][-1] for i in range(len(new_list))])

# q1    
def sum_next_nums(data):
    return sum([predict_next_number(line) for line in data])
    

def predict_first_number(line):
    new_list = get_new_nums_list(line)
    for i in range(len(new_list)-1, 0, -1):
        difference = new_list[i-1][0] - new_list[i][0]
        new_list[i-1].insert(0, difference)
    return new_list[0][0]

# q2   
def sum_first_nums(data):
    return sum([predict_first_number(line) for line in data])
