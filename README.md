# Final_Project

![UI tests](https://github.com/InnaGGB/Final_Project/actions/workflows/tests.yml/badge.svg)

UI test automation for a demo online bookstore, built with Python, Selenium and pytest using the Page Object pattern. It started as the final project of the Stepik course "Automated testing with Selenium and Python".

Target site: http://selenium1py.pythonanywhere.com/

## Stack

- Python 3.12, pytest, Selenium 4
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

## Status

Work in progress: the remaining course tasks are being added step by step.
