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
	
@frappe.whitelist()
def button2Clicked():
	settingsDoc = frappe.get_doc("Superset Settings")
	print(settingsDoc)

	name = settingsDoc.username
	password = settingsDoc.password
	print(name, password)
	
@frappe.whitelist()
def button3Clicked(doc):
	txt = "I am Groot"

	thisDoc = frappe.get_doc("Superset Debug")
	print(thisDoc)
	thisDoc.update({
		'text_field_1': txt
	})
	thisDoc.save()