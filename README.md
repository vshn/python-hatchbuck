
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


#### This python package provides an easy to use python module to interact with the [hatchbuck.com API][https://hatchbuck.freshdesk.com/support/solutions/articles/5000578765-hatchbuck-api-documentation-for-advanced-users-]

## Examples
* ## Search for email

    hatchbuck = Hatchbuck(config['hatchbuck_key'],noop=args.noop)

    profile = hatchbuck.search_email('bashar.said@vshn.ch')

    pp.pprint(profile)

    $ python basharexample.py -c aarno.yaml -v


* ## Search for the Full name

    hatchbuck = Hatchbuck(config['hatchbuck_key'],noop=args.noop)

    profile = hatchbuck.search_name('bashar', 'said')

    pp.pprint(profile)

    $ python basharexample.py -c aarno.yaml -v


* ## Search for multiple emails

    hatchbuck = Hatchbuck(config['hatchbuck_key'],noop=args.noop)

    profile = hatchbuck.search_email_multi(['sgdhfgfdgh@fdvd.com', 'bashar.said@vshn.ch'])

    pp.pprint(profile)

    $ python basharexample.py -c aarno.yaml -v



* Profile updated
* Create profile
* Add address to profile
* profile contains
* Add a profile
* Add tags
* Add birthday to profile
