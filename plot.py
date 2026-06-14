import matplotlib.pyplot as plt
def plot_network(neuron_histories, layers=None, title=''):
    """
    If layers is provided, group neurons by layer.
    Otherwise plot all neurons in a single panel.
    """
    if layers is None:
        # Flat — one panel
        fig, ax = plt.subplots(figsize=(10, 4))
        for n in range(len(neuron_histories)):
            ax.plot(neuron_histories[n][1], neuron_histories[n][0], alpha=0.7)
        ax.set_xlabel('t (ms)')
        ax.set_ylabel('V (mV)')
    else:
        L = len(layers)
        fig, axes = plt.subplots(L, 1, figsize=(10, 2.5 * L), sharex=True, sharey=True)
        if L == 1:
            axes = [axes]
        for l, neuron_indices in enumerate(layers):
            for n in neuron_indices:
                axes[l].plot(neuron_histories[n][1], neuron_histories[n][0], alpha=0.7)
            axes[l].set_ylabel(f'Layer {l}\nV (mV)')
        axes[-1].set_xlabel('t (ms)')
    
    fig.suptitle(title)
    plt.tight_layout()
    plt.show()
    
def plot_chain(title, neuron_histories, subtitle=None):
    """
    Plot V and gating variables for each neuron in the chain.
    neuron_histories: list of (V_history, t_history, m_history, h_history, n_history) tuples.
    """
    N = len(neuron_histories)
    fig, axes = plt.subplots(2 * N, 1, sharex=True, figsize=(10, 2.5 * N))
    
    # If N=1, axes isn't a list — wrap it
    if N == 1:
        axes = [axes[0], axes[1]]
    
    for j, (V_h, t_h, m_h, h_h, n_h) in enumerate(neuron_histories):
        ax_v = axes[2 * j]
        ax_g = axes[2 * j + 1]
        
        ax_v.plot(t_h, V_h, color='blue')
        ax_v.set_ylabel(f'V_{j} (mV)')
        ax_v.set_ylim(-80, 60)
        
        ax_g.plot(t_h, h_h, color='red', label='h')
        ax_g.plot(t_h, n_h, color='green', label='n')
        ax_g.set_ylabel(f'gating_{j}')
        ax_g.set_ylim(0, 1)
        ax_g.legend(loc='upper right', fontsize=8)
    
    axes[-1].set_xlabel('time (ms)')
    
    if subtitle:
        plt.suptitle(f'{title}\n{subtitle}')
    else:
        plt.suptitle(title)
    plt.tight_layout()
    plt.show()

def plot(title, subtitle, V_history, t_history, m_history, h_history, n_history):
    if subtitle == None:
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(t_history, V_history, color='blue')
        ax1.set_ylabel('V (mV)')
        ax1.set_ylim(-80, 60)

        ax2.plot(t_history, h_history, color='red', label='h')
        ax2.plot(t_history, n_history, color='green', label='n')
        ax2.set_ylabel('gating variable')
        ax2.set_xlabel('time (ms)')
        ax2.set_ylim(0, 1)
        ax2.legend()

        plt.suptitle(title)
        plt.tight_layout()
        plt.show()
    else:
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(t_history, V_history, color='blue')
        ax1.set_ylabel('V (mV)')
        ax1.set_ylim(-80, 60)

        ax2.plot(t_history, h_history, color='red', label='h')
        ax2.plot(t_history, n_history, color='green', label='n')
        ax2.set_ylabel('gating variable')
        ax2.set_xlabel('time (ms)')
        ax2.set_ylim(0, 1)
        ax2.legend()

        plt.suptitle(title)
        plt.title(subtitle)
        plt.tight_layout()
        plt.show()
