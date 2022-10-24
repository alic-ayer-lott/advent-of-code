# read method to read data in and split method splits to list
depth = open("data.txt").read().split()
count = 0


for idx,value in enumerate(depth):
    # print(str(idx) + ", " + str(value))
    if idx == 0:
        continue
    if value > depth[idx-1]:
       # print(str(value) + "," + str(depth[idx-1]))
        count += 1

print(count)