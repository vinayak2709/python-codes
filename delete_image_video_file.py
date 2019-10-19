

import os,sys

current_dir = os.getcwd()
path=current_dir

img_name='drone.mp4' #image or file name to be deleted
def remove_img(path, img_name):
    os.remove(path + '/' + img_name)

# check if file exists or not
    if os.path.exists(path + '/' + img_name) is False:
        # file did not exists
        return True
fl=remove_img(path, img_name)
if fl:
    print("done")