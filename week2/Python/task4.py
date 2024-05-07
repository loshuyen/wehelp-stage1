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