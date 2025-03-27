
# 1. str.endswith()

filename = "document.pdf"

if filename.endswith(".pdf"):
    print("This is a PDF file")
else:
    print("This is not a PDF file")

# 2. str.count()
sentence = "Have you tried to push your assignmets, everyone should push."

push_count = sentence.count("push")
print(f"The word 'push' appears {push_count} times")

# 3. str.replace(old, new)
text = "I like cats. Cats are awesome."

new_text1 = text.replace("cats", "dogs")
print(new_text1)
