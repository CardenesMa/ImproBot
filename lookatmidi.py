from mido import MidiFile

midi = MidiFile("midi.mid")
midi = midi.print_tracks(meta_only=False)

print(midi)
