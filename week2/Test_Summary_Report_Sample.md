# Test Summary Report — Demoblaze (Demo E-Commerce Site)

**Tester:** Soumya Kanti Hazra
**Test Period:** 2026-08-01 – 2026-08-06
**Site under test:** https://www.demoblaze.com

---

## 1. Summary
End-to-end functional testing was performed on Demoblaze covering login/authentication, search, product pages, cart, checkout, and account management. Testing combined scripted functional test cases with exploratory and negative-input testing (invalid data, boundary values, session/security edge cases). 15 defects were logged across all modules. Checkout and Cart showed the highest defect concentration and included the most severe issues (duplicate order submission, missing address validation), while Search and Product Page issues were mostly cosmetic. Two Critical bugs were found; both are release blockers until resolved.

## 2. Test Execution Summary
| Metric | Count |
|---|---|
| Total test cases executed | 48 |
| Passed | 31 |
| Failed | 15 |
| Blocked | 2 |
| Pass rate | 64.6% |

*2 checkout test cases were blocked by BUG-008 (duplicate order on double-click), which prevented reliable execution of downstream order-history test cases.*

## 3. Defect Summary
| Metric | Count |
|---|---|
| Total bugs logged | 15 |
| Critical | 2 |
| High | 4 |
| Medium | 6 |
| Low | 3 |
| Closed | 5 |
| Open | 4 |
| In Progress | 2 |
| Fixed | 2 |
| Ready for Retest | 1 |
| Reopened | 1 |

*(Pulled directly from the Summary Dashboard tab of the bug tracker.)*

## 4. Defect Density by Module
| Module | Bugs Found |
|---|---|
| Login/Auth | 2 |
| Search | 2 |
| Cart | 3 |
| Checkout | 4 |
| Account | 2 |
| Product Page | 2 |

Checkout had the highest defect density (4 bugs, including both Critical findings), consistent with it being the most complex and highest-risk flow in the application.

## 5. Notable Defects
- **BUG-001** – SQL injection string (`' OR '1'='1`) in the username field logs the user in without valid credentials – Severity: Critical – Status: Closed
- **BUG-008** – Double-clicking "Place Order" creates two duplicate orders instead of one – Severity: Critical – Status: Open
- **BUG-003** – Checkout completes successfully even with the shipping address field left blank – Severity: High – Status: Open
- **BUG-014** – Account email can be changed without re-entering the current password, allowing account takeover if a session is hijacked – Severity: High – Status: In Progress
- **BUG-002** – Cart accepts negative quantities, producing a negative order total; fix regressed on retest – Severity: High – Status: Reopened

## 6. Bug Lifecycle Observations
Closed bugs took an average of 3–4 days from Open to Closed. The Cart module's quantity-validation bug (BUG-002) is the one reopen in this cycle — the initial fix passed a basic retest but failed again under a slightly different input, indicating the original fix addressed the symptom rather than the root validation logic. Checkout bugs had the slowest average turnaround, likely because two of the four (BUG-003, BUG-008) are Critical/High and still awaiter developer fixes rather than QA retest. No bug sat in "Open" for more than 5 days as of report date, but BUG-008 (Critical) has been open 2 days with no fix yet, which is the primary schedule risk.

## 7. Risks & Recommendations
- Checkout should not be considered release-ready until BUG-003 (missing address validation) and BUG-008 (duplicate order on double-click) are resolved — both directly affect order integrity and revenue.
- BUG-014 (email change with no password confirmation) is a security gap and should be prioritized ahead of its current Medium-priority queue position; recommend reclassifying to P1.
- Recommend adding automated regression tests for cart quantity validation to prevent BUG-002-style regressions from recurring after future fixes.
- Consider disabling the "Place Order" button on first click (client-side debounce) as an immediate mitigation for BUG-008 while a full server-side fix is developed.

## 8. Conclusion
Demoblaze's core browsing, search, and product-viewing flows are stable, but the checkout flow has unresolved Critical and High-severity defects that pose real risk to order integrity and account security. The site is **not release-ready** in its current state; it would be after BUG-001 (already closed), BUG-003, BUG-008, and BUG-014 are fixed and verified in retest.
