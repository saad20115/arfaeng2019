# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase, tagged


@tagged('post_install', '-at_install')
class TestWasmProject(TransactionCase):
    """Automated tests for wasm.project model."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.project = cls.env['wasm.project'].create({
            'name': 'مشروع اختبار',
            'location': 'الرياض',
            'project_type': 'commercial',
            'state': 'completed',
        })

    def test_project_creation(self):
        """Test project is created with correct defaults."""
        self.assertTrue(self.project.exists())
        self.assertTrue(self.project.active)
        self.assertEqual(self.project.state, 'completed')

    def test_project_active_default(self):
        """Test that active defaults to True."""
        project = self.env['wasm.project'].create({
            'name': 'مشروع نشط',
            'location': 'جدة',
        })
        self.assertTrue(project.active)

    def test_project_deactivation(self):
        """Test that project can be deactivated."""
        self.project.write({'active': False})
        self.assertFalse(self.project.active)

    def test_project_states(self):
        """Test valid project states."""
        self.project.write({'state': 'in_progress'})
        self.assertEqual(self.project.state, 'in_progress')
        self.project.write({'state': 'completed'})
        self.assertEqual(self.project.state, 'completed')

    def test_project_types(self):
        """Test valid project types."""
        for ptype in ('commercial', 'residential', 'mep', 'infrastructure'):
            self.project.write({'project_type': ptype})
            self.assertEqual(self.project.project_type, ptype)


@tagged('post_install', '-at_install')
class TestWasmService(TransactionCase):
    """Automated tests for wasm.service model."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.service = cls.env['wasm.service'].create({
            'name': 'خدمة اختبار',
            'icon': 'fa-bolt',
            'category': 'mep',
            'short_description': 'وصف الخدمة',
        })

    def test_service_creation(self):
        """Test service is created with correct values."""
        self.assertTrue(self.service.exists())
        self.assertEqual(self.service.category, 'mep')
        self.assertTrue(self.service.active)

    def test_service_active_default(self):
        """Test that active defaults to True."""
        service = self.env['wasm.service'].create({
            'name': 'خدمة جديدة',
            'icon': 'fa-wrench',
            'category': 'civil',
        })
        self.assertTrue(service.active)

    def test_service_categories(self):
        """Test valid service categories."""
        for cat in ('civil', 'mep', 'hvac', 'finishing', 'renovation'):
            self.service.write({'category': cat})
            self.assertEqual(self.service.category, cat)

    def test_service_deactivation(self):
        """Test that service can be deactivated."""
        self.service.write({'active': False})
        self.assertFalse(self.service.active)


@tagged('post_install', '-at_install')
class TestWasmSiteConfig(TransactionCase):
    """Automated tests for wasm.site.config model (singleton pattern)."""

    def test_get_config_creates_singleton(self):
        """Test that get_config creates a record if none exists."""
        config = self.env['wasm.site.config'].get_config()
        self.assertTrue(config.exists())

    def test_get_config_returns_same_record(self):
        """Test that get_config always returns the same singleton."""
        config1 = self.env['wasm.site.config'].get_config()
        config2 = self.env['wasm.site.config'].get_config()
        self.assertEqual(config1.id, config2.id)

    def test_home_projects_limit_default(self):
        """Test that home_projects_limit defaults to 6."""
        config = self.env['wasm.site.config'].get_config()
        self.assertEqual(config.home_projects_limit, 6)

    def test_projects_page_limit_default(self):
        """Test that projects_page_limit defaults to 12."""
        config = self.env['wasm.site.config'].get_config()
        self.assertEqual(config.projects_page_limit, 12)

    def test_config_write_returns_boolean(self):
        """Test that write returns True (ORM contract)."""
        config = self.env['wasm.site.config'].get_config()
        result = config.write({'home_projects_limit': 4})
        self.assertTrue(result)
