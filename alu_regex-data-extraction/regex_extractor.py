import re

# Load data from a text file
with open('test_data.txt', 'r') as file:
    data = file.read()

# Define regex patterns
patterns = {
    "Emails": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "URLs": r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?",
    "Phone Numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "Credit Cards": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    "Time Formats": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APMapm]{2})?\b",
    "HTML Tags": r"<[^>]+>",
    "Hashtags": r"#[\w]+",
    "Currency Amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

# Apply each pattern and display matches
for label, pattern in patterns.items():
    print("\n--- {} ---".format(label))
    matches = re.findall(pattern, data)
    if matches:
        for match in matches:
            print(match)
    else:
        print("No matches found.")
