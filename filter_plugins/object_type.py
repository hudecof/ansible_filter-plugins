from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import collections
import itertools

from ansible import errors


def islist(a):
    return bool(isinstance(a, list))

def isdict(a):
    return bool(isinstance(a, dict))

def isint(a):
    return bool(isinstance(a, int))

def isstr(a):
    return bool(isinstance(a, basesring))

def isnone(a):
    return bool(a is None)


class FilterModule(object):
    ''' Ansible object type jinja2 filters '''

    def filters(self):
        filters = {
            'islist': islist,
            'isdict': isdict,
            'isint': isint,
            'isstr': isstr,
            'isnone': isnone,
        }

        return filters
