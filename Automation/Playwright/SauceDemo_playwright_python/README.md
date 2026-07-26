# SauceDemo Test Automation — Playwright + Pytest

An end-to-end UI test automation project for [saucedemo.com](https://www.saucedemo.com), built with **Python**, **Playwright**, and **pytest**, following the **Page Object Model (POM)** design pattern.

The suite covers the full user journey — login, product browsing/sorting, cart management, and checkout — with 23 tests validating both happy paths and edge cases (invalid input, locked-out users, blank fields).

## Tech Stack

- **Python 3**
- **Playwright** — browser automation
- **pytest** — test framework
- **pytest-playwright** — Playwright/pytest integration

## Project Structure

```
saucedemo-playwright-pytest/
├── pages/
│   ├── login_page.py        # Login form locators & actions
│   ├── inventory_page.py    # Product listing, cart badge, sorting
│   ├── cart_page.py         # Cart contents & navigation
│   └── checkout_page.py     # 3-step checkout flow
├── tests/
│   ├── test_login.py        # 5 tests
│   ├── test_inventory.py    # 8 tests
│   ├── test_cart.py         # 4 tests
│   └── test_checkout.py     # 6 tests
├── conftest.py               # Shared fixtures (e.g. logged-in state)
├── pytest.ini                 # Pytest configuration
└── requirements.txt
```

## Test Coverage

| Module | Tests | Covers |
|---|---|---|
| **Login** | 5 | Valid login, invalid credentials, locked-out user, blank username, blank password |
| **Inventory** | 8 | Product listing, add/remove from cart, cart badge count, sort by name (A-Z/Z-A) & price (low-high/high-low), cart navigation |
| **Cart** | 4 | Items match what was added, item removal, continue shopping, proceed to checkout |
| **Checkout** | 6 | Form validation (missing first name/last name/postal code), full purchase flow, order confirmation, return to products |

## How to Run

**1. Clone the repo and set up a virtual environment**
```bash
git clone <your-repo-url>
cd saucedemo-playwright-pytest
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
python -m playwright install
```

**3. Run the tests**
```bash
pytest
```

Run a specific file:
```bash
pytest tests/test_checkout.py -v
```

## Design Decisions

- **Page Object Model** — every page's locators and actions live in one class under `pages/`, keeping test files readable and free of raw selectors. If saucedemo changes an element, only one file needs updating.
- **Fixtures for shared state** — `conftest.py` and per-file fixtures (e.g. `checkout_page_with_items`) handle repetitive setup like login and adding items to cart, so each test starts from a clean, predictable state without duplicating steps.
- **Auto-retrying assertions where timing matters** — `expect(locator).to_have_count(...)` / `to_have_text(...)` are used instead of one-shot `assert` checks in places where the UI updates asynchronously (e.g. the cart badge after removing an item), since a single manual read can run before the DOM finishes updating.

## Bugs Found & Fixed

Building this surfaced several real automation bugs — a useful record of debugging, not just script-writing:

- **Locator scope bug** — `.inventory_container` (the wrapper for *all* products) was used instead of `.inventory_item` (a single product card), causing every "add to cart" click to hit all 6 buttons at once.
- **Cart badge race condition** — reading the cart badge with a plain `.inner_text()` right after a click sometimes ran before the UI updated, returning stale data. Fixed by switching to Playwright's auto-retrying `expect(...).to_have_count(0)`.
- **Wrong locator target** — the cart badge locator was accidentally pointed at the "Add to cart" button's own CSS classes instead of `.shopping_cart_badge`, so cart count always read as empty.
- **Mismatched test data** — a hardcoded product name list was missing the `(Red)` variant text used by the real site, caught by a sort-order test.
- **Typos in selectors** — `"bitton"` instead of `"button"`, silently matching nothing instead of raising a clear error.

## Possible Future Improvements

- GitHub Actions workflow to run the suite automatically on push/PR
- Cross-browser runs (Firefox, WebKit) in addition to Chromium
- HTML test reports via `pytest-html`
- Parametrized negative-login tests using `@pytest.mark.parametrize`