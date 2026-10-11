
import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# Scryfall API endpoint for exact card-name lookups.
BASE_URL = "https://api.scryfall.com/cards/named"

# Card we want to retrieve for our first test.
card_name = "Sol Ring"

# Encode the card name so it can safely be included in the URL.
params = urlencode({"exact": card_name})
url = f"{BASE_URL}?{params}"

# Create the GET request.
request = Request(
    url,
    headers={
        "User-Agent": "ScryfallCardLookup/1.0",
        "Accept": "application/json",
    },
    method="GET",
)

try:
    # Send the request and read the response.
    with urlopen(request, timeout=15) as response:
        card_data = json.loads(response.read().decode("utf-8"))

    # Display the returned JSON data.
    print(json.dumps(card_data, indent=2))

except HTTPError as error:
    print(f"HTTP error: {error.code} - {error.reason}")

except URLError as error:
    print(f"Connection error: {error.reason}")

except TimeoutError:
    print("The request timed out.")
