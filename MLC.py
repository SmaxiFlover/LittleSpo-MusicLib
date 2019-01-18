class MLC:

    A3_Freq = 440
    KEY_NUMBER = 12
    N_PIANO_KEYS = 88

    KEYN_TO_N = { 'C' :  0 , 'D' :  2 , 'E' :  4 , 'F' :  5 , 'G' :  7 , 'A' :  9 , 'B' :  11 }
    N_TO_KEYN = {
        0 : "C",
        1 : "Db",
        2 : "D",
        3 : "Eb",
        4 : "E",
        5 : "F",
        6 : "Gb",
        7 : "G",
        8 : "Ab",
        9 : "A",
        10 : "Bb",
        11 : "B"
    }

    SAMPLE_RATE = 44100
    SAMPLE_LOUDNESS_UPPER_BOUND = 32767

    CHORD_MAP = {
        "Maj" : (0, 4, 7),
        "min" : (0, 3, 7),
        "aug" : (0, 4, 8),
        "dim" : (0, 3, 6)
    }
