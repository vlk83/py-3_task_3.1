import json

# страна/территория: [файл, кодировка, "description"-тип] ------------------------------------------
countries_files = {
    'africa': ['newsafr.json', 'utf8', '1'],
    'cyprus': ['newscy.json', 'koi8-r', '1'],
    'italy' : ['newsit.json', 'cp1251', '2']
    }

# функция для создания списка слов из всех description'ов файла ------------------------------------
def all_descriptions_word_list(country):
    
    with open(countries_files[country][0], 'r', encoding=countries_files[country][1]) as f:
        news = json.load(f)
        all_descriptions_word_list = []
        for _ in news["rss"]["channel"]["item"]:
            if countries_files[country][2] == '1':
                all_descriptions_word_list.extend( _ ["description"]["__cdata"].split())
            elif countries_files[country][2] == '2':
                all_descriptions_word_list.extend( _ ["description"].split())
    return all_descriptions_word_list
    
# функция для создания частотного словаря для всех слов длиннее 6 символов -------------------------
def frequency_dictionary(all_descriptions_word_list):
    
    all_descriptions_word_dict = {}
    for word in all_descriptions_word_list:
        if len(word)>6 and word.isalpha():
            if word in all_descriptions_word_dict:
                value = all_descriptions_word_dict[word]
                all_descriptions_word_dict[word] = value + 1
            else:
                all_descriptions_word_dict[word] = 1
    return all_descriptions_word_dict

# функция для вывода топ 10 слов частотного словаря ------------------------------------------------
def print_top_10_words(all_descriptions_word_dict):
    
    count10 = sorted(set(all_descriptions_word_dict.values()), reverse=True)[9]
    
    for word, count in sorted(all_descriptions_word_dict.items(), key=lambda x: x[1], reverse=True):
        if count >= count10:
            print (word, count)
    print('------------------------------------------------')

#-------
for country in countries_files.keys():
    print('топ 10 слов в файле {} и их частота:\n'.format(countries_files[country][0]))
    print_top_10_words(frequency_dictionary(all_descriptions_word_list(country)))