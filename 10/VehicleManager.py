"""Vehicle Manager"""
# Version 0.2A Testing Phase #
LVehicle=[]
class Vehicle(object):
    def __init__(self, brand, model, km, GNS):
        self.brand = brand
        self.model = model
        self.km = km
        self.GNS = GNS

def adding_car():
    print "Please insert the brand of your car"
    brand = raw_input()
    print "Please insert the Model of the car"
    model = raw_input()
    print "Please insert the kilometers of the car"
    km = raw_input()
    print "Please enter the Date of the last Checkup/Service"
    GNS = raw_input()
    addIT = Vehicle(brand=brand, model=model, km=km, GNS=GNS)
    LVehicle.append(addIT)
    print "Car was added"


   # def editing_car

  #  def deleting_car

  #  def listing_car


if __name__ == '__main__':
    w=0
    print "Welcome to Vehicle Manager 0.1A"

    while w == 0:
        w += 1
        print "Do you want to add a Car, please type 1"
        print "If you want to edit a Car, please type 2"
        print "If you want to delete a Car, please type 3"
        print "If you want to see a list of all vehicles type 4"
        print "Press 5 to Quit this Program"
        try:
            CHOICE = int(raw_input())
        except:
            print "Please enter a valid number"
            w = 0

        if CHOICE != 1 or 2 or 3 or 4 or 5:
            print "Please enter a valid number"
            w = 0

        if CHOICE == 1:
            adding_car()
        elif CHOICE == 2:
            editing_car ()
        elif CHOICE == 3:
            deleting_car()
        elif CHOICE == 4:
            listing_car ()
        elif CHOICE == 5:
            quit()





