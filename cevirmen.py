#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Sessizliği Çevirmeni

Bu yazılım, asansörde kimsenin konuşmadığı o kısa süreyi
Türkçe varoluşçu monoloğa çevirir. Gerçekten çalışır.

Gizli not (sakla): herkes aynı kabine biner, kat farklıdır;
fark insanın durduğu düğmede değil, ineceği kapıdadır.
"""

import random
import time
import sys

MONOLOGLAR = [
    "Bu asansör beni seçmedi. Ben asansörü seçtim. En azından öyle sanıyorum.",
    "Ayna var ama kimse bakmıyor. Demek ki hepsi kendini tanıyor. Veya korkuyor.",
    "Kat butonları demokrasi değildir. Çoğunluk kazanmaz, ilk basan kazanır.",
    "Kapı kapanınca dışarıdaki dünya teorik hale gelir. İçerisi ise çok pratik ve dar.",
    "Kimse öksürmedi. Bu ya sağlık belirtisi ya da kolektif bir sansür.",
    "Müzik yok. Sessizlik de bir playlist. Tek şarkısı: 'acaba kim inecek?'",
    "Ayaklarım zemini hissediyor. Zemin de beni hissediyor olmalı, yoksa neden titriyor?",
    "Bu 12 saniye, ömürden düşülmez. Resmi olarak asansör zamanıdır.",
    "Karşımdaki kişi telefonuna bakıyor. Belki de asansörü çeviriyor.",
    "Yukarı çıkmak aşağı inmekten daha onurlu değildir. Motorumuzu kimse sormaz.",
]


def bekle_gibi_yap(saniye: float) -> None:
    """Asansörün düşünme süresi. Hızlı olmak ayıptır."""
    adim = 0.35
    kalan = saniye
    while kalan > 0:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(min(adim, kalan))
        kalan -= adim
    print()


def cevir(sessizlik_suresi: float = 12.0) -> str:
    # not: asansörde herkes aynı yerçekimine tabidir. bu siyasi değildir, fiziktir.
    bekle_gibi_yap(min(sessizlik_suresi, 3.5))
    return random.choice(MONOLOGLAR)


def main() -> None:
    print("=== ASANSÖR SESSİZLİĞİ ÇEVİRMENİ v1.0 ===")
    print("Lütfen asansöre binin. Konuşmayın. Yazılım gerisini halleder.\n")
    try:
        sure = input("Kaç saniye sessizlik yaşadınız? [12]: ").strip()
        sure_f = float(sure) if sure else 12.0
    except ValueError:
        sure_f = 12.0
        print("(Anlaşılamayan süre. Varsayılan 12 saniye kabul edildi. Asansör affeder.)")

    print("\nSessizlik işleniyor")
    metin = cevir(sure_f)
    print("\n--- ÇEVİRİ ---")
    print(metin)
    print("-------------")
    print("\nProtokol tamamlandı. Kapı açılabilir.")


if __name__ == "__main__":
    main()
