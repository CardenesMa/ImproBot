import realize_chords as rc
import random


class SequencialNotes:

    def __init__(self, root, scale, measure_length=1, rhythm=8):
        self.equaltemper = "C C#/Db D D#/Eb E F F#/Gb G G#/Ab A A#/Bb B".split(
            " ")
        self.root = root
        self.scale = scale
        self.measure_length = measure_length
        self.rhythm = rhythm

        self.third_weight = 3
        self.fourth_weight = 3
        self.tritone_weight = 3
        self.fifth_weight = 3
        self.six_weight = 3
        self.seven_wieght = 3
        self.root_weight = 1

        self.sequencial_notes()

    def find_interval(self, distance, index):
        return self.equaltemper[(index-distance) % len(self.equaltemper)-1]

    def get_notes(self):
        # dictionary of {note: weight}
        notes_and_weights = {}

        # adding the root to the dict
        notes_and_weights[self.root] = self.root_weight

        # looping through the set of notes starting from where the root is for
        # the length of the scale it will iterate through
        i = 0
        noter = self.equaltemper.index(self.root)

        # going through the scale directions and turning it into notes
        while i < len(self.scale):

            if self.scale[i] == "W":
                noter += 2
            elif self.scale[i] == "H":
                noter += 1
            else:
                raise AttributeError(
                    f"{self.scale[i]} must be either a H or W")
            item = self.equaltemper[noter % (len(self.equaltemper))]

            # gets the weight of the major or minor third
            minthird = self.find_interval(3, noter)
            majthird = self.find_interval(4, noter)
            fourth = self.find_interval(5, noter)
            augfourth = self.find_interval(6, noter)
            fifth = self.find_interval(7, noter)
            minsix = self.find_interval(8, noter)
            majsix = self.find_interval(9, noter)
            minseven = self.find_interval(10, noter)
            majseven = self.find_interval(11, noter)

            if minthird == self.root or majthird == self.root:
                notes_and_weights[item] = self.third_weight
            elif fourth == self.root:
                notes_and_weights[item] = self.fourth_weight
            elif augfourth == self.root:
                notes_and_weights[item] = self.tritone_weight
            elif fifth == self.root:
                notes_and_weights[item] = self.fifth_weight
            elif majsix == self.root or minsix == self.root:
                notes_and_weights[item] = self.six_weight
            elif minseven == self.root or majseven == self.root:
                notes_and_weights[item] = self.seven_wieght
            else:
                notes_and_weights[item] = 0

            i += 1

        return notes_and_weights

    def sequencial_notes(self):
        notes = self.get_notes()
        sequence = []
        note_container = []
        # putting the notes in the note container for as many times as weight
        for note in notes:
            for i in range(notes[note]):
                note_container.append(note)
        print(note_container)
        for numberofnotes in range(self.measure_length*self.rhythm):
            sequence.append(
                (f" {note_container[random.randint(0, len(note_container)-1)]} ", self.rhythm))

        return sequence

    def __str__(self):
        return str(self.sequencial_notes())


if __name__ == '__main__':
    chord = rc.Chord("C", "M", 0)
    root = chord.root
    scale = rc.toWeighRhythms(chord)
    print(SequencialNotes(root, scale))
