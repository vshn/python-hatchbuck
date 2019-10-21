from hatchbuck import Hatchbuck
import pprint
import sys
import logging

LOGFORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOGFORMAT)
pp = pprint.PrettyPrinter()

hatchbuck = Hatchbuck(sys.argv[1], noop=False)
profile = hatchbuck.search_email(sys.argv[2])
pp.pprint(profile["addresses"])
profile = hatchbuck.clean_all_addresses(profile)
pp.pprint(profile["addresses"])
