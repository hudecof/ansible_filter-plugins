# Filter Plugins

List of filter plugings for jinja templates.

# Requirements

None

# Dependencies

None

Example Playbook
----------------


    - hosts: servers
      roles:
         - { role: hudecof.filter_plugins }

# List of plugins

## Object type
Set of plugins to determine of the object type

- `isdict` if the variabla is type of **dict**
- `islist` if the variabla is type of **list**
- `isint` if the variabla is type of **int**
- `isstr` if the variabla is type of **basesring**
- `isnone` if the variabla is type of **None**


License
-------

BSD

Author Information
------------------

Peter Hudec
CNC, a.s.