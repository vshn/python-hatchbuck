from hatchbuck import Hatchbuck
import pprint
import sys
pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.search_email("bashar.said@vshn.ch")
profile = hatchbuck.add_tag(profile, 'new tag')
pp.pprint(profile)
