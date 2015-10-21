import string

text = '#$I pDF#*&refer pillows that are soft.'
for i in string.punctuation:
    print i
    text = text.replace(i, ' ')
    print text

print text
