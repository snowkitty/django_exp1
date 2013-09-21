#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    print 'hello'
    print 'server2'
    print 'insert server1 back'

    execute_from_command_line(sys.argv)
