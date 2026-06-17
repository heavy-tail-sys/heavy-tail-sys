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
)


# ### Future Implementation: Topological Twist and Berry Phase via Möbius Manifolds

#I am analyzing an architectural extension to this Hamiltonian model. There appears to be a missing algebraic component required to accurately map multi-particle fermionic correlation under non-trivial boundary conditions. 

#The objective is to formalize a new code block that correlates this 2-site Hubbard-like interaction with a non-orientable Möbius strip topology. Specifically, this system expansion investigates how the continuous-time quantum walk encodes the Geometric Berry Phase, evaluating the conditions under which the fermionic wave function undergoes a sign inversion ($e^{i\pi} = -1$) upon completing a full spatial rotation across the topological twist. 

#*UI/UX Visualization Note (Munzner Audit):* 
#Under Tamara Munzner's Nested Model for data visualization, utilizing distinct categorical hues (the current rainbow configuration) for this ordered, quantitative energy spectrum violates visual channel effectiveness guidelines. To maintain mathematical expressiveness, the production implementation should map quantum state occupancy via a sequential luminance gradient (e.g., light to dark steel blue). 

#To prioritize the core algebraic validation of the Hamiltonian, this matplotlib rendering remains unaltered in the current commit. This structural mismatch is left open intentionally as a micro-refactoring vector. 

#If any peer or academic expert wants to audit the topology or formally align the visual channels with Munzner's rules, feel free to submit a Pull Request or fork the kernel. The immediate milestone is to map this non-smooth phase space transformation within category-theoretic structures before deploying the matrix extension in Lean 4 or Qiskit frameworks. (Learning Lean).
