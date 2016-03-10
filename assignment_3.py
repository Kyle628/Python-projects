import math


def convert_char(s):
    letter_value = ord(s)
    if letter_value == ord(' '):
        letter_value == ord(' ')
    if s == '1':
        letter_value = 53
    if s == '2':
        letter_value = 54
    if ord(s) >= ord('a'):
        letter_value = ord(s) - ord('a') + 1
    elif ord(s) > 64:
        letter_value = ord(s) - ord('A') + 27
    return letter_value


def convert_num(n):
    num_char = chr(n)
    if n > 52:
        n = n % 52
        if n < 27:
            num_char = (n % 52 + 96)
        if n > 26:
            num_char = (n % 52 + 38)
    if n < 27:
        num_char = chr(n + 96)
    if 26 < n < 53:
        num_char = chr(n + 38)
    return num_char


def encrypt_char(c):
    c_val = convert_char(c) % 54
    top_val = deck[0]
    top_val_num_right = (convert_char(top_val) + 2)
    key_card = deck[top_val_num_right]
    key_card_num = convert_char(key_card)
    encrypted_char_num = c_val + key_card_num
    encrypted_char_num %= 54
    encrypted_char = convert_num(encrypted_char_num)
    if c_val == ord(' '):
        encrypted_char = ' '
    return encrypted_char


def decrypt_char(c):
    enc_val = convert_char(c) % 54
    top_val = deck[0]
    top_val_num_right = (convert_char(top_val) + 2)
    key_card = deck[top_val_num_right]
    key_card_num = convert_char(key_card)
    decrypted_char_num = enc_val - key_card_num
    decrypted_char_num %= 54
    decrypted_char = convert_num(decrypted_char_num)
    if enc_val == ord(' '):
        decrypted_char = ' '
    return decrypted_char


def encrypt_message(msg, deck):
    char = []
    for i in range(len(msg)):
        pos = msg[i]
        char.append(encrypt_char(pos))
    return char


def decrypt_message(msg, deck):
    char = []
    for i in range(len(msg)):
        pos = msg[i]
        char.append(decrypt_char(pos))
    return char


def shuffle_deck(deck):
    joker_1_pos = deck.find('1')
    str_1 = deck[joker_1_pos]
    str_2 = deck[joker_1_pos - 1]
    str_3 = deck[:joker_1_pos - 1]
    str_4 = deck[joker_1_pos + 1:]
    shuffled = str(str_3 + str_1 + str_2 + str_4)
    if joker_1_pos == 53:
        shuffled = str(deck[:1] + deck[-1] + deck[1:53])
    joker_2_pos = shuffled.find('2')
    str_5 = shuffled[joker_2_pos]
    str_6 = shuffled[joker_2_pos - 2:joker_2_pos]
    str_7 = shuffled[:joker_2_pos - 2]
    str_8 = shuffled[joker_2_pos + 1:]
    shuffled_2 = str(str_7 + str_5 + str_6 + str_8)
    if joker_2_pos == 53:
        shuffled_2 = shuffled[:2] + shuffled[joker_2_pos] + shuffled[2:53]
    if joker_2_pos == 52:
        shuffled_2 = shuffled[:1] + shuffled[joker_2_pos] + shuffled[1:53]
    new_joker_1_pos = shuffled_2.find('1')
    new_joker_2_pos = shuffled_2.find('2')
    if new_joker_1_pos < new_joker_2_pos:
        str_x = shuffled_2[:new_joker_1_pos]
        str_y = shuffled_2[new_joker_1_pos:new_joker_2_pos + 1]
        str_z = shuffled_2[new_joker_2_pos + 1:len(shuffled_2)]
    if new_joker_2_pos < new_joker_1_pos:
        str_x = shuffled_2[:new_joker_2_pos]
        str_y = shuffled_2[new_joker_2_pos:new_joker_2_pos + 1]
        str_z = shuffled_2[new_joker_2_pos + 1:len(shuffled_2)]
    triple_cut = str(str_z + str_y + str_x)
    bot_card = triple_cut[53]
    bot_value = convert_char(bot_card)
    str_bot_value = triple_cut[:bot_value + 1]
    last_step = str(triple_cut[bot_value:] + str_bot_value)
    return last_step


if __name__ == "__main__":
    #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONOPQRSTUVWXYZ12
    #lm qv oCpi

    str = ''
    deck = raw_input('Please input a valid 54 card deck')
    prompt = raw_input('Enter \'e\' to encrypt or \'d\' to decrypt')
    if prompt == 'e':
        msg = raw_input('Enter the message you would like to encrypt')
        encrypted = encrypt_message(msg, deck)
        print str.join(encrypted)
    if prompt == 'd':
        msg = raw_input('Enter the message you would like to decrypt')
        decrypted = decrypt_message(msg, deck)
        print str.join(decrypted)


















