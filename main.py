from __future__ import annotations

import json
import os
import re
from datetime import datetime
from datetime import timedelta

from dotenv import find_dotenv
from dotenv import load_dotenv
from linkedin_api import Linkedin

# Load environment variables
_ = load_dotenv(find_dotenv())

# Extract environment variables
email_address = os.environ.get("LINKEDIN_EMAIL_ADDRES")
password = os.environ.get("LINKEDIN_PASSWORD")
public_id = os.environ.get("LINKEDIN_PUBLIC_ID")


def clean_relative_time(time_str: str) -> tuple[int, str]:
    match = re.search(r"(\d+)([a-zA-Z])", time_str)
    if match:
        number = int(match.group(1))
        letter = match.group(2)
        return number, letter
    else:
        return -1, ""


def extract_and_convert_time(quantity: int, unit: str) -> datetime | None:
    # Mapping relative time units to timedelta arguments
    time_units = {
        "s": "seconds",
        "m": "minutes",
        "h": "hours",
        "d": "days",
        "w": "weeks",
        "M": "months",
        "y": "years",
    }
    if unit in time_units:
        # Calculating the timedelta
        delta = timedelta(**{time_units[unit]: quantity})
        # Calculating the absolute time
        absolute_time = datetime.now() - delta
        return absolute_time
    return None


# Authenticate using any Linkedin account credentials
api = Linkedin(username=email_address, password=password)

# Get profile
profile = api.get_profile(public_id=public_id)

# Get profile posts
posts = api.get_profile_posts(urn_id=profile["urn_id"], post_count=10)


# Key to extract reposts: ["header"]["text"]["text"]
# Key to extract poster name: ["actor"]["name"]["text"]
# Key to extract post content: ["commentary"]["text"]["text"]
# Key to extract relative timestamp ["actor"]["subDescription"]["text"]
curated_posts = []
for post in posts:
    if "repost" in post["header"]["text"]["text"]:
        info = {}
        info["poster_name"] = post["actor"]["name"]["text"]
        info["post_content"] = re.sub(r"[^\w\s]", "", post["commentary"]["text"]["text"]).strip()
        quantity, unit = clean_relative_time(post["actor"]["subDescription"]["text"])
        info["relative_timestamp"] = f"{quantity}{unit} ago"
        absolute_timestamp = extract_and_convert_time(quantity, unit)
        if absolute_timestamp:
            info["absolute_timestamp"] = absolute_timestamp.isoformat()
        curated_posts.append(info)
    else:
        continue

# Save posts to a JSON file
export_dir = os.path.join(os.getcwd(), "data")
os.makedirs(export_dir, exist_ok=True)
export_path = os.path.join(export_dir, "reposted_posts.json")
with open(export_path, "w") as file:
    json.dump(curated_posts, file, indent=4)
