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
        hatchbuck = Hatchbuck("abc123")
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
        hatchbuck = Hatchbuck("abc123")
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
        hatchbuck = Hatchbuck("abc123")
        profile = hatchbuck.add_tag(
            "SUFYbGdOaEQ0cWR2N1JfV183UFNBSDllTktCc3E3OWRsN09qaW4tU3JqbzE1", ""
        )
        self.assertFalse(profile, testProfile)

    def test_profile_add_birthday(self):
        hatchbuck = Hatchbuck("abc123")
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
        self.assertEqual(
            hatchbuck.cleanup_phone_number("+41 (44) 545-53-00"), "+41445455300"
        )
        self.assertEqual(hatchbuck.cleanup_phone_number("+41445455300"), "+41445455300")
        self.assertEqual(
            hatchbuck.cleanup_phone_number("+41 44 545 53 00"), "+41445455300"
        )
        self.assertEqual(
            hatchbuck.cleanup_phone_number("\xa0+41 44 545 53 00\xa0"), "+41445455300"
        )

    def test_format_phone_number(self):
        hatchbuck = Hatchbuck("")
        self.assertEqual(
            hatchbuck.format_phone_number("+41445455300"), "+41 44 545 53 00"
        )
        self.assertEqual(
            hatchbuck.format_phone_number("\xa0+41(44)545-53-00\xa0"),
            "+41 44 545 53 00",
        )
        self.assertEqual(
            hatchbuck.format_phone_number("+41 44 545 53 00"), "+41 44 545 53 00"
        )
        self.assertEqual(hatchbuck.format_phone_number("044 545 53 00"), None)
        self.assertEqual(
            hatchbuck.format_phone_number("044 545 53 00", "CH"), "+41 44 545 53 00"
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
        self.assertEqual(hatchbuck.get_countrycode(testProfile), "CH")  # unique country
        self.assertEqual(hatchbuck.get_countrycode({}), None)  # no country
        self.assertEqual(
            hatchbuck.get_countrycode(
                {"addresses": [{"country": "Switzerland"}, {"country": "Germany"}]}
            ),
            None,
        )  # ambiguous country


if __name__ == "__main__":
    unittest.main()
