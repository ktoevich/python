import webbrowser

def validator(func):
    def wrapper(url):
        if '.' in url:
            func()
        else:
            print("Неверный url")
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)

open_url('https://youtube.com')