"""Vehicle Manager"""
# Version 0.2A Testing Phase #
LVehicle = [0]
class Vehicle(object):
    def __init__(self, brand_f, model_f, km_f, GNS_f):
        self.brand_f = brand_f
        self.model_f = model_f
        self.km_f = km_f
        self.GNS_f = GNS_f

    def adding_car(self,a,b,c,d):
        newcar = Vehicle(a, b, c, d)
        return newcar


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
            print "Please insert the brand of your car"
            e = raw_input()
            print "Please insert the Model of the car"
            f = raw_input()
            print "Please insert the kilometers of the car"
            g = raw_input()
            print "Please enter the Date of the last Checkup/Service"
            h = raw_input()
            adding_car(e, f, g, h)
            LVehicle.append(newcar)
            print newcar, "has been added"
            print LVehicle[01]

        elif CHOICE == 2:
            editing_car ()
        elif CHOICE == 3:
            deleting_car()
        elif CHOICE == 4:
            listing_car ()
        elif CHOICE == 5:
            quit()






