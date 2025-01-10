from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class User:
    username: str
    password: bytes

    first_name: str
    last_name: str
    second_name: str
