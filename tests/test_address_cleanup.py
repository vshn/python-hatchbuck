from hatchbuck import Hatchbuck
import unittest
import copy

if __name__ == "__main__":
    unittest.main()


class TestHatchbuckAddresses(unittest.TestCase):
    testProfile = {
        "addresses": [
            {
                "city": "Zürich",
                "country": "Switzerland",
                "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                "state": "ZH",
                "street": "Neugasse 10",
                "type": "Work",
                "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                "zip": "8005",
            }
        ],
        "campaigns": [],
        "company": "VSHN AG",
        "contactId": "SUFYbGdOaEQ0cWR2N1JfV183UFNBSDllTktCc3E3OWRsN09qaW4tU3JqbzE1",
        "customFields": [
            {"name": "Comments", "type": "MText", "value": ""},
            {"name": "Invoiced", "type": "Number", "value": ""},
            {"name": "Language", "type": "Text", "value": ""},
            {"name": "working at company since", "type": "Text", "value": "1.1.2018"},
            {"name": "company size", "type": "Text", "value": "25"},
            {"name": "Birthday", "type": "Date", "value": ""},
        ],
        "emails": [
            {
                "address": "bashar.said@vshn.ch",
                "id": "S2lIY2NOS2dBRnRCamEyQUZxTG00dzhlYjAxUU9Sa3Z5ZFVENGVHTG1DODE1",
                "type": "Work",
                "typeId": "VmhlQU1pZVJSUFFJSjZfMHRmT1laUmwtT0FMNW9hbnBuZHd2Q1JTdE0tYzE1",
            }
        ],
        "firstName": "Bashar",
        "instantMessaging": [],
        "lastName": "Said",
        "phones": [
            {
                "id": "OHh4U0ZWc3FNVXVBQVF4cjdsak9McWc4TVppZlF4NklrNmZfSnBhaDZwQTE1",
                "number": "+(414) 454-5 53 00",
                "type": "Work",
                "typeId": "QTBncHV0dndnaGNnRVMzLTR0SGtFRmRvZjdqNm4zcVphQi1XX1Z2MXVtRTE1",
            }
        ],
        "referredBy": "",
        "salesRep": {
            "id": "VGpwQTRGTmw4MExVODl1b1BmXzBodTBwWnZXS2dUZzVvSkJKZUx4UlFpdzE1",
            "username": "aarno.aukia",
        },
        "socialNetworks": [
            {
                "address": "https://twitter.com/bashar_2018",
                "id": "S1pEM2NMWlhmZ1VUcDhTUWVvQy1kU21xMjlSbDg5Z3piMERVbEFsam42azE1",
                "typeId": "ZGRlMHpBaXY3M05YUGc4a0pIY3lRdUFKN1JYaDd2VEphbzhSRkdzM2x4bzE1",
            }
        ],
    }

    def setUp(self):
        pass

    def test_address_obsolecence(self):
        hatchbuck = Hatchbuck("", noop=True)
        self.maxDiff = None

        # country only
        self.assertTrue(
            hatchbuck._address_obsolete(
                {
                    "city": "",
                    "country": "Switzerland",
                    "state": "",
                    "street": "",
                    "zip": "",
                },
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "ZH",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
            )
        )
        self.assertFalse(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "ZH",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
                {
                    "city": "",
                    "country": "Switzerland",
                    "state": "",
                    "street": "",
                    "zip": "",
                },
            )
        )
        # city only
        self.assertTrue(
            hatchbuck._address_obsolete(
                {"city": "Zürich", "country": "", "state": "", "street": "", "zip": ""},
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "ZH",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
            )
        )
        self.assertFalse(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "ZH",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
                {"city": "Zürich", "country": "", "state": "", "street": "", "zip": ""},
            )
        )
        # city & country
        self.assertTrue(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "",
                    "zip": "",
                },
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "ZH",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
            )
        )
        self.assertFalse(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "ZH",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "",
                    "zip": "",
                },
            )
        )
        # city, country, zip
        self.assertTrue(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "",
                    "zip": "8005",
                },
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "ZH",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
            )
        )
        self.assertFalse(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "ZH",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "",
                    "zip": "8005",
                },
            )
        )
        # city, country, zip, street
        self.assertTrue(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "Neugasse 10",
                    "zip": "8005",
                },
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "ZH",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
            )
        )
        self.assertFalse(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "ZH",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "Neugasse 10",
                    "zip": "8005",
                },
            )
        )
        # city, country, zip, street, state
        self.assertTrue(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "Neugasse 10",
                    "zip": "8005",
                },
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
            )
        )
        self.assertTrue(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                    "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                    "state": "",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                    "zip": "8005",
                },
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "Neugasse 10",
                    "zip": "8005",
                },
            )
        )
        # subtle differences
        self.assertFalse(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "zip": "8005",
                },
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "Klingenstrasse 1",
                    "type": "Work",
                    "zip": "8005",
                },
            )
        )
        self.assertFalse(
            hatchbuck._address_obsolete(
                {
                    "city": "Zürich",
                    "country": "Switzerland",
                    "state": "",
                    "street": "Neugasse 10",
                    "type": "Work",
                    "zip": "8005",
                },
                {
                    "city": "Zürich",
                    "country": "",
                    "state": "",
                    "street": "Klingenstrasse 1",
                    "type": "Work",
                    "zip": "8005",
                },
            )
        )

    def test_clean_street_name(self):
        hatchbuck = Hatchbuck("", noop=True)
        self.assertEqual(
            hatchbuck._clean_street_name("Klingenstr. 1 "), "Klingenstrasse 1"
        )
        self.assertEqual(
            hatchbuck._clean_street_name("Klingenstr 1 "), "Klingenstrasse 1"
        )
        self.assertEqual(hatchbuck._clean_street_name("geolocation"), "")
        self.assertEqual(hatchbuck._clean_street_name("False"), "")

    def test_clean_city_name(self):
        hatchbuck = Hatchbuck("", noop=True)
        self.assertEqual(
            hatchbuck._clean_city_name("Greater New York City Area"), "New York City"
        )
        self.assertEqual(hatchbuck._clean_city_name("Greater Atlanta Area"), "Atlanta")
        self.assertEqual(hatchbuck._clean_city_name("Zürich und Umgebung"), "Zürich")
        self.assertEqual(
            hatchbuck._clean_city_name("Currais Novos e Região"), "Currais Novos"
        )
        self.assertEqual(hatchbuck._clean_city_name("München und Umgebung"), "München")
        self.assertEqual(hatchbuck._clean_city_name("Région de Genève"), "Genève")
        self.assertEqual(hatchbuck._clean_city_name("Zürich Area"), "Zürich")
        self.assertEqual(hatchbuck._clean_city_name("Zurich Area"), "Zürich")

    def test_clean_country_name(self):
        hatchbuck = Hatchbuck("", noop=True)
        self.assertEqual(
            hatchbuck._clean_country_name("Germany"), "Germany"
        )  # no change
        self.assertEqual(hatchbuck._clean_country_name("Suisse"), "Switzerland")
        self.assertEqual(hatchbuck._clean_country_name("Svizzera"), "Switzerland")
        self.assertEqual(hatchbuck._clean_country_name("Schweiz"), "Switzerland")
        self.assertEqual(hatchbuck._clean_country_name("Deutschland"), "Germany")
        self.assertEqual(hatchbuck._clean_country_name("Brasil"), "Brazil")

    def test_clean_address(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "Neugasse 10",
                    "zip": "8005",
                    "city": "Zürich",
                    "country": "Switzerland",
                }
            ),
            {
                "street": "Neugasse 10",
                "zip": "8005",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )  # no change
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "Neugasse 10",
                    "zip": "8005",
                    "city": "Zurich",
                    "country": "Switzerland",
                }
            ),
            {
                "street": "Neugasse 10",
                "zip": "8005",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address({"country": ""}),
            {
                "street": "",
                "zip": "",
                "city": "",
                "country": "",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Zürich, Canton of Zürich, Switzerland",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Bern, Canton of Bern, Switzerland",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Bern",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Neuenkirch, Kanton Luzern, Schweiz",
                    "country": "",
                    "type": "Other",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Neuenkirch",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Frankfurt Am Main Area, Germany",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Frankfurt Am Main",
                "country": "Germany",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Sankt Gallen Area, Switzerland",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Sankt Gallen",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Santa Monica, California",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Santa Monica",
                "country": "United States",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "San Francisco Bay Area",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "San Francisco",
                "country": "",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {"street": "", "zip": "", "city": "Austria area", "country": ""}
            ),
            {
                "street": "",
                "zip": "",
                "city": "",
                "country": "Austria",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Vienna, Vienna, Austria",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Vienna",
                "country": "Austria",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Wohlen AG, Kanton Aargau, Schweiz",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Wohlen AG",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {"street": "", "zip": "", "city": "Austin, Texas Area", "country": ""}
            ),
            {
                "street": "",
                "zip": "",
                "city": "Austin, Texas",
                "country": "",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Greater New York City Area",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "New York City",
                "country": "",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {"street": "", "zip": "", "city": "Switzerland", "country": ""}
            ),
            {
                "street": "",
                "zip": "",
                "city": "",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Helsinki Area, Finland",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Helsinki",
                "country": "Finland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {"street": "", "zip": "", "city": "United States", "country": ""}
            ),
            {
                "street": "",
                "zip": "",
                "city": "",
                "country": "United States",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Zürich Area, Switzerland",
                    "country": "ch",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Zürich Area, Switzerland",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Brisbane Area, Australia",
                    "country": "au",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Brisbane",
                "country": "Australia",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Amsterdam Area, Netherlands",
                    "country": "nl",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Amsterdam",
                "country": "Netherlands",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Brisbane Area, Australia",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Brisbane",
                "country": "Australia",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {"street": "", "zip": "", "city": "", "country": "CH"}
            ),
            {
                "street": "",
                "zip": "",
                "city": "",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "Pflanzschulstrasse 34",
                    "zip": "CH-8004",
                    "city": "Zürich",
                    "country": "",
                }
            ),
            {
                "street": "Pflanzschulstrasse 34",
                "zip": "8004",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Zürich Area, Svizzera",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {"street": "", "zip": "", "city": "Luxembourg", "country": ""}
            ),
            {
                "street": "",
                "zip": "",
                "city": "",
                "country": "Luxembourg",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Boulogne-Billancourt, Île-de-France, France",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Boulogne-Billancourt",
                "country": "France",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Lausanne, Canton de Vaud, Suisse",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Lausanne",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Région de Lausanne, Suisse",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Lausanne",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Région de Genève, Suisse",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Genève",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Copenhagen, Capital Region, Denmark",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Copenhagen",
                "country": "Denmark",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Copenhagen Area, Capital Region, Denmark",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Copenhagen",
                "country": "Denmark",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "München und Umgebung, Deutschland",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "München",
                "country": "Germany",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Currais Novos e Região, Brasil",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Currais Novos",
                "country": "Brazil",
                "state": "",
                "type": "Other",
            },
        )
        self.assertEqual(
            hatchbuck._clean_address(
                {
                    "street": "",
                    "zip": "",
                    "city": "Zürich und Umgebung, Schweiz",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip": "",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Other",
            },
        )

    def test_clean_all_addresses(self):
        hatchbuck = Hatchbuck("", noop=True)
        self.maxDiff = None

        originalprofile = copy.deepcopy(self.testProfile)
        changedprofile = copy.deepcopy(self.testProfile)
        # fill in test data to be cleaned up
        changedprofile["addresses"].append(
            {
                "id": "1",
                "street": "Klingenstr 1",
                "zip": "8005",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Work",
            }
        )
        changedprofile["addresses"].append(
            {
                "id": "2",
                "street": "Klingenstr. 1",
                "zip": "8005",
                "city": "Zurich",
                "country": "Switzerland",
                "state": "",
                "type": "Work",
            }
        )
        changedprofile["addresses"].append(
            {
                "id": "3",
                "state": "ZH",
                "city": "Zurich",
                "country": "Switzerland",
                "type": "Work",
            }
        )
        changedprofile["addresses"].append(
            {"id": "4", "city": "Zürich", "country": "Switzerland", "type": "Home"}
        )
        changedprofile["addresses"].append(
            {"id": "5", "country": "Switzerland", "type": "Work"}
        )

        # reference to compare
        originalprofile["addresses"] = [
            {
                "city": "Zürich",
                "country": "Switzerland",
                "countryId": "QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1",
                "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                "state": "ZH",
                "street": "Neugasse 10",
                "type": "Work",
                "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1",
                "zip": "8005",
            },
            {
                "id": "1",
                "street": "Klingenstrasse 1",
                "zip": "8005",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Work",
            },
        ]
        self.assertEqual(
            hatchbuck.clean_all_addresses(changedprofile),
            originalprofile,
            "all addresses should have been cleaned and deduplicated",
        )

    def test_add_address(self):
        hatchbuck = Hatchbuck("", noop=True)
        originalprofile = copy.deepcopy(self.testProfile)
        changedprofile = copy.deepcopy(self.testProfile)
        hatchbuck.add_address(
            changedprofile, "Neugasse 10", "8005", "Zürich", "", "Switzerland", "Work"
        )
        self.assertEqual(
            changedprofile,
            originalprofile,
            "redundant address should " "not have been added",
        )
        changedprofile = copy.deepcopy(self.testProfile)
        hatchbuck.add_address(
            changedprofile, "", "", "Zürich", "", "Switzerland", "Work"
        )
        self.assertEqual(
            changedprofile,
            originalprofile,
            "redundant address should " "not have been added",
        )
        changedprofile = copy.deepcopy(self.testProfile)
        hatchbuck.add_address(changedprofile, "", "", "", "", "Switzerland", "Work")
        self.assertEqual(
            changedprofile,
            originalprofile,
            "redundant address should " "not have been added",
        )
        changedprofile = copy.deepcopy(self.testProfile)
        originalprofile["addresses"].append(
            {
                "street": "Klingenstrasse 1",
                "zip": "8005",
                "city": "Zürich",
                "country": "Switzerland",
                "state": "",
                "type": "Work",
            }
        )
        hatchbuck.add_address(
            changedprofile,
            "Klingenstr. 1 ",
            "8005",
            "Zurich",
            "",
            "Switzerland",
            "Work",
        )
        self.assertEqual(originalprofile, changedprofile, "clean address added")
