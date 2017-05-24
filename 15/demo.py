import os

print
print "This is this file", __file__

print os.path.dirname(__file__)
print os.path.join(os.path.dirname(__file__), "templates")
templates_dir = os.path.join(os.path.dirname(__file__), "templates")

print "Template exists:", os.path.exists(templates_dir)

#os.path.dirname(__file__) sagt dir wo sich die auszufuehrende datei befindet