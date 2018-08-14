# Filter Plugins

List of filter plugings for jinja templates.

## Requirements

None

## Dependencies

None

## Example Playbook


    - hosts: servers
      roles:
         - { role: hudecof.filter_plugins }

# List of plugins

## Object type
Set of plugins to determine of the object type

- `isdict`: **true** if the variable is type of **dict**
- `islist`: **true** if the variable is type of **list**
- `isint`: **true** if the variable is type of **int**
- `isstr`: **true** if the variable is type of **basesring**
- `isnone`: **true** if the variable is type of **None**

## Config convert
- `to_python`: converts YAML structure to python objects
- `to_ruby`: converts YAML structure to ruby objects

## License

BSD

## Author Information

Peter Hudec
