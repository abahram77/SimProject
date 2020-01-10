# this method gets input values of project from a input_file file and save the inputs in a dictionary
def get(input_file):
    file = open(input_file, "r")
    raw_input = file.read().split("\n")
    data = {}
    temp = list(map(int, raw_input[0].split(" ")))
    data["M"] = temp[0]
    data["lambda"] = temp[1]
    data["alpha"] = temp[2]
    data["mu"] = temp[3]
    data["servers"] = []
    for i in range(data["M"]):
        temp = list(map(int, raw_input[i+1].split(" ")))
        data["servers"] += [temp[1:]]
    return data

