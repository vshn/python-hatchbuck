
# Hatchbuck.com CRM API bindings for python
## Installation
    The easiest way to install hatchbuck is with pip:

    $ pip install hatchbuck

## Basic Usage
    from hatchbuck import Hatchbuck
    hatchbuck = Hatchbuck(config['hatchbuck_key'],noop=args.noop)
    profile = hatchbuck. ...('...', ...)
    pp.pprint(profile)

    $ python basharexample.py -c aarno.yaml -v


#### This python package provides an easy to use python module to interact with the [hatchbuck.com API](https://hatchbuck.freshdesk.com/support/solutions/articles/5000578765-hatchbuck-api-documentation-for-advanced-users)

## Examples

## Search for email

```
hatchbuck = Hatchbuck(config['hatchbuck_key'],noop=args.noop)
profile = hatchbuck.search_email('bashar.said@vshn.ch')
pp.pprint(profile)

$ python basharexample.py -c aarno.yaml -v

```

### output

```
    {'addresses': [{'city': 'Zürich',
    'country': 'Switzerland',
    'countryId': 'QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1',
    'id': 'Q0NjajF2U1lTWnBHM1hjRFlnQzhzMHZ2UUxLY2d6a1JaU3Nicm5hRTN6azE1',
    'state': 'ZH',
    'street': 'Neugasse 10',
    'type': 'Work',
    'typeId': 'SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1',
    'zip': '8005'}],
```

```
    'campaigns': [],
    'company': 'VSHN AG',
    'contactId': 'SUFYbGdOaEQ0cWR2N1JfV183UFNBSDllTktCc3E3OWRsN09qaW4tU3JqbzE1',
```

```
    'customFields': [{'name': 'Comments', 'type': 'MText', 'value': ''},
    {'name': 'Invoiced', 'type': 'Number', 'value': ''},
    {'name': 'Language', 'type': 'Text', 'value': ''},
    {'name': 'working at company since',
    'type': 'Text',
    'value': '1.1.2018'},
    {'name': 'company size', 'type': 'Text', 'value': '25'},
    {'name': 'Birthday', 'type': 'Date', 'value': ''}],
```

```
    'emails': [{'address': 'bashar.said@vshn.ch',
    'id': 'S2lIY2NOS2dBRnRCamEyQUZxTG00dzhlYjAxUU9Sa3Z5ZFVENGVHTG1DODE1',
    'type': 'Work',
    'typeId': 'VmhlQU1pZVJSUFFJSjZfMHRmT1laUmwtT0FMNW9hbnBuZHd2Q1JTdE0tYzE1'}],
    'firstName': 'Bashar',
    'instantMessaging': [],
    'lastName': 'Said',
```

```
    'phones': [{'id': 'OHh4U0ZWc3FNVXVBQVF4cjdsak9McWc4TVppZlF4NklrNmZfSnBhaDZwQTE1',
    'number': '+(414) 454-5 53 00',
    'type': 'Work',
    'typeId': 'QTBncHV0dndnaGNnRVMzLTR0SGtFRmRvZjdqNm4zcVphQi1XX1Z2MXVtRTE1'}],
    'referredBy': '',
```

```
    'salesRep': {'id': 'VGpwQTRGTmw4MExVODl1b1BmXzBodTBwWnZXS2dUZzVvSkJKZUx4UlFpdzE1',
    'username': 'aarno.aukia'},
```

```
    'socialNetworks': [{'address': 'https://twitter.com/bashar_2018',
    'id': 'S1pEM2NMWlhmZ1VUcDhTUWVvQy1kU21xMjlSbDg5Z3piMERVbEFsam42azE1',
    'type': 'Twitter',
    'typeId': 'ZGRlMHpBaXY3M05YUGc4a0pIY3lRdUFKN1JYaDd2VEphbzhSRkdzM2x4bzE1'},
    {'address': 'https://www.linkedin.com/in/bashar-said-729a54156/',
    'id': 'Tzd0TTBueVQzS09JQVZTLUxiUUxUT25VMmVvT0dua2txc2NHZkNkNEg5VTE1',
    'type': 'LinkedIn',
    'typeId': 'Q2dJTVQ1NW9UYzhJeUd4ckI0dWFNWkpLOUxyTXVGUFVjQlZYbVM2ZlI4bzE1'}],
```

