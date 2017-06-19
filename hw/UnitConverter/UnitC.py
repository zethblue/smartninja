#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    while True:

        print "Unit Converter. We convert km in miles and miles in km"
        print "(1) For km in miles"
        print "(2) For miles in km"
        print "(3) for Quit"

        try:
            chose = int(raw_input())
        except:
            print "Please use a legit number"

        if chose == 3:
            break

        elif chose == 2:
            print "Miles in km chosen\n How many km?\n"
            try:
                kms = float(raw_input())
                miles = kms * 0.621371
                print ""
                print miles, " Miles"

            except:
                print "You didn't write a number"

        elif chose == 1:
            print "Km in Miles chosen \n How many Miles ?\n"
            try:
                miles = float(raw_input())
                kms = miles * 1.60934
                print ""
                print kms, " Kilometers"

            except:
                print "You didn't write a number"









