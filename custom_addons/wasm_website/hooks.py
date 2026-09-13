# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID

def post_init_hook(env):
    """
    Hook to clean up website menus and create standard, non-duplicated,
    bilingual navigation menus (Arabic & English) for Wasm Contracting Co.
    """
    WebsiteMenu = env['website.menu']
    
    # 1. Unlink specific unwanted default menus without destroying other apps' menus
    unwanted = WebsiteMenu.search([('url', 'in', ['/shop', '/jobs', '/contactus', '/blog', '/event'])])
    unwanted.unlink()

    top_menu = WebsiteMenu.search([('website_id', '=', 1), ('parent_id', '=', False)], limit=1)
    if not top_menu:
        top_menu = WebsiteMenu.search([('parent_id', '=', False)], limit=1)
        
    if top_menu:
        top_level_menus = [
            ('الرئيسية', '/', 10),
            ('عن الشركة', '/about', 20),
            ('خدماتنا', '/services', 30),
            ('مشاريعنا', '/projects', 40),
            ('أقسام الشركة', '/contact-team', 50),
            ('طلب عرض سعر', '/quote', 60),
            ('تواصل معنا', '/contactus', 70),
        ]

        services_sub_menus = [
            ('أنظمة البناء الحديثة', '/services#modern-building', 10),
            ('أنظمة الكهروميكانيك MEP', '/services#mep', 20),
            ('المباني الذكية BMS', '/services#smart-building', 30),
            ('حلول الطاقة البديلة', '/services#energy', 40),
            ('أنظمة الإطفاء والوقاية من الحريق', '/services#fire', 50),
            ('أنظمة الغازات الطبية', '/services#medical-gas', 60),
            ('تطوير البنية التحتية', '/services#infrastructure', 70),
        ]
        
        services_menu = False
        for name, url, seq in top_level_menus:
            m = WebsiteMenu.create({
                'name': name,
                'url': url,
                'sequence': seq,
                'parent_id': top_menu.id,
                'website_id': 1,
            })
            if name == 'خدماتنا':
                services_menu = m

        if services_menu:
            for name, url, seq in services_sub_menus:
                WebsiteMenu.create({
                    'name': name,
                    'url': url,
                    'sequence': seq,
                    'parent_id': services_menu.id,
                    'website_id': 1,
                })
