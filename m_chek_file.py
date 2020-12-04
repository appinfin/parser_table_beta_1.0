import os.path

def chek_file():
    path = str('index.html') #input()
    if os.path.exists(path):
        print('file exists, \n===========================')
    else:
        print('file not exists, \n===========================')
        return False

def test():    
    if chek_file()==False:
        print('good job!')
    print('DONE!')
