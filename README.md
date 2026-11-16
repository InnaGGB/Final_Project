# Final_Project

![UI tests](https://github.com/InnaGGB/Final_Project/actions/workflows/tests.yml/badge.svg)

UI test automation for a demo online bookstore, built with Python, Selenium and pytest using the Page Object pattern. It started as the final project of the Stepik course "Automated testing with Selenium and Python".

Target site: http://selenium1py.pythonanywhere.com/

## Stack

- Python 3.13, pytest, Selenium 4
- Page Object pattern (`pages/`: base, main, login, product, basket)
- GitHub Actions: headless Chrome run on every push and pull request, plus a weekly scheduled run; the HTML report is attached to each run as an artifact

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest --language=en             # add --headless to run without a window
```

Requires Google Chrome installed (Selenium downloads the matching driver itself).

## Project layout

```
pages/          page objects and locators
conftest.py     browser fixture, --language and --headless options
test_*.py       tests
.github/workflows/tests.yml   CI pipeline
```

## What's covered

- Main page: login link is visible, guest can open the login page, empty basket check
- Product page: success message after adding to basket (positive and negative checks, with two known-failing checks marked `xfail`), login link, empty basket check
- Registered user scenarios: a fresh user is registered in a `setup` fixture before each test
- Tests are grouped with markers (`login_guest`, `need_review`), so a subset can be run with `pytest -m need_review`

## Notes

- The tests run against a public demo shop, so occasional slowness on the site can cause a failed run. CI retries a failed test once.
