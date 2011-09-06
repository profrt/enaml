from traits.api import implements

from .wx_group import WXGroup

from ..hgroup import IHGroupImpl


class WXHGroup(WXGroup):
    """ A wxPython implementation of IHGroup.

    This is a convienence subclass of WXGroup which restricts the
    layout direction to horizontal.

    See Also
    --------
    IHGroup
    
    """ 
    implements(IHGroupImpl)

    #---------------------------------------------------------------------------
    # IHGroupImpl interface
    #---------------------------------------------------------------------------
    
    # IHGroupImpl interface is empty and fully implemented by WXGroup

