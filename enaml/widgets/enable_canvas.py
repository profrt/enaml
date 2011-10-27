#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from abc import abstractmethod

from traits.api import Instance
from enable.component import Component as EnableComponent

from .control import Control, AbstractTkControl


class AbstractTkEnableCanvas(AbstractTkControl):

    @abstractmethod
    def shell_component_changed(self, component):
        raise NotImplementedError


class EnableCanvas(Control):
    """ An Enable canvas widget that will draw any Enable Component
    object.
    
    """
    #: The enable.component.Component instance to draw.
    component = Instance(EnableComponent)

    #: Overridden parent class trait
    abstract_obj = Instance(AbstractTkEnableCanvas)

