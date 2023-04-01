#___________________Data Encryption Standard_____________https://en.wikipedia.org/wiki/Data_Encryption_Standard__________	



#------	Permutation vectors	https://en.wikipedia.org/wiki/DES_supplementary_material ---------------


# the initial and final permutation vectors have no cryptographic significance
initial_permutation_vector = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
 

# used for expanding 32-bit input to 48-bit output
expansion_vector = [32, 1, 2, 3, 4, 5, 4, 5,
        6, 7, 8, 9, 8, 9, 10, 11,
        12, 13, 12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21, 20, 21,
        22, 23, 24, 25, 24, 25, 26, 27,
        28, 29, 28, 29, 30, 31, 32, 1]

# used for shuffling 32-bit blocks 
permutation_vector = [16,  7, 20, 21,
       	29, 12, 28, 17,
       	1, 15, 23, 26,
       	5, 18, 31, 10,
       	2,  8, 24, 14,
       	32, 27,  3,  9,
       	19, 13, 30,  6,
       	22, 11,  4, 25]

# used for selecting which 56 bit from the key to be used
choose_key_bits_vector = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# used for selecting 48-bit subkeys
subkey_select_vector = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]
 
# used for converting 48-bit blocks to 32-bit blocks by successively substituting 6-bit input with 4-bit output
substitution_boxes = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
 
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
 
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
 
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
 
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
 
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
 
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
 
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
 

# the inverse of the initial permutation vector (number 1 in IP at pos 40, number 2 in IP at pos 8...)
final_permutation_vector = [40, 8, 48, 16, 56, 24, 64, 32,
	    39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]

# specifies how many left rotations should be applied to each 28-bit halfs of the 56-bit key
left_rotations = [1, 1, 2, 2,		
        	2, 2, 2, 2,
        	1, 2, 2, 2,
                2, 2, 2, 1]


# for encryption of messages larger than 64 bits a mode of operation is needed in conjunction with DES https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation

def Permutation(key, permutation_choice):
	permuted = 0
	for i in permutation_choice:
		permuted <<= 1 # "selecting" next bit
		permuted |= ((key >> (i - 1)) & 1) # if the keys bit at position i is set, set permuted bit
	return permuted


def Substitution(block): # substituts 48-bit block with a 32-bit one
	
	# the outer most bits of the 6 bits segments determine substitutionbox row and the other bits determine collumn
	
	substituted = 0
	
	for i in range(8):
		substituted <<= 4
		#taking the outer and inner bits of each 6 bit segments to substitute them
		substituted |= (substitution_boxes[i][(block >> (6*i)) & 0b1 | (block >> (6*i+4) & 0b10)][(block >> (6*i+1) & 0b1111)])
	
	return substituted


def Expansion(block): # expands 32-bit block to a 48-bit one
        expanded = 0
        for i in expansion_vector:
	        expanded <<= 1 # "selecting" next bit
        	expanded |= ((block >> (i - 1)) & 1) # if the keys bit at position i is set, set expanded bit
        return expanded & 0xffffffffffff
	

#	https://en.wikipedia.org/wiki/Circular_shift
def LeftRotate(block, n): # rotates 28-bit block so that the 1st bit becomes the 2nd bit, the 2nd become the 1st, the third becomes the 2nd....
	return ((block << n) | (block >> (28 - n))) & 0xffffffffffffff #  (value << number_rotations)  | (value >> (width-number_rotations)) & 2 pow width -1

def Chunks64ToText():
        pass

def des(key, message, decrypt):
        keys = []
        
        key = Permutation(key, choose_key_bits_vector) # only 56 of the keys bits will be used

        left = (key >> 28) & 0xfffffff
        right = key & 0xfffffff
        
        for i in range(16):
                right = LeftRotate(right, left_rotations[i])
                left = LeftRotate(left, left_rotations[i])

                left_right_concat = ((left << 28) | right) # concatinating left and right halves
                #       56-bit to 48-bit
                keys.append(Permutation(left_right_concat, subkey_select_vector))
        
        # encoding or decoding

        
        message_chunks = []
        ciphered_chunks = []

        if decrypt:
                keys.reverse()  # structure of feistel cipher allows for decryption to be near identical encryption 
                message = int(message, 16)
                while message.bit_length() > 0:
                        message_chunks.append(message & 0xffffffffffffffff)
                        message >>= 64
                message_chunks.reverse()

        else:
                message = message.encode('iso-8859-1')

                n = len(message) % 8

                if n > 0:
                        message += bytes([0]) * (8 - n)
                
                print(message)


                for i in range(0, len(message), 8):
                        chunk = 0
                        for j in range(8):
                                chunk |= message[i+j]
                                chunk <<= 8
                        message_chunks.append(chunk >> 8)
        

        for chunk in message_chunks:
                cipher_chunk = Permutation(chunk, initial_permutation_vector)
                left = (cipher_chunk >> 32) & 0xffffffff
                right = cipher_chunk & 0xffffffff

                for i in range(16):
                        tmp = right
                        right = Expansion(right)
                        right = right ^ keys[i]
                        right = Substitution(right)
                        right = Permutation(right, permutation_vector)
                        right = right ^ left
                        left = tmp
                cipher_chunk = ((right << 32) | left ) & 0xffffffffffffffff
                cipher_chunk = Permutation(cipher_chunk, final_permutation_vector)
                
                for i in range(8):
                        ciphered_chunks.append((cipher_chunk >> (56)) & 0xff)
                        cipher_chunk <<= 8
        
        ciphered_value = 0

        for i in ciphered_chunks:
                ciphered_value <<= 8
                ciphered_value |= i

        print(f'hex representation of encrypted/decrypted message: {hex(ciphered_value)}')
        ciphered_chunks = bytes(ciphered_chunks).decode('iso-8859-1')
        
        return ciphered_chunks
        
def main():
        key = int(input('enter 64 bit number in hex e.g ffffffffffffffff> '), 16)
        message = input('enter text message (if u wanna decrypt use the encrypted message\'s hex representation) > ')
        decrypt = 'y' in input('do you want to decrypt (y/n) ? > ')

        print(f'text representation of encrypted/decrypted message: {des(key,message, decrypt)}')
                        
        

if __name__ == '__main__':
    main()