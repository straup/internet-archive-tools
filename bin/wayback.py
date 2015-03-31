#!/usr/bin/env python

import logging
import sys
import json
import urllib2

def archived(url):

    req = "http://archive.org/wayback/available?url=%s" % url

    try:
        rsp = urllib2.urlopen(req)
        data = json.load(rsp)

        snapshots = data.get('archived_snapshots', None)
        closest = None
        status = None

        if snapshots:
            closest = snapshots.get('closest', None)

        if closest:
            status = closest.get('status', None)

        if status == 200:
            return True

    except Exception, e:
        logging.error("failed to determine availability for %s, because %s" % (url, e))
        return False

def save(url):

    req = "http://web.archive.org/save/%s" % url

    try:
        rsp = urllib2.urlopen(req)
        status = rsp.getcode()

    except Exception, e:
        logging.error("failed to wayback %s, because %s" % (url, e))

    return True

if __name__ == '__main__':

    url = sys.argv[1]

    if not archived(url):

        save(url)
