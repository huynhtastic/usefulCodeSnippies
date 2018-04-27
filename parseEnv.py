import os
import re

EXPORT_REGEX = r'export (?P<name>.*)=\"(?P<value>.*)\"'

# parse through env.sh and set environment variables
with open(self.envSh, 'r') as envFile:
    for line in envFile:
	sreMatch = re.search(self.EXPORT_REGEX, line)
	if sreMatch:
	    envValue = sreMatch.group('value')
	    value = envValue.format(**os.environ).replace('$', '') if '$' in envValue else envValue
	    os.environ[sreMatch.group('name')] = value
