import re


eingabe = "<a>dfsfsf</a>"
eingabe = eingabe.replace("/</g", "&lt;").replace("/>/g", "&gt;")
findings = re.findall("<(\w+)>", eingabe)

for found in findings:
    print found

if findings:
    print "somebody tried to hack"
    print eingabe
else:
    print "Save to publish"
    print eingabe