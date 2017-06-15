##This is it! After so many tries, here comes: the Vehicle Manager 1.0.A

class Vehicle(object):
    def __init__(self, brand_f, model_f, km_f, GNS_f):
        self.brand_f = brand_f
        self.model_f = model_f
        self.km_f = km_f
        self.GNS_f = GNS_f

LVehicle = []

if __name__ == '__main__':
    print "Vehicle Manager 1.0.A loading"

    while True:
        print "Please chose your option:"
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
            newcar = Vehicle(e, f, g, h)
            LVehicle.append(newcar)

            print "A car has been added"

        if CHOICE == 4:

            for cars in LVehicle:
                print ""


