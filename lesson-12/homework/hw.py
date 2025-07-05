import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    for number in range(start, end):
        if is_prime(number):
            result.append(number)

def threaded_prime_checker(start, end, num_threads):
    threads = []
    results = [[] for _ in range(num_threads)]
    step = (end - start) // num_threads

    for i in range(num_threads):
        sub_start = start + i * step
        sub_end = start + (i + 1) * step if i != num_threads - 1 else end
        t = threading.Thread(target=check_primes, args=(sub_start, sub_end, results[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Birlashtiramiz va tartiblaymiz
    all_primes = []
    for sublist in results:
        all_primes.extend(sublist)

    return sorted(all_primes)

# 🧪 Sinov
start = 10
end = 100
num_threads = 4
print("Tub sonlar:", threaded_prime_checker(start, end, num_threads))




import threading
from collections import defaultdict

def count_words(lines, word_counts):
    local_counts = defaultdict(int)
    for line in lines:
        words = line.strip().split()
        for word in words:
            local_counts[word.lower()] += 1
    word_counts.append(local_counts)

def threaded_word_counter(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    threads = []
    results = []
    chunk_size = len(lines) // num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        chunk = lines[start:end]
        result = []
        t = threading.Thread(target=count_words, args=(chunk, result))
        threads.append((t, result))
        t.start()

    final_counts = defaultdict(int)
    for t, result in threads:
        t.join()
        if result:
            for word, count in result[0].items():
                final_counts[word] += count

    return dict(final_counts)

# 🧪 Sinov (test faylni oldin yarating)
file_path = "sample.txt"  # Bu fayl mavjud bo‘lishi kerak
word_stats = threaded_word_counter(file_path)
print("So‘zlar statistikasi:")
for word, count in word_stats.items():
    print(f"{word}: {count}")

