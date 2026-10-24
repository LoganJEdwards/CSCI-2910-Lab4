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


## Issue
1. Repeat-Search Prompt
Issue: After looking up a card, the application needed to ask whether the user wanted to search for another card. The prompt also needed to handle invalid answers instead of accepting any input.
Solution: Added a loop that accepts y or yes to continue and n or no to exit. Any other response displays an error message and asks the user again.
Testing: Verified that the program accepts valid responses, rejects invalid responses, and exits when the user chooses n.

2. Invalid Card Names
Issue: A card name that does not match a card in Scryfall's exact-name lookup returns an HTTP 404 error.
Solution: Added handling for HTTP errors so the program displays a clear message when a card cannot be found instead of terminating unexpectedly.
Testing: Entered an invalid card name and verified that the program displayed an error message and allowed the user to exit normally.

3. Invalid JSON Responses
Issue: The application needed to handle a response that could not be parsed as valid JSON.
Solution: Added handling for JSON decoding errors so the program displays an error message if the response contains invalid JSON.
Testing: The error handler was added. A malformed JSON response has not been independently tested.

4. Unexpected Response Format
Issue: The application needed to verify that the parsed response was a JSON object before trying to retrieve card fields.
Solution: Added a check to ensure the parsed response is a dictionary before accessing card information. If the response has an unexpected format, the program displays an error and returns to the main loop.
Testing: Normal card lookups were verified after the change. The unexpected-format condition has not been independently tested.