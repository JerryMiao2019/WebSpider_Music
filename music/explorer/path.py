import os

class Path():
    def __init__(self):
        self.sep = self.get_sep()
        self.name = self.get_name()
        self.t_path = self.get_path()[0]
        self.m_path = self.get_path()[1] + 'DownloadMusic'

    def get_sep(self):
        '''
        tell us the Directory separator
        '\' or '/':return
        '''
        sep = os.sep
        return sep

    def get_name(self):
        '''
        tell us witch operating system you used
        Windows or Linux/Unix:return
        '''
        name = os.name
        if name == 'nt':
            return 'Windows'
        else:
            return 'Linux/Unix'

    def get_path(self):
        '''
        get the path of this file and the path of the main file
        One is the main file's path,one is this file's path:return
        '''
        t_file = os.getcwd()
        temp = t_file
        temp = temp.split(self.sep)
        temp_list = []
        for i in range(0,len(temp)-2):
            temp_list.append(temp[i]+self.sep)
        m_file = ''.join(temp_list)
        return t_file, m_file

