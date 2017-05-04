#!/usr/bin/env python
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

import json
import six

import archieml

class CopyException(Exception):
    pass

class Error(object):
    """
    An error object that can mimic the structure of the COPY data, whether the error happens at the Copy, Sheet or Row level. Will print the error whenever it gets repr'ed. 
    """
    _error = ''

    def __init__(self, error):
        self._error = error

    def __getitem__(self, i):
        return self
    
    def __iter__(self):
        return iter([self])

    def __len__(self):
        return 1

    def __repr__(self):
        return self._error

    def __bool__(self):
        return False 

    def __nonzero__(self):
        return False 

class Section(object):
    """
    Wrap copy text, for a single worksheet, for error handling.
    """
    name = None
    _section = []

    def __init__(self, name, data):
        self.name = name
        self._section = data

    def __getitem__(self, i):
        """
        Allow dict-style item access by index (row id), or by row name ("key" column).
        """
        if isinstance(i, int):
            if i >= len(self._section):
                return Error('COPY.%s.%i [row index outside range]' % (self.name, i))

            return self._section[i]

        if i not in self._section:
            return Error('Could not find attribute %s' % i)

        return self._section[i]

    def __getattr__(self, attr):
        return self[attr]

    def __iter__(self):
        return iter(self._section)

    def __len__(self):
        return len(self._section)



class Copy(object):
    """
    Wraps copy text, for multiple worksheets, for error handling.
    """

    def __init__(self, filename):
        self._filename = filename
        self._copy = {}
        self.load()

    def __getitem__(self, name):
        """
        Allow dict-style item access by sheet name.
        """
        print self, name
        if name not in self._copy:
            return Error('COPY.%s [sheet does not exist]' % name)

        return self._copy[name]

    def __getattr__(self, attr):
        return self[attr]

    def load(self):
        """
        Parses the downloaded Excel file.
        """
        try:
            with open(self._filename) as f:
                doc = archieml.load(f)
        except IOError:
            raise CopyException('"%s" does not exist. Have you run "fab update_copy"?' % self._filename)

        for section in doc:
            self._copy[section] = Section(section, doc[section])



#c = Copy('data/copy.txt')

#print dir(c)

# for section in c:
#     print '---------------------'
#     print section



with open('data/copy.txt') as f:
    a = archieml.load(f)

print a
for section in a:
    print '---------------------'
    print section
    if type(a[section]) in [OrderedDict,list,dict]:
        for item in a[section]:
            print item



