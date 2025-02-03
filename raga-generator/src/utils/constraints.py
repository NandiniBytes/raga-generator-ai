class RagaConstraints:
    def __init__(self):
        self.thaats = {
            'Bilawal': ['S', 'R', 'G', 'M', 'P', 'D', 'N'],
            'Kafi': ['S', 'R', 'g', 'M', 'P', 'D', 'n'],
            'Kalyan': ['S', 'R', 'G', 'M#', 'P', 'D', 'N'],
            'Marwa': ['S', 'R', 'G#', 'M#', 'P', 'D', 'N'],
            'Asavari': ['S', 'R', 'g', 'M', 'P', 'd', 'n'],
            'Bhairav': ['S', 'r', 'G', 'M', 'P', 'd', 'N'],
            'Bhairavi': ['S', 'r', 'g', 'M', 'P', 'd', 'n'],
            'Khamaj': ['S', 'R', 'G', 'M', 'P', 'D', 'n'],
            'Poorvi': ['S', 'r', 'G#', 'M#', 'P', 'd', 'N'],
            'Todi': ['S', 'r', 'g#', 'M#', 'P', 'd', 'N']
        }
        self.vadi_samvadi = {
            'Yaman': ('G', 'N'),
            'Bhairav': ('D', 'R'),
            'Bageshree': ('M', 'S'),
            'Darbari Kanada': ('R', 'P'),
            'Bhairavi': ('M', 'S')
        }
        self.time_theory = {
            'Morning': ['Bhairav', 'Todi', 'Asavari'],
            'Afternoon': ['Bhairavi', 'Kafi'],
            'Evening': ['Yaman', 'Kalyan', 'Marwa'],
            'Night': ['Khamaj', 'Poorvi']
        }
        self.note_constraints = {
            'Yaman': {
                'ascending': ['S', 'R', 'G', 'M#', 'P', 'D', 'N', 'S'],
                'descending': ['S', 'N', 'D', 'P', 'M#', 'G', 'R', 'S']
            },
            'Bhairav': {
                'ascending': ['S', 'r', 'G', 'M', 'P', 'd', 'N', 'S'],
                'descending': ['S', 'N', 'd', 'P', 'M', 'G', 'r', 'S']
            }
        }