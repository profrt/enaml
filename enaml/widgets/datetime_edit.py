#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from traits.api import Str

from .bounded_datetime import BoundedDatetime

from ..core.trait_types import EnamlEvent


class DatetimeEdit(BoundedDatetime):
    """ A datetime widget that displays a Python datetime.datetime object 
    using an appropriate toolkit specific control.

    """
    #: A python date format string to format the datetime. If None is
    #: supplied (or is invalid) the system locale setting is used.
    #: This may not be supported by all backends.
    datetime_format = Str

    #: Triggered whenever the user changes the date through the ui
    #: control, but not programmatically. The event payload will be 
    #: the datetime on the control.
    datetime_changed = EnamlEvent

    #: How strongly a component hugs its contents' width. DatetimeEdits 
    #: ignore the width hug by default, so they expand freely in width.
    hug_width = 'ignore'

    #--------------------------------------------------------------------------
    # Initialization
    #--------------------------------------------------------------------------
    def bind(self):
        """ A method called after initialization which allows the widget
        to bind any event handlers necessary.

        """
        super(DatetimeEdit, self).bind()
        self.default_send_attr_bind(
            'datetime_format',
            )

    def initial_attrs(self):
        """ Return a dictionary which contains all the state necessary to
        initialize a client widget.

        """
        super_attrs = super(DatetimeEdit, self).initial_attrs()
        attrs = {
            'datetime_format' : self.datetime_format,
        }
        super_attrs.update(attrs)
        return attrs

    #--------------------------------------------------------------------------
    # Toolkit Communication
    #--------------------------------------------------------------------------
    def receive_datetime_changed(self, context):
        """ Callback from the UI when the datetime value is changed.

        """
        self._setting = True
        self.datetime = context['value']
        self._setting = False
        self.datetime_changed(self.datetime)

