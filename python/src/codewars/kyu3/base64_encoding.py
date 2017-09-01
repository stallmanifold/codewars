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
    while True:
        if (i < buf_size) and (bits_in_rem < 6):
            sextet = ((buf[i] & sextet_mask[bits_in_rem]) >> (bits_in_rem + 2)) | rem
            rem = (buf[i] & rem_mask[bits_in_rem]) << rem_shift[bits_in_rem]
            bits_in_rem += 2
            i += 1
        elif (i < buf_size) and (bits_in_rem >= 6):
            sextet = rem
            rem = 0
            bits_in_rem = 0
        elif (i >= buf_size) and (bits_in_rem > 0):
            # We have run out of bytes, but we have not processed
            # all of the sextets yet.
            sextet = rem
            rem = 0
            bits_in_rem = 0
        else:
            # We are out of bytes, and there are no more sextet chunks
            # remaining.
            break

        assert (sextet & 0xC0) == 0
        yield sextet

def to_base64(byte_string):
    return bytes(map(lambda sextet: TO_BASE64[sextet], to_base64_iter(byte_string)))

def to_base_64(string):
    return to_base64(string.encode('utf-8')).decode('utf-8')

def from_base64_iter(buf):
    mask_upper  = {}
    mask_lower  = {}
    shift_upper = {}
    shift_lower = {}

    buf_size = len(buf)
    octet = 0
    rem   = 0
    bits_in_rem = 0
    i = 0
    while i < buf_size:
        if bits_in_rem == 6:
            # We have not reached not processed a 
            # batch of 4 setets yet.
            upper = rem << 2
            lower = (buf[i] & 0x30) >> 4
            octet = upper | lower
            rem = buf[i] & 0x0F
            bits_in_rem -= 2
            i += 1

            yield octet
        elif bits_in_rem == 4:
            # We have not reached not processed a 
            # batch of 4 setets yet.
            upper = rem << 4
            lower = (buf[i] & 0x3C) >> 2
            octet = upper | lower
            rem = buf[i] & 0x03
            bits_in_rem -= 2
            i += 1

            yield octet
        elif bits_in_rem == 2:
            # We have not reached not processed a 
            # batch of 4 setets yet.
            upper = rem << 6
            lower = (buf[i] & 0x3F) >> 0
            octet = upper | lower
            rem = buf[i] & 0x00
            bits_in_rem -= 2
            i += 1

            yield octet
        else:
            assert bits_in_rem == 0, 'bits_in_rem != 0.'
            # We have processed a batch of 4 sextets. Now we
            # set up for the next batch of 4 sextets.
            upper = 0
            lower = 0
            octet = upper | lower
            rem = buf[i] & 0x3F
            bits_in_rem = 6
            i += 1


    if bits_in_rem > 0:
        # we have consumed every byte but there are
        # still unprocessed bits remaining.
        octet = rem
        rem = 0
        bits_in_rem = 0

        yield octet
    """
    shift_upper = 2
    shift_lower = 4
    mask_upper  = 0x3F
    mask_lower  = 0x30
    i = 0
    while True:
        if (i < buf_size-1) and (shift_lower >= 0):
            upper = (buf[i] & mask_upper) << shift_upper
            lower = (buf[i+1] & mask_lower) >> shift_lower
            octet = upper | lower
            mask_upper >>= 2
            mask_lower = mask_lower | (mask_lower >> 2)
            shift_upper += 2
            shift_lower -= 2
            i += 1

            yield octet
        elif (i < buf_size-1) and (shift_lower < 0):
            # We have consumed 3 bytes, or 4 sextets.
            # So we reset the masks.
            shift_upper = 2
            shift_lower = 4
            mask_upper = 0x3F
            mask_lower = 0x30
            i += 1
        elif (shift_lower > 0):
            octet = buf[i-1] & mask_lower
            shift_lower = 0
            yield octet
        else:
            break
    """


def from_base64(byte_string):
    try:
        sextets = []
        for char in byte_string:
            sextets.append(FROM_BASE64[char])
    
        return bytes(from_base64_iter(sextets))
    except:
        raise Exception("Invalid Base64 string.")

def from_base_64(base64_string):
    return from_base64(base64_string.encode('utf-8')).decode('utf-8')
