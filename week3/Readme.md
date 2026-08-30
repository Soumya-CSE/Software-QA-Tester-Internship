# Week 3 — Automation & API Testing

QA Tester study materials and hands-on practice for Week 3, covering Selenium WebDriver automation and API testing with Postman.

## 📚 Study Resources

- Introduction to Selenium WebDriver & automation basics
- Locating web elements – XPath, CSS selectors, IDs
- Writing automated test scripts in Python/Java
- API testing with Postman – GET, POST, PUT, DELETE


## 🎯 Topic Focus

**Automation & API Testing**

## ✅ Practice Tasks

- [ ] Set up Selenium WebDriver and automate login on a demo site
- [ ] Write 5 automated test scripts for form validations
- [ ] Test 3 REST APIs using Postman – validate status codes & response body
- [ ] Create a Postman collection with environment variables

## 🚀 Mini Project — Week 3

**Automate a demo web application end-to-end:**

1. Automate 10 test scenarios using Selenium (login, search, add to cart, checkout)
2. Test 5 APIs with Postman
3. Export the Postman collection

## 📁 Suggested Repo Structure

```
week-3/
├── README.md
├── selenium/
│   ├── login_test.py
│   ├── form_validation_tests/
│   └── mini-project/
│       ├── test_login.py
│       ├── test_search.py
│       ├── test_add_to_cart.py
│       └── test_checkout.py
├── postman/
│   ├── api-tests.postman_collection.json
│   ├── environment.postman_environment.json
│   └── mini-project-collection.postman_collection.json
```

## 🛠 Tools Used

- Selenium WebDriver
- Python / Java
- Postman

## 📌 Notes

- Locator priority: prefer **ID** > **CSS selector** > **XPath** for stability and speed.
- For API tests, validate both the **status code** and the **response body structure/values**.
- Use Postman **environment variables** (e.g., base URL, auth tokens) instead of hardcoding values, so the collection is portable across environments.
