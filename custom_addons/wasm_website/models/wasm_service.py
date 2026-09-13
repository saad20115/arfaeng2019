# -*- coding: utf-8 -*-
from odoo import models, fields, api

class WasmService(models.Model):
    _name = 'wasm.service'
    _description = 'خدمات شركة عرفة الهندسية'
    _order = 'sequence, id'

    name = fields.Char(string='اسم الخدمة', required=True, translate=True)
    sequence = fields.Integer(string='التصميم والترتيب', default=10)
    icon = fields.Char(string='أيقونة الخدمة', default='fa-building-o', help='اسم الفئة من FontAwesome مثل fa-wrench, fa-bolt, fa-building-o')
    image = fields.Image(string='صورة الخدمة التوضيحية', max_width=1024, max_height=1024)
    short_description = fields.Text(string='وصف مختصر للخدمة', translate=True)
    detailed_description = fields.Html(string='شرح مفصل لنطاق العمل والخدمات الشاملة', translate=True)

    category = fields.Selection([
        ('civil', 'الأعمال الإنشائية وبناء العظم'),
        ('mep', 'الأعمال الكهربائية والميكانيكية (MEP)'),
        ('hvac', 'أعمال التكييف والتبريد المركزية'),
        ('finishing', 'أعمال التشطيبات الفاخرة والديكور'),
        ('renovation', 'أعمال الترميم والتأهيل الهيكلي'),
    ], string='تصنيف الخدمة', default='civil', required=True)

    active = fields.Boolean(string='نشط على الموقع', default=True)

    def write(self, vals):
        res = super(WasmService, self).write(vals)
        if any(k in vals for k in ('image', 'name', 'short_description', 'sequence')):
            self._sync_to_site_config()
        return res

    @api.model_create_multi
    def create(self, vals_list):
        records = super(WasmService, self).create(vals_list)
        records._sync_to_site_config()
        return records

    def _sync_to_site_config(self):
        config = self.env['wasm.site.config'].sudo().get_config()
        if not config:
            return
        mapping = {
            'Modern building systems': 1,
            'Electromechanical systems': 2,
            'Smart building systems': 3,
            'Alternative energy solutions': 4,
            'Fire protection & prevention systems': 5,
            'Medical Gas Systems': 6,
            'Infrastructure Development': 7,
            'Planning & Construction': 8,
        }
        for rec in self:
            card_num = mapping.get(rec.name)
            if card_num:
                updates = {}
                if rec.image:
                    updates[f'srv{card_num}_img'] = rec.image
                if rec.short_description:
                    updates[f'srv{card_num}_desc_en'] = rec.short_description
                if updates:
                    config.sudo().write(updates)
