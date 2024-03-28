input_text = input('input text: ')

if input_text.isnumeric():
    input_text = int(input_text)
    print(bin(input_text), oct(input_text), hex(input_text))
else:
    print('текст написан в ASCII' if input_text.isascii() else 'test not in ASCII')

