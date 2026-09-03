# Test Plan — [Demo E-Commerce Site Name]

**Project:** Week 2 Mini Project — End-to-End E-Commerce Testing
**Tester:** Soumya Kanti Hazra
**Date:** [start date]
**Site under test:** [URL, e.g. saucedemo.com / demoblaze.com]

---

## 1. Objective
Perform end-to-end functional testing of the demo e-commerce site to identify, log, and track defects through their full lifecycle, and summarize quality findings in a final report.

## 2. Scope

### In Scope
- User registration / login / logout
- Product search and filtering
- Product detail page
- Cart (add, update quantity, remove)
- Checkout flow (address, payment, order confirmation)
- Account/profile management
- Basic responsive/cross-browser checks

### Out of Scope
- Backend/API testing
- Performance/load testing
- Payment gateway's actual transaction processing (use test/sandbox mode)

## 3. Test Approach
- Manual functional testing (positive + negative test cases)
- Exploratory testing on high-risk areas (checkout, payments, auth)
- Boundary and negative-input testing (empty fields, special characters, large inputs, script injection)
- Cross-browser spot-check (Chrome, Firefox, at least one more)

## 4. Environment
| Item | Detail |
|---|---|
| Browsers | Chrome [version], Firefox [version] |
| OS | Windows 11 / macOS [version] |
| Test data | [test accounts / sample products used] |
| Tools | Jira (bug tracking), [browser dev tools, Postman if used] |

## 5. Entry Criteria
- Site is accessible and stable
- Test cases are written and reviewed
- Jira project is set up with severity/priority fields

## 6. Exit Criteria
- All planned test cases executed
- 15+ bugs logged with severity/priority
- No open Critical-severity bugs remain untriaged
- Test summary report completed

## 7. Test Deliverables
- This Test Plan
- Test case list
- Bug Tracker (Jira export / spreadsheet)
- Test Summary Report

## 8. Risks & Assumptions
- Demo site data may reset periodically, affecting repeatability of some test cases
- No real payment processing — checkout tested up to confirmation step only
- [add more as you go]

## 9. Schedule
| Phase | Duration |
|---|---|
| Test planning & case design | Day 1 |
| Test execution & bug logging | Day 2–4 |
| Retesting fixed bugs | Day 5 |
| Summary report | Day 6 |
