import string

text = "I @Love Python!"
print(text)
lower_case = text.lower()
print(lower_case)
print(string.punctuation)
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
print(cleaned_text)