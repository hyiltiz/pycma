"""versatile shortcuts for quick typing in an (i)python shell or even
``from cma.s import *`` in interactive sessions.

Provides various aliases from within the `cma` package, to be reached like
``cma.s....``

Don't use for stable code.
"""
# from . import fitness_functions as ff
from . import evolution_strategy as es
from . import fitness_transformations as ft
from . import transformations as tf
from . import constraints_handler as ch
from .utilities import utils
from .evolution_strategy import CMAEvolutionStrategy as CMAES
from .utilities.utils import pprint
from .utilities.math import Mh
# from .fitness_functions import elli as felli

try:
    from matplotlib.pyplot import savefig as figsave, close as figclose, ion as figion
    figion()  # prevents that execution stops after plotting
    def figshow():
        """`pyplot.show` to make a plotted figure show up"""
        # is_interactive = matplotlib.is_interactive()
        import pyplot  # like this it doesn't show up in the interface
        pyplot.ion()
        pyplot.show()
        # if we call now matplotlib.interactive(True), the console is
        # blocked
except:
    figsave, figclose, figshow = 3 * ['not available']
    print('Could not import matplotlib.pyplot, therefore ``cma.plot()``' +
          ' etc. is not available')
