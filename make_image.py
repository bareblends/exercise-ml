from pandas import read_csv
from matplotlib import pyplot

import sys

def makeFile(File):
    my_dpi=250 # this is the size of my monitor 96 x 96 px
    pyplot.figure(figsize=(600, 600), dpi=my_dpi)

    series = read_csv(File, header=0, index_col=0, parse_dates=True, squeeze=False)
    series = series.astype(float)
   

    series.plot(legend=None)
    #fig, ax = pyplot.subplots()
    #ax.axis("off")
    pyplot.plot(series, linewidth=1, color='C0')
    #pyplot.axes('off')
    pyplot.savefig(('fig%s.png' % File), dpi=my_dpi)
    #pyplot.imsave(('fig%s.png' % File), series, format="png", cmap="hot")
    pyplot.close()
#pyplot.show()

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        if i > 0:
            makeFile(arg)