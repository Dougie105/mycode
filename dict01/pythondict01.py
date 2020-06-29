#!/usr/bin/env python3

switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

print( switch['hostname'])
print( switch['ip'])
print()

print('Printing get')
print( switch.get('lynx'))
print( switch.get('lynx', 'THE KEY IS IN ANOTHER CASTLE'))
print( switch.get('version'))
print()

print('Printing the keys')
print( switch.keys())
print()

print('Printing the values')
print(switch.values())
print()

print('Printing Pop')
switch.pop('version')
print('keys:', switch.keys())
print('values:', switch.values())
print()

print('Adding a New Value')
switch['adminLogin'] = 'karl08'
print('keys:', switch.keys())
print('values:', switch.values())
print()

print("Adding Another Value")
switch['password'] = 'qwerty'
print('keys:', switch.keys())
print('values:', switch.values())
