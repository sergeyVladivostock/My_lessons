from Luck_tiket.Moscow.luck_msc import *

from Luck_tiket.SPB.luck_spb import *

from Luck_tiket.KRDR.luck_krdr import *



def luck_all():
   f = int(input('введите номер билета - '))
   luck_krd(f)
   luck_msc(f)
   luck_spb(f)


if __name__ == "__main__":

      luck_all()