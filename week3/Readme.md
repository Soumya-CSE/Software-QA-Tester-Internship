# 🤖 WEEK 3 — AUTOMATION & API TESTING

QA Tester study materials and hands-on practice for **Week 3**, focusing on **Selenium WebDriver automation, web element locators, automated test scripts, and REST API testing with Postman**.

## 📚 STUDY RESOURCES

* Introduction to **Selenium WebDriver & Test Automation**
* Locating Web Elements — **ID, Name, CSS Selector & XPath**
* Writing Automated Test Scripts using **Python / Java**
* WebDriver Waits — Implicit, Explicit & Expected Conditions
* API Testing with **Postman**
* REST API Methods — **GET, POST, PUT & DELETE**
* API Response Validation — Status Codes, Headers & Response Body

## 🎯 TOPIC FOCUS

### **Automation & API Testing**

Learning how to automate repetitive web application test scenarios using Selenium and validate REST APIs using Postman.

## ✅ PRACTICE TASKS

* [ ] Set up **Selenium WebDriver** and automate login on a demo website
* [ ] Practice locating elements using **ID, CSS Selector and XPath**
* [ ] Write **5 automated test scripts** for form validation
* [ ] Implement appropriate **explicit waits** in Selenium tests
* [ ] Test **3 REST APIs** using Postman
* [ ] Validate status codes, response body, headers and key response values
* [ ] Create a **Postman Collection**
* [ ] Use **environment variables** for base URL and authentication data

## 🚀 MINI PROJECT — WEEK 3

### **End-to-End Web Automation & API Testing**

Automate and test a demo web application:

1. Automate **10 critical test scenarios** using Selenium

   * Login
   * Logout
   * Search
   * Product selection
   * Add to cart
   * Remove from cart
   * Checkout
   * Form validation
   * Invalid login
   * Session/logout validation

2. Test **5 REST APIs** using Postman

3. Validate status codes and response data

4. Create a reusable **Postman Collection**

5. Configure **environment variables**

6. Export the Postman Collection and environment

7. Document automation results and API test results

## 🛠️ TOOLS & TECHNOLOGIES

* **Selenium WebDriver** — Web Automation
* **Python / Java** — Automation Programming
* **Postman** — API Testing
* **Chrome / Edge DevTools** — Element Inspection
* **Git & GitHub** — Version Control & Project Documentation

## 📌 AUTOMATION BEST PRACTICES

* Prefer stable locators such as **ID** and reliable **CSS selectors** where available.
* Use **XPath** when elements cannot be reliably located using simpler strategies.
* Avoid hard-coded delays such as excessive `sleep()` usage; prefer **explicit waits**.
* Keep test scripts **reusable, readable and maintainable**.
* Use assertions to verify expected results.
* Separate test data and configuration from automation logic where possible.

## 🌐 API TESTING CHECKLIST

For every API request, verify:

* **HTTP Method**
* **Status Code**
* **Response Body**
* **Response Headers**
* **Response Time**
* **Required Fields**
* **Data Types**
* **Expected Values**
* **Error Responses**

Example:

**GET Request → 200 OK → Validate JSON Structure → Validate Required Fields → Validate Values**

## 🔐 POSTMAN BEST PRACTICES

Use **environment variables** instead of hardcoding values such as:

* `{{base_url}}`
* `{{auth_token}}`
* `{{user_id}}`

This makes the collection reusable across different environments such as **Development, Testing and Production**.

## 📊 WEEK 3 DELIVERABLES

By the end of Week 3, the following should be completed:

* ✅ Selenium WebDriver Setup
* ✅ 5 Form Validation Automation Scripts
* ✅ 10 End-to-End Automated Test Scenarios
* ✅ Selenium Locator Practice
* ✅ Explicit Wait Implementation
* ✅ 5 API Test Cases
* ✅ Postman Collection
* ✅ Postman Environment Variables
* ✅ API Response Validation
* ✅ Exported Postman Collection & Environment
* ✅ Automation & API Test Execution Report

## 🎯 WEEK 3 GOAL

> **Learn to automate critical web application scenarios and perform structured REST API testing using Selenium and Postman.**

