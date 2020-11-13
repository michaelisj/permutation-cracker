import pickle

WORDS_DB = open("db.bin", 'rb').read()
WORDS_DB = pickle.loads(WORDS_DB)

FREQUENCY = [0.0466,
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

CHARACTERS = set(range(ord('א'), ord('ת') + 1)) - \
    set(map(ord, ['ם', 'ף', 'ן', 'ך', 'ץ']))
CHARACTERS = list(CHARACTERS)
CHARACTERS.sort()
FREQUENCY = {char: freq for char, freq in zip(CHARACTERS, FREQUENCY)}
