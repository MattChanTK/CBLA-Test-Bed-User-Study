import os
import matplotlib.pyplot as plt


def save(fig, filename, directory='', ext='png', close=True, verbose=True):
    """Save a figure from pyplot.
 
    Parameters
    ----------
    path : string
        The path (and filename, without the extension) to save the
        figure to.
 
    ext : string (default='png')
        The file extension. This must be supported by the active
        matplotlib backend (see matplotlib.backends module).  Most
        backends support 'png', 'pdf', 'ps', 'eps', and 'svg'.
 
    close : boolean (default=True)
        Whether to close the figure after saving.  If you want to save
        the figure multiple times (e.g., to multiple formats), you
        should NOT close it in between saves or you will have to
        re-plot it.
 
    verbose : boolean (default=True)
        Whether to print information about when and where the image
        has been saved.
 
    """
    
    # Extract the directory and filename from the given path
    filename = "%s.%s" % (filename, ext)
    if directory == '':
        directory = '.'
 
    # If the directory does not exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
 
    # The final path to save to
    savepath = os.path.join(directory, filename)
 
    if verbose:
        print("Saving figure to '%s'..." % savepath),

    # maximizing the figure
    # figManager = plt.get_current_fig_manager()
    # figManager.window.showMaximized()

    # Actually save the figure
    fig.savefig(savepath, bbox_inches='tight')
    
    # Close it
    #if close:
    #    plt.close()
 
    if verbose:
       print("Done")