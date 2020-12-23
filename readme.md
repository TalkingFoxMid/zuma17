# Спецификация игры zuma_17
https://github.com/TalkingFoxMid/zuma17
## Уникальные фичи:
- Геймплей
    - Несколько уровней.
    - Движущиеся по конвееру шары.
    - Лягушка, умеющая стреляться шарами.
    - Столкновение летающих шаров с конвеерными.
    - Система очков.
    - Исчезновение кластера шаров одного цвета,
    при попадении в него шаром того же цвета, при условии, что
      суммарный размер кластера после попадения больше или равен 3.
    
    - Физика конвеерных шаров (если шары слишком близко, то тот, что ближе
      к концу пути, выталкивается вперёд, причём тем быстрее, чем
      меньше расстояние между шарами). Последний шар всегда движется с постоянной скоростью. 
      Шары, которые не подталкиваются ничем сзади, начинают медленно отъезжать назад.
    - Наличие комбинаций. После исчезновения кластера шаров одного цвета, возникает пустое пространство.
      Через некоторое место произойдёт столкновение двух частей конвеера, а в месте столкновения, если будет больше 2
      шаров одного цвета, они также исчезнут.
    - Возможность проиграть, если хотя бы один из шаров достигнет конца пути.
    - Возможность победить, если на карте больше не останется конвеерных шаров.
    - Три способа взаимодействия пользователя с игрой:
    1) Выстрел летающим шаром цвета, который игрок может видеть
    под ногами у жабки. Осуществляется нажатием левой кнопки мыши.
    2) Циклическая смена шаров. Первый переходит во второй, второй в третий, третий в первый.
    Осуществляется путём нажатия игроком правой кнопки мыши.
    3) Полный сброс шаров. Имеет перезарядку 10 секунд. Осуществляется путём нажатия игроком
    колёсика мыши.
- Интерактивное меню.
    - Летающие шары, которые сталкиваются друг с другом.
    - Плавающий бэк-граунд.
    - Жабка и шарики, которые крутятся вокруг неё.
    - Иконка метасплойта.
    - Кнопки, реагирующие при наведении на них курсора.
- Красивый минималистичный дизайн, оформленный в программе Paint.
    - Нарисованные самостоятельно элементы графического интерфейса.
    - Нарисованные карты, уровни.
- Зал славы.
    - Возможность после победы вписать свой ник, и, если результат оказался рекордным,
    попасть в зал славы.
    - Зал славы отражает в себе только лучших игроков, абсолютные рекорды по каждому из уровней.
    - Зал славы содержит в себе место для девяти уровней (пока в игре присутствует лишь три).
    - В каждой ячейке зала славы отражается ник игрока, поставившего рекорд на данном уровне
    и непосредственно очки, которые ему удалось набрать.
    - Нумерация ячеек происходит по принципу чтения книги (Библии).
    - Возможность сбежать из зала славы с помощью кнопки с оригинальным дизайном.
- Возможность поставить паузу.
    - Анимация поставления игры на паузу.
- Кадило.