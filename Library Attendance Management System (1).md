**GIET - Central Library Attendance Management System**

INTRODUCTION

The Library Management System automates attendance recording for students and staff using QR codes and facial recognition technology. It enables efficient library card issuance, accurate attendance logging, and enhanced security, all through a user-friendly interface and streamlined workflows.

OBJECTIVES

- Automate attendance logging for library entry and exit.
- Use QR codes and facial recognition for secure, efficient tracking.
- Provide a user-friendly interface with robust security.
- Generate detailed reports for effective library management.

METHODOLOGY

Software & Hardware Requirements

- **Operating System:** Windows 10 or 11
- **Software:** XAMPP, MySQL Workbench, Python (with libraries: OpenCV, Numpy, PIL, PyAutoGUI, etc.)
- **Hardware:** High-resolution camera for facial recognition

User Roles

- **Admin:** Manages student and staff records, generates attendance reports, and accesses the database.
- **Students:** Logs in and out via facial recognition; a double beep signals login success, while a single beep indicates logout.

System and Design

- Supports QR code generation for library cards.
- Utilizes facial recognition for precise attendance tracking.

IMPLEMENTATION PHASES

1. **System Setup:** Install and configure XAMPP, MySQL, and Python.
1. **Module Development:** Build facial recognition and QR code generation functionalities.
1. **Dashboard & Features:** Develop the admin dashboard, attendance management system, and reporting tools.
1. **Testing & Debugging:** Perform thorough testing and debugging for optimal performance.
1. **Deployment & Presentation:** Deploy the system and present the final project.

INSTALLATION GUIDE

1. **Install XAMPP:** Download and install the XAMPP software.
1. **Project Files:** Copy the project files to “C:\xampp\htdocs”.
1. **MySQL Setup:** Download and install MySQL, including Server, Workbench, and Shell.
1. **Database Initialization:** Import “lib\_data.sql” in MySQL Workbench or run the

   queries from “query.txt”.

5. **Python Libraries:** Install required libraries via pip

   “pip install mysql numpy pillow pyautogui opencv-python-headless winsound”

ADMIN GUIDE

Starting the System

1. **Launch XAMPP:** Open the XAMPP Control Panel and start the Apache module.
1. **Access the System:** Open a browser and navigate to “localhost/odugu/”.

Managing Attendance

1. **Admin Dashboard:** Log in with admin credentials to access the dashboard, view attendance logs, and export reports in Excel format.
1. **Database Management:** Add, update, or delete student profiles as needed, and manage suspensions.

BUDGET OVERVIEW

Justification for Equipment

- **Camera:** Essential for precise facial recognition (**5k**).
- **Workstation Setup:** Includes hardware and peripherals necessary for system operation (**3k**).

Software Costs

**Python Libraries, MySQL, QR Code Tools:** Open-source, no cost.

FEATURES AND ADDITIONAL DETAILS

- **Real-Time Display:** A live clock on the admin dashboard for tracking attendance.
- **Database Management:** Admins can view and manage student profiles, including departmental details and suspension status.
- **Student Profile Management:** Options to update details, manage suspensions, and delete profiles.
- **Report Generation:** Ability to export attendance reports.

TEAM CONTRIBUTIONS (Final year - IT)

- **Mohanraj S:** System Interface and Design.
- **Rajkumar K:** Development and Testing.
- **Rajan N:** Database Management.
- **Rishi Kanna S:** Algorithms and Error Handling

CONCLUSION

The Library Management System optimizes library operations with automated QR code and facial recognition attendance, delivering a secure, efficient, and user-friendly solution for streamlined administration and effective work management.
