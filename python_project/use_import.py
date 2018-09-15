# 1.stone
# 2.cut
# 3.cloth
import random #import package

your_input = int(input("please input your hands stone(1) /cut (2) /cloth (3) :"))

computer_hand = random.randint(1,3)  # computer always give stone
print("Player give %d-Computer give %d" % (your_input, computer_hand))

if ((your_input == 1 and computer_hand == 2)
        or (your_input == 2 and computer_hand == 3)
        or (your_input == 3 and computer_hand == 1)):

    print("player win!")
elif (your_input == computer_hand):
    print("Equal!")
else:
    print("Computer win")
