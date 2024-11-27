# Employee Management System – Back End

## Project Description
The **Employee Management System (EMS)** is a backend application designed to facilitate the management of companies, departments, employees, and projects. The system provides Create, Read, Update, and Delete (CRUD) functionality for each entity, alongside workflows for handling the onboarding process of employees and role-based access control (RBAC) for secure data handling.

### Key Features
- **Comprehensive Management**: Handle Companies, Departments, Employees, and Projects effectively.
- **Automatic Calculations**: Automate metrics like department count, employee count, and project assignments.
- **Input Validation**: Validate email and mobile formats.
- **Cascading Logic**: Manage dependencies between entities during updates or deletions.
- **Secure Access Control**: Role-based access control (RBAC) for user permissions.
- **Onboarding Workflows**: Customizable transitions for employee onboarding.
- **Enterprise-Ready**: Scalable, secure, and adheres to real-world enterprise needs.

---

## Prerequisites for Installation

To set up this system on your local machine using Docker, ensure the following prerequisites are met:

### 1. **Docker and Docker Compose**
- Install Docker: [Docker Official Website](https://www.docker.com/)
- Install Docker Compose (usually included with Docker Desktop).

Verify installation with:

```bash
docker --version
docker-compose --version
```
## 2. System Requirements

### Minimum Requirements:
- **RAM**: 4GB
- **CPU**: 2 cores
- **Supported Operating Systems**: Windows, macOS, or Linux
---

## Installation Steps
### Step 1: Clone the Frappe Docker Repository
```bash
git clone https://github.com/frappe/frappe_docker.git
cd frappe_docker
```

### Step 2: Edit docker-compose.override.yml
Add your custom app to the docker-compose.override.yml file. Below is an example configuration to include your app:

```docker
version: "3.7"
services:
backend:
volumes:
- ./apps:/workspace/development/apps
```

Ensure you replace ./apps with the correct path to your custom app if necessary.

### Step 3: Run the Docker Setup
Build and start the Docker containers:
```bash
docker-compose up -d
```

Wait for 5 minutes for ERPNext site to be created or check create-site container logs before opening browser on port 8080. (username: Administrator, password: admin)

If you ran in a Dev Docker environment, to view container logs: docker compose -f pwd.yml logs -f create-site. Don't worry about some of the initial error messages, some services take a while to become ready, and then they go away.

### Step 4: Install the Custom App on Your Site
Once the containers are running, follow these steps to install your custom app:

Access the backend container:
```bash
docker exec -it frappe_docker-backend-1 /bin/bash
```

Get your custom app from the repository:
```bash
bench get-app ems https://github.com/MohamedAliSmk/EMS-App.git
```
Install the app on your site:
```bash
bench --site site-name install-app ems
```
Replace site-name with the name of your site.

## API Documentation
Check the postman_collection.json file for all the available API endpoints.

Create Employee<br>
Description: Creates a new employee record.<br>
Method: `POST`<br>
Endpoint: `{{base_url}}/api/resource/EMS Employee`<br>

Authorization:<br>
Key: `Authorization`<br>
Value: `token {{api_token}}:{{api_secret}}`<br>
Request Body:<br>
Content-Type: application/json<br>
```json
{
    "employee_name": "Mohamed Ali",
    "email_address": "mohamedali@gmail.com",
    "address": "123cairo",
    "designation": "software engineer",
    "ems_company": "Apple",
    "ems_department": "Development - AAP"
}
```
Expected Response:<br>
Status: 201 Created<br>
Response Body:<br>
```json
{
    "data": {
        "name": "Mohamed Ali",
        "owner": "Administrator",
        "creation": "2024-11-27 20:08:06.441083",
        "modified": "2024-11-27 20:08:06.441083",
        "modified_by": "Administrator",
        "docstatus": 0,
        "idx": 0,
        "workflow_state": "Application Received",
        "employee_name": "Mohamed Ali",
        "email_address": "mohamedali@gmail.com",
        "address": "123cairo",
        "designation": "software engineer",
        "ems_company": "Apple",
        "ems_department": "Development - AAP",
        "number_of_assigned_projects": 0,
        "days_employed": 0,
        "doctype": "EMS Employee"
    }
}
```
Thanks<br>
Mohamed Ali
