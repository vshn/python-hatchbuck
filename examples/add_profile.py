from hatchbuck import Hatchbuck
import pprint
import sys

pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.profile_add(
    "emails", "address", "baschar.said@hotmail.com", {"type": "Home"}
)
pp.pprint(profile)
