# armo una lista de hashtags
def sacar_hashtags(posts):
    hashtags = []

    for post in posts:
        palabras = post.split()

        for palabra in palabras: 
            if palabra.startswith("#"):
                hashtag = palabra.strip(".,")
                hashtags.append(hashtag)
    
    return hashtags

# cuento los hashtags
def contar_hashtags(hashtags):
    conteo = {}

    for hashtag in hashtags:
        if hashtag in conteo:
            conteo[hashtag] += 1
        else:
            conteo[hashtag] = 1
    
    return conteo

# armo los hashtags trending
def hashtags_trending(conteo):
    trending = {}

    for hashtag in conteo:
        if conteo[hashtag] > 1:
            trending[hashtag] = conteo[hashtag]
    
    return trending

