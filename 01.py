# encoding: utf-8
# author : Ding
import os
from pathlib import Path

p = Path("E:/")
file_dict = {}
file_list = []


for directory in os.listdir(str(p.absolute())):
    directory_path = p/ directory
    if os.path.isdir(str(directory_path.absolute())):
        for walk in os.walk(directory_path.absolute()):
            current_directory, _, files = walk
            for file in files:
                file_path = os.path.join(current_directory, file)
                if os.path.isfile(file_path):
                    file_dict[file_path] = (os.path.getsize(file_path), file_path)
                    pbar.update(1)
for values in file_dict.values():
    file_list.append(values)
file_list.sort(key=lambda x: x[0], reverse=True)
with open(r"F:\Numpy&&Opencv\爬虫\e盘的大文件.txt","w") as f:
    for file_tuple in file_list[:101]:
        f.write(file_tuple[1]+"     大小:"+str(file_tuple[0])+"字节\n")


