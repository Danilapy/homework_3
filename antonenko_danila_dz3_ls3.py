from random import randrange


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    joke_list = []
    for joke in range(n):
        joke = ' '.join([nouns[randrange(len(nouns))], adverbs[randrange(len(adverbs))], adjectives[randrange(len(adjectives))]])
        joke_list.append(joke)
        print(joke_list)
    print(joke_list)




get_jokes(5)