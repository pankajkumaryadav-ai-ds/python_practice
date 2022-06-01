# first question
name=input("Enter your name: ")
print("Good Afternoon, "+ name)

# second question
letter='''Dear <|Name|>,
You are selected! We are offering you a wonderful package in our company.
Date:<|Date|>'''
name=input("Enter your name: ")
Date=input("Enter the date: ")
# letter.replace("<|Name|>",name) this wont replace
# letter.replace("<|DAte|>",Date) we have to change it by doing leter =
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",Date)
print(letter)

# 3rd question
st="THIS IS A STRING WITH double   spaces"
doublespaces=st.find("  ")
print(doublespaces)

# 4th question
st="THIS IS A STRING WITH double   spaces"
st=st.replace("  ","")
print(st).

# 5th question
letter="Dear Pankaj This python  course is nice! Thanks"
formatted_letter="Dear Pankaj,\n\tThis python course is nice\nThanks!"
print(formatted_letter)