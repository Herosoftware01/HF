import pathlib

p = pathlib.Path("Database/models.py")

# Read as text, replacing any decoding errors with a placeholder
text = p.read_text(encoding="utf-8", errors="replace")

# Remove null characters
clean_text = text.replace("\x00", "")

# Write back out as UTF-8 text
p.write_text(clean_text, encoding="utf-8")

# Report how many were removed (optional)
print("Removed", text.count("\x00"), "null characters")