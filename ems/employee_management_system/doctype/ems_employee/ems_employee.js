// Copyright (c) 2024, BrainWise and contributors
// For license information, please see license.txt

frappe.ui.form.on('EMS Employee', {
    refresh: function(frm) {
        frm.set_query('ems_department', function() {
            return {
                filters: {
                    company: frm.doc.ems_company 
                }
            };
        });
        if (frm.doc.hired_on) {
            const hiredDate = new Date(frm.doc.hired_on);
            const today = new Date();
            const timeDifference = today - hiredDate; 
            const daysEmployed = Math.floor(timeDifference / (1000 * 60 * 60 * 24));

            frm.fields_dict.days_employed.$wrapper.html(
                `<b>Number of Days Employed:</b> ${daysEmployed}`
            );
        } else {
            frm.fields_dict.days_employed.$wrapper.html(`<b>Hired On:</b> Not Available`);
        }

        frappe.db.count("Project Assigned Employes", {
            filters: {
                assigned_employee: frm.doc.name
            }
        }).then(function(count) {
            frm.fields_dict.number_of_assigned_projects.$wrapper.html(
                `<b>Number of Assigned Projects:</b> ${count}`
            );
        });
    }
});