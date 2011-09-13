from traits.api import implements

from .qt_component import QtComponent

from ..container import IContainerImpl


class QtContainer(QtComponent):
    """ A Qt implementation of Container.

    The QtContainer class serves as a base class for other container
    widgets. It is not meant to be used directly.

    See Also
    --------
    Container

    """
    implements(IContainerImpl)

    #---------------------------------------------------------------------------
    # IContainerImpl interface
    #---------------------------------------------------------------------------
    
    # The IContainerImpl interface is empty
