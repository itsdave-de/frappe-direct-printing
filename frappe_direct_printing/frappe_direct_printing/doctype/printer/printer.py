# Copyright (c) 2024, itsdave GmbH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import cups

class Printer(Document):
	pass

# Get a list of printers from cups
@frappe.whitelist()
def get_printer_list():
	try:
		conn = cups.Connection()
		printers = conn.getPrinters()
		return [f"{prt} ({printers[prt]['printer-make-and-model'].split(',')[0]})" for prt in printers]
	except:
		return ['printer not found']
