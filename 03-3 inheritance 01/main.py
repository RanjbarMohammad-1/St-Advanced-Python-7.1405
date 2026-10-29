from Adam import Adam
from IranianChild import IranianChild


def main():

    print(2*"\n")
    print("\n=== Create an Adam object ===")
    adam1 = Adam()
    adam1.introduce()
    adam1.walk()
    adam1._pray()
    
    

    print("\n=== Create a Habil object ===")
    habil1 = Habil()
    habil1.introduce()
    habil1.walk()
    habil1._pray()

    print("\n=== Habil object with name and eye color ===")
    habil2=Habil("habil2","brown")
    habil2.introduce()

    print("\n=== Use inherited getter and setter ===")
    habil1.set_eyeColor("Brown")
    print("Habil's eye color:", habil1.get_eyeColor())


if __name__=='__main__':
    main()


