from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import collections
import itertools

from ansible import errors


def islist(a):
    return bool(isinstance(a, (list, tuple)))

def isdict(a):
    return bool(isinstance(a, dict))

def isint(a):
    return bool(isinstance(a, (int, float)))

def isstr(a):
    return bool(isinstance(a, basestring))

def isnone(a):
    return bool(a is None)

def istrue(a):
    return bool(a is True)

def isfalse(a):
    return bool(a is False)

def isbool(a):
    return isfalse(a) or istrue(a)


class FilterModule(object):
    ''' Ansible object type jinja2 filters '''

    def filters(self):
        filters = {
            'islist': islist,
            'isdict': isdict,
            'isint': isint,
            'isstr': isstr,
            'isnone': isnone,
            'istrue': istrue,
            'isfalse': isfalse,
            'isbool': isbool,
        }

        return filters
