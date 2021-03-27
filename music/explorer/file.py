import os
import path

def find_all_file(path):
    '''
    it get the name of this directory
    only can use in Unix/Windows
    file name:return
    '''
    try:
        temp_a_file = os.walk(path)
        a_file = []
        for file in temp_a_file:
            a_file.append(file)
        return a_file
    except:
        return 0


def get_file_path(filepath, filename):
    if filepath == False:
        _path = path.get_path()[1]
    else:
        _path = filepath
    file_list = find_all_file(_path)
    print(file_list[0][2][0])

def search_file(filepath=False, filename=False, main_size=1000):
    pass


print(get_file_path(filepath=False, filename=False))
