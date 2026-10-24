
import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# Scryfall API endpoint for exact card-name lookups.
BASE_URL = "https://api.scryfall.com/cards/named"


def search_card(card_name):
    """Look up a card by its exact name and display its information."""

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

        # Extract and display selected card information.
        print("\n--- Card Information ---")
        print(f"Name: {card_data.get('name', 'Unknown')}")
        print(f"Mana Cost: {card_data.get('mana_cost', 'None')}")
        print(f"Type: {card_data.get('type_line', 'Unknown')}")
        print(f"Rules Text: {card_data.get('oracle_text') or 'No rules text'}")

        colors = card_data.get("colors", [])
        print(f"Colors: {', '.join(colors) if colors else 'Colorless'}")

        print(f"Set: {card_data.get('set_name', 'Unknown')}")
        print(f"Rarity: {card_data.get('rarity', 'Unknown').title()}")

    except HTTPError as error:
        if error.code == 404:
            print(f"Error: No card found with the exact name '{card_name}'.")
        else:
            print(f"HTTP error: {error.code} - {error.reason}")

    except URLError as error:
        print(f"Connection error: {error.reason}")

    except TimeoutError:
        print("The request timed out.")

# Repeat searches until the user chooses to exit.
while True:
    # Ask the user which card they want to find.
    card_name = input("\nEnter a Magic: The Gathering card name: ").strip()

    if not card_name:
        print("Error: Card name cannot be empty.")
    else:
        search_card(card_name)

    # Ask whether the user wants to search again.
    repeat = input("\nWould you like to search for another card? (y/n): ")
    if repeat.strip().lower() not in ("y", "yes"):
        print("Exiting Scryfall Card Lookup.")
        break