import sys
sys.path.append('..')
from hatchbuck import Hatchbuck
import pprint
pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.create({
    "firstName": "Hawar",
    "lastName": "Afrin",
    "title": "Hawar1",
    "company": "HAWAR",
    "emails": [
        {
            "address": "bashar.said.2018@gmail.com",
            "type": "work",
        }
    ],
    "phones": [
        {
            "number": "0041 76 803 77 34",
            "type": "work",
        }
    ],
    "status": {
        "name": "Employee",
    },
    "temperature": {
        "name": "Hot",
    },
    "addresses": [
        {
            "street": "Langäcker 12",
            "city": "wettingen",
            "state": "AG",
            "zip": "5430",
            "country": "Schweiz",
            "type": "work",
        }
    ],
    "timezone": "W. Europe Standard Time",
    "socialNetworks": [
        {
            "address": "'https://twitter.com/bashar_2018'",
            "type": "Twitter",
        }
    ],
})
pp.pprint(profile)