from Luck_tiket.Moscow.luck_msc import *

from Luck_tiket.SPB.luck_spb import *

from Luck_tiket.KRDR.luck_krdr import *



def luck_all():
   f = int(input('введите номер билета - '))
   luck_krd(f)
   luck_msc(f)
   luck_spb(f)
   from Luck_tiket.KRDR.luck_krdr import krdr
   from Luck_tiket.Moscow.luck_msc import msc
   from Luck_tiket.SPB.luck_spb import spb
   if msc == 1 and spb == 1 and krdr == 1:
      print('\n', "Вам надо срочно в казино. Ваш билет счастливый по всем статьям")

if __name__ == "__main__":

      luck_all()