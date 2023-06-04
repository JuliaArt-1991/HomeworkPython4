# Задача 34
def beat(song):
    sg = song.lower().split()
    f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    tmp = f(sg[0])
    if all([f(i) == tmp for i in sg]):
        return 'Парам пам-пам'
    return 'Пам парам'


print(beat('пара-ра-рам рам-пам-папам па-ра-па-да'))
