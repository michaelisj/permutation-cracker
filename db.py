import pickle

# WORDS_DB = open("db.bin", 'rb').read()
# WORDS_DB = pickle.loads(WORDS_DB)

FREQUENCY_WIKI = [0.0466,
                  0.0536,
                  0.0178,
                  0.0266,
                  0.084,
                  0.112,
                  0.0093,
                  0.022,
                  0.0178,
                  0.117,
                  0.0188,
                  0.062,
                  0.0513,
                  0.0365,
                  0.0223,
                  0.0265,
                  0.0229,
                  0.013,
                  0.0262,
                  0.0665,
                  0.0424,
                  0.0546]

FREQUENCY = [0.048,    # 1
             0.054,    # 2
             0.014,    # 3
             0.026,    # 4
             0.082,    # 5
             0.106,    # 6
             0.008,    # 7
             0.026,    # 8
             0.013,    # 9
             0.114,    # 10
             0.027,    # 20
             0.070,    # 30
             0.091,    # 40
             0.043,    # 50
             0.019,    # 60
             0.030,    # 70
             0.024,    # 80
             0.016,    # 90
             0.023,    # 100
             0.057,    # 200
             0.049,    # 300
             0.059,    # 400
             ]

CHARACTERS = set(range(ord('א'), ord('ת') + 1)) - \
    set(map(ord, ['ם', 'ף', 'ן', 'ך', 'ץ']))
CHARACTERS = list(CHARACTERS)
CHARACTERS.sort()
FREQUENCY = {char: freq for char, freq in zip(CHARACTERS, FREQUENCY)}
