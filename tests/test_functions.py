from hatchbuck import Hatchbuck
import unittest
import copy


class TestHatchbuck(unittest.TestCase):
    global testProfile
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
            "id": "VGpwQTRGTmw4MExVODl1b1BmXzBodTBwWnZXS2dUZ" "zVvSkJKZUx4UlFpdzE1",
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
        #      'zip': "8001",
        #      'city': "Zürich",
        #      'country': "Switzerland"}
        #
        # self.assertFalse(hatchbuck.address_exists(profile, {
        #     'street': newaddress['street'],
        #     'zip': newaddress['zip'],
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
        #     'zip': newaddress['zip'],
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

        profile3 = {
            "phones": [
                {
                    "id": "1",
                    "number": "(044) 545-53-00",
                    "type": "Work",
                    "typeId": "asdf",
                }
            ],
            "addresses": [{"country": "Switzerland "}],  # note the space
        }
        self.assertEqual(
            hatchbuck.clean_all_phone_numbers(profile3),
            {
                "phones": [
                    {
                        "id": "1",
                        "number": "+41 44 545 53 00",
                        "type": "Work",
                        "typeId": "asdf",
                    }
                ],
                "addresses": [{"country": "Switzerland "}],
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

    def test_safe_update(self):
        hatchbuck = Hatchbuck("", noop=True)
        self.maxDiff = None

        # top level fields
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        changedprofile["firstName"] = "Hello"
        changedprofile["lastName"] = "World"
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile, {"firstName": "Hello", "lastName": "World"}
            ),
            changedprofile,
        )

        # field with dict
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        changedprofile["salesRep"] = {"username": "hello.world"}
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile, {"salesRep": {"username": "hello.world"}}
            ),
            changedprofile,
        )

        # field with list of dict, update by id
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        changedprofile["emails"] = [
            {
                "address": "test@vshn.ch",
                "id": "S2lIY2NOS2dBRnRCamEyQUZxTG00dzhlYjAxUU9Sa3Z5ZFVENGVHTG1DODE1",
                "type": "Work",
                "typeId": "VmhlQU1pZVJSUFFJSjZfMHRmT1laUmwtT0FMNW9hbnBuZHd2Q1JTdE0tYzE1",
            }
        ]
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile,
                {
                    "emails": [
                        {
                            "address": "test@vshn.ch",
                            "id": "S2lIY2NOS2dBRnRCamEyQUZxTG00dzhlYjAxUU9Sa3Z5Z"
                            "FVENGVHTG1DODE1",
                        }
                    ]
                },
            ),
            changedprofile,
        )

        # field with list of dict, deleting empty by id
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        changedprofile["emails"] = []
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile,
                {
                    "emails": [
                        {
                            "address": "",
                            "id": "S2lIY2NOS2dBRnRCamEyQUZxTG00dzhlYjAxUU9Sa3Z5Z"
                            "FVENGVHTG1DODE1",
                        }
                    ]
                },
            ),
            changedprofile,
        )

        # field with list of dict, deleting empty by id
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        changedprofile["addresses"] = []
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile,
                {
                    "addresses": [
                        {
                            "id": "Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU"
                            "3Nicm5hRTN6azE1",
                            "city": "",
                            "country": "",
                            "state": "",
                            "street": "",
                            "zip": "",
                        }
                    ]
                },
            ),
            changedprofile,
        )

        # field with list of dict, deleting empty by id
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        changedprofile["phones"] = []
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile,
                {
                    "phones": [
                        {
                            "number": "",
                            "id": "OHh4U0ZWc3FNVXVBQVF4cjdsak9McWc4TVppZlF4NklrN"
                            "mZfSnBhaDZwQTE1",
                        }
                    ]
                },
            ),
            changedprofile,
        )

        # field with list of dict, deleting empty by id
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        changedprofile["socialNetworks"] = []
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile,
                {
                    "socialNetworks": [
                        {
                            "address": "",
                            "id": "S1pEM2NMWlhmZ1VUcDhTUWVvQy1kU21xMjlSbDg5Z3piM"
                            "ERVbEFsam42azE1",
                        }
                    ]
                },
            ),
            changedprofile,
        )

        # field with list of dict, adding new
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        changedprofile["emails"] = [
            {
                "address": "bashar.said@vshn.ch",
                "id": "S2lIY2NOS2dBRnRCamEyQUZxTG00dzhlYjAxUU9Sa3Z5ZFVENGVHTG1DODE1",
                "type": "Work",
                "typeId": "VmhlQU1pZVJSUFFJSjZfMHRmT1laUmwtT0FMNW9hbnBuZHd2Q1JTdE0tYzE1",
            },
            {"address": "test@vshn.ch", "type": "Home"},
        ]
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile,
                {"emails": [{"address": "test@vshn.ch", "type": "Home"}]},
            ),
            changedprofile,
        )
        # field with list of dict, updating by listdictkey
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        changedprofile["emails"] = [
            {
                "address": "bashar.said@vshn.ch",
                "id": "S2lIY2NOS2dBRnRCamEyQUZxTG00dzhlYjAxUU9Sa3Z5ZFVENGVHTG1DODE1",
                "type": "Home",
                "typeId": "VmhlQU1pZVJSUFFJSjZfMHRmT1laUmwtT0FMNW9hbnBuZHd2Q1JTdE0tYzE1",
            }
        ]
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile,
                {"emails": [{"address": "bashar.said@vshn.ch", "type": "Home"}]},
            ),
            changedprofile,
        )
        # field with list of dict, not adding empty address
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile,
                {
                    "addresses": [
                        {
                            "city": "",
                            "country": "",
                            "state": "",
                            "street": "",
                            "zip": "",
                        }
                    ]
                },
            ),
            changedprofile,
        )

        # field with list of dict, not adding empty address
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile,
                {
                    "addresses": [
                        {
                            "city": "",
                            "country": "",
                            "state": "",
                            "street": "",
                            "zip": "",
                        }
                    ]
                },
            ),
            changedprofile,
        )

        # field with list of dict, not adding empty/incomplete email
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        self.assertEqual(
            hatchbuck.safe_update(
                originalprofile, {"emails": [{"address": "", "type": "Home"}]}
            ),
            changedprofile,
        )

        # field with list of dict, adding incomplete address
        originalprofile = copy.deepcopy(testProfile)
        changedprofile = copy.deepcopy(testProfile)
        changedprofile["addresses"] = [
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
        ]
        self.assertEqual(
            hatchbuck.safe_update(originalprofile, {"addresses": [{"city": "Zürich"}]}),
            changedprofile,
        )


if __name__ == "__main__":
    unittest.main()
