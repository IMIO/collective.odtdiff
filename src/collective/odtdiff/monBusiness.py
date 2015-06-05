import os
import tempfile

from collective.odtdiff.interfaces import IDocumentCompare
from imio.pyutils.system import runCommand
from pyodcompare import compare
from zope.interface import implements


class maClasse(object):
    implements(IDocumentCompare)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def ma_methode(self, source_doc_path, modified_doc_path):
        diff_path = '/tmp/brol.odt'
        CONVSCRIPT = '%s/compare.py' % os.path.dirname(compare.__file__)
        cmd = '{} {} {} {} {}'.format('/usr/bin/python', CONVSCRIPT, modified_doc_path, source_doc_path, diff_path)
        runCommand(cmd)
        diff_file = open(diff_path, 'rb')
        diff = diff_file.read()
        diff_file.close()

        return diff

