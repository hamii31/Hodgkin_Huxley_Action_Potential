import matplotlib.pyplot as plt

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
