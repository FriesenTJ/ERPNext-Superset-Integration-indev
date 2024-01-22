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
                }
            ]
        }
    ]
    return config