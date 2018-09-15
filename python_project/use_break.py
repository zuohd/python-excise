# 1x1=1
# 1x2=2  2x2=4
# 1x3=3  2x3=6  3x3=9
# 1x4=4  2x4=8  3x4=12 4x4=16
# 1x5=5  2x5=10 3x5=15 4x5=20 5x5=25

#define variable x,y;
i = 0
j=0
while i < 9:
    i += 1
    # if i == 3:
    #     continue
    #     print(i)
    # print(i)
    while j<i:
        j+=1
        # print(j)
        if j<i:
            print("%dX%d=%-2d " %(j,i,i*j),end="")
        else:
            print("%dX%d=%-2d " %(j,i,i*j))
    j=0

# print(i)
