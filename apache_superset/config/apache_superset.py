from __future__ import unicode_literals
from frappe import _

def get_data():
    config = [
        {
            "label": _("Apache Example"),
            "items": [
                {
                    "type": "doctype",
                    "name": "cash purchase",
                    "label": "Cash Purchase Example",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "item purchase",
                    "label": "Item Purchase Example",
                    "onboard": 2,
                }
            ]
        }
    ]
    return config