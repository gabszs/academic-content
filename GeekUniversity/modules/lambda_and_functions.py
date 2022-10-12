def dict_to_list(lst_dct):
    return list(map(lambda dct: list(dct), lst_dct))


dct = [{'gabriel': 17}, {'gab': 15}, {'riel': 21}, {'abr': 12}, {'gabrl': 23}]

year_to_month = lambda dct_nome: {keys: values * 12 for keys, values in dct_nome.items()}
names_months = map(year_to_month, dct)


age_minor_map = map(lambda dct_nome: list(dct_nome.values())[0] < 18, dct)
age_minor_filter = filter(lambda dct_nome: list(dct_nome.values())[0] < 18, dct)

lst_order_name = sorted(dct, key=lambda dct_nome: list(dct_nome.values())[0])

musics = [{"title": "alelek", "tocou": 2},
          {"title": "papapapa", "tocou": 33},
          {"title": "ai meu deus", "tocou": 4},
          {"title": "babilonia", "tocou": 1},
          {"title": "break it", "tocou": 77}]

# print(max(musics, key=lambda musica: musica['tocou'])["title"])

rlst = sorted(musics, key=lambda musica: musica['tocou'], reverse=True)

print(musics)
max = 0
for keys, musicas in enumerate(musics):
    print(keys)
    print(musicas[keys])
    if musicas['tocou'] > max:
        max = musicas['tocou']
        most_pmusic = musicas['title']
    # max = musicas['tocou'], most_pmusic = musicas['title'] if musicas['tocou'] > max else max = max

