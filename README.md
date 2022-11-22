# Brain-games
### Проект содержит 5 игр:
1. brain-calc - в игре предлагается угадать результат вычислений двех числел. Используются операции сожения, вычитания и умножения.
2. brain-even - пользователю выводится случайное число на экран, его задача ответить является ли оно четным.
3. brain_gcd - необходимо угадать наибольший общий делитель.
4. brain-prime - на экран выводится случайное число, цель игры угадать является ли оно простым.
5. brain-progression - пользователю выводится арифметическая прогрессия, с пропущеным числом, цель игры угадать какое число пропущено.

### Установка необходимых пакетов и запуск игр

 Для корректной работы проекта, необходимо установить:
- python - 3.6.1 версии и выше
- библиотеку prompt версии 0.4.1
- poetry - при помощи команды ```make install```

Запуск игр осуществляется командами:
- ```make brain-calc``` - запускает игру brain-calc и далее так же:
- ```make brain-even```
- ```make brain_gcd```
- ```make brain-prime```
- ```make brain-progression```

brain-prime
[![brain-even](https://asciinema.org/a/JomavCUlqvIH0MpTXxSXrSsWz.svg)](https://asciinema.org/a/JomavCUlqvIH0MpTXxSXrSsWz)
brain-calc
[![asciicast](https://asciinema.org/a/6oBmqL24NU3n19GasfjHOUIdu.svg)](https://asciinema.org/a/6oBmqL24NU3n19GasfjHOUIdu)
game-progression
[![asciicast](https://asciinema.org/a/h0I2dthtF8Qh5wPw8VrR6ZUa6.svg)](https://asciinema.org/a/h0I2dthtF8Qh5wPw8VrR6ZUa6)
game-gcd
[![asciicast](https://asciinema.org/a/zKxExmGTk6hmvaqmuu9tFJb2J.svg)](https://asciinema.org/a/zKxExmGTk6hmvaqmuu9tFJb2J)

### Hexlet tests and linter status:
[![Actions Status](https://github.com/pavel-teglev/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/pavel-teglev/python-project-49/actions)
<a href="https://codeclimate.com/github/pavel-teglev/python-project-49/maintainability"><img src="https://api.codeclimate.com/v1/badges/ed98c72993af0a4af8a0/maintainability" /></a>
<a href="https://codeclimate.com/github/pavel-teglev/python-project-49/test_coverage"><img src="https://api.codeclimate.com/v1/badges/ed98c72993af0a4af8a0/test_coverage" /></a>