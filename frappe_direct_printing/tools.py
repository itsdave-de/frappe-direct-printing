import frappe
import cups
import os

# Get a list of printers from cups
@frappe.whitelist()
def get_printer_list():
	try:
		conn = cups.Connection()
		printers = conn.getPrinters()
		return [f"{prt} ({printers[prt]['printer-make-and-model'].split(',')[0]})" for prt in printers]
	except:
		return ['printer not found']


# Print a page test
@frappe.whitelist()
def print_test_page(printer_name):
	try:
		conn = cups.Connection()
		pdf_page = f'{os.getcwd()}/assets/frappe_direct_printing/misc/print_test.pdf'
		options = {}
		print_job_id = conn.printFile(printer_name, pdf_page, "Frappe Print Test Page", options)
		return f"Print job was sent with ID: {print_job_id}"

	except cups.IPPError as e:
		return f"Error sending print job: {e}"
