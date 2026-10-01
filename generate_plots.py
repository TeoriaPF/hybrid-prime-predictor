python
import numpy as np

# Të dhënat reale nga eksperimenti në zonën 50M - 55M
gaps = ['2', '4', '6', '8 (F6)', '10', '12', '22']
frequencies = [0, 1924, 2405, 0, 2302, 1788, 1235]
total_instances = sum(frequencies) + 16099 - sum(frequencies) # 16,099 raste totale

# Llogaritja e përqindjeve (probabiliteteve) empirike
probabilities = [(f / 16099) * 100 for f in frequencies]

print("📊 Duke përgatitur vizualizimin e Matricës së Tranzicionit...")
print(f"Totali i rasteve të analizuara për Gap 8: 16,099")

# Ky skript përgatit strukturën e të dhënave për matricën tuaj të rezonancës.
# Kur ta ekzekutoni në kompjuter lokal me 'python generate_plots.py', 
# ai do të gjenerojë një skedar imazhi të quajtur 'fibonacci_blocking_effect.png'.

try:
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10, 6))
    colors = ['red' if (g == '2' or 'F6' in g) else 'royalblue' for g in gaps]
    bars = plt.bar(gaps, probabilities, color=colors, edgecolor='black', alpha=0.8)
    
    plt.title("Empirical Verification of the Fibonacci Blocking Effect (F6 = 8)\n[Evaluated in Deep High-Density Zone: 50M to 55M]", fontsize=12, fontweight='bold')
    plt.xlabel("Subsequent Prime Gap ($d_{n+1}$)", fontsize=11)
    plt.ylabel("Transition Probability (%)", fontsize=11)
    plt.ylim(0, max(probabilities) + 5)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Shtimi i vlerave mbi shtylla
    for bar in bars:
        yval = bar.get_height()
        if yval == 0:
            plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, "0.00%\n(Blocked)", ha='center', va='bottom', color='red', fontweight='bold', fontsize=9)
        else:
            plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.3, f"{yval:.2f}%", ha='center', va='bottom', fontsize=9)
            
    plt.tight_layout()
    plt.savefig('fibonacci_blocking_effect.png', dpi=300)
    print("✅ Grafiku u ruajt me sukses si 'fibonacci_blocking_effect.png'!")
    
except ImportError:
    print("\n⚠️ OOPS: Libraria 'matplotlib' nuk është e instaluar.")
    print("Për ta parë grafikun në kompjuter, ekzekutoni: pip install matplotlib")
