from hatchbuck import Hatchbuck
import unittest


class TestHatchbuck(unittest.TestCase):
    global testProfile
    testProfile = {
        "addresses": [
            {
                "city": "Zürich",
                "country": "Switzerland",
                "countryId": "QmJzeldzQ25rbXluZG"
                "c4RzlDYmFmYlZOY2xTemMwX2"
                "ZoMll5UTJPenhsNDE1",
                "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMH" "Z2UUxLY2d6a1JaU3Nicm5hRTN6azE1",
                "state": "ZH",
                "street": "Neugasse 10",
                "type": "Work",
                "typeId": "SjFENlU0Y2s2RDFpM0NKWEExRm"
                "VvSjZ4T3NJMG5pLWNYZjRse"
                "DBSaTVfVTE1",
                "zip": "8005",
            }
        ],
        "campaigns": [],
        "company": "VSHN AG",
        "contactId": "SUFYbGdOaEQ0cWR2N1JfV183UFNBS" "DllTktCc3E3OWRsN09qaW4tU3JqbzE1",
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
                "id": "S2lIY2NOS2dBRnRCamEyQU" "ZxTG00dzhlYjAxUU9Sa3Z5ZFVENGVHTG1DODE1",
                "type": "Work",
                "typeId": "VmhlQU1pZVJSUFFJSjZfM"
                "HRmT1laUmwtT0FMNW9hbnBuZHd"
                "2Q1JTdE0tYzE1",
            }
        ],
        "firstName": "Bashar",
        "instantMessaging": [],
        "lastName": "Said",
        "phones": [
            {
                "id": "OHh4U0ZWc3FNVXVBQVF4cjdsak9McWc4T" "VppZlF4NklrNmZfSnBhaDZwQTE1",
                "number": "+(414) 454-5 53 00",
                "type": "Work",
                "typeId": "QTBncHV0dndnaGNnRVMzLTR0SGtF"
                "RmRvZjdqNm4zcVphQi1XX1Z2MXV"
                "tRTE1",
            }
        ],
        "referredBy": "",
        "salesRep": {
            "id": "VGpwQTRGTmw4MExVODl1b1BmXzBodTBwWnZXS2dUZ" "zVvSkJKZUx4UlFpdzE1",
            "username": "aarno.aukia",
        },
        "socialNetworks": [
            {
                "address": "https://twitter.com/bashar_2018",
                "id": "S1pEM2NMWlhmZ1VUcDhTUWVvQy1kU21xMjlSbDg" "5Z3piMERVbEFsam42azE1",
                "typeId": "ZGRlMHpBaXY3M05YUGc4a0pIY3lRdUFKN1JYa"
                "Dd2VEphbzhSRkdzM2x4bzE1",
            }
        ],
    }

    def setUp(self):
        pass

    def test_profile_add_address(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        existingaddress = {
            "street": "Neugasse 10",
            "zip_code": "8005",
            "city": "Zürich",
            "country": "Switzerland",
        }
        # We're trying to add an address that is already there
        # Check that the address is there already
        self.assertTrue(
            hatchbuck.address_exists(
                testProfile,
                {
                    "street": existingaddress["street"],
                    "zip": existingaddress["zip_code"],
                    "city": existingaddress["city"],
                    "country": existingaddress["country"],
                    "type": "Work",
                },
            )
        )

        # try to add the address again
        profile = hatchbuck.profile_add_address(testProfile, existingaddress, "Work")

        # Check that the address is still there
        self.assertTrue(
            hatchbuck.address_exists(
                profile,
                {
                    "street": existingaddress["street"],
                    "zip": existingaddress["zip_code"],
                    "city": existingaddress["city"],
                    "country": existingaddress["country"],
                    "type": "Work",
                },
            )
        )

        # check that the profile was not modified by
        #  trying to add an existing address
        self.assertTrue(profile == testProfile)

        # We can't test adding an address offline
        # # adding a new address
        # newaddress = {'street': "Bahnhofstrasse 1",
        #      'zip_code': "8001",
        #      'city': "Zürich",
        #      'country': "Switzerland"}
        #
        # self.assertFalse(hatchbuck.address_exists(profile, {
        #     'street': newaddress['street'],
        #     'zip': newaddress['zip_code'],
        #     'city': newaddress['city'],
        #     'country': newaddress['country'],
        #     'type': 'Home',
        # }))
        #
        # profile = hatchbuck.profile_add_address(testProfile,
        #                                         newaddress,
        #                                         "Home"
        # )
        # print(len(profile['addresses']))
        # print(profile)
        # self.assertTrue(len(profile['addresses']) == 2)
        #
        # self.assertTrue(hatchbuck.address_exists(profile, {
        #     'street': newaddress['street'],
        #     'zip': newaddress['zip_code'],
        #     'city': newaddress['city'],
        #     'country': newaddress['country'],
        #     'type': 'Home',
        # }))

    def test_profile_contains(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        profile = hatchbuck.profile_contains(
            {
                "contactId": "SUFYbGdOaEQ0cWR2N1JfV183U"
                "FNBSDllTktCc3E3OWRsN09qaW4tU3JqbzE1",
                "phones": [{"number": "+(414) 454-5 53 00", "type": "work"}],
            },
            "phones",
            "number",
            "+(414) 454-5 53 00",
        )
        self.assertTrue(profile, testProfile)

    def test_add_tag(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        profile = hatchbuck.add_tag(
            "SUFYbGdOaEQ0cWR2N1JfV183UFNBSDllTktCc3E3OWRsN09qaW4tU3JqbzE1", ""
        )
        self.assertFalse(profile, testProfile)

    def test_profile_add_birthday(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        profile = hatchbuck.profile_add_birthday(
            {
                "contactId": "TmpmT0QyUGE3UGdGejZMay1x"
                "bDNyUHJFWU91M2VwN0hCdGtZZFFCaWRZczE1"
            },
            {"month": "1", "day": "1", "year": "1984"},
        )
        self.assertTrue(profile, testProfile)

    def test_cleanup_phone_number(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        self.assertEqual(
            hatchbuck._cleanup_phone_number("+41 (44) 545-53-00"), "+41445455300"
        )
        self.assertEqual(
            hatchbuck._cleanup_phone_number("+41445455300"), "+41445455300"
        )
        self.assertEqual(
            hatchbuck._cleanup_phone_number("+41 44 545 53 00"), "+41445455300"
        )
        self.assertEqual(
            hatchbuck._cleanup_phone_number("\xa0+41 44 545 53 00\xa0"), "+41445455300"
        )

    def test_format_phone_number(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        self.assertEqual(
            hatchbuck._format_phone_number("+41445455300"), "+41 44 545 53 00"
        )
        self.assertEqual(
            hatchbuck._format_phone_number("\xa0+41(44)545-53-00\xa0"),
            "+41 44 545 53 00",
        )
        self.assertEqual(
            hatchbuck._format_phone_number("+41 44 545 53 00"), "+41 44 545 53 00"
        )
        self.assertEqual(hatchbuck._format_phone_number("044 545 53 00"), None)
        self.assertEqual(
            hatchbuck._format_phone_number("044 545 53 00", "CH"), "+41 44 545 53 00"
        )

    def test_clean_all_phone_numbers(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        profile1 = {
            "phones": [
                {
                    "id": "1",
                    "number": "+(414) 454-5 53 00",
                    "type": "Work",
                    "typeId": "asdf",
                },
                {
                    "id": "2",
                    "number": "+(414) 454-5 53 00",
                    "type": "Home",
                    "typeId": "qwer",
                },
                {
                    "id": "3",
                    "number": "(044) 545-53-00",
                    "type": "Work",
                    "typeId": "asdf",
                },
            ]
        }
        self.assertEqual(
            hatchbuck.clean_all_phone_numbers(profile1),
            {
                "phones": [
                    {
                        "id": "1",
                        "number": "+41 44 545 53 00",
                        "type": "Work",
                        "typeId": "asdf",
                    }
                ]
            },
        )
        profile2 = {
            "phones": [
                {
                    "id": "1",
                    "number": "(044) 545-53-00",
                    "type": "Work",
                    "typeId": "asdf",
                }
            ],
            "addresses": [{"country": "Switzerland"}],
        }
        self.assertEqual(
            hatchbuck.clean_all_phone_numbers(profile2),
            {
                "phones": [
                    {
                        "id": "1",
                        "number": "+41 44 545 53 00",
                        "type": "Work",
                        "typeId": "asdf",
                    }
                ],
                "addresses": [{"country": "Switzerland"}],
            },
        )

    def test_short_contact(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        self.assertEqual(
            hatchbuck.short_contact(testProfile),
            "Contact(Bashar Said, bashar.said@vshn.ch)",
        )
        self.assertEqual(hatchbuck.short_contact({}), "Contact()")
        self.assertEqual(
            hatchbuck.short_contact({"firstName": "firstName", "lastName": "lastName"}),
            "Contact(firstName lastName)",
        )
        self.assertEqual(
            hatchbuck.short_contact(
                {"emails": [{"address": "emailaddress@example.com"}]}
            ),
            "Contact(emailaddress@example.com)",
        )

    def test_get_countrycode(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        self.assertEqual(
            hatchbuck._get_countrycode(testProfile), "CH"
        )  # unique country
        self.assertEqual(hatchbuck._get_countrycode({}), None)  # no country
        self.assertEqual(
            hatchbuck._get_countrycode(
                {"addresses": [{"country": "Switzerland"}, {"country": "Germany"}]}
            ),
            None,
        )  # ambiguous country

    def test_clean_all_addresses(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True

    def test_clean_address(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "Neugasse 10",
                    "zip_code": "8005",
                    "city": "Zürich",
                    "country": "Switzerland",
                }
            ),
            {
                "street": "Neugasse 10",
                "zip_code": "8005",
                "city": "Zürich",
                "country": "Switzerland",
            },
        )  # no change
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Zürich, Canton of Zürich, Switzerland",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Zürich", "country": "Switzerland"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Bern, Canton of Bern, Switzerland",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Bern", "country": "Switzerland"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Neuenkirch, Kanton Luzern, Schweiz",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Neuenkirch",
                "country": "Switzerland",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Frankfurt Am Main Area, Germany",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Frankfurt Am Main",
                "country": "Germany",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Sankt Gallen Area, Switzerland",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Sankt Gallen",
                "country": "Switzerland",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Santa Monica, California",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Santa Monica",
                "country": "United States",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "San Francisco Bay Area",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "San Francisco Bay Area",
                "country": "",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {"street": "", "zip_code": "", "city": "Austria area", "country": ""}
            ),
            {"street": "", "zip_code": "", "city": "", "country": "Austria"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Vienna, Vienna, Austria",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Vienna", "country": "Austria"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Wohlen AG, Kanton Aargau, Schweiz",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Wohlen AG",
                "country": "Switzerland",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Austin, Texas Area",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Austin, Texas Area", "country": ""},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Greater New York City Area",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Greater New York City Area",
                "country": "",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {"street": "", "zip_code": "", "city": "Switzerland", "country": ""}
            ),
            {"street": "", "zip_code": "", "city": "", "country": "Switzerland"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Helsinki Area, Finland",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Helsinki", "country": "Finland"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {"street": "", "zip_code": "", "city": "United States", "country": ""}
            ),
            {"street": "", "zip_code": "", "city": "", "country": "United States"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Zürich Area, Switzerland",
                    "country": "ch",
                }
            ),
            {"street": "", "zip_code": "", "city": "Zürich", "country": "Switzerland"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Zürich Area, Switzerland",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Zürich", "country": "Switzerland"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Brisbane Area, Australia",
                    "country": "au",
                }
            ),
            {"street": "", "zip_code": "", "city": "Brisbane", "country": "Australia"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Amsterdam Area, Netherlands",
                    "country": "nl",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Amsterdam",
                "country": "Netherlands",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Brisbane Area, Australia",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Brisbane", "country": "Australia"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {"street": "", "zip_code": "", "city": "", "country": "CH"}
            ),
            {"street": "", "zip_code": "", "city": "", "country": "Switzerland"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "Pflanzschulstrasse 34",
                    "zip_code": "CH-8004",
                    "city": "Zürich",
                    "country": "",
                }
            ),
            {
                "street": "Pflanzschulstrasse 34",
                "zip_code": "8004",
                "city": "Zürich",
                "country": "Switzerland",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Zürich Area, Svizzera",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Zürich", "country": "Switzerland"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {"street": "", "zip_code": "", "city": "Luxembourg", "country": ""}
            ),
            {"street": "", "zip_code": "", "city": "", "country": "Luxembourg"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Boulogne-Billancourt, Île-de-France, France",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Boulogne-Billancourt",
                "country": "France",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Lausanne, Canton de Vaud, Suisse",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Lausanne",
                "country": "Switzerland",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Région de Lausanne, Suisse",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Lausanne",
                "country": "Switzerland",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Région de Genève, Suisse",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Genève", "country": "Switzerland"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Copenhagen, Capital Region, Denmark",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Copenhagen", "country": "Denmark"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Copenhagen Area, Capital Region, Denmark",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Copenhagen", "country": "Denmark"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "München und Umgebung, Deutschland",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "München", "country": "Germany"},
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Currais Novos e Região, Brasil",
                    "country": "",
                }
            ),
            {
                "street": "",
                "zip_code": "",
                "city": "Currais Novos",
                "country": "Brazil",
            },
        )
        self.assertEqual(
            hatchbuck.clean_address(
                {
                    "street": "",
                    "zip_code": "",
                    "city": "Zürich und Umgebung, Schweiz",
                    "country": "",
                }
            ),
            {"street": "", "zip_code": "", "city": "Zürich", "country": "Switzerland"},
        )

    def test_clean_city_name(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
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

    def test_clean_country_name(self):
        hatchbuck = Hatchbuck("")
        hatchbuck.noop = True
        self.assertEqual(
            hatchbuck._clean_country_name("Germany"), "Germany"
        )  # no change
        self.assertEqual(hatchbuck._clean_country_name("Suisse"), "Switzerland")
        self.assertEqual(hatchbuck._clean_country_name("Svizzera"), "Switzerland")
        self.assertEqual(hatchbuck._clean_country_name("Schweiz"), "Switzerland")
        self.assertEqual(hatchbuck._clean_country_name("Deutschland"), "Germany")
        self.assertEqual(hatchbuck._clean_country_name("Brasil"), "Brazil")


if __name__ == "__main__":
    unittest.main()
