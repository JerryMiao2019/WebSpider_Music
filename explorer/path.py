import os


def get_sep():
    '''
    tell us the Directory separator
    '\' or '/':return
    '''
    sep = os.sep
    return sep


def get_name():
    '''
    tell us witch operating system you used
    Windows or Linux/Unix:return
    '''
    name = os.name
    if name == 'nt':
        return 'Windows'
    else:
        return 'Linux/Unix'


def get_Music_path():
    '''
    get the path of this file and the path of the main file
    One is the main file's path,one is this file's path:return
    '''
    t_file = os.getcwd()
    temp = t_file
    temp = temp.split(get_sep())
    temp_list = []
    for i in range(0, len(temp) - 1):
        #we should use the '/' or '\\' but not '\'
        temp_list.append(temp[i] + '/')
    m_file = ''.join(temp_list)
    return t_file, m_file + 'DownloadMusic'

print(get_Music_path())
