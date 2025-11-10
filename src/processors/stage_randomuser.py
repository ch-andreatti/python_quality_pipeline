# Imports

import pandas as pd
import requests
from pydantic import ValidationError

from src.validators.data_schemas import User

# Data collection and validation

valid_users = []

response = requests.get(
    "https://randomuser.me/api/?results=10&inc=gender, name, location, email, cell, nat"
)
data = response.json()
for user in data["results"]:

    try:
        valid_user = User(**user)
        valid_users.append(valid_user)

    except ValidationError as e:
        # print(f"Error at validation of user {user}: {e}")
        continue

user_test = valid_users[0].model_dump()
print(type(user_test))
print(user_test)

df = pd.DataFrame([user_test])
print(df.columns)
