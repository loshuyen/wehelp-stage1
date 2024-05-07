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
