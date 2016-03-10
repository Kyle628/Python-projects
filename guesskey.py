#f2456661-b5ea-40_c-9897-e4ca403_e7df
#-5 a

def guess_key():
    cd_key = 'f2456661-b5ea-40fc-9897-e4ca403_e7df'
    for i in range(26):
        place_16 = chr(97 + i)
        str_16 = str(place_16)
        new_key = cd_key[:31] + str_16 + cd_key[32:]
        print new_key


cd_key = 'f2456661-b5ea-40fc-9897-e4ca403_e7df'
print guess_key()


