from __future__ import unicode_literals
from frappe import _

def get_data():
    config = [
        {
            "label": _("Apache Dashboard"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Superset Dashboard",
                    "label": "Superset Dashboard",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Dashboard Settings",
                    "label": "Dashboard Settings",
                    "onboard": 1,
                }
            ]
        }
    ]
    return config