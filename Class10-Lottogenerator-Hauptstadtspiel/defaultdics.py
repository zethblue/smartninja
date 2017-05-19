import collections

if __name__ == '__main__':
    freunde = collections.defaultdict(list) #defaultdict ist eine Klasse. In der Klasse gibt es bestimmte Methoden. Durch default dict ist die def _missing funktion bekannt
    # dadurch stuerzt er bei Schluessel die es nicht gibt ab, sondern added die mit leerem Wert
    freunde["Susi"].append("Robert") # Erstellt die Liste Robert im Dictionary Susi. Erstellt auch das Dictionary Susi durch defaultdict , da es dieses nicht gibt.
    # Das ist durch die def_missing funktion moeglich.
    freunde["Susi"].append("Benni")
    freunde["Benni"].append("Susi")
    freunde["Robert"].extend(["Benni", "Tobi"]) #Wenn ich eine Liste bereits habe und ich mache mehr dazu, wird mit .extend hinten drangehaengt. Funktioniert nur bei Listen!

    for xx9, xx10 in freunde.iteritems():
        print xx9, xx10
