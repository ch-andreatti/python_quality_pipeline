# Imports

import requests
from pydantic import BaseModel, ValidationError

# Helper classes


class Street(BaseModel):
    number: int
    name: str


class Coordinates(BaseModel):
    latitude: str
    longitude: str


class Timezone(BaseModel):
    offset: str
    description: str


class Location(BaseModel):
    street: Street
    city: str
    state: str
    country: str
    postcode: int
    coordinates: Coordinates
    timezone: Timezone


class Name(BaseModel):
    title: str
    first: str
    last: str


class User(BaseModel):
    gender: str
    name: Name
    location: Location
    email: str
    cell: str
    nat: str


# Data preparation and validation

valid_users = []

resp = requests.get(
    "https://randomuser.me/api/?results=10&inc=gender, name, location, email, cell, nat"
)
data = resp.json()
for user in data["results"]:

    try:
        valid_user = User(**user)
        valid_users.append(valid_user)

    except ValidationError as e:
        print(f"Error at validation of user {user}: {e}")
        continue
