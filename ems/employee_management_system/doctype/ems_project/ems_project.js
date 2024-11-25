// Copyright (c) 2024, BrainWise and contributors
// For license information, please see license.txt

frappe.ui.form.on('EMS Project', {
    refresh: function(frm) {
        frm.set_query('ems_department', function() {
            return {
                filters: {
                    company: frm.doc.ems_company 
                }
            };
        });
        frm.set_query("assigned_employee", "assigned_employees", function (doc, cdt, cdn) {
            return {
              "filters": {
                "ems_company": frm.doc.ems_company,
                "ems_department":frm.doc.ems_department
              },
            };
        });
    }
});
