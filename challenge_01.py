file = open('./message_01.txt', 'r')

array_words = file.readline().split(" ")

file.close()

words_counter = dict()
order = 1
for word in array_words:

    word.lower()
    word = word.replace('\n','')

    if word in words_counter:
        words_counter[word]['counter'] += 1
    else:
        words_counter[word] = {
            'word': word,
            'counter': 1,
            'order': order
        }
        order += 1

# print('words_counter: ',words_counter)
final_text = ""
for value in words_counter.values():
    print('value',value)
    final_text += value['word'] + str(value['counter'])

print(final_text)

