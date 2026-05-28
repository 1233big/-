#加密/解密后台实现过程
def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.' #判断偏移量是否是一个数

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.' #判断偏移量是否合规

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift #解密，默认加密

    shifted_alphabet = alphabet[shift:] + alphabet[:shift] #偏远后的字串
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()) #为原始字串和偏移字串创建一个映射表
    encrypted_text = text.translate(translation_table) #调用映射表加密/解密字串
    return encrypted_text

#加密函数
def encrypt(text, shift):
    return caesar(text, shift) 

#解密函数
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
