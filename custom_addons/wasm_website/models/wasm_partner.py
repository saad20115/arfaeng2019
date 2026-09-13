# -*- coding: utf-8 -*-
from odoo import models, fields, api

class WasmPartner(models.Model):
    _name = 'wasm.partner'
    _description = 'شركاء النجاح - Our Partners'
    _order = 'sequence, id'

    name = fields.Char(string='اسم الشريك / Partner Name', required=True)
    sequence = fields.Integer(string='الترتيب / Sequence', default=10)
    logo = fields.Binary(string='شعار الشريك / Logo Image', help='قم برفع صورة شعار الشريك')
    logo_url = fields.Char(string='رابط الشعار الخارجي / External Logo URL', help='يمكنك إدخال رابط مباشر لصورة الشعار')
    website_url = fields.Char(string='رابط موقع الشريك / Partner Website URL', help='رابط الموقع الخارجي للشريك (مثال: https://www.wyndhamhotels.com)')
    description = fields.Text(string='وصف مختصر / Description')
    active = fields.Boolean(string='نشط / Active', default=True)

    def get_logo_src(self):
        """Returns binary endpoint URL or raw logo_url if provided."""
        self.ensure_one()
        if self.logo:
            return f'/wasm/partner/{self.id}/logo'
        elif self.logo_url:
            return self.logo_url
        return '/web/static/img/placeholder.png'
