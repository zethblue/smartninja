"""Lottozahlen"""
import random

def Lottozahlgenerator(ANZAHL):
    return sorted(random.sample(range(1,50),ANZAHL))


if __name__ == '__main__':

    print Lottozahlgenerator(int(raw_input()))
