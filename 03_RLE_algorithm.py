# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#aaaaabbbcccc -> 5a3b4c
#5a3b4c -> aaaaabbbcccc


with open(r'compression.txt', 'r') as data:
    text_to_comp = data.read()

with open(r'recovery.txt', 'r') as data:
    text_to_rec = data.read()

def compression_data(to_comp):          # Сжатие данных
    compression_str = ''
    count = 1
    if not to_comp:
        return ''
    for i in range(1, len(to_comp)):
        if to_comp[i] == to_comp[i-1]:
            count+=1
        else:
            if count == 1:
                compression_str += to_comp[i-1]
            else:
                compression_str += str(count) + to_comp[i-1]
                count = 1
    else:
        if count == 1:
            compression_str += to_comp[i]
        else:
            compression_str += str(count) + to_comp[i]
    return compression_str

def recovery_data(to_rec):
    recovery_str = ''
    count = ''
    for item in to_rec:
        if item.isdigit():
            count += item
        else:
            if not count:
                recovery_str += item
            else:
                recovery_str += int(count) * item
                count = ''
    return recovery_str


print (f' После сжатия данных: {compression_data (text_to_comp)}')
print (f' После восстановления данных: {recovery_data(text_to_rec)}')


with open(r'after_compression.txt', 'w') as res:
    res.write(f'Data after string compression {text_to_comp}:\n')
    res.write(compression_data (text_to_comp))

with open(r'after_recovery.txt', 'w') as res:
    res.write(f'Data after row recovery {text_to_rec}:\n')
    res.write(recovery_data(text_to_rec))
