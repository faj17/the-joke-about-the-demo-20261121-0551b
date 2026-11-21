import os

JOKE = "Halfway through my demo, my AI agent took the keyboard, fixed the bug I was about to show, and introduced itself as the senior engineer."

# The brief caps the entry at 1-280 Unicode code points; fail loudly instead
# of submitting an over-long text.
assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} code points, must be 1-280"
# Guard the shape before writing: exactly one line, no leading/trailing
# whitespace, so the file the judge reads is the joke and nothing else.
assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
assert JOKE == JOKE.strip(), "joke must not carry leading/trailing whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
