# Week 3 Mini Project — Ready-to-Run Demo

Real, working automation you can copy-paste and run as-is — no setup guesswork.

## 📁 Files

| File | What it does |
|---|---|
| `test_ecommerce_demo.py` | Selenium script automating **10 scenarios** (login, search, add to cart, checkout) on the live public demo site [automationexercise.com](https://www.automationexercise.com) |
| `requirements.txt` | Python dependencies |
| `QA_Week3_API_Tests.postman_collection.json` | Postman collection — **5 REST API tests** (GET, GET, POST, PUT, DELETE) against the live public API [reqres.in](https://reqres.in), each with real assertions |
| `QA_Week3_Environment.postman_environment.json` | Postman environment with `base_url` variable |

## ▶️ Run the Selenium tests

```bash
pip install -r requirements.txt
python test_ecommerce_demo.py
```

- Uses Chrome automatically (via `webdriver-manager` — no manual driver download needed).
- 8 of the 10 tests run fully out of the box (search, cart, checkout flow, negative login).
- 2 tests (`test_02`, `test_04`) need a **real account** — register free at automationexercise.com, then edit `VALID_EMAIL` / `VALID_PASSWORD` at the top of the file. If left as-is, they auto-skip instead of failing.

## ▶️ Run the Postman collection

1. Open Postman → **Import** → select both `.json` files (collection + environment).
2. Select **"QA Week3 Environment"** in the top-right environment dropdown.
3. Click **Run** on the collection (or run requests individually) — all 5 requests hit the live reqres.in API and assert status codes + response bodies automatically.

## ✅ What's covered

**Selenium (10 scenarios):**
1. Home page loads
2. Valid login
3. Invalid login (negative test)
4. Logout
5. Search for a product
6. Verify search results appear
7. Add single product to cart
8. Verify cart contents
9. Add multiple products to cart
10. Proceed to checkout

**Postman (5 APIs):**
1. GET list of users
2. GET single user
3. POST create user
4. PUT update user
5. DELETE user
