# -*- coding: utf-8 -*-
# Copyright (c) 2023, Richard and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe,json
from frappe.model.document import Document

class SupersetDebug(Document):
	pass

@frappe.whitelist()
def button1Clicked(doc):
	print("Hello")
	print(doc)