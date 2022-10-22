import weighrhythms
import realize_chords
from realize_chords import Chord
import random
from mido import MidiFile, MidiTrack, Message, MetaMessage


class Piece:
    def __init__(self, measures: int, chords: list, output_file="midi.mid", bpm=120):
        self.measures = measures
        self.chords = chords
        self.output_file = output_file
        self.bpm = bpm

        self.trip_weight = 30
        self.dup_weight = 60
        self.six_weight = 10

        self.write_piece()

    def write_piece(self):

        # declare this new midi file. all messages are on one track
        midi_file = MidiFile(type=0)
        # create a track in the midi file
        track = MidiTrack()
        # put a track in the midi file
        midi_file.tracks.append(track)
        # put in the metamessages for the piece
        track.append(MetaMessage('time_signature', numerator=4, denominator=4,
                     clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
        track.append(MetaMessage('set_tempo', tempo=6000*self.bpm, time=0))
        track.append(MetaMessage('channel_prefix', channel=0, time=0))
        track.append(MetaMessage('instrument_name', name=' ', time=0))

        for i in range(self.measures):
            for k in self.chords:
                # call the chord from the declared chords in the list
                chord = k
                # find the root of the chord
                root = chord.root
                # get the scale for the chord
                scale = realize_chords.toWeighRhythms(chord)
                # turn the scale into a sequence
                sequence = weighrhythms.SequencialNotes(
                    root, scale).sequencial_notes()
                # write the data to the midi file
                WriteMidiTrack(sequence, track,
                               output_file=self.output_file, bpm=self.bpm)

        midi_file.save(self.output_file)
        return midi_file

    def __str__(self):
        midi = MidiFile(self.output_file)
        midi = midi.print_tracks(meta_only=False)
        return str(midi)


class WriteMidiTrack(Piece):
    def __init__(self, sequence, track, output_file="midi.mid", rhythm=4, bpm=120):
        self.sequence = sequence
        self.output_file = output_file
        self.rhythm = rhythm
        self.track = track
        self.bpm = bpm
        self.write(track)

    def write(self, track):
        # map the notes to the key number
        notes = dict(zip(
            "C C#/Db D D#/Eb E F F#/Gb G G#/Ab A A#/Bb B".split(" "),
            (i for i in range(60, 71))))
        # this will be the time for the midi event
        quarter_note_time = 960
        for i in self.sequence:
            i = i[0].strip(" ")  # PUT RHYTHM WEIGHTS HERE ###
            # this is a 1/10 hange of choosing the rest
            random_rest_generator = random.randint(0, 10)
            if random_rest_generator != 2:
                # seeing if the sequence is within the available notes
                for k in notes:
                    # if so, put the note in there
                    if k == i:
                        track.append(Message("note_on", note=notes[k], time=0))
                        track.append(
                            Message("note_off", note=notes[k],
                                    time=quarter_note_time//self.rhythm))
            else:
                #
                track.append(Message("note_on", note=64,
                             time=quarter_note_time//self.rhythm))
                track.append(Message("note_off", note=64,
                             time=quarter_note_time//self.rhythm))

    def __str__(self):
        openmidi = MidiFile(self.output_file)
        track_values = openmidi.print_tracks(meta_only=False)
        return str(track_values)


if __name__ == '__main__':
    print(
        Piece(1, [Chord("D", "m", -1, five=-1), Chord("G", "M", -1), Chord("C", "M", 0), Chord("C", "M", 0), Chord("D", "m", -1, five=-1), Chord("G", "M", -1), Chord("C", "M", 0), Chord("C", "M", 0), Chord("D", "m", -1, five=-1), Chord("G", "M", -1), Chord("C", "M", 0), Chord("C", "M", 0), Chord("D", "m", -1, five=-1), Chord("G", "M", -1), Chord("C", "M", 0), Chord("C", "M", 0), Chord("D", "m", -1, five=-1), Chord("G", "M", -1), Chord("C", "M", 0), Chord("C", "M", 0), Chord("D", "m", -1, five=-1), Chord("G", "M", -1), Chord("C", "M", 0), Chord("C", "M", 0), Chord("D", "m", -1, five=-1), Chord("G", "M", -1), Chord("C", "M", 0), Chord("C", "M", 0), Chord("D", "m", -1, five=-1), Chord("G", "M", -1), Chord("C", "M", 0), Chord("C", "M", 0), Chord("D", "m", -1, five=-1), Chord("G", "M", -1), Chord("C", "M", 0), Chord("C", "M", 0)]))
