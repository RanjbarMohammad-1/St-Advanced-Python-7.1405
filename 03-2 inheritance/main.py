from Adam import Adam


def main():

    print(3*"\n")
    print("=============Create an object  using the default values================")
    # Create an object using the default values
    adam1 = Adam()
    adam1.introduce()
    print("=============Create an object using parameters================")
    # Create an object using parameters
    adam2 = Adam("Adam", "Brown")
    print("Adam(Adam, Brown)")
    adam2.introduce()


if __name__=='__main__':
    main()


