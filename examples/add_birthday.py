import sys
sys.path.append('..')
from hatchbuck import Hatchbuck
import pprint
pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.search_email("bashar.said@vshn.ch")
profile = hatchbuck.profile_add_birthday(profile,{'month': '1', 'day': '1', 'year': '1984'})
pp.pprint(profile)