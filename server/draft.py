# from cryptography.fernet import Fernet
 
# # Генерация ключа
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)
 
# # Шифрование данных
# data = b"Hello, world!"
# encrypted_data = cipher_suite.encrypt(data)
 
# # Дешифрование данных
# decrypted_data = cipher_suite.decrypt(encrypted_data)
 
# print("Исходные данные:", data)
# print("Зашифрованные данные:", encrypted_data)
# print("Расшифрованные данные:", decrypted_data)

from ast import literal_eval

print(literal_eval("[('Здаров, как дела?', 'text', '21:36 05.01.2025'), ('Здаров, как дела?', 'text', '21:36 05.01.2025')]"))