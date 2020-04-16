import os, shutil

def get_directory():
    ''' Prompt user for a directory'''
    
    print("Welcome to FileMover")
    print("This script moves all files in a directory to folders in that directory with the file extension names")
    print("Paste a directory path here:")
    
    choice = input("> ")
    
    #print(os.path.Path(choiceP))
    return choice
    
def get_extension(lst):
    ''' Check if extension is None or not, append ones that aren't to list and return'''

    item_list = []

    for item in lst:
    
        i = os.path.splitext(os.path.basename(item))[1]
    
        # If extension is blank
        if i != '': item_list.append(item)
    
    return item_list

def folder_control(var, directory):
    '''Gets extension of var, checks if a directory exists for it in directory and creates one if not'''
    
    # Path is directory and the 2nd item in the tuple os.path.splitext(var) which is the extension
    path = f"{directory}\\{os.path.splitext(var)[1]}"
    check = os.path.exists(path)
        
    if not check:
        print(f'Folder for {os.path.splitext(var)[1]} does not exist, creating....')
        
        try:
            os.mkdir(path)
            print("Success")
        except:
            print("Fail")
    
    return

def list_d(place):
    ''' Returns list of items in directory place '''
    
    return os.listdir(place)

d = get_directory()

# Build list of items in directory d
directory_list = list_d(d)

extension_list = get_extension(directory_list)

# For item in extension_list...
for item_list in extension_list:
    
    # Split item into file name and extension
    extension = os.path.splitext(os.path.abspath(item_list))[1]
    
    # Call folder_control to check and make folder named with extension
    folder_control(item_list, d)
    
    # The source is... the source
    source = f"{d}\\{item_list}"
    
    # The destination is the folder in input directory with extension name
    destination = f"{d}\\{extension}\\{item_list}"
    
    # Attempt move
    try:
        shutil.move(source, destination)
        print("Success moving")
    except:
        print("Fail moving file")

print("Done!")