import sys
sys.path.append('..')

from hatchbuck import Hatchbuck
import pprint
pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.profile_add_address({
"contactId": "TmpmT0QyUGE3UGdGejZMay1xbDNyUHJFWU91M2VwN0hCdGtZZFFCaWRZczE1"},
{'street':"Langäcker 13",
 'zip_code':"5430",
 'city':"Wettingen",
 'country':"Switzerland"},
"Home"
)
pp.pprint(profile)