from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput, FocusBehavior
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition
from kivy.uix.popup import Popup
import re
from kivy.modules import inspector
from kivy.core.text import LabelBase
from kivymd.uix.list import OneLineIconListItem

eV = 1.602*10**-19
eCharge = 1.602*10**-19
eMass = 9.109*10**-31
hBar = 6.5821*10**-16
hBarJ = 1.054*10**-34
hNobar = 6.6261*10**-29
kBeV = 8.6173*10**-5
kB = 1.3807*10**-23
cLight = 2.9989248*10**8
eSpace = 8.8542*10**-12



class Error(Popup):
    pass

class ColorLabel(Label):
    pass

class LabelButton(ButtonBehavior, Image):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class AccountScreen(Screen):
    pass

class ShareScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

class RelativityScreen(Screen):
    pass

class QuantumScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class LengthContractionScreen(Screen):

    def get_length(self, lE, vE, lP):


        if lE == "":
            lE = (0.0)

        if vE == "":
            vE = (0.0)

        if lP == "":
            lP = (0.0)

        lE = float(lE)
        vE = float(vE)
        lP = float(lP)


        if bool(lE) == True and bool(vE) == True and lP == 0.0:

            print(lE, vE, lP)
            # Returns Relative Length
            output = lE * ((1-(((vE)/(cLight))**2))**(1/2))
            self.display[2].text = str(output)
            return


        if bool(lE) == True and bool(lP) == True and vE == 0.0:

            print(lE, vE, lP)
            # Returns Velocity vE of moving frame
            output = cLight * (((1-((lP)/(lE))**2))**(1/2))
            self.display[1].text = str(output)
            return

        if bool(lP) == True and bool(vE) == True and lE == 0.0:

            print(lE, vE, lP)
            # Returns Proper Length lE
            output = lP / ((1-((vE)/(cLight))**2)**(1/2))
            self.display[0].text = str(output)
            return

        else:
            #ADD POPUP MESSAGE SAYING Enter ONLY TWO known variables"
            Error().open()
    pass

class VelocityAdditionScreen(Screen):


    def get_velocity(self, uX, uPx, vE):


        if uX == "":
            uX = (0.0)

        if uPx == "":
            uPx = (0.0)

        if vE == "":
            vE = (0.0)

        uX = float(uX)
        uPx = float(uPx)
        vE = float(vE)


        if bool(uPx) == True and bool(vE) == True and uX == 0.0:

            print(uPx, vE, uX)
            # Returns velocity of Event as seen by observer on resting frame uX
            output = cLight * (((uPx + vE) / (1 + ((vE * uPx) / cLight ** 2))) / cLight)
            self.display[0].text = str(output)
            return


        if bool(uX) == True and bool(vE) == True and uPx == 0.0:

            print(uPx, vE, uX)
            # Returns Velocity of Event relative to S' observer uPx
            output = cLight * (((uX - vE) / (1 - ((vE * uX) / cLight ** 2))) / cLight)
            self.display[1].text = str(output)
            return

        if bool(uX) == True and bool(uPx) == True and vE == 0.0:

            print(uPx, vE, uX)
            # Returns Velocity of S' as seen by observer on resting frame vE
            output = cLight * (((uX - uPx) / (1 - ((uPx * uX) / cLight ** 2))) / cLight)
            self.display[2].text = str(output)
            return

        else:
            #ADD POPUP MESSAGE SAYING Enter ONLY TWO known variables"
            Error().open()

class TimeDilationScreen(Screen):
    def get_time(self, tE, vE, tP):


        if tE == "":
            tE = (0.0)

        if vE == "":
            vE = (0.0)

        if tP == "":
            tP = (0.0)

        tE = float(tE)
        vE = float(vE)
        tP = float(tP)


        if bool(tE) == True and bool(vE) == True and tP == 0.0:

            print(tE, vE, tP)
            # Returns Dilated Time tP (Observer Time)
            output = tE / ((1-(((vE)/(cLight))**2))**(1/2))
            self.display[2].text = str(output)
            return


        if bool(tE) == True and bool(tP) == True and vE == 0.0:

            print(tE, vE, tP)
            # Returns Velocity vE of Clock on moving Frame
            output = cLight * (((1-((tE)/(tP))**2))**(1/2))
            self.display[1].text = str(output)
            return

        if bool(tP) == True and bool(vE) == True and tE == 0.0:

            print(tE, vE, tP)
            # Returns Proper Time tE
            output = tP * ((1-((vE)/(cLight))**2)**(1/2))
            self.display[0].text = str(output)
            return

        else:
            #ADD POPUP MESSAGE SAYING Enter ONLY TWO known variables"
            Error().open()
    pass





class FloatInput(TextInput):

    pat = re.compile('[^0-9\-+]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat

        if '.' in self.text:
            s = re.sub(pat, '', substring)


        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])

        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''




class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Physquick(MDApp):

    def build(self):
        return Builder.load_file('main.kv')

    def screen_changer(self):
        print(self.root.ids.content_drawer.ids.md_list)




    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''


        


Physquick().run()