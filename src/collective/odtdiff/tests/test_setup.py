# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.odtdiff.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of collective.odtdiff into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.odtdiff is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.odtdiff'))

    def test_uninstall(self):
        """Test if collective.odtdiff is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.odtdiff'])
        self.assertFalse(self.installer.isProductInstalled('collective.odtdiff'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollectiveOdtdiffLayer is registered."""
        from collective.odtdiff.interfaces import ICollectiveOdtdiffLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveOdtdiffLayer, utils.registered_layers())
