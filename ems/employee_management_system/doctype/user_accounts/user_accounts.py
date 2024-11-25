# Copyright (c) 2024, BrainWise and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class UserAccounts(Document):
    def before_insert(self):
        #set user name based on first (its mandatory) middle and last name
        # and if username is not unique, genrate a custom username
        name_parts = filter(None, [self.first_name, self.middle_name, self.last_name])
        base_user_name = " ".join(name_parts)


        self.user_name = self._generate_unique_username(base_user_name)
    
    def _generate_unique_username(self, base_user_name):
        """
        Generate a unique username by appending a counter if necessary.
        """
        username = base_user_name
        counter = 1
        while frappe.db.exists("User Accounts", {"user_name": username}):
            username = f"{base_user_name}-{counter}"
            counter += 1
        return username