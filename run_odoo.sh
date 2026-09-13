#!/usr/bin/env bash
export PYTHONPATH="/home/saad/odoo 20/odoo19-community/usr/lib/python3/dist-packages:${PYTHONPATH}"
python3 "/home/saad/odoo 20/odoo19-community/usr/bin/odoo" -c "/home/saad/arfa/odoo19-arfa2026.conf" "$@"
