import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

def build_hamiltonian(eps1, eps2, t):
    return np.array([
        [0,    0,    0,         0        ],
        [0,    eps2, t,         0        ],
        [0,    t,    eps1,      0        ],
        [0,    0,    0,         eps1+eps2]
    ])

def plot_niveles(eps1, eps2, t):
    H  = build_hamiltonian(eps1, eps2, t)
    Es = np.sort(np.linalg.eigvalsh(H))
    fig, ax = plt.subplots(figsize=(8, 10))  # más grande para escritorio
    colores   = ['royalblue', 'seagreen', 'darkorange', 'crimson']
    etiquetas = ['E₀ |00⟩ vacío', 'E₁ 1 partícula', 'E₂ 1 partícula', 'E₃ |11⟩ lleno']
    Emin, Emax = Es[0] - 0.5, Es[3] + 0.5
    for i, (E, col, lbl) in enumerate(zip(Es, colores, etiquetas)):
        ax.hlines(E, 0.25, 0.75, colors=col, linewidth=4)
        ax.text(0.80, E, f'{lbl}\n{E:.4f} Ha',
                va='center', fontsize=12, color=col, fontweight='bold')
    for i in range(1, 4):
        dE  = Es[i] - Es[i-1]
        mid = (Es[i] + Es[i-1]) / 2
        ax.annotate('', xy=(0.13, Es[i]), xytext=(0.13, Es[i-1]),
                    arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))
        ax.text(0.02, mid, f'ΔE={dE:.3f}', va='center', fontsize=10, color='gray')
    ax.set_xlim(0, 1.5)
    ax.set_ylim(Emin, Emax)
    ax.set_ylabel('Energía (Ha)', fontsize=14)
    ax.set_title(f'Fermiones: ε₁={eps1:.2f}, ε₂={eps2:.2f}, t={t:.2f}', fontsize=14)
    ax.set_xticks([])
    ax.spines[['top', 'right', 'bottom']].set_visible(False)
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

widgets.interact(
    plot_niveles,
    eps1 = widgets.FloatSlider(value=1.0, min=-2, max=4, step=0.05,
                               description='ε₁', style={'description_width': 'initial'},
                               layout=widgets.Layout(width='400px')),
    eps2 = widgets.FloatSlider(value=2.0, min=-2, max=4, step=0.05,
                               description='ε₂', style={'description_width': 'initial'},
                               layout=widgets.Layout(width='400px')),
    t    = widgets.FloatSlider(value=0.5, min=-2, max=2, step=0.05,
                               description='t (hopping)', style={'description_width': 'initial'},
                               layout=widgets.Layout(width='400px'))




# Heavy-tail-sys: Simple 2-Site Fermionic Hubbard Hamiltonian Solver

This is a minimal numerical playground written in Python to visualize eigenvalue splits in a reduced 2-site fermionic Hubbard matrix. 

The script utilizes NumPy (np.linalg.eigvalsh) to solve a basic 4D Fock space matrix under localized energy potentials and hopping terms ($t$).

## The Conceptual Roadmap (Future Work):
The code currently executes a static matrix solver. The long-term objective is to scale this toy model into a continuous functional framework, exploring how wave-function sign inversions ($e^{i\pi} = -1$) behave under non-orientable Möbius boundary conditions. 

If you want to rigorously correct my math or optimize these basic NumPy loops, please don't hesitate to do so. (Epoch Base-16: 0x7D9).
