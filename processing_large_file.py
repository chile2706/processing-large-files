# Chi Le
# le000422

PUN_CHARS = '[(.,;:\")]/]!?\n'
IGNORE_FILE = 'data/ignore_words.txt'
def remove_punctuation_and_lower(word: str):
    word = word.lower()
    remove = ""
    for val in word:
        if val in PUN_CHARS:
            remove = remove + ""
        else:
            remove = remove + val
    return remove

def get_words_from_file(source_filename, ignored_words_list=[]):
    word_list = []
    with open(source_filename, 'r') as fp:
        for line in fp:
            line = line.split(',')
            for ele in line:
                ele = ele.split(' ')
                for word in ele:
                    word = remove_punctuation_and_lower(word)
                    if not(word in ignored_words_list or word == ''):
                       word_list.append(word)
    return word_list

def get_word_frequency(word_list):
    count = {}
    for key in word_list:
        if key in count:
            count[key] += 1
        else:
            count[key] = 1
    return count

def save_popular_words(word_frequency, destination_file, k=10):
    count = list(word_frequency.values())
    count.sort()
    with open(destination_file,'w') as fp:
        for i in range(1,k+1):
            for key, value in word_frequency.items():
                if value == count[-i]:
                    fp.write(str(key)+': '+str(value)+'\n')
def main():
    type_arr = ['Fake', 'True']
    for news_type in type_arr:
        source_file = f'data/{news_type}.csv'
        popular_words_file = f'data/{news_type}_popular_words.txt'

        ignored_words_list = get_words_from_file(IGNORE_FILE)
        word_list = get_words_from_file(source_file, 
ignored_words_list=ignored_words_list)
        word_frequency = get_word_frequency(word_list)
        # Save the top k most popular words
        save_popular_words(word_frequency, popular_words_file)
if __name__ == "__main__":
    main()
