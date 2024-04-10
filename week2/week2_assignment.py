def find_and_print(messages, current_station):
    stations=["Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing", "Songjiang Nanjing", "Zhongshan", "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-Shek Memorial Hall", "Guting", "Taipower Building", "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang", "Xindian City Hall", "Xindian", "Xiaobitan"]
    stations_index_dic={}
    for station in stations:
        i=stations.index(station)
        stations_index_dic[station]=i
    stations_index_dic["Xiaobitan"]=stations_index_dic["Qizhang"]
    locations={}
    for station in stations:
        for name in messages:
            if station in messages[name]:
                locations[name]=stations_index_dic[station]
    index_of_current_station=stations_index_dic[current_station]
    distance_dic={}
    for name in locations:
        d = abs(locations[name]-index_of_current_station)
        if current_station=="Xiaobitan" or ("Xiaobitan" in messages[name]):
            distance_dic[name]=d+1
        else:
            distance_dic[name]=d
    print(min(distance_dic, key=distance_dic.get))

messages={
    "Leslie":"I'm at home near Xiaobitan station.", 
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.", 
    "Copper":"I just saw a concert at Taipei Arena.", 
    "Vivian":"I'm at Xindian station waiting for you."
}
print("==========TASK 1==========")
find_and_print(messages, "Wanlong") # print Mary 
find_and_print(messages, "Songshan") # print Copper 
find_and_print(messages, "Qizhang") # print Leslie 
find_and_print(messages, "Ximen") # print Bob 
find_and_print(messages, "Xindian City Hall") # print Vivian

hour_occupied={}
def book(consultants, hour, duration, criteria):
    request_hour=set()
    for i in range(hour, hour+duration):
        request_hour.add(i)
    # print("request_hour:",request_hour)
    for consultant in consultants:
        if consultant["name"] not in hour_occupied:
            hour_occupied[consultant["name"]]=set()
    # print("hour_occupied:", hour_occupied)
    candidates=set()
    for name in hour_occupied:
        intersac=request_hour & hour_occupied[name]
        if not intersac:
            candidates.add(name)
    # print("candidates:", candidates)
    if not candidates:
        print("No Service")
        return
    if criteria=="price":
        candidates_price={}
        for name in candidates:
            for consultant in consultants:
                if consultant["name"]==name:
                    candidates_price[name]=consultant["price"]
        # print(candidates_price)
        min_price_candidate_name=min(candidates_price, key=candidates_price.get)
        hour_occupied[min_price_candidate_name]=hour_occupied[min_price_candidate_name] | request_hour
        print(min_price_candidate_name)
    if criteria=="rate":
        candidates_rate={}
        for name in candidates:
            for consultant in consultants:
                if consultant["name"]==name:
                    candidates_rate[name]=consultant["rate"]
        # print(candidates_rate)
        max_rate_candidate_name=max(candidates_rate, key=candidates_rate.get)
        hour_occupied[max_rate_candidate_name]=hour_occupied[max_rate_candidate_name] | request_hour
        print(max_rate_candidate_name)

consultants=[
    {"name":"John", "rate":4.5, "price":1000}, 
    {"name":"Bob", "rate":3, "price":1200}, 
    {"name":"Jenny", "rate":3.8, "price":800}
]
print("==========TASK 2==========")
book(consultants, 15, 1, "price") # Jenny 
book(consultants, 11, 2, "price") # Jenny 
book(consultants, 10, 2, "price") # John 
book(consultants, 20, 2, "rate") # John 
book(consultants, 11, 1, "rate") # Bob 
book(consultants, 11, 2, "rate") # No Service 
book(consultants, 14, 3, "price") # John

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

def get_number(index):
    seq=[]
    for i in range(index):
        for j in range(3):
            seq.append(i*7+j*4)
    print(seq[index])
print("==========TASK 4==========")
get_number(1) # print 4
get_number(5) # print 15 
get_number(10) # print 25 
get_number(30) # print 70

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
