1. is_prime(n) funksiyasi
is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

Misollar:
Kiritish:
4
Natija:
False
(Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)

Kiritish:
7
Natija:
True
(Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.)



def digit_sum(k):
    s = 0
    while k > 0:
        s += k % 10
        k //= 10
    return s



def powers_of_two(N):
    p = 2
    while p <= N:
        print(p, end=' ')
        p *= 2
