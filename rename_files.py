import os
def rename_files():
    # get filenames
    file_list = os.listdir(r"/home/luiz/DEVEL/PyNow/prank")
    print(file_list)
    os.chdir(r"/home/luiz/DEVEL/PyNow/prank")
    #2 for each file rename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print(file_name)

rename_files()
