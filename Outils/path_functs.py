import os
def create_dir_if_unexisting(name, path='./') -> bool:
    '''
    :name: name of the file/folder to check existance of\n
    :path: where the file is supposed to be and would be created the file
    ------
    :bool: of if it was created or not
    '''
    v_dir = os.listdir(path)
    print('\n'.join(i for i in v_dir))
    try: v_dir.index(name); return False
    except: os.mkdir(f"{path}/{name}"); return True
def remove_dir(name, path='./'):
    '''
    :name: name of the folder to remove\n
    :path: where is the folder
    ------
    :bool: of if it was removed or not
    '''
    v_dir = os.listdir(f"{path}/{name}")
    for file in v_dir:
        os.remove(f"{path}/{name}/{file}")
    os.rmdir(f"{path}/{name}")
def is_file(name, path='./') -> bool:
    '''
    :name: name of the file to check existance of\n
    :path: where the file is supposed to be
    '''
    is_there = True
    v_dir = os.listdir(path)
    try: v_dir.index(name)
    except: is_there = False
    return is_there
def is_dir(name, path='./') -> bool:
    '''
    :name: name of the folder to check existance of\n
    :path: where the folder is supposed to be
    '''
    is_there = True
    v_dir = os.listdir(path)
    try: v_dir.index(name)
    except: is_there = False
    return is_there