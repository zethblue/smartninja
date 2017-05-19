import datetime
import time
#datetime ist ein package, das uns hilft mit Zeit-Daten umzugehen

if __name__ == '__main__':
    print datetime.datetime.now() #druck die normale Zeit aus  //print package.class.methode
    print datetime.datetime.utcnow() #datetime UTC
    print time.time() #Zeigt die Sekunden an, die seit 1970 vegangen sind.
    print datetime.datetime.fromtimestamp(time.time()) #Zeit umwandeln in eine lesbare Zeit

    my_list = [1, 2, 3, 4, 5, 6, 7]
    my_big_list = [10, 20, 30, 40, 50]


    print map(str,my_list)
    print map(float, my_big_list)
    print map(lambda x33: x33**2, my_list) #Lambda ist das Stichwort, diese Funktion wird allerdings immer erst direkt danach definiert. In unserem Fall das **2 fuer Quadrieren
    print map(lambda x33: x33**2, range(10))

    #Skript um Sachen zu verschluesseln. Zuerst wird das Passwort in Zahlen mittels ASCII Code umgewandelt. Danach wird es mit encrypt verschluesselt. danach wird es wieder als text ausgegeben
    print map(ord, "Hello") # Interepretiert jeden einzelnen Buchstaben mit den Ascii werten als Zahl!
    word = "Hello"
    encrypt = map(lambda x:ord(x)+3 word) #Encrypted das Wort
    encrypted_word = "".join(map(chr, encrypt)) #chr ist Charakter, das versucht einen Ascii Code in einen Character umzuwandeln.
    print encrypted_word # das ist das verschluesselte Wort
    decrypt = map(lambda x: ord(x) - 3, word) #Entschluesselt wieder indem das Wort wieder in ASCII umgewandelt wird und die 3 Zahlen wieder abgezogen werden
    decrypt_word =  "".join(map(chr, decrypt))
    print decrypt_word