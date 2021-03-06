# Set graph styling to common styles
from matplotlib import pyplot as plt
import matplotlib
import seaborn

from metrics import max
plt.style.use('seaborn-poster')
matplotlib.rcParams['font.family'] = 'League Spartan'

# So I don't have to keep looking up how to do this...
def f_int(x):
    return format(int(x), ',')
# some matplotlib functions pass in a position, which we don't need
def mf_int(x, pos):
    return f_int(x)
def format_axis_labels_with_commas(axis):
    axis.set_major_formatter(matplotlib.ticker.FuncFormatter(mf_int))
def format_plt_labels_with_commas(plt):
    # I have no idea what the 111 magic number is. It was in a quora post and seems to work.
    axis = plt.get_subplot(111)
    format_axis_labels_with_commas(axis)
def annotate(axis, text, xy, xy_text):
    axis.annotate("${:,}".format(int(text)), xy=xy,
             xytext=xy_text,
             arrowprops=dict(facecolor='black', connectionstyle="arc3,rad=.2"),
             fontsize=14)

def find_smallest(s):
    smallest = min(s)
    index_of = s.index(smallest)
    return(index_of, smallest)

def find_biggest(s):
    biggest = max(s)
    index_of = s.index(biggest)
    return(index_of, biggest)

def annotate_smallest(axis, s, location=None):
    (x, y) = find_smallest(s)
    if location == None:
        location = (x * Decimal('1.1'), y * Decimal('.9'))

    annotate(axis, y, (x, y), location)

def annotate_biggest(axis, s, location=None):
    (x, y) = find_biggest(s)
    if location == None:
        location = (x * Decimal('0.9'), y * Decimal('1.1'))

    annotate(axis, y, (x, y), location)

def plot(s, x_label='', y_label='', title='', add_commas=True, zero_based=True):
    fig, ax1 = plt.subplots()

    if add_commas:
        format_axis_labels_with_commas(ax1.get_yaxis())

#    if zero_based:
#        ax1.set_ylim(bottom=0)

    ax1.set_ymargin(0.05)
    ax1.set_ylabel(y_label)
    ax1.set_xlabel(x_label)

    ax1.plot(s)
    plt.title(title)
    plt.show()

def plot_n(series, xlabel, title, add_commas=True, zero_based=True):
    # series should be a dict where the key is the label and the value is the
    # series. e.g. { 'Prime Harvesting' : [...] }
    fig, ax = plt.subplots()
    if add_commas:
        format_axis_labels_with_commas(ax.get_yaxis())
    plt.xlabel(xlabel)
    plt.title(title)

    for label in series.keys():
        ax_n = fig.add_subplot(111, sharex=ax, sharey=ax)
        ax_n.plot(series[label], label=label)
        ax_n.set_ymargin(0.05)
    plt.legend(loc=0)
    if zero_based:
        ax.set_ylim(bottom=0)
    plt.show()

def plot_two(s1, s2, s1_title='', s2_title='', x_label='', title='', y_lim=None):
    # This deprecated. Use plot_n instead.
    m_1 = max(s1)
    m_2 = max(s2)
    mm = max([m_1, m_2])
    y_lim_default = (0, mm)

    fig, ax1 = plt.subplots()
    ax1.plot(s1, 'b')
    ax1.set_ylabel(s1_title, color='b')
    ax1.set_xlabel(x_label)
    if y_lim:
        ax1.set_ylim(y_lim)
    else:
        ax1.set_ylim(y_lim_default)
    for tl in ax1.get_yticklabels():
        tl.set_color('b')

    format_axis_labels_with_commas(ax1.get_yaxis())

    ax2 = ax1.twinx()
    ax2.plot(s2, 'g')
    ax2.set_ylabel(s2_title, color='g')
    if y_lim:
        ax2.set_ylim(y_lim)
    else:
        ax1.set_ylim(y_lim_default)

    for tl in ax2.get_yticklabels():
        tl.set_color('g')
    format_axis_labels_with_commas(ax2.get_yaxis())

    plt.xlabel(x_label)
    plt.title(title)
    plt.show()
