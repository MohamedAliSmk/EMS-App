# Copyright (c) 2024, BrainWise and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EMSDepartment(Document):
	def before_insert(self):
		self.department = f"{self.department_name} - {self.company_abbr}"
