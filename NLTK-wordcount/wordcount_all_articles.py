#counts words in all articles
from os import walk
from wordcounter import wordCounter
fold = "../texts/";
for (dirpath, dirnames, filenames) in walk(fold):
	for fi in filenames:
		f = open(fold+fi, "r+")
		wordCounter(f)
		

# f1 = open("../texts/apple_supplier.txt", "r+")
# f2 = open("../texts/applesecurity.txt", "r+")
# f3 = open("../texts/asteroid.txt", "r+")
# f4 = open("../texts/iphone6.txt", "r+")
# f5 = open("../texts/obamacare.txt", "r+")

# print "\nApple supplier:\n"
# wordCounter(f1)

# print "\nApple security:\n"
# wordCounter(f2)

# print "\nAsteroid:\n"
# wordCounter(f3)

# print "\niPhone6:\n"
# wordCounter(f4)

# print "\nObamacare:\n"
# wordCounter(f5)

