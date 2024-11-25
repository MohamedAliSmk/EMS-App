import frappe
from frappe import _

"""
APIs:
a. Create a RESTful API that supports all CRUD operations for all models:
    i. Company
        • GET: Retrieve a single company or list all companies
    ii. Department
        • GET: Retrieve a single department or list all departments
    iii. Employee
        • POST: Create a new employee
        • GET: Retrieve a single employee or list all employees
        • PATCH: Update an existing employee
        • DELETE: Delete an employee
    iv. Project (Bonus)
        • POST: Create a new project
        • GET: Retrieve a single project or list all projects
        • PATCH: Update an existing project
        • DELETE: Delete a project
b. Ensure the API handles data securely
c. Ensure the API follows RESTful conventions (e.g., using proper HTTP methods like GET, POST, etc.)
d. If applicable, provide clear documentation on the API endpoints, parameters and expected responses
"""

@frappe.whitelist()
def get_ems_company(company_name=None):
    """
    Retrieve a single company or list all companies.

    Args:
        company_name (str): The name of the company to retrieve (optional).

    Returns:
        dict: A dictionary containing the status and the company data.
    """
    try:
        if company_name:
            # Retrieve a single company
            company = frappe.get_doc("EMS Company", company_name)
            return {"status": "success", "data": company.as_dict()}
        else:
            # List all companies
            companies = frappe.get_all("EMS Company", fields=["name","abbr"])
            return {"status": "success", "data": companies}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Company not found.")}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error Retrieving Company"))
        return {"status": "error", "message": str(e)}

@frappe.whitelist()
def get_ems_department(department_name=None):
    """
    Retrieve a single Department or list all companies.

    Args:
        department_name (str): The name of the Department to retrieve (optional).

    Returns:
        dict: A dictionary containing the status and the Department data.
    """
    try:
        if department_name:
            # Retrieve a single Department
            Department = frappe.get_doc("EMS Department", department_name)
            return {"status": "success", "data": Department.as_dict()}
        else:
            # List all companies
            companies = frappe.get_all("EMS Department", fields=["name","department_name","ems_company"])
            return {"status": "success", "data": companies}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Department not found.")}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error Retrieving Department"))
        return {"status": "error", "message": str(e)}

#Employee
@frappe.whitelist(allow_guest=False)
def create_employee(data):
    """
    Create a new EMS Employee.
    
    Args:
        data (str): JSON string containing employee details.

    Returns:
        dict: The created employee's data.
    """
    try:
        data = frappe.parse_json(data)
        employee = frappe.new_doc("EMS Employee")
        employee.update(data)
        employee.insert()
        frappe.db.commit()
        return {"status": "success", "data": employee.as_dict()}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error Creating Employee"))
        return {"status": "error", "message": str(e)}

@frappe.whitelist(allow_guest=False)
def get_employee(employee_name=None):
    """
    Retrieve a single employee or list all employees.
    
    Args:
        employee_name (str): The unique name of the employee (optional).

    Returns:
        dict: Employee data.
    """
    try:
        if employee_name:
            employee = frappe.get_doc("EMS Employee", employee_name)
            return {"status": "success", "data": employee.as_dict()}
        else:
            employees = frappe.get_all("EMS Employee", fields=["name",
                                                                "workflow_state",
                                                                "email_address",
                                                                "mobile_number",
                                                                "address",
                                                                "designation",
                                                                "ems_company",
                                                                "ems_department",
                                                                "hired_on"
                                        ])
            return {"status": "success", "data": employees}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Employee not found.")}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error Retrieving Employee"))
        return {"status": "error", "message": str(e)}

@frappe.whitelist(allow_guest=False)
def update_employee(employee_name, data):
    """
    Update an existing employee.
    
    Args:
        employee_name (str): The unique name of the employee.
        data (str): JSON string containing updated fields.

    Returns:
        dict: Updated employee data.
    """
    try:
        data = frappe.parse_json(data)
        employee = frappe.get_doc("EMS Employee", employee_name)
        employee.update(data)
        employee.save()
        frappe.db.commit()
        return {"status": "success", "data": employee.as_dict()}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Employee not found.")}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error Updating Employee"))
        return {"status": "error", "message": str(e)}

@frappe.whitelist(allow_guest=False)
def delete_employee(employee_name):
    """
    Delete an existing employee.
    
    Args:
        employee_name (str): The unique name of the employee.

    Returns:
        dict: Success message.
    """
    try:
        frappe.delete_doc("EMS Employee", employee_name)
        frappe.db.commit()
        return {"status": "success", "message": _("Employee deleted successfully.")}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Employee not found.")}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error Deleting Employee"))
        return {"status": "error", "message": str(e)}

# Project
@frappe.whitelist(allow_guest=False)
def create_project(data):
    """
    Create a new EMS Project.
    
    Args:
        data (str): JSON string containing Project details.

    Returns:
        dict: The created Project's data.
    """
    try:
        data = frappe.parse_json(data)
        project = frappe.new_doc("EMS Project")
        project.update(data)
        project.insert()
        frappe.db.commit()
        return {"status": "success", "data": project.as_dict()}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error Creating Project"))
        return {"status": "error", "message": str(e)}

@frappe.whitelist(allow_guest=False)
def get_project(project_name=None):
    """
    Retrieve a single Project or list all Projects.
    
    Args:
        project_name (str): The unique name of the Project (optional).

    Returns:
        dict: project data.
    """
    try:
        if project_name:
            Project = frappe.get_doc("EMS Project", project_name)
            return {"status": "success", "data": Project.as_dict()}
        else:
            Projects = frappe.get_all("EMS Project", fields=["name",
                                                                "description",
                                                                "start_date",
                                                                "end_date",
                                                                "ems_company",
                                                                "ems_department"])
            return {"status": "success", "data": Projects}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Project not found.")}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error Retrieving Project"))
        return {"status": "error", "message": str(e)}

@frappe.whitelist(allow_guest=False)
def update_project(project_name, data):
    """
    Update an existing Project.
    
    Args:
        project_name (str): The unique name of the Project.
        data (str): JSON string containing updated fields.

    Returns:
        dict: Updated Project data.
    """
    try:
        data = frappe.parse_json(data)
        project = frappe.get_doc("EMS Project", project_name)
        project.update(data)
        project.save()
        frappe.db.commit()
        return {"status": "success", "data": project.as_dict()}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Project not found.")}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error Updating Project"))
        return {"status": "error", "message": str(e)}

@frappe.whitelist(allow_guest=False)
def delete_project(project_name):
    """
    Delete an existing Project.
    
    Args:
        project_name (str): The unique name of the Project.

    Returns:
        dict: Success message.
    """
    try:
        frappe.delete_doc("EMS Project", project_name)
        frappe.db.commit()
        return {"status": "success", "message": _("Project deleted successfully.")}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Project not found.")}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error Deleting Project"))
        return {"status": "error", "message": str(e)}


