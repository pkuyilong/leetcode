

import os
import re

pattern = "\d{2,3}\.py"

re_obj = re.compile(pattern)
dir_path = "/Users/mayilong/PycharmProjects/leetcode/python_version/linked_list"
for item in os.listdir(dir_path):
    res = re_obj.search(item)
    if res:
        with open(os.path.join(dir_path, item), "r") as f:
            num, ext = os.path.splitext(item)
            print(num, ext)
            line_1 = f.readline()
            line_2 = f.readline()
            en_name = line_2.split("/")[-2]
            # print(en_name)
            new_name = num + "." + en_name + ext
            print(new_name)
            os.rename(os.path.join(dir_path, item),
                      os.path.join(dir_path, new_name))


