import os
import shutil

folder = r"/Users/imac_21/Desktop/2000/"
dst_folder = r"/Users/imac_21/Desktop/2000_copy/"
files = os.listdir(folder)
# new_files = files
# print(files)
new_dirs = set(file[:6] for file in files)
#list_newdirs = list(new_dirs)
#list_newdirs.remove('.DS_St')
# print(list_newdirs)
for dirs in new_dirs:
    os.mkdir(f"{dst_folder}{dirs}")


for file in files:
    source = folder + file
    destination = f'{dst_folder}/{file[:6]}'
    shutil.move(source, destination)


# print(files)
# print(new_files)


"""
for fol_nam in files:
    new = {fol_nam[:6]}
    for num in new:
        new_2 = {num + num}
    #os.mkdir(f"/Users/imac_21/Desktop/2000/{name}")
    print(new_2)
# shutil.move(f"/Users/imac_21/Desktop/2000/{files[:5]}")
"""

