from performance import Performance


class Disco(Performance):
    def __init__(self, name, musicians_number, avg_ticket_price,
                 discoball_color, music_genre):
        Performance.__init__(self, name, musicians_number, avg_ticket_price)
        self.discoball_color = discoball_color
        self.music_genre = music_genre

    def print_info(self):
        print(f"In disco {self.name} there are "
              f"{self.musicians_number} musicians.\nAverage ticket price is "
              f"{self.avg_ticket_price}.\nThe color of the discoball is "
              f"{self.discoball_color}.\nHere you can hear {self.music_genre} "
              f"music."
              )

    def get_discoball_color(self):
        return self.discoball_color

    def get_music_genre(self):
        return self.music_genre

    def set_discoball_color(self, discoball_color):
        self.discoball_color = discoball_color

    def set_(self, music_genre):
        self.music_genre = music_genre
