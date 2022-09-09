def muunna(gal):
    return (gal / 0.264)

gal = float(input('syötä galloonat: '))
galloonat = 0
while gal >= 0:
    galloonat = muunna(gal)
    print(f'{galloonat:.2f} litraa')
    gal = float(input('syötä galloonat: '))