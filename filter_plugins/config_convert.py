from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import collections
import itertools
import json

from ansible import errors

class ConfigRubyEncoder(json.JSONEncoder):
    def default(self, obj):
        if (obj is None):
            return 'nil'
        if (obj is True):
            return 'true'
        if (obj is False):
            return 'false'
        return super(ConfigRubyEncoder, self).default(self, obj)

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
    return ''
#    return json.dumps(a, cls=ConfigRubyEncoder, *args, **kw)

def to_python(a):
    return None


class FilterModule(object):
    ''' Ansible hash/list to code conversion filters '''

    def filters(self):
        filters = {
            'to_ruby': to_ruby,
            'to_python': to_python,
        }

        return filters
