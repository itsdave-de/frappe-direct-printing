// Copyright (c) 2024, itsdave GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on('Printer', {
    onload: function(frm) {
        frappe.call({
            method: "frappe_direct_printing.frappe_direct_printing.doctype.printer.get_printer_list",
            callback: function(r) {
                if (r.message) {
                    let printer_field = frm.fields_dict['address'];
                    printer_field.df.options = r.message;
                    printer_field.refresh();
                }
            }
        });
    }
});
