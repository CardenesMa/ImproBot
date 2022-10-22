# This program spits out a scale based on the chord you give it

class Chord:

    """This class returns a set of tuples (degree, value) for each
     extension in a chord"""

    def __init__(self, root: str, type: str, seven: int, five=None, nine=None, eleven=None, thirteen=None):
        self.root = root
        self.type = type
        self.five = five
        self.seven = seven
        self.nine = nine
        self.eleven = eleven
        self.thirteen = thirteen

    # turns the -1 1 0 into flat and sharp

    def root(self):
        return str(self.root)

    def __str__(self):
        # a list of tuples in the form (modification, extension number)
        modifiers = [
            (self.five, "5"),
            (self.seven, "7"),
            (self.nine, "9"),
            (self.eleven, "11"),
            (self.thirteen, "13")
            ]

        print(modifiers)
        # this will be what it ends up looking like
        formatted_string = ""

        # i is a tuple
        for i in modifiers:
            if i[0] is not None:
                # change -1 to flat
                if i[0] == -1:
                    formatted_string += "b" + i[1] + " "
                # change 1 to share
                elif i[0] == 1:
                    formatted_string += "#" + i[1]+" "
                elif i[0] == 0 and i[1] != "5":
                    formatted_string += i[1]

        # what it looks like when you print the class
        return f"{self.root} {self.type} {formatted_string}"


class Scale:

    """given a Chord object, this class returns a series of scales you might use
     for the chord given"""

    def __init__(self, chord: Chord):
        self.chord = chord
        self.scales = {
            "Dorian":           "WHWWWHW",
            "Mixolydian":        "WWHWWHW",
            "Major":            "WWHWWWH",
            "Lochrian":          "HWWHWWW",
            "Altered Domonant":  "HWHWWWW",
            "Diminished # 1":    "WHWHWHWH",
            "Diminished # 2":    "HWHWHWHW",
            "Natural Minor":     "WHWWHWW",
            "Jazz Melodic Minor": "WHWWWWH",
            "Phrygian":          "HWWWHWW",
            "Whole Tone":        "WWWWWW",
            "Lydian":            "WWWHWWH"
        }

    def get_scale(self):

        possible_scales = {}
        is_altered = False

        if self.chord.nine is not None or self.chord.eleven is not None or self.chord.thirteen is not None:
            is_altered = True

        def assign(scale):
            possible_scales[scale] = self.scales[scale]

        if not is_altered:  # only checking the unaltered chords

            if self.chord.type == "m":  # min chords

                if self.chord.seven == -1:  # all min 7 chords
                    if self.chord.five == 0 or self.chord.five is None:  # min maj 7
                        # harmonic minor with min 7 as well as maj 7
                        assign("Dorian")
                    else:
                        assign("Lochrian")
                elif self.chord.seven == 0:
                    assign("Jazz Melodic Minor")
                elif self.chord.seven == 1:
                    assign("Whole Tone")

            if self.chord.type == "M":  # major chords

                if self.chord.seven == -1:
                    if self.chord.five == 0:
                        assign("Mixolydian")  # domonat 7
                    if self.chord.five == -1:
                        assign("Whole Tone")  # com 7 flat 5

                if self.chord.seven == 0:
                    if self.chord.five is None or self.chord.five == 0:  # major 7
                        assign("Major")
                    if self.chord.five == -1:  # major flat 5
                        assign("Lydian")
                if self.chord.seven == -1:
                    assign("Mixolydian")

        else:
            if self.chord.nine == -1:
                assign("Diminished # 2")
            else:
                assign("Altered Domonant")

        # returning just the WHWHWHw etc from the scale. The name is in the dict
        # because we use it for __str__
        if len(possible_scales.values()) > 0:
            return str(list(possible_scales.values())[0])
        else:
            return ""

    def __str__(self):
        return str(self.get_scale())


def toWeighRhythms(Chord):
    return Scale(Chord).get_scale()


if __name__ == '__main__':

    print(toWeighRhythms(Chord("C", "m", 1)))
