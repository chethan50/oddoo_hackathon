# Odoo Legal Case Management (Community, Odoo 18)

This module provides a minimal, clean, and testable application for managing legal cases within Odoo. Designed for Odoo 18, it handles core legal office tasks, including client and lawyer management, case registration, hearing scheduling, document handling, and fixed-fee invoicing.

### **Key Features**

* **Client & Lawyer Management**: Use boolean flags on partners for easy identification and filtering.
* **Case Registration**: Create cases with a unique sequence (`CASE/YYYY/SEQ`) and a simple lifecycle (Intake, Active, Closed).
* **Hearing & Sitting Calendar**: Plan and track hearings with a dedicated calendar view.
* **Document Management**: Attach documents to cases via the chatter. A smart button provides quick access to all linked files.
* **Fixed-Fee Invoicing**: Generate a draft invoice with a single click, using a pre-defined fixed fee amount from the case.
* **Simple Reporting**: Print a `Case Summary` PDF report for each case and export case lists.

---

### **Installation**

1. Install Prerequisites:
	•	Download and install Git: https://git-scm.com/downloads
	•	Download and install Docker Desktop: https://www.docker.com/products/docker-desktop/
2.	Clone the repository:git clone https://github.com/chethan50/oddoo_hackathon.git
3.	Go to the project folder:cd odoo_hackathon
4.	Start Odoo with Docker Compose:docker-compose up -d
5.	Open Odoo in your browser:http://localhost:8069
6.	6. Create a New Database:
	•	Click “Create Database.”
	•	Check the Demo data box to load sample data.
7. Install the Module:
	•	Go to Apps → Update Apps List.
	•	Search for Legal Case Management.
	•	Click Install.


---

### **Configuration**

* **User Roles**: The module uses two basic roles: **Legal User** (restricted access) and **Legal Manager** (full access).
* **Partners**: Go to **Contacts** and flag partners as **Lawyers** or **Clients**.
* **Invoicing**: Ensure a product named **"Legal Services"** exists in your accounting app for invoicing.

---

### **Usage**

1. Access the application via the new top-level menu named "Legal."
2. Create a case by navigating to Legal > Cases and clicking the Create button.
3. Manage hearings and attach documents from the form view of an individual case.
4. Print a "Case Summary" PDF report from the Print menu on a case record

---

### **Authors**
**Light Code**:
* Deeksha S J
* Chethan P
* Sanjay N 
* Bhargav M

---

### **License**

This module is licensed under the **AGPL-3**.
