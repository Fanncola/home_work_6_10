from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    phone: str
    email: str
    gender: str
    birth_date: object
    hobbies: str
    current_address: str
