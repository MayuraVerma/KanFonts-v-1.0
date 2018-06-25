#!/AFDKOPythonBuild/bin/python2.7

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


"""
This script attempts to send some email.
"""

### Twisted Preamble
# This makes sure that users don't have to set up their environment
# specially in order to run these programs from bin/.
import sys, os
path = os.path.abspath(sys.argv[0])
while os.path.dirname(path) != path:
    if os.path.basename(path).startswith('Twisted'):
        sys.path.insert(0, path)
        break
    path = os.path.dirname(path)
### end of preamble

from twisted.mail.scripts import mailmail
mailmail.run()
