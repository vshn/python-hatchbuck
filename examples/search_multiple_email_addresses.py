import sys
sys.path.append('..')

from hatchbuck import Hatchbuck
import pprint
pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck('cE91YTNnQ3NBWVRaaXlERHBKR1NaZjJyTTFKa1BrRXlQYjZQVjVuLVpSSTE1')
profile = hatchbuck.search_email_multi(['sgdhfgfdgh@fdvd.com', 'bashar.said@vshn.ch'])
pp.pprint(profile)
