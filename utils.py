import numpy as np

def load_from_file(file_name):
    print(f'loading {file_name}...\n')
    with open(f'{file_name}.txt', "r") as f:
        data = []
        for l in f:
            data.append(float(l))
        return data

'''
get_data_from_file - get single value of data from config file you wrote before

    input
        file_name: str data
        data_name: str data


    output
        data: data which you wrote, type is automatically evaluated.
'''
def get_data_from_file(file_name, data_name):
    print(f'loading {data_name} from {file_name}')
    with open(f'{file_name}.txt', "r") as f:
        data = []
        for l in f:
            if l.split("=")[0] == data_name:
                data = i.split("=")[1]
                print(f"{data_name} = {data}")
                if type(data) == type("a"):
                    return data
                return eval(data)

        print(f"Can't find data name with {data_name}. abort")
        return -1

'''
color_getter - get color from config file with matching camera name

    input
        cam_name: str data label the camera name (ex: logi, labtop, '' means default)
        color: str data of color which you want to get

    output
        lower: list with 3 elements which you want to cut low
        upper: list with 3 elements which you want to cut high
'''
def color_getter(cam_name, color):
    data = load_from_file(f'config_{cam_name}_{color}')
    lower = [data[0], data[1], data[2]]
    upper = [data[3], data[4], data[5]]
    return lower, upper
   

    

    

        