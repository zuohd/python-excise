# input price

price_str = input("Price of Apple: ")
# input weight

weight_str = input("Weight of buying: ")
# calculate the total money
total_money = (float(price_str) * float(weight_str))

# print money %%buzhuanyi
print("%%60 Apple price:%s$/kg,weight of buying:%s kg,total money:%.2f" % (price_str, weight_str, total_money))

scale=0.252
print("Data is %.2f%%"%(scale*100))