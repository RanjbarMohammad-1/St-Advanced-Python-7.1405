from Adam import Adam
from IranianChild import IranianChild
from BritishChild import BritishChild
from ArabChild    import ArabChild
def main():

    print("==========objectAdam1=============")
    objectAdam1=Adam("adam","brown")
    objectAdam1.speak()

    print("==========objectIranianChild=============")
    # iranian
    objectIranianChild=IranianChild()
    objectIranianChild.speak()


    print("===========objectBritishChild============")
    # British
    objectBritishChild=BritishChild()
    objectBritishChild.speak()


    print("============objectArabicChild===========")
    # Arabic
    objectArabicChild=ArabChild()
    objectArabicChild.speak()

    print("=======================")




if __name__=='__main__':
    main()


