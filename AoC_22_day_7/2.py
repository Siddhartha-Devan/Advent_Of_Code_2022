with open ('inp.txt', 'r') as file:
    inp = file.read()
    # print(inp)

inp = inp.split("\n")
# print(inp)

dir_sizes={'main':0}
dir_level = ['main']

holy_fuck = []
holy_fuckk = []

def updater(dir_sizes, dir_level, file_size):
    curr_lvl = "-".join(dir_level)
    to_be_updated = ["-".join(dir_level[:i]) for i in range(1, len(dir_level)+1)]
    # print(to_be_updated)
    # print(file_size)
    for i in to_be_updated:
        # print(i)
        
        if i in dir_sizes.keys():
            dir_sizes[i]+=file_size
        else:
            dir_sizes[i] = file_size
    

# print(updater({}, ["main", 'weef', 'vijo', 'ijw'], 200))

def parser(inp, start=0, end = len(inp)):
    cnd = 0
    dirs = []
    for i in range(start, end):
        if inp[i][0] == "$":
            # print("Comm: ", inp[i])
            if inp[i][-2:] == ' /':
                print("main")
                dir_level = ['main']
            elif inp[i][-2:] == 'ls':
                # start_ = i+1
                # for ii in range(i+1, len(inp)):
                #     if inp[ii][1] == "$":
                #         end_ =ii-1
                #         break
                # parser(inp, start_ = start, end = end_)
                # print("oru ls")
                print("", end='')

            elif inp[i] == '$ cd ..':
                # print("oru lvl veliya")
                dir_level.pop()
            
            elif inp[i][:4] == '$ cd' and inp[i]!= "$ cd ..":
                # print("oru lvl ulla")
                names = inp[i].split(" ")
                # print(names, len(names))
                dir_level.append(names[-1])

        elif inp[i][:3] == 'dir':
            cnd+=1
            names = inp[i].split(" ")
            # try:
            # out = dir_sizes[names[-1]]
                # print(out, names[-1])
            # except:
            l_dir = "-".join(dir_level)+"-"+names[-1]
            if l_dir in dir_sizes.keys():
                print('irukku', dir_level, names[-1])
            else:
                dir_sizes[l_dir]=0
            dirs.append("-".join(dir_level) +"-"+names[-1])
        
        else:
            names = inp[i].split(" ")
            
            # print(names, len(names))
            # for lvl in range(0, -len(dir_level), -1):

                # dir_sizes[dir_level[lvl]]+= int(names[0])
            updater(dir_sizes, dir_level, int(names[0]))
                # curr -= 1

    print("cnd =", cnd)
#     print(dir_level)
parser(inp)
# print(dir_sizes)

tot_sum = 0
match_dir = []
match_nums = []

for i in dir_sizes.keys():
    if dir_sizes[i] <= 100000:
        # print(dir_sizes[i])
        tot_sum+=dir_sizes[i]
        match_dir.append((i, dir_sizes[i]))
        match_nums.append(dir_sizes[i])
    # print(i, dir_sizes[i])
print(tot_sum)
print(len(match_dir))

# for i in match_dir:
#     print(i)

print(len(dir_sizes.keys()))
# print(dir_sizes['nfz'], dir_sizes['jtzw'] )

n = 0

for i in dir_sizes.values():
    if i <= 100000:
        n+=i
#         print(n)


tot_disk = 70000000
update_size = 30000000
main_size = dir_sizes['main']
# print(main_size)
free_space = tot_disk-main_size
print(free_space)
req_space = update_size-free_space
print('req = ', req_space)

new_dir_sizes = {}
for i in dir_sizes.keys():
    if dir_sizes[i] >= req_space:
        new_dir_sizes[i] =  dir_sizes[i]

print(len(new_dir_sizes.keys()))
print(new_dir_sizes)

print(sorted(new_dir_sizes.values()))