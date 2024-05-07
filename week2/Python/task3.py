def func(*data):
    middle_name={}
    middle_name_list=[]
    for name in data:
        if len(name)==2:
            middle_name[name]=name[1]
            middle_name_list.append(name[1])
        elif len(name)==4:
            middle_name[name]=name[2]
            middle_name_list.append(name[2]) 
        else:
            middle_name[name]=name[len(name)//2]
            middle_name_list.append(name[len(name)//2])
    middle_name_count={x:0 for x in middle_name_list}
    for name in middle_name_list:
        if name in middle_name_count:
            middle_name_count[name]+=1
    result = [name for name, count in middle_name_count.items() if count == 1]
    if result:
        result_name = [name for name, middle in middle_name.items() if middle == result[0]]
        print(result_name[0])
    else:
        print("沒有")           
print("==========TASK 3==========")
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有 
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安