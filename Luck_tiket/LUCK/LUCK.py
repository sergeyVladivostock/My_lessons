from Luck_tiket.Moscow.luck_msc import luck_msc

from Luck_tiket.SPB.luck_spb import luck_spb

from Luck_tiket.KRDR.luck_krdr import luck_krd

f = luck_spb.spb()
def luck_all(a):
   luck_krd(f)
   luck_msc(f)
   luck_spb(f)

luck_all(123321)