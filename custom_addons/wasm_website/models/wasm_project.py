# -*- coding: utf-8 -*-
from odoo import models, fields

class WasmProject(models.Model):
    _name = 'wasm.project'
    _description = 'مشاريع شركة عرفة الهندسية'
    _order = 'sequence, id desc'

    name = fields.Char(string='اسم المشروع', required=True, translate=True)
    sequence = fields.Integer(string='التسلسل', default=10)
    image = fields.Image(string='صورة المشروع الرئيسية', max_width=1024, max_height=1024)
    description = fields.Text(string='وصف مختصر للمشروع', translate=True)
    detailed_description = fields.Html(string='التفاصيل الهندسية والفنية للمشروع', translate=True)
    video_url = fields.Char(string='رابط فيديو المشروع (MP4 / YouTube)', help='رابط مقطع فيديو استعراضي للمشروع')
    attachment_ids = fields.Many2many('ir.attachment', string='معرض صور وفيديوهات المشروع')

    state = fields.Selection([
        ('in_progress', 'تحت التنفيذ'),
        ('completed', 'مكتمل بنجاح'),
    ], string='حالة المشروع', default='completed', required=True)

    project_type = fields.Selection([
        ('commercial', 'أبراج ومشاريع تجارية'),
        ('residential', 'مجمعات سكنية وفلل'),
        ('mep', 'أعمال كهروميكانيكية وتكييف'),
        ('infrastructure', 'بناء عظم وبنية تحتية'),
    ], string='نوع المشروع', default='commercial', required=True)

    location = fields.Char(string='موقع المشروع (المدينة/المحافظة)', required=True, translate=True)
    client_name = fields.Char(string='الجهة المترأسة / المالك', translate=True)
    area = fields.Float(string='المساحة المنفذة (م²)')
    completion_date = fields.Date(string='تاريخ التسليم / الإنجاز')
    active = fields.Boolean(string='نشط للموقع', default=True)
