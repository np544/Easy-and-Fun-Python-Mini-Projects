customdomain={'gmail':'Google','outlook':'Microsoft','hotmail':'Microsoft','yahoo':'Yahoo'}
email=input("Enter your email id\n")
user_name=email[:email.index('@')].capitalize()
domain=email[email.index('@')+1:email.index('.')]
if(domain in customdomain.keys()):
    print(f'Hey {user_name}, I see your email is registered with {domain}. Thats cool!')
else:
    print(f'Hey {user_name}, looks like you have got your own custom setup at {domain} or it may be that I havent included it in the list :). Impressive!')

