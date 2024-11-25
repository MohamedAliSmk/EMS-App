// Copyright (c) 2024, BrainWise and contributors
// For license information, please see license.txt
frappe.ui.form.on("EMS Company", {
    refresh(frm) {
        frappe.db.count("EMS Department", {
            filters: {
                ems_company: frm.doc.name
            }
        }).then(function(count) {
            frm.fields_dict.number_of_departments.$wrapper.html(`<b>Number of Departments:</b> ${count}`);
        });

        frappe.db.count("EMS Employee", {
            filters: {
                ems_company: frm.doc.name
            }
        }).then(function(count) {
            frm.fields_dict.number_of_employees.$wrapper.html(`<b>Number of Employees:</b> ${count}`);
        });

        frappe.db.count("EMS Project", {
            filters: {
                ems_company: frm.doc.name
            }
        }).then(function(count) {
            frm.fields_dict.number_of_projects.$wrapper.html(`<b>Number of Projects:</b> ${count}`);
        });
    }
});
