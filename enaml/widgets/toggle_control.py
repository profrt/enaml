#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from abc import abstractmethod

from traits.api import Bool, Event, Str, Instance, Property

from .control import Control, AbstractTkControl


class AbstractTkToggleControl(AbstractTkControl):
        
    @abstractmethod
    def shell_checked_changed(self, checked):
        raise NotImplementedError
    
    @abstractmethod
    def shell_text_changed(self, text):
        raise NotImplementedError


class ToggleControl(Control):
    """ An abstract toggle element. 
    
    An element which toggles the value of a boolean field. This is an
    abstract class which should not be used directly. Rather, it provides
    common functionality of subclasses such as RadioButton and CheckBox.

    """
    #: Whether the element is currently checked.
    checked = Bool

    #: A read only property which indicates whether the user is 
    #: currently pressing the element.
    down = Property(Bool, depends_on='_down')

    #: The text to use as the element's label.
    text = Str
    
    #: Fired when the element is toggled.
    toggled = Event
    
    #: Fired when the element is pressed.
    pressed = Event

    #: Fired when the element is released.
    released = Event

    #: Internal storage for the down attribute
    _down = Bool

    #: Overridden parent class trait
    abstract_obj = Instance(AbstractTkToggleControl)

    #--------------------------------------------------------------------------
    # Property methods 
    #--------------------------------------------------------------------------
    def _get_down(self):
        """ The property getter for the 'down' attribute.

        """
        return self._down

