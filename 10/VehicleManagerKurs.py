
class Vehicle(object):
    def __init__(self, brand, model, km, service_date):
        self.brand = brand
        self.model = model
        self.km = km
        self.service_date = service_date

    def show(self):
        print "{} {} {} {}".format(self.brand, self.model, self.km, self.service_date)

if __name__ == '__main__':
    All_Vehicles = []


    while True:
        answer = raw_input("Please select an option. \n"
                  "(1) Show Vehicles\n"
                  "(2) Edit Vehicles\n"
                  "(3) Add Vehicles \n"
                  "(q) Quit Program\n")

        if answer.lower() == "q":
            #todo save cars list to file
            print "Exiting Program"
            break

        elif answer == "1":
            for V9 in All_Vehicles:
                V9.show()

        elif answer == "3":
            print "Adding Vehicle\n"
            brand = raw_input("Please add the brand of the new vehicle\n")
            model = raw_input("Please add the model of the new vehicle\n")
            km = raw_input("Please add the kilometers of the new vehicle\n")
            service_date = raw_input("Please enter the service date of the new vehicle\n")
            myvehicle = Vehicle(brand, model, km, service_date)
            All_Vehicles.append(myvehicle)
            print "Vehicle added"

        else:
            print "Please check your input\n"
