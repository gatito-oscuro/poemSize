import tkinter
from tkinter import messagebox, END
import re
import requests
import lxml
from bs4 import BeautifulSoup

window = tkinter.Tk()
window.title("poemSize")
window.geometry("800x500")


def stress():
    url_begin = "https://где-ударение.рф/в-слове-"
    prepositions = {'на', 'о', 'об', 'про', 'под', 'над', 'за', 'из', 'до', 'без', 'во', 'вне', 'для', 'ко', 'меж',
                    'от', 'пред', 'перед', 'передо', 'по', 'при', 'со', 'у', 'чрез', 'то', 'и', 'или'}
    vowels = 0  # счетчик гласных
    res = ''  # строка для хранения введенного четверостишия с расставленными ударениями
    strings = poem_text.get("1.0", END).split('\n')
    for string in strings:
        words = re.findall(r'[а-я-]+', string.lower())  # разбиение введенного четверостишия на слова
        for word in words:
            # формирование url запроса для определения ударения в слове
            url = url_begin + word + '/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            rule = soup.find('div', class_='rule')
            if rule is not None:
                # результат запроса формируется в соответствии с особенностями источника
                # проверяемое слово с ударением, выделенным заглавной буквой, стоит после знака '—'
                res = res + (rule.text[rule.text.find('—') + 2: rule.text.find('.')]) + ' '
            else:
                # если слово состоит из одного слога
                if word not in prepositions:
                    for letter in word:
                        if letter in 'аоуэыиеёюя':
                            vowels += 1
                    if vowels == 1:
                        for letter in word:
                            if letter in 'аоуэыиеёюя':
                                word = word.replace(letter, letter.upper())
                res = res + word + ' '
                vowels = 0
        res = res + '\n'
    stress_text.delete("1.0", END)
    stress_text.insert("1.0", res)


def calculate():
    # списки возможных ударных слогов для каждой размерности стихотворения
    iamb = {2, 4, 6, 8, 10, 12}
    trochee = {1, 3, 5, 7, 9, 11}
    dactyl = {1, 4, 7, 10, 13}
    amphi = {2, 5, 8, 11, 14}
    anapest = {3, 6, 9, 12, 15}

    i = 0

    # счетчики совпадений с каждым из видов размерности
    cur_iamb = 0
    cur_trochee = 0
    cur_dactyl = 0
    cur_amphi = 0
    cur_anapest = 0

    res = stress_text.get("1.0", END)
    if res == ("" or "\n" or "\n\n"):
        messagebox.showinfo(title="Ошибка", message="Поле с ударениями пусто")
    else:
        # подсчет количества совпадений с каждым видом размерности
        while i < len(res):
            syl = 0
            while res[i] != '\n':
                if res[i] in 'аоуэыиеёюя':
                    syl += 1
                elif res[i] in 'АОУЭЫИЕЁЮЯ':
                    syl += 1
                    if syl in iamb:
                        cur_iamb += 1
                    if syl in trochee:
                        cur_trochee += 1
                    if syl in dactyl:
                        cur_dactyl += 1
                    if syl in amphi:
                        cur_amphi += 1
                    if syl in anapest:
                        cur_anapest += 1
                i += 1
            i += 1
        max_match = max(cur_iamb, cur_trochee, cur_dactyl, cur_amphi, cur_anapest)

        # вывод результата анализа размера введенного четверостишия пользователю
        result = "Наиболее вероятный размер: "
        if max_match == 0:
            result = "Не удалось определить размер. Возможно введен некорректный текст"
        elif max_match == cur_iamb:
            result += 'ямб'
        elif max_match == cur_trochee:
            result += 'хорей'
        elif max_match == cur_dactyl:
            result += 'дактиль'
        elif max_match == cur_amphi:
            result += 'амфибрахий'
        elif max_match == cur_anapest:
            result += 'анапест'
        else:
            result = "Какая-то непонятная ошибка"
        messagebox.showinfo(title="Результат", message=result)


frame = tkinter.Frame()
# Widgets
poem_label = tkinter.Label(frame, text="Стихотворение", font=("Ariel", 12))
poem_text = tkinter.Text(frame,  width=34, height=18, font=("Ariel", 12), borderwidth=8)
stress_label = tkinter.Label(frame, text="Ударения", font=("Ariel", 12))
stress_text = tkinter.Text(frame, width=34, height=18, font=("Ariel", 12), borderwidth=8)
stress_button = tkinter.Button(frame, text="Расставить ударения", font=("Papyrus", 12), command=stress)
calculate_button = tkinter.Button(frame, text="Определить размер", font=("Papyrus", 12), command=calculate)

# Placing
poem_label.grid(row=0, column=0, padx=8, sticky="nsew")
stress_label.grid(row=0, column=1, padx=8, sticky="nsew")
poem_text.grid(row=1, column=0, sticky="w")
stress_text.grid(row=1, column=1, sticky="w")
stress_button.grid(row=2, column=0, pady=8, sticky="ns")
calculate_button.grid(row=2, column=1, pady=8, sticky="ns")

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)

frame.pack(anchor="center")

window.mainloop()
