VList = []

class V:
    def __init__(self, car_id, car_brand, car_type, car_km, car_lastservice):
        self.car_id = car_id
        self.car_brand = car_brand
        self.car_type = car_type
        self.car_km = car_km
        self.car_lastservice = car_lastservice

def list_it(vehicles):

    for index, V in enumerate(vehicles):
        print "%s) %s %s with %s km driven so far. Last service date: %s" % (index + 1, car_brand, car_type, car_km, car_lastservice)


if __name__ == '__main__':

    ri = 0

    while ri == 0:

        print "Please chose one of the following options:"
        print "1 - Add a new Car"
        print "2 - Delete a Car"
        print "3 - Modify a Car"
        print "4 - List all Cars"
        print "5 - Quit the Program"

        ri = int(raw_input(" "))

        if ri == 1:
            zv = raw_input("Please enter the ID of the Car")
            zz = raw_input("Please enter the Brand of the Car")
            zy = raw_input("Please enter the Type of the Car")
            zx = raw_input("Please enter the KM of the car")
            zw = raw_input("Please enter the last Service Date")

            VList.append(V(car_id=zv,car_brand=zz, car_type=zy, car_km=zx, car_lastservice=zw))
            print "ID ", zv, "was added to your list"
            ri = 0

        if ri == 2:
            print len(VList), "Cars found in list"
            print VList
            print "Which entry do you want to delete?"
            # Eintragloeschen
            ri = 0

        if ri == 3:
            print len(VList), "Cars found in list"
            print VList
            print "Which entry do you want to modify?"
            # Eintragueberschreiben
            ri = 0

        if ri == 4:
            print len(VList), "Cars found in list"
            print VList
            ri = 0


        if ri == 5:
            quit()












