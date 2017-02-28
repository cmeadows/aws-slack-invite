#!/usr/bin/env python

import json
import logging
import urllib
import urllib2

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    # Simple check for email validation
    if "@" not in event.get("email", ""):
        raise Exception("The email provided is not valid.")

    url = 'https://slack.com/api/users.admin.invite'
    data = urllib.urlencode({
        "token": "{{cookiecutter.slack_oauth_token}}",
        "email": event.get("email")})

    try:
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        r = json.loads(response.read())

        if r.get('ok'):
            return {
                "success": True,
                "message": "WOOOT! Check your email!"
            }
        else:
            return {
                "success": False,
                "message": "Error while sending invitation: " + r.get("error")
            }
    except Exception:
        return {
            "success": False,
            "message": "Error while sending invitation: " + r.get("error")
        }
