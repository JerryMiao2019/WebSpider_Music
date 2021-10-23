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
    '''
    get the whole filepath
    :param filename: the name of th file
    :param filepath:
    :return:
    '''
    return filepath + '/' + filename

def search_file(filename, filepath=path.get_Music_path()[1], main_size=1024):
    '''
    it search file in the filepath
    :param filename: the name of the file
    :param filepath: the path where is the file
    :param main_size:
    :return:
    '''
    a_file = find_all_file(filepath)
    print(a_file)

search_file('不再犹豫.mp3')