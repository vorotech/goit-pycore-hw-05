"""Module for handling commands."""

import re

# Phonebook where key is name and value is phone number
contacts = {}

class ContactError(Exception):
    """Custom exception for contact errors."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

def input_error(strerror: str = "Invalid input."):
    """Decorator for handling input errors.

    Args:
        strerror (str, optional): Message returned in case of invalid input. Defaults to "Invalid input.".
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ContactError as e:
                return e.message
            except(ValueError, IndexError):
                return strerror
        return wrapper
    return decorator

@input_error(strerror="Invalid command. Usage: add [ім'я] [номер телефону]")
def add_contact(*args) -> str:
    """Adds a contact to the phonebook."""
    name, phone = args

    if name in contacts:
        raise ContactError("Contact already exists.")
    contacts[name] = _normalize_phone(phone)
    return "Contact added."

@input_error(strerror="Invalid command. Usage: change [ім'я] [номер телефону]")
def change_contact(*args) -> str:
    """Change a contact."""
    name, phone = args

    if name not in contacts:
        raise ContactError("No such contact.")

    contacts[name] = _normalize_phone(phone)
    return "Contact updated."

@input_error(strerror="Invalid command. Usage: phone [ім'я]")
def get_phone(*args) -> str:
    """Gets a phone number."""
    (name,) = args

    if name not in contacts:
        raise ContactError("No such contact.")

    return contacts[name]

def get_all_contacts() -> dict:
    """Gets all contacts."""
    return contacts


def _normalize_phone(phone_number: str, country_code = "38") -> str:
    """Normalizes phone number by removing all non-digit characters
    or `+` and adding country code if it is missing.

    Args:
        phone_number (str): Phone nummber to normalize.

    Raises:
        PhoneBookError: If phone number length is not valid

    Returns:
        str: Narmonized phone number.
    """
    pattern = r"[+\d]"
    phone_number = "".join(re.findall(pattern, phone_number))

    if not phone_number.startswith("+"):
        phone_number = re.sub(fr"^({country_code})?", f"+{country_code}", phone_number)

    if len(phone_number) != 13:
        raise ValueError("Invalid phone number.")

    return phone_number
