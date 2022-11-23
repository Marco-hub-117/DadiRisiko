import random


DICE_ART = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


class LancioDadiRisiko:
    
    def __init__(self, numeroDadiAttaccante, numeroDadiDifensore) -> None:
        self.numeroDadiAttaccante = numeroDadiAttaccante
        self.numeroDadiDifensore = numeroDadiDifensore
        self.dadiLanciatiAttaccante = self.lancia_n_dadi(self.numeroDadiAttaccante, sorted = True)
        self.dadiLanciatiDifensore = self.lancia_n_dadi(self.numeroDadiDifensore, sorted = True)
        self.carriPersiDifensore, self.carriPersiAttaccante = \
            self.determina_carri_persi(self.dadiLanciatiDifensore, self.dadiLanciatiAttaccante, sorted = True)
    
    def lancia_n_dadi(self, nDadi, sorted = True):
        lancio = []
    
        for i in range(0, nDadi):
            lancio.append(random.randint(1, 6))
    
        if(sorted):
            lancio.sort(reverse=True)
        
        return lancio

    def determina_carri_persi(self, dadiDifensoreList, dadiAttaccanteList, sorted = False):
    
        if (sorted):
            dadiDifensoreList.sort(reverse = True)
            dadiAttaccanteList.sort(reverse = True)
        
        carriPersiDifensore = 0
        carriPersiAttaccante = 0
        numeroConfronti = min(len(dadiDifensoreList), len(dadiAttaccanteList))
        for i in range(0,numeroConfronti):
            if(dadiDifensoreList[i] >= dadiAttaccanteList[i]):
                carriPersiAttaccante += 1
            else:
                carriPersiDifensore += 1

        return carriPersiDifensore,carriPersiAttaccante


def generate_dice_faces_diagram(dice_values, label = 'RESULTS'):
    """Return an ASCII diagram of dice faces from `dice_values`.

    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:

    ~~~~~~~~~~~~~~~~~~~ label ~~~~~~~~~~~~~~~~~~~
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ │         │ │  ●      │ │  ●      │
    │         │ │    ●    │ │    ●    │ │         │
    │  ●   ●  │ │         │ │      ●  │ │      ●  │
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """
    # Generate a list of dice faces from DICE_ART
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = label.center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


def main():
    # a scopo di test
    print()
    scontro = LancioDadiRisiko(3, 2)

    print("\n@@@ ATTACCANTE @@@")
    print(generate_dice_faces_diagram(scontro.dadiLanciatiAttaccante, label = 'ATTACCANTE'))
    #print(f"Lancio attaccante: {scontro.dadiLanciatiAttaccante}")
    print(f"Carri persi dall'attaccante: {scontro.carriPersiAttaccante}")
    print("\n@@@ DIFENSORE @@@")
    print(generate_dice_faces_diagram(scontro.dadiLanciatiDifensore, label = 'DIFENSORE'))
    #print(f"Lancio difensore: {scontro.dadiLanciatiDifensore}")
    print(f"Carri persi difensore: {scontro.carriPersiDifensore}")



if __name__ == '__main__':
    main()
