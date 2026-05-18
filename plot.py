import matplotlib.pyplot as plt

def action_potential_plot(title, subtitle, V_history, t_history):
    if subtitle == None:
        plt.suptitle(title)
        plt.plot(t_history, V_history)
        plt.xlabel('time (ms)')
        plt.ylabel('V (mV)')
        plt.ylim(-80, 60)
        plt.show()
    else:
        plt.suptitle(title)
        plt.title(subtitle)
        plt.plot(t_history, V_history)
        plt.xlabel('time (ms)')
        plt.ylabel('V (mV)')
        plt.ylim(-80, 60)
        plt.show()
