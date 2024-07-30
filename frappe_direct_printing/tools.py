import frappe
import cups

# Get a list of printers from cups
@frappe.whitelist()
def get_printer_list():
	try:
		conn = cups.Connection()
		printers = conn.getPrinters()
		return [f"{prt} ({printers[prt]['printer-make-and-model'].split(',')[0]})" for prt in printers]
	except:
		return ['printer not found']
