# Imports

import logging
import os

import great_expectations as gx
import pandas as pd
import requests
from pydantic import ValidationError

from src.validators.data_schemas import User

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Data collection and validation

logging.info("Starting data collection")

valid_users = []

response = requests.get(
    "https://randomuser.me/api/?results=10&?nat=au,br,ca,ch,es,fr,gb,mx,us&inc=gender,name,location,email,cell,nat"
)
data = response.json()
for user in data["results"]:

    try:
        valid_user = User(**user)
        valid_users.append(valid_user)

    except ValidationError as e:
        logging.warning(f"Error at validation of user {user}: {e}")
        continue

valid_users = [user.model_dump() for user in valid_users]


for user in valid_users:
    print(user, "\n")

df = pd.json_normalize(valid_users)
print(df.columns)

# Data quality

context = gx.get_context(mode="ephemeral")

DATA_SOURCE_NAME = "randomuser"
data_source = context.data_sources.add_pandas(name=DATA_SOURCE_NAME)

DATA_ASSET_NAME = "randomuser_df"
data_asset = data_source.add_dataframe_asset(name=DATA_ASSET_NAME)

BATCH_DEFINITION_NAME = "randomuser_batch_definition"
batch_definition = data_asset.add_batch_definition_whole_dataframe(
    BATCH_DEFINITION_NAME
)
batch_parameters = {"dataframe": df}
batch = batch_definition.get_batch(batch_parameters=batch_parameters)

expect_columns = [
    "gender",
    "email",
    "cell",
    "nat",
    "name.title",
    "name.first",
    "name.last",
    "location.street.number",
    "location.street.name",
    "location.city",
    "location.state",
    "location.country",
    "location.postcode",
    "location.coordinates.latitude",
    "location.coordinates.longitude",
    "location.timezone.offset",
    "location.timezone.description",
]
expectation = gx.expectations.ExpectTableColumnsToMatchSet(
    column_set=expect_columns, exact_match=True
)

validation_results = batch.validate(expectation)
print(validation_results)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(CURRENT_DIR)
PROJECT_ROOT = os.path.dirname(SRC_DIR)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "data", "stage")

print("CURRENT_DIR", CURRENT_DIR)
print("SRC_DIR", SRC_DIR)
print("PROJECT_ROOT", PROJECT_ROOT)
print("OUTPUT_DIR", OUTPUT_DIR)

os.makedirs(OUTPUT_DIR, exist_ok=True)

output_path = os.path.join(OUTPUT_DIR, "randomuser.parquet")
df.to_parquet(output_path, index=False)
