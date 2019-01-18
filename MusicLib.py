from MLC import MLC
import wave, math, struct, winsound, time, os

class MusicLib:

    """
    Python Music Library
    powered by Smaxi Flover 陆一洲
    Project Start from 2019-01-02
    > Aimed to help contemporary music research
    """

    def keyToIdx(key_str):
        patch = 1 if key_str[1] == "#" else -1 if key_str[1] == "b" else 0
        return patch + MLC.KEYN_TO_N[key_str[0]] + int(key_str[-1]) * MLC.KEY_NUMBER

    def idxToKey(key_idx):
        keyn = key_idx % MLC.KEY_NUMBER
        leveln = key_idx // MLC.KEY_NUMBER
        return MLC.N_TO_KEYN[keyn] + str(leveln)

    def keyToFreq(key_str):
        key_dist = MusicLib.keyToIdx(key_str) - MusicLib.keyToIdx("A3")
        return MLC.A3_Freq * 2 ** ( key_dist / MLC.KEY_NUMBER)

    def freqToKey(key_freq):
        key_dist = math.log(key_freq / MLC.A3_Freq, 2) * MLC.KEY_NUMBER
        return MusicLib.idxToKey(round(key_dist) + MusicLib.keyToIdx("A3"))

    def idxToFreq(key_idx):
        key_dist = key_idx - MusicLib.keyToIdx("A3")
        return MLC.A3_Freq * 2 ** ( key_dist / MLC.KEY_NUMBER)

    def freqToIdx(key_freq):
        key_dist = math.log(key_freq / MLC.A3_Freq, 2) * MLC.KEY_NUMBER
        return round(key_dist) + MusicLib.keyToIdx("A3")

    def moveToMid(key_freq):
        std_lower_bound = MusicLib.keyToFreq("C3")
        std_upper_bound = std_lower_bound * 2
        while (key_freq >= std_upper_bound):
            key_freq /= 2
        while (key_freq < std_lower_bound):
            key_freq *= 2
        return key_freq

    def stdFreq(key_freq):
        return MusicLib.keyToFreq(MusicLib.freqToKey(key_freq))

    def keyFreqError(key_freq):
        return math.log(key_freq / MusicLib.stdFreq(key_freq), 2) * MLC.KEY_NUMBER

    class Note:

        def __init__(self, freq = 0, name = "", idx = -1):
            # Freq and name cannot be defined simultaneously
            self.f = 0
            if (freq != 0):
                self.f = freq
            elif (name != ""):
                self.f = MusicLib.keyToFreq(name)
            elif (idx != -1):
                self.f = MusicLib.idxToFreq(idx)

        def freq(self):
            return self.f

        def setFreq(self, freq = 0, name = "", idx = -1):
            self.f = 0
            if (freq != 0):
                self.f = freq
            elif (name != ""):
                self.f = MusicLib.keyToFreq(name)
            elif (idx != 0):
                self.f = idxToFreq(idx)

        def name(self):
            return MusicLib.freqToKey(self.f)

        def error(self):
            return MusicLib.keyFreqError(self.f)

        def demo(self, demoName = True, demoFreq = True, demoError = True):
            demo_s = ""
            if demoName:
                demo_s += "%5s" % self.name()
            if demoFreq:
                demo_s += "%9.2lf" % self.freq()
            if demoError:
                demo_s += "%8.2lf%%" % (self.error() * 100)
            print(demo_s)

    def playNodesVertically(nodes, file_name="cache/test.wav", length = 1000, loudness = 500, erase = True):
        f=wave.open(file_name,'w')
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(MLC.SAMPLE_RATE)
        f.setcomptype('NONE','Not Compressed')

        frame_length = round(length / 1000 * MLC.SAMPLE_RATE)
        frame_loudness = round(loudness / 1000 * MLC.SAMPLE_LOUDNESS_UPPER_BOUND)
        frames = b''

        for i in range(frame_length):
            cur_wav = 0
            for j in nodes:
                cur_wav += math.sin(2 * math.pi * i * j.freq() / MLC.SAMPLE_RATE)
            cur_wav /= len(nodes)
            frames += struct.pack('h', round(frame_loudness * cur_wav))

        f.writeframesraw(frames + b'')
        f.close()
        winsound.PlaySound(file_name, flags = 1)
        time.sleep(length / 1000)
        if erase:
            os.remove(file_name)

    class Chord:

        def __init__(self, base = "C", type = "Maj"):
            self.keys = []
            for i in MLC.CHORD_MAP[type]:
                self.keys.append(MusicLib.keyToIdx(base + "0") + i)
            self.keys.sort()

        def play(self, length = 1000, loudness = 500):
            nodes = []
            for i in self.keys:
                nodes.append(MusicLib.Note(idx = i + 36))
            MusicLib.playNodesVertically(nodes, length = 1000)

        def demo(self):
            for i in self.keys:
                print(MusicLib.idxToKey(i)[:-1], end = " ")
            print()
            self.play()


a = MusicLib.Chord(base = "C", type = "Maj")
a.demo()
