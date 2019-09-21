from hatchbuck import Hatchbuck
import pprint
import sys

pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.search_email("bashar.said@vshn.ch")
profile = hatchbuck.profile_contains(
    profile, "phones", "number", "+(414) 454-5 53 00"
)
pp.pprint(profile)
