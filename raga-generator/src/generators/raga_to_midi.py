from midiutil import MIDIFile

class RagaToMidi:
    def __init__(self, tempo=120, instrument=0):
        self.tempo = tempo
        self.instrument = instrument
        self.midi = MIDIFile(1)  # One track
        self.midi.addTempo(0, 0, self.tempo)
        self.midi.addProgramChange(0, 0, 0, self.instrument)

    def note_to_midi(self, note):
        note_map = {'S': 60, 'r': 61, 'R': 62, 'g': 63, 'G': 64, 'M': 65, 'M#': 66, 'P': 67, 'd': 68, 'D': 69, 'n': 70, 'N': 71}
        return note_map.get(note, 60)  # Default to 'S' if note not found

    def add_notes(self, raga_sequence):
        time = 0
        for note, duration in raga_sequence:
            midi_note = self.note_to_midi(note)
            self.midi.addNote(0, 0, midi_note, time, duration, 100)  # Channel 0, velocity 100
            time += duration

    def save_midi(self, filename):
        with open(filename, 'wb') as output_file:
            self.midi.writeFile(output_file)

# Example usage
if __name__ == "__main__":
    raga_sequence = [('S', 1), ('R', 1), ('G', 1), ('M#', 1), ('P', 1), ('D', 1), ('N', 1), ('S', 1)]
    raga_to_midi = RagaToMidi(tempo=120, instrument=0)
    raga_to_midi.add_notes(raga_sequence)
    raga_to_midi.save_midi("generated_raga.mid")