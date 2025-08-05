import matplotlib.pyplot as plt

plt.ion()
try:
    from IPython import display
    _USE_IPYTHON = True
except Exception:  # pragma: no cover - fallback when IPython not available
    display = None
    _USE_IPYTHON = False

def plot(scores, mean_scores):
    plt.clf()
    plt.title('Training')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(round(mean_scores[-1], 2)))
    if _USE_IPYTHON:
        display.clear_output(wait=True)
        display.display(plt.gcf())
    else:
        plt.draw()
        plt.pause(0.001)
