import sys
sys.path.append('..')

from hatchbuck import Hatchbuck
import pprint
pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.search_email("bashar.said@vshn.ch")
profile = hatchbuck.profile_add_address(profile,
                                        {'street':"Langäcker 13",
                                         'zip_code':"5430",
                                         'city':"Wettingen",
                                         'country':"Switzerland"},
                                        "Home")
pp.pprint(profile)