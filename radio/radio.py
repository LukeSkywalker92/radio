import argparse
import vlc
import time
import sys

class Radio:

    STREAMS = {
        'bayern1': 'http://streams.br.de/bayern1fran_2.m3u',
        'bayern2': 'https://streams.br.de/bayern2nord_2.m3u',
        'bayern3': 'https://streams.br.de/bayern3_2.m3u',
        'puls': 'https://streams.br.de/puls_2.m3u'
    }

    def __init__(self, sender):
        self.instance = vlc.Instance()
        self.sender = sender.lower()
        if self.sender in self.STREAMS.keys():
            self.stream = self.STREAMS[sender.lower()]
            self.start_player()
            self.play()
        else:
            print(f'Sender {self.sender} not found.')

    def start_player(self):
        self.player = self.instance.media_list_player_new()
        self.media = self.instance.media_list_new([self.stream])
        self.player.set_media_list(self.media)

    def play(self):
        self.player.play()

def main():
    radio = Radio(sys.argv[1])
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print('')
            print("Bye")
            sys.exit()


if __name__ == '__main__':
    main()


    

