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