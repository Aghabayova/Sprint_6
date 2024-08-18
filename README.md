# <h><center> Project: Yandex Scooter</h>


### prepared by Samira Aghabayova


## Test Coverage:

## 1. Dropdown List in the "Вопросы о важном" Section

**Objective:** Verify that clicking the arrow next to each question expands the corresponding text.

**Details:** A separate test is written for each question to ensure accurate and individual validation.

## 2. Verification of Positive Flow of Scooter Order

**Objective:** Test the complete positive scenario for placing an order using two sets of test data.

**Details:**

- **Entry Points:**
  - "Order" button at the top of the page.
  - "Order" button at the bottom of the page.

- **Scenario Steps:**
  1. Click the "Order" button.
  2. Complete the order form.
  3. Verify that a popup window appears with a successful order creation message.
  4. Check that clicking the "Scooter" logo navigates to the Scooter main page.
  5. Verify that clicking the "Yandex" logo opens the Yandex Zen main page in a new window via redirect.

**Data:**

- Minimum of two sets of test data.
- The specific data sets used are at the tester’s discretion.
- Tests are designed to cover the general scenario and do not require separate testing for each entry point.

## Project Launch: 

1. Install pytest using pip:
```
    pip install pytest
```
2. Install selenium using pip:

```
   pip install selenium
```
3. Install allure using homebrew:

```
   brew install allure
```
4. Run the Tests with pytest:

```
   pytest -v
```
## Comands to obtain the report


1. Install pytest using pip:
```
pytest --alluredir=allure_results
```
2. Install selenium using pip:

```
 allure serve allure_results
```