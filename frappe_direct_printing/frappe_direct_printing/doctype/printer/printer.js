// Copyright (c) 2024, itsdave GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on('Printer', {
    refresh: function(frm) {
        frm.fields_dict['print_test_page'].input.onclick = function() {
            var printer_name = frm.doc.printer_name;
            frappe.call({
                method: "frappe_direct_printing.tools.print_test_page",
                args: {
                    printer_name: printer_name
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint(r.message);
                    }
                }
            });
        };
    }
});


