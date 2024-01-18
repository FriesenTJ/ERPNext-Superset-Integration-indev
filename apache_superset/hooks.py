# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "apache_superset"
app_title = "Apache Superset"
app_publisher = "Friesen Tjou Jazernicky"
app_description = "Integration between ERPNext and Apache Superset"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "friesen.tjou@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/apache_superset/css/apache_superset.css"
# app_include_js = "/assets/apache_superset/js/apache_superset.js"

# include js, css files in header of web template
# web_include_css = "/assets/apache_superset/css/apache_superset.css"
# web_include_js = "/assets/apache_superset/js/apache_superset.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "apache_superset.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "apache_superset.install.before_install"
# after_install = "apache_superset.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "apache_superset.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doctype_js = {
    # 'Work Order':'public/js/work_order.js',
    # 'Purchase Order':'public/js/purchase_order.js',
    # 'Sales Order':'public/js/sales_order.js',
    # 'Bin':'public/js/bin.js',
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"apache_superset.tasks.all"
# 	],
# 	"daily": [
# 		"apache_superset.tasks.daily"
# 	],
# 	"hourly": [
# 		"apache_superset.tasks.hourly"
# 	],
# 	"weekly": [
# 		"apache_superset.tasks.weekly"
# 	]
# 	"monthly": [
# 		"apache_superset.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "apache_superset.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "apache_superset.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "apache_superset.task.get_dashboard_data"
# }

