from core import Hand, Bank, Deck
from core import Singleton


class Blackjack(metaclass=Singleton):
    def __init__(self):
        # Deck setup
        self._current_deck = Deck()
        self._current_deck.shuffle()  # Maybe I'll add a stirring animation

        # Dealer setup
        self._dealer_hand = Hand()
        self._dealer_hand.add_card(self._current_deck.deal())
        self._dealer_hand.add_card(self._current_deck.deal())

        # Player setup
        self._player_hand = Hand()
        self._player_hand.add_card(self._current_deck.deal())
        self._player_hand.add_card(self._current_deck.deal())

        self._player_bank = Bank(1000) # Total player bank
        self.player_turn = True

    def play(self):  # TODO: дописать процесс игры
        self._take_bet(self._player_bank)

    def _hit_or_stand(self, deck, hand):   # TODO: переписать под веб
        while self.player_turn:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

            if x[0].lower() == 'h':
                self._hit(deck, hand)  # hit() function defined above

            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                self.player_turn = False

            else:
                print("Sorry, please try again.")
                continue
            break

    # TODO: Написать отображение карт
    def _show_one_card(self):
        pass

    def _show_all_cards(self):
        pass

    @staticmethod
    def _take_bet(bank):  # TODO: допилить под js
        while True:
            try:
                bank.bet = int(input('Your bet: '))
            except ValueError:
                print('ValueError')
            else:
                if bank.bet > bank.total:
                    print("Sorry, your bet can't exceed", bank.total)
                else:
                    break

    @staticmethod
    def _hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()
