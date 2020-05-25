# A Figure is either Mr. X (id = 0) or an Agent (id > 0)
# A figure holds on to his tickets and his current position

class Figure:

    def __init__(self, id, position):
        self.id = id
        self.position = position
        if id > 0:
            self.tickets = {'taxi': 10, 'bus': 8, 'underground': 4, 'black': 0}
        else:
            self.tickets = {'taxi': 99, 'bus': 99, 'underground': 99, 'black': 4}
