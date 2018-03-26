from hatchbuck import Hatchbuck
import pprint
import sys
pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.search_email_multi(['sgdhfgfdgh@fdvd.com', 'bashar.said@vshn.ch'])
pp.pprint(profile)
