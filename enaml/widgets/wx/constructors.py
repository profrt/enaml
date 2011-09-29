#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from traits.api import implements

from ...constructors import IToolkitConstructor, BaseToolkitCtor


#-------------------------------------------------------------------------------
# Base Constructors
#-------------------------------------------------------------------------------
class WXBaseComponentCtor(BaseToolkitCtor):
    pass


#-------------------------------------------------------------------------------
# Window constructors
#-------------------------------------------------------------------------------
class WXWindowCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..window import Window
        from .wx_window import WXWindow
        window = Window(toolkit_impl=WXWindow())
        return window


class WXDialogCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..dialog import Dialog
        from .wx_dialog import WXDialog
        dialog = Dialog(toolkit_impl=WXDialog())
        return dialog


#-------------------------------------------------------------------------------
# Panel Constructors
#-------------------------------------------------------------------------------
class WXPanelCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..panel import Panel
        from .wx_panel import WXPanel
        panel = Panel(toolkit_impl=WXPanel())
        return panel


#-------------------------------------------------------------------------------
# Container Constructors
#-------------------------------------------------------------------------------
class WXFormCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..form import Form
        from .wx_form import WXForm
        form = Form(toolkit_impl=WXForm())
        return form


class WXGroupCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..group import Group
        from .wx_group import WXGroup
        group = Group(toolkit_impl=WXGroup())
        return group


class WXVGroupCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..vgroup import VGroup
        from .wx_vgroup import WXVGroup
        vgroup = VGroup(toolkit_impl=WXVGroup())
        return vgroup


class WXHGroupCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..hgroup import HGroup
        from .wx_hgroup import WXHGroup
        hgroup = HGroup(toolkit_impl=WXHGroup())
        return hgroup


class WXStackedGroupCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..stacked_group import StackedGroup
        from .wx_stacked_group import WXStackedGroup
        stacked_group = StackedGroup(toolkit_impl=WXStackedGroup())
        return stacked_group


class WXTabGroupCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..tab_group import TabGroup
        from .wx_tab_group import WXTabGroup
        tab_group = TabGroup(toolkit_impl=WXTabGroup())
        return tab_group


#-------------------------------------------------------------------------------
# Element Constructors
#-------------------------------------------------------------------------------
class WXGroupBoxCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..group_box import GroupBox
        from .wx_group_box import WXGroupBox
        group_box = GroupBox(toolkit_impl=WXGroupBox())
        return group_box


class WXCalendarCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..calendar import Calendar
        from .wx_calendar import WXCalendar
        calendar = Calendar(toolkit_impl=WXCalendar())
        return calendar


class WXCheckBoxCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..check_box import CheckBox
        from .wx_check_box import WXCheckBox
        check_box = CheckBox(toolkit_impl=WXCheckBox())
        return check_box


class WXComboBoxCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..combo_box import ComboBox
        from .wx_combo_box import WXComboBox
        combo_box = ComboBox(toolkit_impl=WXComboBox())
        return combo_box


class WXFieldCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..field import Field
        from .wx_field import WXField
        field = Field(toolkit_impl=WXField())
        return field


class WXHtmlCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..html import Html
        from .wx_html import WXHtml
        html = Html(toolkit_impl=WXHtml())
        return html


class WXImageCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..image import Image
        from .wx_image import WXImage
        image = Image(toolkit_impl=WXImage())
        return image


class WXLabelCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..label import Label
        from .wx_label import WXLabel
        label = Label(toolkit_impl=WXLabel())
        return label


class WXPushButtonCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..push_button import PushButton
        from .wx_push_button import WXPushButton
        push_button = PushButton(toolkit_impl=WXPushButton())
        return push_button


class WXRadioButtonCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..radio_button import RadioButton
        from .wx_radio_button import WXRadioButton
        radio_button = RadioButton(toolkit_impl=WXRadioButton())
        return radio_button


class WXSliderCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..slider import Slider
        from .wx_slider import WXSlider
        slider = Slider(toolkit_impl=WXSlider())
        return slider


class WXSpinBoxCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..spin_box import SpinBox
        from .wx_spin_box import WXSpinBox
        spin_box = SpinBox(toolkit_impl=WXSpinBox())
        return spin_box


class WXSpacerCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..spacer import Spacer
        from .wx_spacer import WXSpacer
        spacer = Spacer(toolkit_impl=WXSpacer())
        return spacer


class WXEnableCanvasCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..enable_canvas import EnableCanvas
        from .wx_enable_canvas import WXEnableCanvas
        canvas = EnableCanvas(toolkit_impl=WXEnableCanvas())
        return canvas


class WXTraitsUIItemCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..traitsui_item import TraitsUIItem
        from .wx_traitsui_item import WXTraitsUIItem
        traits_ui_item = TraitsUIItem(toolkit_impl=WXTraitsUIItem())
        return traits_ui_item


class WXTableViewCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..table_view import TableView
        from .wx_table_view import WXTableView
        table_view = TableView(toolkit_impl=WXTableView())
        return table_view


class WXCheckGroupCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..check_group import CheckGroup
        from .wx_check_group import WXCheckGroup
        check_group = CheckGroup(toolkit_impl=WXCheckGroup())
        return check_group


class WXDateEditCtor(WXBaseComponentCtor):

    implements(IToolkitConstructor)

    def component(self):
        from ..date_edit import DateEdit
        from .wx_date_edit import WXDateEdit
        date_edit = DateEdit(toolkit_impl=WXDateEdit())
        return date_edit

