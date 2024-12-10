#def sort_word(text,root):
 #   str(root).count()
  #  for j in text:
   #     if j == root



def single_root_words(root_word,*other_words):
    same_words =[]
    count = 0
    for i in other_words:
        count = str(i).lower().count(root_word.lower())
        if count > 0:
            same_words.append(i)
            count = 0
            print(i,"---Добавили слова---")
    return same_words

result = single_root_words("кот","Котенок","Котичка","Котик","Кошка","Котераптор","роБоКото")
print(result)

