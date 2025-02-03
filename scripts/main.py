from vae_raga_generator import VAERagaGenerator
from raga_to_midi import RagaToMidi
from raga_to_sargam import RagaToSargam
from scripts.play_midi import MidiPlayer
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Raga Generation Pipeline")
    parser.add_argument('--input', type=str, help="Input file (MIDI/audio/text) or manual input of swaras")
    parser.add_argument('--tempo', type=int, default=120, help="Tempo for the generated MIDI file")
    parser.add_argument('--instrument', type=int, default=0, help="Instrument for the generated MIDI file")
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Step 1: Take an input file or manual input of swaras
    input_data = args.input

    # Step 2: Extract musical features and identify the raga
    raga_generator = VAERagaGenerator()
    features = raga_generator.extract_features(input_data)
    identified_raga = raga_generator.identify_raga(features)

    # Step 3: Generate a new raga based on Hindustani music rules
    new_raga_sequence = raga_generator.generate_raga(identified_raga)

    # Step 4: Convert the generated raga into MIDI and Sargam formats
    raga_to_midi = RagaToMidi(tempo=args.tempo, instrument=args.instrument)
    raga_to_midi.add_notes(new_raga_sequence)
    midi_filename = "generated_raga.mid"
    raga_to_midi.save_midi(midi_filename)

    raga_to_sargam = RagaToSargam(vadi=identified_raga['vadi'], samvadi=identified_raga['samvadi'])
    sargam_notation = raga_to_sargam.convert_to_sargam(new_raga_sequence, spacing=True)
    print("Generated Sargam Notation:")
    print(sargam_notation)

    # Step 5: Play the generated MIDI file
    midi_player = MidiPlayer(midi_filename)
    midi_player.play()
    print("Playing generated MIDI file. Press Enter to stop.")
    input()
    midi_player.stop()
    print("Playback stopped.")

if __name__ == "__main__":
    main()