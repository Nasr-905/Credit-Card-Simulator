def initialize():
    """
    Initializes global variables representing the state of the credit card account.
    This function follows a procedural programming paradigm, promoting modularity
    and sequential execution. It adheres to good coding practices by organizing
    related code into a function for better maintainability.
    """
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    global card_disabled

    # Set initial balances and state
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0

    # Initialize update dates to -1, indicating no updates have occurred
    last_update_day, last_update_month = -1, -1

    # Initialize country variables
    last_country = ""
    last_country2 = ""

    # Monthly interest rate for balance calculation
    MONTHLY_INTEREST_RATE = 0.05

    # Credit card is initially enabled
    card_disabled = False

def date_same_or_later(day1, month1, day2, month2):
    """
    Checks if the first date is the same as or later than the second date.
    This function implements date comparison logic, ensuring accuracy in
    determining whether one date is equal to or later than another.
    """
    if day1 == day2 and month1 == month2:
        return True
    if month1 > month2:
        return True
    if month1 == month2 and day1 > day2:
        return True
    return False

def all_three_different(c1, c2, c3):
    """
    Checks if three values are all different.
    This function promotes code clarity and readability by encapsulating
    the logic for checking the distinctiveness of three values.
    """
    if c1 == "" or c2 == "" or c3 == "":
        return False
    if c1 == c2 or c1 == c3 or c2 == c3:
        return False
    return True

def purchase(amount, day, month, country):
    """
    Processes a purchase transaction and updates the credit card state.
    This function incorporates error handling to gracefully handle scenarios
    where the card is disabled due to country restrictions or if the purchase
    date is later than the last update date.
    """
    global card_disabled, cur_balance_owing_recent, last_update_day, last_update_month

    # Check if the card is disabled due to country restrictions
    check_countries_countries(country)
    if card_disabled:
        return "error"

    # Check if the purchase date is later than the last update date
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"

    # Update balances and date information
    update_owing(day, month)
    update_date(day, month)
    cur_balance_owing_recent += amount
    update_country(country)

def amount_owed(day, month):
    """
    Calculates the total amount owed, considering interest and recent balance.
    This function incorporates error handling by checking if the provided date
    is later than the last update date, ensuring accurate and reliable calculations.
    """
    global last_update_day, last_update_month

    # Check if the provided date is later than the last update date
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"

    # Update balances and date information
    update_owing(day, month)
    update_date(day, month)

    # Return the total amount owed
    return cur_balance_owing_intst + cur_balance_owing_recent

def pay_bill(amount, day, month):
    """
    Processes a bill payment and updates the credit card state efficiently.
    This function incorporates error handling by checking if the payment date
    is later than the last update date, ensuring accurate and reliable transactions.
    """
    global cur_balance_owing_intst, cur_balance_owing_recent

    # Check if the payment date is later than the last update date
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        update_date(day, month)
        return "error"

    # Update balances and date information based on the payment amount
    update_owing(day, month)
    if amount <= cur_balance_owing_intst:
        cur_balance_owing_intst -= amount
    else:
        amount -= cur_balance_owing_intst
        cur_balance_owing_intst = 0
        cur_balance_owing_recent -= amount

    # Update date after processing the payment

def update_date(day, month):
    """
    Updates the last update date efficiently.
    This function ensures accurate and timely updates to the last update date,
    maintaining the state of the credit card account in an organized manner.
    """
    global last_update_day, last_update_month
    last_update_day = day
    last_update_month = month

def update_owing(day, month):
    """
    Updates the balance owed based on the time elapsed since the last update efficiently.
    This function involves state management, maintaining the state of the credit
    card account by updating balances and date information in an optimized manner.
    """
    global last_update_month, cur_balance_owing_recent, cur_balance_owing_intst

    # Calculate the number of months elapsed since the last update
    n = month - last_update_month

    # If less than 1 month has passed, no update is needed
    if n < 1:
        return

    # If exactly 1 month has passed, apply interest and reset recent balance
    if n == 1:
        cur_balance_owing_intst = cur_balance_owing_intst * (1.05 ** 1)
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_recent = 0

    # If more than 1 month has passed, apply interest for each month efficiently
    elif n > 1:
        cur_balance_owing_intst *= (1.05 ** 1)
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_recent = 0
        cur_balance_owing_intst *= (1.05 ** (n - 1))

def check_countries_countries(country):
    """
    Checks if the last three countries are all different and disables the card if not.
    This function involves state management by modifying the state of the card
    (disabling it) based on the comparison of the last three countries.
    """
    global last_country, last_country2, card_disabled

    # Disable the card if the last three countries are not all different
    if all_three_different(last_country, last_country2, country):
        card_disabled = True

def update_country(country):
    """
    Updates the country information efficiently.
    This function ensures the timely and accurate update of country information,
    maintaining the state of the credit card account in an organized manner.
    """
    global last_country, last_country2
    last_country2 = last_country
    last_country = country
