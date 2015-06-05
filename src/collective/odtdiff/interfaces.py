# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveOdtdiffLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IDocumentCompare(Interface):

    def ma_methode(self, source_doc_path, modified_doc_path):
        """
        """