```
    'source': {'id': 'MHZFdHZqcWVXT1IyNHZGYlM1RGppWVVJcGc3aHgtU3lXRWtfQmFXN0lCODE1',
    'name': 'vshn.ch'},
```

```
    'status': {'id': 'UE9zMy1abnhnNUJQWnVORE5BQzNicUFWQ3huLXF2eGlSdlIyYVFmVXh4UTE1',
    'name': 'Employee'},
    'subscribed': True,
    'tags': [],
```

```
    'temperature': {'id': 'UTI0Nm14TlB4SmRkdVNLMjNWQWgwR2R2TjhySE1US1RtVEQ0T24tRWtFbzE1',
    'name': 'Hot'},
    'timezone': 'W. Europe Standard Time',
```

```
    'title': 'DevOps Engineer Intern',
```

```
    'website': [{'id': 'bktodFBCalVCU2J6aFhjaXc5UVZkUHM5OHFnd0ZuQmdJTTU0cDRScm1KSTE1',
    'websiteUrl': 'https://vshn.ch'}]}
```


## Search for the Full name

 ```
hatchbuck = Hatchbuck(config['hatchbuck_key'],noop=args.noop)
profile = hatchbuck.search_name('bashar', 'said')
pp.pprint(profile)

$ python basharexample.py -c aarno.yaml -v
 ```

### output
```
    We get the same results When we search by email address because the firstname and lastname(bashar, said) belong to the same email address(bashar.said@vshn.ch)
```

## Search for multiple emails
```
hatchbuck = Hatchbuck(config['hatchbuck_key'],noop=args.noop)
profile = hatchbuck.search_email_multi(['sgdhfgfdgh@fdvd.com', 'bashar.said@vshn.ch', ...])
pp.pprint(profile)

$ python basharexample.py -c aarno.yaml -v
```

  **Note:** The emails must be in list form, and the search process stops getting the first match

### output

```
    2018-03-08 11:00:21,079 - hatchbuck - DEBUG - searching for {'emails': [{'address': 'sgdhfgfdgh@fdvd.com'}]}
    2018-03-08 11:00:21,091 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTPS connection (1): api.hatchbuck.com
    2018-03-08 11:00:21,857 - requests.packages.urllib3.connectionpool - DEBUG - "POST /api/v1/contact/search?
    2018-03-08 11:00:21,860 - hatchbuck - DEBUG - not found
```

#### We did not find a profile with an email address: 'sgdhfgfdgh@fdvd.com'
```
    2018-03-08 11:00:21,860 - hatchbuck - DEBUG - searching for {'emails': [{'address': 'bashar.said@vshn.ch'}]}
    2018-03-08 11:00:21,862 - requests.packages.urllib3.connectionpool - INFO - Starting new HTTPS connection (1): api.hatchbuck.com
    2018-03-08 11:00:22,641 - requests.packages.urllib3.connectionpool - DEBUG - "POST /api/v1/contact/search?
    2018-03-08 11:00:22,643 - hatchbuck - DEBUG - found: {......}
```

#### We found a profile with his email address: 'bashar.said@vshn.ch'

### output

```
    We get the same results When we search by email address
```

## Create profile
```
hatchbuck = Hatchbuck(config['hatchbuck_key'],noop=args.noop)
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
        #"subscribed": true,
        "timezone": "W. Europe Standard Time",
        "socialNetworks": [
            {
                "address": "'https://twitter.com/bashar_2018'",
                "type": "Twitter",
            }
        ],
    })
pp.pprint(profile)

$ python basharexample.py -c aarno.yaml -v

```
### output

```
    {'addresses': [ {
    "street": "Langäcker 12",
    "city": "wettingen",
    "state": "AG",
    "zip": "5430",
    "country": "Schweiz",
    "type": "work",
    }],
```

```
    'campaigns': [],
    'company': 'HAWAR',
    'contactId': 'TmpmT0QyUGE3UGdGejZMay1xbDNyUHJFWU91M2VwN0hCdGtZZFFCaWRZczE1',
    'customFields': [{'name': 'Comments', 'type': 'MText', 'value': ''},
    {'name': 'Invoiced', 'type': 'Number', 'value': ''},
    {'name': 'Language', 'type': 'Text', 'value': ''},
    {'name': 'working at company since',
    'type': 'Text',
    'value': ''},
    {'name': 'company size', 'type': 'Text', 'value': ''},
    {'name': 'Birthday', 'type': 'Date', 'value': ''}],
```

