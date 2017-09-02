FROM_BASE64 = {
    'A':  0, 'B':  1, 'C':  2, 'D':  3, 'E':  4, 'F':  5, 'G':  6,
    'H':  7, 'I':  8, 'J':  9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
    'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
    'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27,
    'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34,
    'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41,
    'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48,
    'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55,
    '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62,
    '/': 63,
}

FROM_BASE64 = dict((ord(k), v) for k,v in FROM_BASE64.items())

TO_BASE64 = dict((v,k) for k,v in FROM_BASE64.items())

def to_base64_iter(buf):
    rem_shift   = { 0: 4, 2: 2, 4: 0 }
    rem_mask    = { 0: 0x03, 2: 0x0F, 4: 0x3F }
    sextet_mask = { 0: 0xFC, 2: 0xF0, 4: 0xC0 }
    
    buf_size = len(buf)
    bits_in_rem = 0
    rem = 0
    sextet = 0
    i = 0
    while i < buf_size:
        if bits_in_rem < 6:
            sextet = ((buf[i] & sextet_mask[bits_in_rem]) >> (bits_in_rem + 2)) | rem
            rem = (buf[i] & rem_mask[bits_in_rem]) << rem_shift[bits_in_rem]
            bits_in_rem += 2
            i += 1
        else:
            assert bits_in_rem == 6, 'bits_in_rem != 6'
            sextet = rem
            rem = 0
            bits_in_rem = 0

        assert sextet & 0xC0 == 0
        yield sextet

    if bits_in_rem > 0:
        # We have run out of bytes, but another sextets needs
        # to be processed.
        sextet = rem
        rem = 0
        bits_in_rem = 0

        assert sextet & 0xC0 == 0
        yield sextet

def to_base64(string):
    byte_string = list(map(ord, string))
    return ''.join(map(chr, map(lambda sextet: TO_BASE64[sextet], to_base64_iter(byte_string))))

def to_base_64(string):
    return to_base64(string)

def from_base64_iter(buf):
    mask_rem    = { 6: 0x0F, 4: 0x03, 2: 0x00 }
    mask_lower  = { 6: 0x30, 4: 0x3C, 2: 0x3F }
    shift_upper = { 6: 2, 4: 4, 2: 6 }
    shift_lower = { 6: 4, 4: 2, 2: 0 }

    buf_size = len(buf)
    octet = 0
    rem   = 0
    bits_in_rem = 0
    i = 0
    while i < buf_size:
        if bits_in_rem > 0:
            # We have not reached not processed a 
            # batch of 4 setets yet. 
            # Note: 4 sextets makes 3 bytes.
            upper = rem << shift_upper[bits_in_rem]
            lower = (buf[i] & mask_lower[bits_in_rem]) >> shift_lower[bits_in_rem]
            octet = upper | lower
            rem = buf[i] & mask_rem[bits_in_rem]
            bits_in_rem -= 2
            i += 1

            yield octet
        else:
            assert bits_in_rem == 0, 'bits_in_rem != 0'
            # We have processed a batch of 4 sextets. Now we
            # set up for the next batch of 4 sextets.
            # Note: 4 sextets makes 3 bytes.
            rem = buf[i] & 0x3F
            bits_in_rem = 6
            i += 1

    if (bits_in_rem > 0) and (rem != 0):
        # we have consumed every byte but there are
        # still unprocessed bits remaining.
        octet = rem 
        rem = 0
        bits_in_rem = 0

        yield octet


def from_base64(base64_string):
    try:
        sextets = list(map(lambda ch: FROM_BASE64[ord(ch)], base64_string))
        return ''.join(map(chr, from_base64_iter(sextets)))
    except:
        raise ValueError("Invalid Base64 string.")

def from_base_64(base64_string):
    return from_base64(base64_string)
