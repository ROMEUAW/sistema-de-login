lista = [1,2,3,4,5]
it = iter(lista)
while True:
    try:
        e = next(it)
        print(e)
    except StopIteration:
        print("Não há mais elementos")
        break



