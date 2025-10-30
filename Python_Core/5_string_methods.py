text = "  hello python  "

print(text.upper())       # HELLO PYTHON
print(text.strip())       # hello python
print(text.replace("python", "world"))  # hello world
print(text.count("l"))    # 2
print(text.startswith("h"))  # False (because of spaces)
print(text.strip().startswith("h"))  # True
