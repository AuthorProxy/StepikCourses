# https://stepik.org/lesson/3380/step/2?unit=963
# Sample Input 1:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
# Sample Output 1:
# *d*%*d*#*d*
# dacabac
# Sample Input 2:
# dcba
# badc
# dcba
# badc
# Sample Output 2:
# badc
# dcba

crypt_template = input()
substitution_template = input()
str_to_crypt = input()
str_to_decrypt = input()

encryption_dict = dict(zip(crypt_template, substitution_template))
decryption_dict = dict(zip(substitution_template, crypt_template))

str_to_crypt_result = ""
str_to_decrypt_result = ""
for letter in str_to_crypt:
    str_to_crypt_result += encryption_dict[letter]

for letter in str_to_decrypt:
    str_to_decrypt_result += decryption_dict[letter]

print(str_to_crypt_result)
print(str_to_decrypt_result)
