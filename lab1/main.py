NameBloger = input("Введите ваше имя: ") # Запрос у пользователя Имени.

NumberSubscribers = int(input("Введите количество подписчиков: ")) # Запрос у пользователя количество подписчиков.

YoutubeLink =  input("Введите ссылку на ваш ютуб канал: ") # Запрос у пользователя ссылки на ютуб канал.

print(f"Привет, {NameBloger}!") # Вывод в консоль приветствия с именем пользователя.

if NumberSubscribers >= 100000 and NumberSubscribers < 1000000:
    print("У вас уже есть серебряная кнопка!")
elif NumberSubscribers >= 1000000:
    print("У вас уже есть серебряная и золотая кнопки!")
elif NumberSubscribers < 100000 and NumberSubscribers >= 0:
    print("У вас пока недостаточно подписчиков для кнопки Ютуба!")
else:
    print("Error! Введите правильное значение!")

print(f"Подписаться на канал {NameBloger}, вот ссылка: {YoutubeLink}") # Вывод в консоль сообщения "подписаться на канал" и "ссылка на канал".