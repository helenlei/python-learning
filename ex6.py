text = "X-DSPAM-Confidence:    0.8475"
number_start = text.find('0')
num = text[number_start:]
f_num = float(num)
print(f_num)
