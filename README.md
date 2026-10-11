# CSCI-2910-Lab4

Scryfall API
Part 1:
	The Scryfall API can provide information about Magic: The Gathering cards, allowing developers to retrieve card information from its database for use in their own applications. The API can provide information that describes a specific card, such as its name, colors, mana cost, type, and other details. As a developer, I can send GET requests using the name of a card to receive information about that card. The API then returns the information in JSON format, which can be used by the application.

Part 2:
	The application will allow a user to enter the exact name of a card they would like to look up. After entering a name associated with a Magic: The Gathering card, a GET request will be sent to retrieve the card's information from the Scryfall database. The API will return information about the card in JSON format, and the program will extract and display selected information for the user.
Part 3:
Example URL: GET https://api.scryfall.com/cards/named?exact=Sol%20Ring
Example JSON:
{
  "name": "Sol Ring",
  "mana_cost": "{1}",
  "type_line": "Artifact",
  "oracle_text": "{T}: Add {C}{C}.",
  "colors": [],
  "set_name": "Commander Masters",
  "rarity": "uncommon"
}
JSON Sent:
	None is being sent only retrieved to display the information about the retrieved card.
Description:
	This request searches the Scryfall database for a card with the exact name "Sol Ring." Scryfall returns information about the card in JSON format. The Python application will receive this response and extract the information that it needs to display to the user, such as the card's name, mana cost, type, rules text, set, etc.

## Issues
