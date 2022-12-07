with open("2022/res/in07.txt") as file:
    logs = file.read().split("\n")

TOTAL_DISK = 70000000
DISK_NEEDED = 30000000


class Dir:
    def __init__(self, name, parent_dir, sub_dirs, files):
        self.name = name
        self.parent_dir = parent_dir
        self.sub_dirs = sub_dirs
        self.files = files


root = Dir("/", None, {}, [])
curr = root
for log in logs:
    if log == "$ cd /":
        continue
    elif log == "$ cd ..":
        curr = curr.parent_dir
    elif log.startswith("$ cd"):
        name = log.split(" ")[-1]
        curr = curr.sub_dirs[name]
    elif log.startswith("dir"):
        sub_name = log.split(" ")[-1]
        curr.sub_dirs[sub_name] = Dir(sub_name, curr, {}, [])
    elif log.split(" ")[0].isnumeric():
        size, file_name = log.split(" ")
        curr.files.append((file_name, int(size)))


def get_size(curr, size_array):
    size = 0
    for _, file_size in curr.files:
        size += file_size
    for sub_dir in curr.sub_dirs.values():
        dir_size, _ = get_size(sub_dir, size_array)
        size += dir_size
    size_array.append(size)
    return size, size_array


total_size, sizes = get_size(root, [])

space_remaining = TOTAL_DISK - total_size
space_needed = DISK_NEEDED - space_remaining

pt1 = sum(filter(lambda x: x <= 100000, sizes))
pt2 = min(filter(lambda x: x >= space_needed, sizes))

print("Part 1: ", pt1)
print("Part 2: ", pt2)
