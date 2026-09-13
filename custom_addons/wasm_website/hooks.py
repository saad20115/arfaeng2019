# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID

def post_init_hook(env):
    """
    Hook to clean up website menus and create standard, non-duplicated,
    bilingual navigation menus (Arabic & English) for Wasm Contracting Co.
    """
    WebsiteMenu = env['website.menu']
    
    # 1. Unlink unwanted default menus (/shop, /jobs, /contactus) and children of top menus
    top_menus = WebsiteMenu.search([('parent_id', '=', False)])
    for tm in top_menus:
        children = WebsiteMenu.search([('parent_id', '=', tm.id)])
        children.unlink()
        
    unwanted = WebsiteMenu.search([('url', 'in', ['/shop', '/jobs', '/contactus', '/blog', '/event'])])
    unwanted.unlink()

    top_menu = WebsiteMenu.search([('website_id', '=', 1), ('parent_id', '=', False)], limit=1)
    if not top_menu:
        top_menu = WebsiteMenu.search([('parent_id', '=', False)], limit=1)
        
    if top_menu:
        top_level_menus = [
            ({'en_US': 'HOME'}, '/', 10),
            ({'en_US': 'ABOUT US'}, '/about-us', 20),
            ({'en_US': 'SERVICES'}, '#', 30),
            ({'en_US': 'PROJECTS'}, '/projects', 40),
            ({'en_US': 'OUR COMPANY'}, '/our-company', 50),
            ({'en_US': 'NEWS'}, '/blog/2', 60),
            ({'en_US': 'CONTACT US'}, '/contactus', 70),
        ]

        services_sub_menus = [
            ({'en_US': 'Modern building systems'}, '/modern-building-systems', 10),
            ({'en_US': 'Electromechanical systems'}, '/electromechanical-systems', 20),
            ({'en_US': 'Smart building systems'}, '/smart-building-systems', 30),
            ({'en_US': 'Alternative energy solutions'}, '/alternative-energy-solutions', 40),
            ({'en_US': 'Fire protection & prevention systems'}, '/fire-protection-prevention-systems', 50),
            ({'en_US': 'Medical Gas Systems'}, '/medical-gas-systems', 60),
            ({'en_US': 'Infrastructure Development'}, '/infrastructure-development', 70),
            ({'en_US': 'Planning & Construction'}, '/planning-construction', 80),
        ]
        
        services_menu = False
        for name_dict, url, seq in top_level_menus:
            m = WebsiteMenu.create({
                'name': name_dict,
                'url': url,
                'sequence': seq,
                'parent_id': top_menu.id,
                'website_id': 1,
            })
            if name_dict.get('en_US') == 'SERVICES':
                services_menu = m

        if services_menu:
            for name_dict, url, seq in services_sub_menus:
                WebsiteMenu.create({
                    'name': name_dict,
                    'url': url,
                    'sequence': seq,
                    'parent_id': services_menu.id,
                    'website_id': 1,
                })
