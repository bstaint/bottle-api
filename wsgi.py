#!/usr/bin/python
import os
import sys

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

#IMPORTANT: Put any additional includes below this line.  If placed above this
#line, it's possible required libraries won't be in your searchable path

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)

from mybottle import application
