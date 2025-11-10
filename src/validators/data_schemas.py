# Imports

from pydantic import BaseModel

# randomuser - pydantic


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
