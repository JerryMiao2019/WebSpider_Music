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
        return 1


def get_file_path(filename, filepath=path.get_Music_path()[1]):
    _path = filepath
    file_list = find_all_file(_path)
    for i in (file_list[0][2]):
        if i == filename:
            return _path + r'/' + filename
        else:
            pass
    return False


def search_file(filename=False, filepath=path.get_Music_path()[1], main_size=1024):
    pass


print(get_file_path('This Is It.mp3'))