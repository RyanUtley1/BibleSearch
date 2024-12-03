import re

# Updated regex to account for books starting with numbers (e.g., "1 John 1:1")
verse_pattern = re.compile(r"^\d?\s?[A-Za-z]+ \d+:\d+")

# Open the input and output files
with open("KJV.txt", "r") as infile, open("KJVsingleLine.txt", "w") as outfile:
    current_verse = ""  # Temporary storage for the current verse
    for line in infile:
        stripped_line = line.strip()
        if verse_pattern.match(stripped_line):
            # Write the previous verse to the file, if it exists
            if current_verse:
                outfile.write(current_verse.strip() + "\n")
            # Start a new verse
            current_verse = stripped_line
        else:
            # Append continuation text to the current verse
            current_verse += " " + stripped_line
    # Write the last verse to the file
    if current_verse:
        outfile.write(current_verse.strip() + "\n")
