from collections import defaultdict

text = open("text.txt", "r", encoding="UTF-8").read()

print(f"длина текста до обработки: {len(text)}")

text = text.lower()

allowed_chars = set("abcdefghijklmnopqrstuvwxyz")
text_clean = [c for c in text if c in allowed_chars]

unique_chars = set(text_clean)
assert len(unique_chars) <= 32, "Слишком много уникальных символов"

text_clean = "".join(text_clean)

print(f"длина текста после обработки: {len(text_clean)}")


# 1
char_freq = defaultdict(int)
for c in text_clean:
    char_freq[c] += 1

print("Частота символов:")
for char, freq in sorted(char_freq.items()):
    print(f"{char}: {freq / len(text_clean):.4f}")

pair_freq = defaultdict(int)
for i in range(len(text_clean) - 1):
    pair = text_clean[i] + text_clean[i+1]
    pair_freq[pair] += 1

print("\nЧастота пар символов (топ-5):")
for pair, freq in sorted(pair_freq.items(), key=lambda x: -x[1])[:5]:
    print(f"{pair}: {freq}")



# 2
import heapq
from collections import Counter
from math import log2


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_huffman_codes(node, current_code="", codes=None):
    if node is None:
        return

    if codes is None:
        codes = dict()

    if node.char is not None:
        codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", codes)
    build_huffman_codes(node.right, current_code + "1", codes)
    return codes


# Построение кодов
freq_dict = Counter(text_clean)
huffman_tree = build_huffman_tree(freq_dict)
huffman_codes = build_huffman_codes(huffman_tree)

# Закодированный текст
encoded_huffman = "".join([huffman_codes[c] for c in text_clean])

# Сравнение с равномерным кодированием (5 бит на символ)
uniform_bits = len(text_clean) * 5
huffman_bits = len(encoded_huffman)

print(f"Равномерное кодирование: {uniform_bits} бит")
print(f"Кодирование Хаффмана: {huffman_bits} бит")
print(f"Экономия: {uniform_bits - huffman_bits} бит")

# Энтропия по Шеннону
entropy = -sum((freq / len(text_clean)) * log2(freq / len(text_clean)) for freq in freq_dict.values())
print(f"Энтропия Шеннона: {entropy:.2f} бит/символ")



# 3
def lzw_compress(text):
    dictionary = {chr(i): i for i in range(256)}  # Имитация начального словаря
    next_code = 256
    s = text[0]
    compressed = []

    for c in text[1:]:
        sc = s + c
        if sc in dictionary:
            s = sc
        else:
            compressed.append(dictionary[s])
            dictionary[sc] = next_code
            next_code += 1
            s = c

    compressed.append(dictionary[s])
    return compressed


# Кодирование текста
compressed = lzw_compress(text_clean)
lzw_bits = len(compressed) * 12  # Предположим, что коды 12-битные

print(f"LZW: {lzw_bits} бит")
print(f"Сравнение с Хаффманом: {lzw_bits - huffman_bits} бит")