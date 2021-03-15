class VelocityAdditionScreen(Screen):
    pass

<HomeScreen>:

    FloatLayout:
        canvas:
            Color:
                rgb: utils.get_color_from_hex("#69B3F2")
            Rectangle:
                size: self.size
                pos: self.pos

        ScrollView:
            pos_hint: {"top": 1,"right":1}
            size_hint: 1,1

            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height
                row_default_height: '100dp'
                spacing: 10,10
                row_force_default: False
                FloatLayout:
                    Label:
                        font_color:
                            utils.get_color_from_hex("#424FFF")
                        id: general_relativity_label
                        font_size: 35
                        font_name: "Rubik-Bold.ttf"
                        text: "Calculator (by Gleb)"
                        pos_hint: {"top": 0.9, "left": 1}
                        size_hint: 1,0.3
                        markup: True
                FloatLayout:
                    pos_hint: {"top": 0.9,"right":1}
                    size_hint: 1,0.225

                    ImageButton:
                        pos_hint: {"top": 0.8, "right":.85}
                        size_hint: 0.2, 0.7
                        source: "Icons4/014-gravity.png"
                        on_release:
                            app.change_screen("kinematics_screen", direction='right', mode='push')

                    ImageButton:
                        pos_hint: {"top": 0.8, "right": 0.35}
                        size_hint: 0.2, 0.7
                        source: "Icons4/019-relativity.png"
                        on_release:
                            app.change_screen("relativity_screen", direction='right', mode='push')

                    Label:
                        pos_hint: {"top": 0.1, "right": .85}
                        size_hint: .2,0.15
                        font_color:
                            utils.get_color_from_hex("#425FFF")
                        font_size: 18
                        text: "Kinematics"
                        markup: True

                    Label:
                        pos_hint: {"top": 0.1,"right": 0.35}
                        size_hint: .2,0.15
                        font_color:
                            utils.get_color_from_hex("#425FFF")
                        font_size: 18
                        text: "Relativity"
                        markup: True

                FloatLayout:

                    pos_hint: {"top": 0.675, "left":1}
                    size_hint: 1,0.225
                    #Quantum Tunneling, Energy of H atom

                    ImageButton:
                        pos_hint: {"top":0.8,"right":.85}
                        size_hint: .2,.7
                        source: "Icons4/049-atom.png"
                        on_release:
                            app.change_screen("quantum_screen", direction='right', mode='push')

                    ImageButton:
                        pos_hint: {"top": 0.8, "right":0.35}
                        size_hint: .2,.7
                        source: "Icons4/046-transverse wave.png"
                        on_release:
                            print("Waves")


                    Label:
                        pos_hint: {"top": 0.1,"right":.85}
                        size_hint: .2,.15
                        font_color:
                            utils.get_color_from_hex("#425FFF")
                        font_size: 18
                        text: "Quantum"
                        markup: True

                    Label:
                        pos_hint: {"top": 0.1,"right":.35}
                        size_hint: .2,.15
                        font_color:
                            utils.get_color_from_hex("#425FFF")
                        font_size: 18
                        text: "Waves"
                        markup: True

                FloatLayout:

                    pos_hint: {"top": 0.450,"left":1}
                    size_hint: 1,.225


                    ImageButton:
                        pos_hint: {"top": 0.8,"right":.85}
                        size_hint: .2,.7
                        source: "Icons4/034-orbit.png"
                        on_release:
                            print("Astronomy")

                    ImageButton:
                        pos_hint: {"top": 0.8,"right":.35}
                        size_hint: .2,.7
                        source: "Icons4/018-clamp.png"
                        on_release:
                            print("Forces")

                    Label:
                        pos_hint: {"top": 0.1,"right":.85}
                        size_hint: .2,.15
                        font_color:
                            utils.get_color_from_hex("#425FFF")
                        font_size: 18
                        text: "Astro"

                    Label:
                        pos_hint: {"top": 0.1,"right":.35}
                        size_hint: .2,.15
                        font_color:
                            utils.get_color_from_hex("#425FFF")
                        font_size: 18
                        text: "Forces"


    FloatLayout:

        canvas:
            Color:
                rgb: utils.get_color_from_hex("#0a5a97")
            Rectangle:
                size: self.size
                pos: self.pos
        pos_hint: {"top":0.125,"right":1}
        size_hint: 1,.125


        ImageButton:
            source: "Icons5/040-user.png"
            pos_hint: {"top":0.97,"right":.6}
            size_hint: .07,.73
            on_press:
                print("Account")

        ImageButton:
            source: "Icons5/002-settings.png"
            pos_hint: {"top":0.97,"right":.3}
            size_hint: .07,.73
            on_press:
                print("Settings")

        ImageButton:
            source: "Icons5/015-idea.png"
            pos_hint: {"top":0.97,"right":.8}
            size_hint: .07,.73
            on_press:
                print("Info")


        ImageButton:
            source: "Icons5/003-home.png"
            pos_hint: {"top":0.97,"right":.15}
            size_hint: .07,.73
            on_press:
                print("Home")
                app.change_screen("home_screen", direction='right', mode='push')

        BoxLayout:

            Label:
                pos_hint: {"top":0.2,"right":.25}
                size_hint: .07,.15
                font_color:
                    utils.get_color_from_hex("#425FFF")
                font_size: 16
                text: "Home"
                markup: True

            Label:
                pos_hint: {"top":0.2,"left":.5}
                size_hint: .07,.15
                font_color:
                    utils.get_color_from_hex("#425FFF")
                font_size: 16
                text: "Settings"
                markup: True

            Label:

                pos_hint: {"top":0.2,"right":.85}
                size_hint: .07,.15
                font_color:
                    utils.get_color_from_hex("#425FFF")
                font_size: 16
                text: "Account"
                markup: True


            Label:
                pos_hint: {"top":0.2,"right":.5}
                size_hint: .07,.15
                font_color:
                    utils.get_color_from_hex("#425FFF")
                font_size: 16
                text: "Info"
                markup: True
