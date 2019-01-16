from MLC import MLC
import wave, math, struct, winsound, time

class MusicLib:

    """
    Python Music Library
    powered by Smaxi Flover 陆一洲
    Project Start from 2019-01-02
    > Aimed to help contemporary music research
    """

    def keyToInt(keystr):
        patch = 1 if keystr[1] == "#" else -1 if keystr[1] == "b" else 0
        return patch + MLC.KEYN_TO_N[keystr[0]] + int(keystr[-1]) * MLC.KEY_NUMBER

    def intToKey(keynum):
        keyn = keynum % MLC.KEY_NUMBER
        leveln = keynum // MLC.KEY_NUMBER
        return MLC.N_TO_KEYN[keyn] + str(leveln)

    def keyToFreq(keystr):
        key_dist = MusicLib.keyToInt(keystr) - MusicLib.keyToInt("A3")
        return MLC.A3_Freq * 2 ** ( key_dist / MLC.KEY_NUMBER)

    def freqToKey(keyFreq):
        key_dist = math.log(keyFreq / MLC.A3_Freq, 2) * MLC.KEY_NUMBER
        return MusicLib.intToKey(round(key_dist) + MusicLib.keyToInt("A3"))

    def moveToMid(keyFreq):
        std_lower_bound = MusicLib.keyToFreq("C3")
        std_upper_bound = std_lower_bound * 2
        while (keyFreq >= std_upper_bound):
            keyFreq /= 2
        while (keyFreq < std_lower_bound):
            keyFreq *= 2
        return keyFreq

    def stdFreq(keyFreq):
        return MusicLib.keyToFreq(MusicLib.freqToKey(keyFreq))

    def keyFreqError(keyFreq):
        return math.log(keyFreq / MusicLib.stdFreq(keyFreq), 2) * MLC.KEY_NUMBER

    class Note:

        def __init__(self, freq = 0, name = ""):
            # Freq and name cannot be defined simultaneously
            self.f = 0
            if (freq != 0):
                self.f = freq
            elif (name != ""):
                self.f = keyToFreq(name)

        def freq(self):
            return self.f

        def setFreq(self, freq = 0, name = ""):
            self.f = 0
            if (freq != 0):
                self.f = freq
            elif (name != ""):
                self.f = keyToFreq(name)

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

    def playChord(nodes, file_name="test.wav", length = 500, loudness = 500):
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
        winsound.PlaySound("test.wav", flags = 1)
        time.sleep(length / 1000)
