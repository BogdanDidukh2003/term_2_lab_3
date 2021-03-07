from .performance import Performance


class Disco(Performance):
    def __init__(self, name, musicians_number, avg_ticket_price,
                 discoball_color, music_genre):
        Performance.__init__(self, name, musicians_number, avg_ticket_price)
        self.__discoball_color = discoball_color
        self.__music_genre = music_genre

    def print_info(self):
        print(f"In disco {self._name} there are "
              f"{self._musicians_number} musicians.\nAverage ticket price is "
              f"{self._avg_ticket_price}.\nThe color of the discoball is "
              f"{self.__discoball_color}.\nHere you can hear "
              f"{self.__music_genre} music."
              )

    def get_discoball_color(self):
        return self.__discoball_color

    def set_discoball_color(self, discoball_color):
        self.__discoball_color = discoball_color

    def get_music_genre(self):
        return self.__music_genre

    def set_music_genre(self, music_genre):
        self.__music_genre = music_genre
