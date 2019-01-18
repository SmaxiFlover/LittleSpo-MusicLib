from MusicLib import *

def experiment1():
    nodes = []
    nodes.append(MusicLib.Note(freq = MusicLib.moveToMid(MusicLib.keyToFreq("C3") * 2)))
    nodes.append(MusicLib.Note(freq = MusicLib.moveToMid(MusicLib.keyToFreq("C3") * 3)))
    nodes.append(MusicLib.Note(freq = MusicLib.moveToMid(MusicLib.keyToFreq("C3") * 5)))
    for i in range(4):
        for j in nodes:
            j.demo()
        print("")
        MusicLib.playNodesVertically(nodes, length = 1000)

        def func(x):
            return x / 3

        for j in nodes:
            j.setFreq(freq = MusicLib.moveToMid(func(j.freq())))

def experiment2():
    chord_math = (0, 0, 0)

    def chordFreq(chord_math):
        res = []
        for i in chord_math:
            res.append(MusicLib.Note(freq = MusicLib.moveToMid(MusicLib.keyToFreq("C3") * (2 ** i))))
        return tuple(res)

    def displayChordMath(chord_math, times = 1, length = 1000):
        chord = chordFreq(chord_math)
        for i in chord:
            i.demo()
        for i in range(times):
            MusicLib.playNodesVertically(chordFreq(chord_math), length = length)
        print()

    def func(chord_math, step = (0)):
        res = []
        if (step == (0)):
            step = [3] * len(chord_math)
        for i in range(len(chord_math)):
            res.append(chord_math[i] + math.log(step[i], 2))
        return tuple(res)

    step1 = ( ## pop 4566 in c minor
        (1/3, 5/3, 1), (9, 9, 9), (5/9, 1/15, 5/9), (1, 1, 1)
    )

    step2 = ( ## pop 4536 in c minor
        (1/5, 1, 3/5), (9, 9, 9), (5/3, 1/5, 5/3), (1/3, 1/3, 1/3)
    )

    step3 = ( ## 1451 in C Major
        (2, 3, 5), (1/3, 1/3, 1/3), (9, 9, 9), (1/3, 1/3, 1/3)
    )

    step = step3

    for i in range(len(step)):
        chord_math = func(chord_math, step[i])
        displayChordMath(chord_math, length = 1000)

if __name__ == "__main__":
    experiment2()
