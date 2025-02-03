class RagaToSargam:
    def __init__(self, vadi=None, samvadi=None):
        self.vadi = vadi
        self.samvadi = samvadi

    def format_note(self, note):
        if note == self.vadi:
            return f"**{note}**"  # Bold vadi
        elif note == self.samvadi:
            return f"*{note}*"  # Italicize samvadi
        else:
            return note

    def convert_to_sargam(self, raga_sequence, spacing=True):
        sargam = []
        for note, _ in raga_sequence:
            formatted_note = self.format_note(note)
            sargam.append(formatted_note)
        if spacing:
            return ' '.join(sargam)
        else:
            return ''.join(sargam)

# Example usage
if __name__ == "__main__":
    raga_sequence = [('S', 1), ('R', 1), ('G', 1), ('M#', 1), ('P', 1), ('D', 1), ('N', 1), ('S', 1)]
    raga_to_sargam = RagaToSargam(vadi='G', samvadi='N')
    sargam_notation = raga_to_sargam.convert_to_sargam(raga_sequence, spacing=True)
    print(sargam_notation)