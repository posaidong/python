import requests
from enchant.checker import SpellChecker


# Sometimes this function is not accurate to recognize if it is english,
# for example: it recognizes 'Faça Um para réplica' as english
def is_in_english(quote):
    d = SpellChecker("en_US")
    d.set_text(quote)
    errors = [err.word for err in d]
    return False if ((len(errors) > 4) or len(quote.split()) < 3) else True


# translate to english, return a Tuple 'Status,Text'
def translate(txt):

    # if is_in_english(txt):
    #     print('is english, return directly: ' + txt)
    #     return True, txt
    # else:
    #     print('translating from google...' + txt)

    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=en&dt=t&q=" + txt;
    response = requests.get(url)
    translatedTxt = ''
    isSuccess = False
    if response.status_code == 200:
        translatedTxt = response.json()[0][0][0]
        isSuccess = True
    else:
        print('ERROR: ' + response.status_code + ',' + response.text)
    return isSuccess, translatedTxt


def main():
    txt = "Impossible de connecter mes enceintes , dès que je lance l,'appli je me retrouve bloqué sur un menu qui m'emmene vers mes paramètres , pour activer la loca alors quelle est dejà activé , c'est pas ouf"
    print(translate(txt))


if __name__ == '__main__':
    main()
