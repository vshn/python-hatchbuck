from hatchbuck import Hatchbuck
import pprint
import sys

pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.search_name("Bashar", "Said")
pp.pprint(profile)
