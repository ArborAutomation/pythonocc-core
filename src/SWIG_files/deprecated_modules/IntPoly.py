import warnings
warnings.simplefilter('once', DeprecationWarning)
warnings.warn("OCC.IntPoly is deprecated since pythonocc-0.18.2. Use OCC.Core.IntPoly", DeprecationWarning)

from OCC.Core.IntPoly import *
