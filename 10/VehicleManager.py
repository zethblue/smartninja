"""Vehicle Manager"""
# Version 0.3A Testing Phase #
LVehicle = []
class Vehicle(object):
    def __init__(self, brand_f, model_f, km_f, GNS_f):
        self.brand_f = brand_f
        self.model_f = model_f
        self.km_f = km_f
        self.GNS_f = GNS_f

def adding_car(a ,b ,c ,d):
    LVehicle.append(Vehicle(a, b, c, d))
    return LVehicle

   # def editing_car

  #  def deleting_car

  #  def listing_car


if __name__ == '__main__':

    print "Welcome to Vehicle Manager 0.1A"

    while True:

        print "Do you want to add a Car, please type 1"
        print "If you want to edit a Car, please type 2"
        print "If you want to delete a Car, please type 3"
        print "If you want to see a list of all vehicles type 4"
        print "Press 5 to Quit this Program"
        try:
            CHOICE = int(raw_input())
        except:
            print "Please enter a valid number"


        if CHOICE not in range(1, 6):
            print "Please enter a valid number"


        if CHOICE == 1:
            print "Please insert the brand of your car"
            e = raw_input()
            print "Please insert the Model of the car"
            f = raw_input()
            print "Please insert the kilometers of the car"
            g = raw_input()
            print "Please enter the Date of the last Checkup/Service"
            h = raw_input()
            adding_car(e, f, g, h)
            print "a car has been added"
            for vehicle in LVehicle:
                print vehicle.brand_f
                print vehicle.model_f
                print vehicle.GNS_f
                print vehicle.km_f

        elif CHOICE == 2:
            editing_car ()
        elif CHOICE == 3:
            deleting_car()
        elif CHOICE == 4:
            listing_car ()
        elif CHOICE == 5:
            quit()






