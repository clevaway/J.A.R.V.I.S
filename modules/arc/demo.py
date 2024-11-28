# demo.py

from jarvis_ui import JarvisUI

# Instantiate JarvisUI
ui = JarvisUI(text='My name is jarvis', text_position='below')

ui.setCaption(text='Listening...', text_position='below')
ui.setState(State.LISTENING)

ui.setCaption(text='Processing...', text_position='below')
ui.setState(State.SPEAKING)

ui.setCaption(text='Idle', text_position='below')
ui.setState(State.IDLE)
