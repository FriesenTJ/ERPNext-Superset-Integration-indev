from __future__ import unicode_literals
from apache_superset import _

def get_data():
    config = [
        {
            "label": _("Hello"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Superset Example",
                    "label": "Superset Example",
                    "onboard": 1,
                }
            ]
        }
    ]
    return config