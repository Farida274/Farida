'''
import re
# \n
text = "ismim Sohib, 1992-yilda tug'ilganman. \
    Sen-chi, ey odam?! \
        iltimos"
pattern = r"^i"
result = re.findall(pattern, text) 
print(result)
print(len(result))


email_text = "연락처: hello123@example.com"
result = re.findall(r'\w+@\w+\.\w+', email_text)
print(result)

def extract_emails(text):
    words = text.split()
    emails = []

    for word in words:
        if "@" in word and "." in word:
            emails.append(word.strip(",.?!"))
            
    return emails

def extract_emails_regex(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

text = "contact me at john.doe@example.com or support@company.co.kr! Also, check info@domain123.net."
print(extract_emails_regex(text))
'''
#def extract_111(text):
   # pattern = r("[^123]")
   # return re.findall(pattern, text)
   # text = "a b c 5 4 3 2 1"

with open("C:\\Users\\xafiz\\OneDrive\\바탕 화면\\한국어 정보처리 (전태희)\\sample.txt", 'r') as z:
    text = z.read()
    
print(text)

import re

p = re.compile("com+it+e+e")

sujongbon = p.sub("committee", text)
print(sujongbon)

with open("yangi.txt", "w+") as f:
    f.write(sujongbon)

# my change