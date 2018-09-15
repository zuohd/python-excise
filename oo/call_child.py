from child import Child


def main():
    c = Child(1000, 30)
    print(c.money, c.faceValue)
    c.play()
    c.feed()
    c.same()  # if super class have the same function,calling the funtion return the first super class's


if __name__ == '__main__':
    main()
