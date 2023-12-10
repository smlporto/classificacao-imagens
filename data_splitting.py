import os
import shutil
import splitfolders

input_path = './images_full/'
output_path = './images_split/'

def delete_images(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.makedirs(path)

def rename_images(path):
    if os.path.exists(path):
        for dirpath , dirnames , filenames in os.walk(path):
            for index, file in enumerate(filenames):
                full_path = os.path.join(dirpath,file)
                extension = '.'+full_path.split('.')[-1]
                newfilename = ''.join(['image'+str(index), extension])
                os.rename(full_path,os.path.join(dirpath,newfilename))

def exec_split():
    delete_images(output_path)
    splitfolders.ratio(input=input_path, output=output_path,
    seed=1337, ratio=(.8, .2), group_prefix=None, move=False) 
    rename_images(output_path)