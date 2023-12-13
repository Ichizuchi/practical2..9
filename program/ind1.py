def all_perms(arr):
    if len(arr) == 1:
        return [arr]
    else:
        a = arr[0]  # Первый элемент списка
        p = all_perms(arr[1:])  # Все перестановки
        r = []
        for pp in p:
            for i in range(len(pp)):
                tmp = pp[0:i] + [a] + pp[i:]
                r.append(tmp)
            r.append(pp + [a])
        return r


n = int(input("N="))
print(all_perms([i for i in range(1, n + 1)]))
