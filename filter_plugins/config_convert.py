from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import collections
import itertools
import json

from ansible import errors

def to_ruby(a,):
    if bool(a is None):
        return 'nil'
    if bool(a is True):
        return 'true'
    if bool(a is False):
        return 'false'
    if bool(isinstance(a, basestring)):
        return "'%s'" % a
    if bool(isinstance(a, (int, float))):
        return str(a)
    if bool(isinstance(a, (list, tuple))):
        items = []
        for v in a:
            items.append(to_ruby(v))
        return "[%s]" % ','.join(items)

    if bool(isinstance(a, dict)):
        items = []
        for k,v in a.iteritems():
            items.append("%s: %s" % (to_ruby(k), to_ruby(v)))
        return "{%s}" % ','.join(items)

    raise ValueError('unsupported type %s' % type(a))

def to_python(a):
    if bool(a is None):
        return str(a)
    if bool(a is True):
        return str(a)
    if bool(a is False):
        return str(a)
    if bool(isinstance(a, basestring)):
        return "'%s'" % a
    if bool(isinstance(a, (int, float))):
        return str(a)
    if bool(isinstance(a, (list, tuple))):
        items = []
        for v in a:
            items.append(to_python(v))
        return "[%s]" % ','.join(items)

    if bool(isinstance(a, dict)):
        items = []
        for k,v in a.iteritems():
            items.append("%s: %s" % (to_python(k), to_python(v)))
        return "{%s}" % ','.join(items)

    raise ValueError('unsupported type %s' % type(a))


class FilterModule(object):
    ''' Ansible hash/list to code conversion filters '''

    def filters(self):
        filters = {
            'to_ruby': to_ruby,
            'to_python': to_python,
        }

        return filters
