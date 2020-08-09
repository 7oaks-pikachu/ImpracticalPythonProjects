cipher_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
cipher_list = list(cipher_text.split())

print(f"length of cipher list = {len(cipher_list)}")

#initialise variables
COLS = 4
ROWS = 5
keys = '-1 2 -3 4'
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

key_int = [int(i) for i in keys.split()]
for k in key_int:
    if k<0:
        col_items = cipher_list[start:stop]
    elif k>0:
        col_items = list(reversed(cipher_list[start:stop]))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print(f"\ncipyher text = {cipher_text}")
print(f"\ntranslation matrix = ", *translation_matrix, sep='\n')
print(f"\nkey length {len(key_int)}")

#loop through nexted lists popping off last item to new list
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ' '

print(f"\nplaintext = {plaintext}")


