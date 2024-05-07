def find(spaces, stat, n):
    available_car={}
    for i in range(len(stat)):
        if stat[i] == 1:
            available_car[i]=spaces[i]
    space_diff={}
    for car in available_car:
        if available_car[car]-n >= 0:
            space_diff[car]=available_car[car]-n
    if not space_diff:
        print(-1)
        return
    print(min(space_diff, key=space_diff.get))
print("==========Task 5==========")   
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5 
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1 
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2