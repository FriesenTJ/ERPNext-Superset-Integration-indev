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
                }
            ]
        },
    ]
    return config