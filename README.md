# Odoo Legal Case Management (Community, Odoo 18)

This module provides a minimal, clean, and testable application for managing legal cases within Odoo. It's designed to handle core legal office tasks, including client and lawyer management, case registration, hearing scheduling, document handling, and fixed-fee invoicing.

### **Key Features**

* **Client & Lawyer Management**: Use boolean flags on partners for easy identification and filtering.
* **Case Registration**: Create cases with a unique sequence (`CASE/YYYY/SEQ`) and a simple lifecycle (Intake, Active, Closed).
* **Hearing & Sitting Calendar**: Plan and track hearings with a dedicated calendar view.
* **Document Management**: Attach documents to cases via the chatter. A smart button provides quick access to all linked files.
* **Fixed-Fee Invoicing**: Generate a draft invoice with a single click, using a pre-defined fixed fee amount from the case.
* **Simple Reporting**: Print a `Case Summary` PDF report for each case and export case lists.

---

### **Installation**

1.  Place this module in your Odoo custom addons path.
2.  Install the required dependencies: `base`, `mail`, `account`, and `calendar`.
3.  Go to **Apps**, click **"Update Apps List"**, and then search for and install **"Legal Case Management"**.

---

### **Configuration**

* **User Roles**: The module uses two basic roles: **Legal User** (restricted access) and **Legal Manager** (full access).
* **Partners**: Go to **Contacts** and flag partners as **Lawyers** or **Clients**.
* **Invoicing**: Ensure a product named **"Legal Services"** exists in your accounting app for invoicing.

---

### **Usage**

1.  Access the module via the new top-level **"Legal"** menu.
2.  Create a case under **Legal > Cases**.
3.  Add hearings from the case form or the **Legal > Hearings** calendar.
4.  Attach documents using the **chatter** on the case form.
5.  Click the **"Create Invoice"** button on the case form to generate a draft invoice.
6.  Print a **"Case Summary"** PDF from the print actions on a case record.

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
