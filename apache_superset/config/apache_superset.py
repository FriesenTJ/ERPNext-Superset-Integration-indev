from __future__ import unicode_literals
from frappe import _

def get_data():
    config = [
        {
            "label": _("Apache Setup"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Superset Settings",
                    "label": "Superset Settings",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Superset Debug",
                    "label": "Code Debug",
                    "onboard": 1,
                }
            ]
        }
    ]
    return config