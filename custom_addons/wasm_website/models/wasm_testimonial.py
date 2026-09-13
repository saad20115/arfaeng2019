# -*- coding: utf-8 -*-
from odoo import models, fields, api

class WasmTestimonial(models.Model):
    _name = 'wasm.testimonial'
    _description = 'Client Testimonial & Review - ARFA SPECIALIZED SYSTEMS'
    _order = 'sequence, id desc'

    name = fields.Char(string='Client Name', required=True)
    role_or_project = fields.Char(string='Role / Project Name', help='e.g., Riyadh Commercial Tower or Residential Fitout Owner')
    rating = fields.Selection([
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars')
    ], string='Rating', default='5', required=True)
    feedback = fields.Text(string='Review Content / Feedback', required=True)
    image = fields.Image(string='Client Avatar / Logo', max_width=512, max_height=512)
    sequence = fields.Integer(string='Sequence', default=10)
    active = fields.Boolean(string='Active', default=True)
