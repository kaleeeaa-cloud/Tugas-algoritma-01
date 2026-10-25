jam = int(input("durasi parkir(jam bulat):"))
if jam <1:
    print("durasi parkir minimal 1 jam")    
else:
    jam_tambahan = jam - 1
    tarif_tambahan = jam_tambahan * 2000
    biaya = 3000 + tarif_tambahan
    print(f"biaya parkir= Rp{biaya}")