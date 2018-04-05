import sys
sys.path.append('..')
from hatchbuck import Hatchbuck
import pprint
pp = pprint.PrettyPrinter()
hatchbuck = Hatchbuck(sys.argv[1])
profile = hatchbuck.profile_contains({
  "contactId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
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
  "addresses": [
          {
              "street": "Neugasse 10",
              "city": "Zürich",
              "state": "ZH",
              "zip": "8005",
              "country": "Switzerland",
              "type": "work",
          }
      ],
  "phones": [
          {
              "number": "0041 76 803 77 34",
              "type": "work",
          }
      ]


}, "phones", "number", "0041 76 803 77 34")

pp.pprint(profile)