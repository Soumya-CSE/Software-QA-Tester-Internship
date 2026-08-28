# OrangeHRM Mini Project — Week 1

## 📌 Project Overview

This project focuses on performing complete **manual testing** of the OrangeHRM demo web application.

The objective is to practice real-world Software Quality Assurance (QA) activities, including test planning, test case design, test execution, defect reporting, screenshot documentation, and Requirements Traceability Matrix (RTM) preparation.

---

## 🎯 Project Objectives

* Create a detailed Test Plan.
* Design and document **30+ manual test cases**.
* Execute the test cases on the OrangeHRM application.
* Identify and document actual software defects.
* Assign appropriate severity and priority to defects.
* Capture screenshots as bug evidence.
* Maintain an RTM to ensure requirement coverage.
* Understand the complete manual testing workflow.

---

## 🧪 Application Under Test

**Application:** OrangeHRM Demo

**Testing Type:** Manual Testing

**Testing Approach:** Functional, UI, Negative, Boundary, Regression, and Exploratory Testing

---

## 📋 Modules Covered

The following application modules are included in the testing scope:

* Login
* Dashboard
* Employee Management
* Employee Search
* Add Employee
* Edit Employee
* Delete Employee
* Leave Management
* Logout

---

## 📁 Project Structure

```text
05-OrangeHRM-Mini-Project/
│
├── README.md
│
├── Test-Plan/
│   └── OrangeHRM_Test_Plan.docx
│
├── Test-Scenarios/
│   └── OrangeHRM_Test_Scenarios.xlsx
│
├── Test-Cases/
│   └── OrangeHRM_Test_Cases.xlsx
│
├── Test-Execution/
│   └── OrangeHRM_Test_Execution.xlsx
│
├── Bug-Reports/
│   └── OrangeHRM_Bug_Reports.xlsx
│
├── Screenshots/
│   ├── BUG-ORH-001.png
│   ├── BUG-ORH-002.png
│   └── ...
│
└── RTM/
    └── OrangeHRM_RTM.xlsx
```

---

## 📝 Test Plan

The Test Plan defines the overall testing strategy and includes:

* Project Objective
* Scope
* Testing Approach
* Testing Types
* Modules Covered
* Test Environment
* Entry Criteria
* Exit Criteria
* Test Deliverables
* Risks and Assumptions

---

## ✅ Test Cases

More than **30 test cases** are designed to cover positive, negative, boundary, and functional testing scenarios.

Each test case contains:

* Test Case ID
* Module
* Test Scenario
* Test Case Description
* Preconditions
* Test Steps
* Test Data
* Expected Result
* Actual Result
* Status
* Bug ID

### Test Case Distribution

| Module              | Test Cases |
| ------------------- | ---------: |
| Login               |          7 |
| Dashboard           |          4 |
| Employee Management |         10 |
| Employee Search     |          4 |
| Leave Management    |          5 |
| Logout              |          2 |
| **Total**           |    **32+** |

---

## ▶️ Test Execution

All test cases are executed manually against the OrangeHRM application.

Test results are recorded using:

* **PASS** — Actual result matches expected result.
* **FAIL** — Actual result does not match expected result.
* **BLOCKED** — Testing cannot continue because of a blocking issue.
* **NOT EXECUTED** — Test case has not yet been executed.

Failed test cases are linked to their corresponding Bug IDs.

---

## 🐞 Bug Reporting

Defects discovered during testing are documented in the Bug Reports section.

Each bug report contains:

* Bug ID
* Bug Title
* Module
* Severity
* Priority
* Preconditions
* Steps to Reproduce
* Expected Result
* Actual Result
* Status
* Screenshot

### Bug Severity

| Severity | Description                                               |
| -------- | --------------------------------------------------------- |
| Critical | Application or major functionality is completely unusable |
| High     | Major functionality is significantly affected             |
| Medium   | Functionality is affected but a workaround may exist      |
| Low      | Minor UI or functional issue                              |

### Bug Priority

| Priority | Description                                     |
| -------- | ----------------------------------------------- |
| High     | Should be fixed immediately                     |
| Medium   | Should be fixed in the normal development cycle |
| Low      | Can be fixed later                              |

---

## 📸 Screenshot Evidence

Screenshots are stored separately and linked to the corresponding Bug IDs.

Example:

```text
Screenshots/
├── BUG-ORH-001.png
├── BUG-ORH-002.png
├── BUG-ORH-003.png
└── ...
```

Screenshots provide visual evidence of the actual defect observed during testing.

---

## 🔗 Requirements Traceability Matrix

The RTM establishes traceability between requirements, test cases, test execution results, and defects.

```text
Requirement
     ↓
Test Case
     ↓
Test Execution
     ↓
PASS / FAIL
     ↓
Bug ID
```

Example:

| Requirement ID | Requirement                              | Test Case ID | Status | Bug ID      |
| -------------- | ---------------------------------------- | ------------ | ------ | ----------- |
| ORH-REQ-001    | User should be able to login             | TC-LOGIN-001 | PASS   | —           |
| ORH-REQ-002    | Admin should be able to add employee     | TC-EMP-001   | PASS   | —           |
| ORH-REQ-003    | Admin should be able to search employees | TC-EMP-002   | FAIL   | BUG-ORH-001 |

---

## 🔄 Testing Workflow

```text
Requirement Analysis
        ↓
Test Planning
        ↓
Test Scenario Creation
        ↓
Test Case Design
        ↓
Test Execution
        ↓
Pass / Fail
        ↓
Defect Reporting
        ↓
Screenshot Evidence
        ↓
RTM Update
        ↓
Test Summary
```

---

## 🛠️ Tools Used

* OrangeHRM Demo Application
* Microsoft Excel
* Microsoft Word
* Web Browser
* Git
* GitHub
* Screenshot Tool

---

## 📊 Project Deliverables

| Deliverable    | File/Folder       |
| -------------- | ----------------- |
| Test Plan      | `Test-Plan/`      |
| Test Scenarios | `Test-Scenarios/` |
| 30+ Test Cases | `Test-Cases/`     |
| Test Execution | `Test-Execution/` |
| Bug Reports    | `Bug-Reports/`    |
| Bug Evidence   | `Screenshots/`    |
| RTM            | `RTM/`            |

---

## 📌 Project Status

**Status:** In Progress

This project will be updated as test cases are executed and additional defects are identified.

---

## 👨‍💻 Author

**Soumya Kanti Hazra**

Computer Science & Engineering
Manual QA Testing / Software Testing
