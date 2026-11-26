import os

# The single word for this round, written exactly as-is.
WORD = "Panopticon"

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(WORD)

print(WORD)
