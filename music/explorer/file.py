import os
import path

path = path.Path()

class File():
    def __init__(self):
        self.m_path = path.m_path
        self.a_file = self.find_all_file()

    def find_all_file(self):
        '''
        it get the name of this directory
        only can use in Unix/Windows
        file name:return
        '''
        try:
            temp_a_file = os.walk(self.m_path)
            a_file = []
            for file in temp_a_file:
                a_file.append(file)
            return a_file
        except:
            False


    def search_file(self, filepath=None, filename=None, main_size=0):
        pass

file =File()
print(file.m_path)
print(file.a_file)