```
    'emails': [{'address': 'bashar.said.2018@gmail.com',
    'id': 'M2FaYWpqY1pBMldGeVpYYW11cXRpTUw2NndOcFJsUXIzZGI2VC1JRmdSYzE1',
    'type': 'Work',
    'typeId': 'VmhlQU1pZVJSUFFJSjZfMHRmT1laUmwtT0FMNW9hbnBuZHd2Q1JTdE0tYzE1'}],
```

```
    'firstName': 'Hawar',
    'instantMessaging': [],
    'lastName': 'Afrin',
```

```
    'phones': [{'id': 'MVhxaXBHdlRWOWdLX05FbHF6ZnczMERGVTMyWWRkZ0xsSFFQcXVNYW5NTTE1',
    'number': '0041 76 803 77 34',
    'type': 'Work',
    'typeId': 'QTBncHV0dndnaGNnRVMzLTR0SGtFRmRvZjdqNm4zcVphQi1XX1Z2MXVtRTE1'}],
```

```
    'referredBy': '',
    'salesRep': {'id': 'VGpwQTRGTmw4MExVODl1b1BmXzBodTBwWnZXS2dUZzVvSkJKZUx4UlFpdzE1',
    'username': 'aarno.aukia'},
```

```
    'socialNetworks': [{'address': "'https://twitter.com/bashar_2018'",
    'id': 'Y0c2YktIcG1kakt4RTJiRkh3NVVnYzNqejdkUkVrQVRkUE0tUVQ3TUpPdzE1',
    'type': 'Twitter',
    'typeId': 'ZGRlMHpBaXY3M05YUGc4a0pIY3lRdUFKN1JYaDd2VEphbzhSRkdzM2x4bzE1'}],
```

```
    'status': {'id': 'UE9zMy1abnhnNUJQWnVORE5BQzNicUFWQ3huLXF2eGlSdlIyYVFmVXh4UTE1',
    'name': 'Employee'},

```

```
    'subscribed': True,
    'tags': [],
    'temperature': {'id': 'UTI0Nm14TlB4SmRkdVNLMjNWQWgwR2R2TjhySE1US1RtVEQ0T24tRWtFbzE1',
    'name': 'Hot'},
    'timezone': 'W. Europe Standard Time',
    'title': 'Hawar1',
    'website': []}

```
## Profile updated

#### For example, we want to update the address in the previous profile
```
hatchbuck = Hatchbuck(config['hatchbuck_key'],noop=args.noop)
profile = hatchbuck.update('TmpmT0QyUGE3UGdGejZMay1xbDNyUHJFWU91M2VwN0hCdGtZZFFCaWRZczE1', {
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
             	"street": "Neugasse 10",
                "city": "Zürich",
                "state": "ZH",
                "zip": "8005",
                "country": "Switzerland",
                "type": "work",
            }
        ],
        #"subscribed": true,
        "timezone": "W. Europe Standard Time",
        "socialNetworks": [
            {
                "address": "'https://twitter.com/bashar_2018'",
                "type": "Twitter",
            }
        ],
    }
)
pp.pprint(profile)

$ python basharexample.py -c aarno.yaml -v

```
### output

```
    {'addresses': [{'city': 'Zürich',
    'country': 'Switzerland',
    'countryId': 'QmJzeldzQ25rbXluZGc4RzlDYmFmYlZOY2xTemMwX2ZoMll5UTJPenhsNDE1',
    'id': 'OEFPUzJBeTdaWlVhU3FDR194dEk3NU8xTThxakZuQXV4aE9obHM3SVdKTTE1',
    'state': 'ZH',
    'street': 'Neugasse 10',
    'type': 'Work',
    'typeId': 'SjFENlU0Y2s2RDFpM0NKWEExRmVvSjZ4T3NJMG5pLWNYZjRseDBSaTVfVTE1',
    'zip': '8005'}],
```

## Add address to profile
## profile contains
## Add a profile
## Add tags
## Add birthday to profile
