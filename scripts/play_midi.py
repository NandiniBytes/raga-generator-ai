import pygame
import time

class MidiPlayer:
    def __init__(self, midi_file):
        self.midi_file = midi_file
        pygame.init()
        pygame.mixer.init()
        self.is_playing = False

    def load_midi(self):
        pygame.mixer.music.load(self.midi_file)

    def play(self):
        if not self.is_playing:
            self.load_midi()
            pygame.mixer.music.play()
            self.is_playing = True

    def stop(self):
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False

    def wait_for_completion(self):
        while pygame.mixer.music.get_busy():
            time.sleep(1)

# Example usage
if __name__ == "__main__":
    midi_player = MidiPlayer("generated_raga.mid")
    midi_player.play()
    print("Playing MIDI file. Press Enter to stop.")
    input()
    midi_player.stop()
    print("Playback stopped.")