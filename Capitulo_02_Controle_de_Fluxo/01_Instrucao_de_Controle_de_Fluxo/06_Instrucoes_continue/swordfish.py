while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue  # Volta para o início do loop se o nome não for 'Joe'
    
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break  # Sai do loop se a senha estiver correta

print('Access granted.')