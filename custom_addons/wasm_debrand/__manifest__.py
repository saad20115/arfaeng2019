# -*- coding: utf-8 -*-
{
    'name': 'Wasm Debranding & White Label - إخفاء العلامة التجارية لشركة وسم',
    'summary': 'Remove Odoo branding, "Powered by Odoo" footer, and white-label website & backend interfaces',
    'description': """
Wasm Debranding & White Label Module
=====================================
- Removes "Powered by Odoo" / "مشغل بواسطة Odoo" from website & portal footers.
- Customizes website footer copyright to Wasm General Contracting Co.
- Removes Odoo branding from backend login screen.
- Replaces browser tab title suffixes with company brand.
    """,
    'author': 'Wasm General Contracting Co.',
    'website': 'https://wasm-contracting.com',
    'category': 'Website/Customization',
    'version': '19.0.1.0.0',
    'depends': ['base', 'web', 'website'],
    'data': [
        'views/wasm_debrand_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'wasm_debrand/static/src/css/wasm_debrand.css',
        ],
        'web.assets_backend': [
            'wasm_debrand/static/src/css/wasm_debrand.css',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
