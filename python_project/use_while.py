# print("Hello Python\n" * 5)
# i = 0
# while i < 5:
#     print("Hello world")
#     i += 1  # means i=i+1
#
# print("when loop end,the i is %d" % i)

sum = 0
# define the variable to count
i = 0
while i <= 100:
    if i % 2 != 0:
        sum += i
    i += 1
    # print(i)
print(sum)
