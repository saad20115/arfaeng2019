# -*- coding: utf-8 -*-
from odoo import models, fields, api

class WasmSiteConfig(models.Model):
    _name = 'wasm.site.config'
    _description = 'Site Config & Media Settings - ARFA SPECIALIZED SYSTEMS'

    name = fields.Char(string='Config Name', default='Official Website Config', required=True)
    
    # Display Limit & Section Toggle Controls
    home_projects_limit = fields.Integer(string='Homepage Projects Limit', default=6, help='Maximum number of projects displayed on homepage')
    projects_page_limit = fields.Integer(string='Projects Page Limit', default=12, help='Maximum number of projects displayed on projects page')
    show_testimonials = fields.Boolean(string='Show Client Testimonials Section', default=True, help='Toggle to display or hide the "What Our Clients Say" section on the homepage.')

    # Showcase Video & Content Settings
    showcase_video_file = fields.Binary(string='Vision Showcase Video (MP4)', attachment=True, help='Upload custom MP4 video file for hero showcase')
    showcase_video_filename = fields.Char(string='Video Filename')
    showcase_video_url = fields.Char(string='Video URL / Path', default='/wasm_website/static/src/video/hero_construction.mp4', help='External video URL or default static path')
    showcase_poster = fields.Image(string='Video Poster Cover', max_width=1920, max_height=1080, help='Cover image before video starts')

    # Showcase Content & Text Controls
    showcase_title_ar = fields.Char(string='Showcase Title', default="Building Saudi Arabia's Infrastructure Vision")
    showcase_title_en = fields.Char(string='Showcase Title (English)', default="Building Saudi Arabia's Infrastructure Vision")
    showcase_desc_ar = fields.Text(string='Showcase Description', default='Watch how ARFA SPECIALIZED SYSTEMS executes major structural and commercial development projects adhering to Saudi Building Code and strict quality metrics.')
    showcase_desc_en = fields.Text(string='Showcase Description (English)', default='Watch how ARFA SPECIALIZED SYSTEMS executes major structural and commercial development projects adhering to Saudi Building Code and strict quality metrics.')
    
    showcase_bullet1_ar = fields.Char(string='Bullet 1', default='Execution strictly adhering to Saudi Building Code (SBC 301-306).')
    showcase_bullet1_en = fields.Char(string='Bullet 1 (English)', default='Execution strictly adhering to Saudi Building Code (SBC 301-306).')
    showcase_bullet2_ar = fields.Char(string='Bullet 2', default='Complete MEP engineering: HVAC, fire fighting, and electrical networks.')
    showcase_bullet2_en = fields.Char(string='Bullet 2 (English)', default='Complete MEP engineering: HVAC, fire fighting, and electrical networks.')
    showcase_bullet3_ar = fields.Char(string='Bullet 3', default='Certified team of engineers accredited by the Saudi Council of Engineers.')
    showcase_bullet3_en = fields.Char(string='Bullet 3 (English)', default='Certified team of engineers accredited by the Saudi Council of Engineers.')
    
    showcase_bg_image = fields.Image(string='Showcase Background Image', max_width=1920, max_height=1080)

    # Hero Banner Settings
    hero_title_ar = fields.Char(string='Hero Title', default="Building Saudi Arabia's Infrastructure Vision")
    hero_title_en = fields.Char(string='Hero Title (English)', default="Building Saudi Arabia's Infrastructure Vision")
    hero_bg_image = fields.Image(string='Hero Background Image', max_width=1920, max_height=1080)
    # Company Profile PDF Document
    company_profile_pdf = fields.Binary(string='Company Profile PDF Document', attachment=True, help='Upload official company profile PDF file')
    company_profile_filename = fields.Char(string='Company Profile Filename', default='Arfa_Company_Profile_2026.pdf')

    # Contact Info Settings
    contact_phone = fields.Char(string='Official Phone', default='+966 11 234 5678')
    contact_phone_secondary = fields.Char(string='Mobile / WhatsApp', default='+966 54 543 2343')
    contact_email = fields.Char(string='Official Email', default='info@arfa-sa.com')
    contact_address_ar = fields.Char(string='Address', default='Riyadh - Al Sahafa District - King Fahd Road')
    contact_address_en = fields.Char(string='Address (English)', default='Riyadh - Al Sahafa District - King Fahd Road')
    contact_working_hours_ar = fields.Char(string='Working Hours', default='Sun - Thu: 8:00 AM - 5:00 PM')
    contact_working_hours_en = fields.Char(string='Working Hours (English)', default='Sun - Thu: 8:00 AM - 5:00 PM')

    # Email Server & Notification Settings
    target_notification_email = fields.Char(
        string='البريد المستهدف لاستقبال الإشعارات',
        default='info@arfa-sa.com',
        help='البريد الإلكتروني الذي تصل إليه إشعارات طلبات التسعير والاتصال الجديدة من الموقع الإلكتروني'
    )
    enable_email_notifications = fields.Boolean(
        string='تفعيل إرسال إشعارات البريد للإدارة',
        default=True,
        help='عند التفعيل سيتم إرسال رسالة بريد إلكترونية فورية للبريد المستهدف عند تعبئة أي نموذج'
    )
    enable_customer_confirmation_email = fields.Boolean(
        string='إرسال بريد تأكيد تلقائي للعميل بالرقم المرجعي',
        default=True,
        help='إرسال بريد إلكتروني تلقائي للعميل يتضمن الرقم المرجعي المميز وتأكيد استلام الطلب'
    )

    # Pillar Cards (3 Hero Cards)
    pillar1_img = fields.Image(string='Pillar 1 Image', max_width=1200, max_height=800)
    pillar1_title_ar = fields.Char(string='Pillar 1 Title', default='Structural & Civil Contracting')
    pillar1_title_en = fields.Char(string='Pillar 1 Title (English)', default='Structural & Civil Contracting')
    pillar1_desc_ar = fields.Text(string='Pillar 1 Description', default='Concrete framing, foundations, and heavy structural developments executed strictly to SBC codes.')
    pillar1_desc_en = fields.Text(string='Pillar 1 Description (English)', default='Concrete framing, foundations, and heavy structural developments executed strictly to SBC codes.')
    pillar1_link = fields.Char(string='Pillar 1 URL', default='/services')

    pillar2_img = fields.Image(string='Pillar 2 Image', max_width=1200, max_height=800)
    pillar2_title_ar = fields.Char(string='Pillar 2 Title', default='MEP & Mechanical Systems')
    pillar2_title_en = fields.Char(string='Pillar 2 Title (English)', default='MEP & Mechanical Systems')
    pillar2_desc_ar = fields.Text(string='Pillar 2 Description', default='Advanced HVAC ducting, plumbing, electrical grid infrastructure, and smart automation.')
    pillar2_desc_en = fields.Text(string='Pillar 2 Description (English)', default='Advanced HVAC ducting, plumbing, electrical grid infrastructure, and smart automation.')
    pillar2_link = fields.Char(string='Pillar 2 URL', default='/services')

    pillar3_img = fields.Image(string='Pillar 3 Image', max_width=1200, max_height=800)
    pillar3_title_ar = fields.Char(string='Pillar 3 Title', default='Turnkey Project Delivery')
    pillar3_title_en = fields.Char(string='Pillar 3 Title (English)', default='Turnkey Project Delivery')
    pillar3_desc_ar = fields.Text(string='Pillar 3 Description', default='Comprehensive engineering management, interior fitouts, and end-to-end turnkey delivery.')
    pillar3_desc_en = fields.Text(string='Pillar 3 Description (English)', default='Comprehensive engineering management, interior fitouts, and end-to-end turnkey delivery.')
    pillar3_link = fields.Char(string='Pillar 3 URL', default='/services')

    # Company Statistics (4 Cards)
    stat1_val = fields.Char(string='Stat 1 Value', default='150+')
    stat1_label_ar = fields.Char(string='Stat 1 Label', default='Completed Projects')
    stat1_label_en = fields.Char(string='Stat 1 Label (English)', default='Completed Projects')

    stat2_val = fields.Char(string='Stat 2 Value', default='18+')
    stat2_label_ar = fields.Char(string='Stat 2 Label', default='Years Experience')
    stat2_label_en = fields.Char(string='Stat 2 Label (English)', default='Years Experience')

    stat3_val = fields.Char(string='Stat 3 Value', default='1,200,000+')
    stat3_label_ar = fields.Char(string='Stat 3 Label', default='m² Executed Area')
    stat3_label_en = fields.Char(string='Stat 3 Label (English)', default='m² Executed Area')

    stat4_val = fields.Char(string='Stat 4 Value', default='85+')
    stat4_label_ar = fields.Char(string='Stat 4 Label', default='Engineers & Specialists')
    stat4_label_en = fields.Char(string='Stat 4 Label (English)', default='Engineers & Specialists')

    # Why Choose Us Cards (6 Cards)
    why1_img = fields.Image(string='Why 1 Image', max_width=1200, max_height=800)
    why1_title_ar = fields.Char(string='Why 1 Title', default='SBC Code Compliance')
    why1_title_en = fields.Char(string='Why 1 Title (English)', default='SBC Code Compliance')
    why1_desc_ar = fields.Text(string='Why 1 Description', default='Strict adherence to Saudi Building Code specifications across all concrete structural works.')
    why1_desc_en = fields.Text(string='Why 1 Description (English)', default='Strict adherence to Saudi Building Code specifications across all concrete structural works.')

    why2_img = fields.Image(string='Why 2 Image', max_width=1200, max_height=800)
    why2_title_ar = fields.Char(string='Why 2 Title', default='BIM 3D Project Tech')
    why2_title_en = fields.Char(string='Why 2 Title (English)', default='BIM 3D Project Tech')
    why2_desc_ar = fields.Text(string='Why 2 Description', default='Advanced 3D modeling and clash detection prior to site execution ensuring zero errors.')
    why2_desc_en = fields.Text(string='Why 2 Description (English)', default='Advanced 3D modeling and clash detection prior to site execution ensuring zero errors.')

    why3_img = fields.Image(string='Why 3 Image', max_width=1200, max_height=800)
    why3_title_ar = fields.Char(string='Why 3 Title', default='Owned Heavy Machinery')
    why3_title_en = fields.Char(string='Why 3 Title (English)', default='Owned Heavy Machinery')
    why3_desc_ar = fields.Text(string='Why 3 Description', default='Complete fleet of excavators, cranes, and concrete pumps to accelerate timelines.')
    why3_desc_en = fields.Text(string='Why 3 Description (English)', default='Complete fleet of excavators, cranes, and concrete pumps to accelerate timelines.')

    why4_img = fields.Image(string='Why 4 Image', max_width=1200, max_height=800)
    why4_title_ar = fields.Char(string='Why 4 Title', default='Strict Timelines')
    why4_title_en = fields.Char(string='Why 4 Title (English)', default='Strict Timelines')
    why4_desc_ar = fields.Text(string='Why 4 Description', default='Guaranteed project completion within agreed schedule and transparent budget.')
    why4_desc_en = fields.Text(string='Why 4 Description (English)', default='Guaranteed project completion within agreed schedule and transparent budget.')

    why5_img = fields.Image(string='Why 5 Image', max_width=1200, max_height=800)
    why5_title_ar = fields.Char(string='Why 5 Title', default='Certified Quality Lab')
    why5_title_en = fields.Char(string='Why 5 Title (English)', default='Certified Quality Lab')
    why5_desc_ar = fields.Text(string='Why 5 Description', default='Rigorous core testing and ultrasound concrete strength inspection on site.')
    why5_desc_en = fields.Text(string='Why 5 Description (English)', default='Rigorous core testing and ultrasound concrete strength inspection on site.')

    why6_img = fields.Image(string='Why 6 Image', max_width=1200, max_height=800)
    why6_title_ar = fields.Char(string='Why 6 Title', default='ISO & Site Safety Compliance')
    why6_title_en = fields.Char(string='Why 6 Title (English)', default='ISO & Site Safety Compliance')
    why6_desc_ar = fields.Text(string='Why 6 Description', default='Zero-hazard workplace policies adhering to international safety frameworks.')
    why6_desc_en = fields.Text(string='Why 6 Description (English)', default='Zero-hazard workplace policies adhering to international safety frameworks.')

    # Service Cards (8 Cards matching exact website menu tabs)
    srv1_img = fields.Image(string='Service 1 Image', max_width=1200, max_height=800)
    srv1_title_ar = fields.Char(string='Service 1 Title', default='Modern building systems')
    srv1_title_en = fields.Char(string='Service 1 Title (English)', default='Modern building systems')
    srv1_desc_ar = fields.Text(string='Service 1 Description', default='Advanced modern construction tech, glass facades, prefab steel framing, and turnkey fitouts.')
    srv1_desc_en = fields.Text(string='Service 1 Description (English)', default='Advanced modern construction tech, glass facades, prefab steel framing, and turnkey fitouts.')
    srv1_url = fields.Char(string='Service 1 URL', default='/modern-building-systems')

    srv2_img = fields.Image(string='Service 2 Image', max_width=1200, max_height=800)
    srv2_title_ar = fields.Char(string='Service 2 Title', default='Electromechanical systems')
    srv2_title_en = fields.Char(string='Service 2 Title (English)', default='Electromechanical systems')
    srv2_desc_ar = fields.Text(string='Service 2 Description', default='Design, supply, and installation of power grids, mechanical infrastructure, and sanitary networks.')
    srv2_desc_en = fields.Text(string='Service 2 Description (English)', default='Design, supply, and installation of power grids, mechanical infrastructure, and sanitary networks.')
    srv2_url = fields.Char(string='Service 2 URL', default='/electromechanical-systems')

    srv3_img = fields.Image(string='Service 3 Image', max_width=1200, max_height=800)
    srv3_title_ar = fields.Char(string='Service 3 Title', default='Smart building systems')
    srv3_title_en = fields.Char(string='Service 3 Title (English)', default='Smart building systems')
    srv3_desc_ar = fields.Text(string='Service 3 Description', default='Building automation, smart control panels, security systems, and early warning technology.')
    srv3_desc_en = fields.Text(string='Service 3 Description (English)', default='Building automation, smart control panels, security systems, and early warning technology.')
    srv3_url = fields.Char(string='Service 3 URL', default='/smart-building-systems')

    srv4_img = fields.Image(string='Service 4 Image', max_width=1200, max_height=800)
    srv4_title_ar = fields.Char(string='Service 4 Title', default='Alternative energy solutions')
    srv4_title_en = fields.Char(string='Service 4 Title (English)', default='Alternative energy solutions')
    srv4_desc_ar = fields.Text(string='Service 4 Description', default='Photovoltaic solar energy systems and energy optimization solutions for commercial sectors.')
    srv4_desc_en = fields.Text(string='Service 4 Description (English)', default='Photovoltaic solar energy systems and energy optimization solutions for commercial sectors.')
    srv4_url = fields.Char(string='Service 4 URL', default='/alternative-energy-solutions')

    srv5_img = fields.Image(string='Service 5 Image', max_width=1200, max_height=800)
    srv5_title_ar = fields.Char(string='Service 5 Title', default='Fire protection & prevention systems')
    srv5_title_en = fields.Char(string='Service 5 Title (English)', default='Fire protection & prevention systems')
    srv5_desc_ar = fields.Text(string='Service 5 Description', default='Automatic fire suppression, alarm networks, and civil defense certified pump installations.')
    srv5_desc_en = fields.Text(string='Service 5 Description (English)', default='Automatic fire suppression, alarm networks, and civil defense certified pump installations.')
    srv5_url = fields.Char(string='Service 5 URL', default='/fire-protection-prevention-systems')

    srv6_img = fields.Image(string='Service 6 Image', max_width=1200, max_height=800)
    srv6_title_ar = fields.Char(string='Service 6 Title', default='Medical Gas Systems')
    srv6_title_en = fields.Char(string='Service 6 Title (English)', default='Medical Gas Systems')
    srv6_desc_ar = fields.Text(string='Service 6 Description', default='Design and installation of central medical gas pipelines and operating theatre infrastructure.')
    srv6_desc_en = fields.Text(string='Service 6 Description (English)', default='Design and installation of central medical gas pipelines and operating theatre infrastructure.')
    srv6_url = fields.Char(string='Service 6 URL', default='/medical-gas-systems')

    srv7_img = fields.Image(string='Service 7 Image', max_width=1200, max_height=800)
    srv7_title_ar = fields.Char(string='Service 7 Title', default='Infrastructure Development')
    srv7_title_en = fields.Char(string='Service 7 Title (English)', default='Infrastructure Development')
    srv7_desc_ar = fields.Text(string='Service 7 Description', default='Underground piping, drainage networks, site excavation, and public infrastructure works.')
    srv7_desc_en = fields.Text(string='Service 7 Description (English)', default='Underground piping, drainage networks, site excavation, and public infrastructure works.')
    srv7_url = fields.Char(string='Service 7 URL', default='/infrastructure-development')

    srv8_img = fields.Image(string='Service 8 Image', max_width=1200, max_height=800)
    srv8_title_ar = fields.Char(string='Service 8 Title', default='Planning & Construction')
    srv8_title_en = fields.Char(string='Service 8 Title (English)', default='Planning & Construction')
    srv8_desc_ar = fields.Text(string='Service 8 Description', default='Concrete framing, foundations, and heavy structural developments executed strictly to SBC code.')
    srv8_desc_en = fields.Text(string='Service 8 Description (English)', default='Concrete framing, foundations, and heavy structural developments executed strictly to SBC code.')
    srv8_url = fields.Char(string='Service 8 URL', default='/planning-construction')

    @api.model
    def get_config(self):
        """ Get or create single config record (enforces singleton behavior) """
        configs = self.search([], order='id desc')
        if not configs:
            return self.create({})
        if len(configs) > 1:
            main_config = configs[0]
            configs[1:].unlink()
            return main_config
        return configs[0]

    @api.model
    def action_open_config(self):
        """ Action to open singleton config record directly in backend """
        config = self.get_config()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Website Config & Media Settings',
            'res_model': 'wasm.site.config',
            'res_id': config.id,
            'view_mode': 'form',
            'target': 'current',
        }
