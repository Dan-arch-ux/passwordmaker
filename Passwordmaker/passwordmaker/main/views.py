from django.shortcuts import render
import secrets
import string

def generate_password(lenghth ,lowercase, uppercase, numbers, symbols):
    characters =''
    try:
     if lowercase:
        characters += string.ascii_lowercase
        if uppercase:
            characters += string.ascii_uppercase
            if numbers:
                characters += string.digits
                if symbols:
                    characters += string.punctuation
     elif uppercase:
       characters += string.ascii_uppercase
       if numbers:
           characters +=string.digits
           if symbols:
               characters += string.punctuation
     elif numbers:
        characters += string.digits
        if symbols:
            characters += string.punctuation
     elif symbols:
        characters += string.punctuation
     password = ''.join(secrets.choice(characters) for _ in range(lenghth))
     return password
    except IndexError:
        return characters


def index(request):
    password = ''
    if request.method == 'POST':
        letters = request.POST.getlist('include-lowercase')
        uppercase = request.POST.getlist('include-uppercase')
        numbers = request.POST.getlist('include-numbers')
        symbols = request.POST.getlist('include-symbols')
        length = int(request.POST.get('length'))
        password = generate_password(length,letters,uppercase,numbers,symbols)
    dict = {
        'password': password,
        }
    return render(request, 'main/index.html', dict)
