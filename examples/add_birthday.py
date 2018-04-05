import sys
sys.path.append('..')
from hatchbuck import Hatchbuck
import pprint
pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.profile_add_birthday({
"contactId": "TmpmT0QyUGE3UGdGejZMay1xbDNyUHJFWU91M2VwN0hCdGtZZFFCaWRZczE1"},
{'month': '1', 'day': '1', 'year': '1984'})
pp.pprint(profile)