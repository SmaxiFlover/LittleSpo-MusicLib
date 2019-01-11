from MLC import *
import math
import winsound
import threading

class MusicLib:

    """
    Python Music Library
    powered by Smaxi Flover 陆一洲
    Project Start from 2019-01-02
    > Aimed to help research of contemporary music
    """

    def keyToInt(keystr):
        patch = 1 if keystr[0] == "#" else -1 if keystr[0] == "b" else 0
        return patch + MLC.KEYN_TO_N[keystr[-2]] + int(keystr[-1]) * MLC.KEYN_NUMBER

    def intToKey(keynum):
        keyn = keynum % MLC.KEYN_NUMBER
        leveln = keynum // MLC.KEYN_NUMBER
        return MLC.N_TO_KEYN[keyn] + str(leveln)

    def keyToHz(keystr):
        key_dist = MusicLib.keyToInt(keystr) - MusicLib.keyToInt("A3")
        return MLC.A3_Hz * 2 ** ( key_dist / MLC.KEY_NUMBER)

    def HzToKey(keyHz):
        key_dist = math.log(keyHz / MLC.A3_Hz, 2) * MLC.KEY_NUMBER
        return MusicLib.intToKey(round(key_dist) + MusicLib.keyToInt("A3"))

    def MoveToMid(keyHz):
        std_lower_bound = MusicLib.keyToHz("C3")
        std_upper_bound = std_lower_bound * 2
        while (keyHz >= std_upper_bound):
            keyHz /= 2
        while (keyHz < std_lower_bound):
            keyHz *= 2
        return keyHz

    def StdHz(keyHz):
        return MusicLib.keyToHz(MusicLib.HzToKey(keyHz))

    def keyHzError(keyHz):
        return math.log(keyHz / MusicLib.StdHz(keyHz), 2) * MLC.KEY_NUMBER

    class Note:

        def __init__(self):
            self.Hz = 0

        def Hz(self):
            return self.Hz

        def keyName(self):
            return MusicLib.HzToKey(self.Hz)

        def error(self):
            return MusicLib.keyHzError(self.Hz)

    def beepHzArr(Hz_arr, sound_len):
        for i in Hz_arr:
            winsound.Beep(round(i), sound_len)

Hz_arr = []

Hz_arr.append(MusicLib.MoveToMid(MusicLib.keyToHz("C3") / 2))
Hz_arr.append(MusicLib.MoveToMid(MusicLib.keyToHz("C3") / 3))
Hz_arr.append(MusicLib.MoveToMid(MusicLib.keyToHz("C3") / 5))
Hz_arr.append(MusicLib.MoveToMid(MusicLib.keyToHz("C3") / 7))
Hz_arr.append(MusicLib.MoveToMid(MusicLib.keyToHz("C3") / 11))
Hz_arr.append(MusicLib.MoveToMid(MusicLib.keyToHz("C3") / 13))
Hz_arr.append(MusicLib.MoveToMid(MusicLib.keyToHz("C3") / 17))
#Hz_arr.sort()
for i in Hz_arr:
    print("%s %.2f %.2f %.2f%%" % (MusicLib.HzToKey(i), i, MusicLib.StdHz(i), MusicLib.keyHzError(i) * 100))
