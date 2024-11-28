# jarvis_ui.py

import tkinter as tk
import math
import random
from enum import Enum

class State(Enum):
    IDLE = 0
    LISTENING = 1
    SPEAKING = 2

class JarvisUI:
    def __init__(self, text='', text_position='below'):
        self.text = text
        self.text_position = text_position
        self.state = State.IDLE

        # Initialize the Tkinter root window
        self.root = tk.Tk()
        self.root.title("Jarvis UI")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)  # Remove window decorations

        # Center the window
        x = (self.root.winfo_screenwidth() - 400) // 2
        y = (self.root.winfo_screenheight() - 450) // 2
        self.root.geometry(f"+{x}+{y}")

        # Create Canvas
        self.canvas = tk.Canvas(self.root, width=400, height=450, bg='black', highlightthickness=0)
        self.canvas.pack()

        # Animation parameters
        self.angle = 0
        self.inner_ring_angle = 0
        self.outer_ring_angle = 0
        self.particles = [self.createParticle() for _ in range(100)]  # Reduced number for performance

        # Start the animation loop
        self._update_animation()

        # Start the simulation after 2 seconds
        self.root.after(2000, self.simulate_states)

        # Start the main loop
        self.root.mainloop()

    def simulate_states(self):
        self.setState(State.LISTENING)
        self.setCaption(text='Listening...', text_position='below')
        self.root.after(5000, self.update_state_to_speaking)

    def update_state_to_speaking(self):
        self.setState(State.SPEAKING)
        self.setCaption(text='Processing...', text_position='below')
        self.root.after(5000, self.update_state_to_idle)

    def update_state_to_idle(self):
        self.setState(State.IDLE)
        self.setCaption(text='Ready', text_position='below')

    def _update_animation(self):
        if self.state == State.IDLE:
            # Standard animations
            self.angle += 1
            self.inner_ring_angle += 2
            self.outer_ring_angle += 0.5
        elif self.state == State.LISTENING:
            # Accelerate rotations
            self.angle += 2
            self.inner_ring_angle += 4
            self.outer_ring_angle += 1
        elif self.state == State.SPEAKING:
            # Decelerate rotations
            self.angle += 0.5
            self.inner_ring_angle += 1
            self.outer_ring_angle += 0.25

        # Update particles
        for particle in self.particles:
            particle['angle'] += particle['speed']
            if particle['angle'] > 360:
                particle['angle'] -= 360
                particle['radius'] = random.uniform(50, 150)
                particle['size'] = random.uniform(1, 3)
                particle['speed'] = random.uniform(0.5, 2)

        # Redraw the canvas
        self.draw()

        # Schedule the next frame
        self.root.after(16, self._update_animation)  # Roughly 60 FPS

    def draw(self):
        self.canvas.delete('all')  # Clear the canvas

        center_x, center_y = 200, 200  # Center of the canvas
        base_radius = 100

        # Draw the glowing core
        self.drawCore(center_x, center_y, base_radius)

        # Draw rotating rings
        self.drawRings(center_x, center_y, base_radius)

        # Draw particles
        self.drawParticles(center_x, center_y)

        # Draw text
        self.drawText(center_x, center_y, base_radius)

    def drawCore(self, center_x, center_y, radius):
        # Approximate the glowing effect by drawing multiple circles
        for i in range(20):
            intensity = int(255 * (1 - i / 20))
            color = f'#{0:02x}{intensity:02x}{intensity:02x}'
            self.canvas.create_oval(
                center_x - radius + i,
                center_y - radius + i,
                center_x + radius - i,
                center_y + radius - i,
                fill=color,
                outline=''
            )

    def drawRings(self, center_x, center_y, radius):
        # Inner rotating ring
        self.canvas.create_oval(
            center_x - radius * 0.8,
            center_y - radius * 0.8,
            center_x + radius * 0.8,
            center_y + radius * 0.8,
            outline='cyan',
            width=2
        )

        # Outer rotating ring
        self.canvas.create_oval(
            center_x - radius * 1.2,
            center_y - radius * 1.2,
            center_x + radius * 1.2,
            center_y + radius * 1.2,
            outline='blue',
            width=2
        )

        # Middle ring with indicators
        num_indicators = 12
        angle_offset = self.angle
        for i in range(num_indicators):
            angle_deg = i * (360 / num_indicators) + angle_offset
            angle_rad = math.radians(angle_deg)
            x = center_x + math.cos(angle_rad) * radius
            y = center_y + math.sin(angle_rad) * radius
            self.canvas.create_oval(
                x - 5, y - 5, x + 5, y + 5,
                fill='green', outline=''
            )

    def drawParticles(self, center_x, center_y):
        for particle in self.particles:
            angle_rad = math.radians(particle['angle'])
            x = center_x + math.cos(angle_rad) * particle['radius']
            y = center_y + math.sin(angle_rad) * particle['radius']
            size = particle['size']
            self.canvas.create_oval(
                x - size, y - size, x + size, y + size,
                fill='cyan', outline=''
            )

    def createParticle(self):
        return {
            'angle': random.uniform(0, 360),
            'radius': random.uniform(50, 150),
            'size': random.uniform(1, 3),
            'speed': random.uniform(0.25, 1.5)
        }

    def drawText(self, center_x, center_y, base_radius):
        text = self.text
        text_position = self.text_position

        if text:
            # Determine position
            if text_position == 'above':
                x = center_x
                y = center_y - base_radius - 30
            else:  # 'below'
                x = center_x
                y = center_y + base_radius + 30

            self.canvas.create_text(
                x, y,
                text=text,
                fill='cyan',
                font=('Helvetica', 16, 'bold')
            )

    def setState(self, state):
        self.state = state

    def setCaption(self, text='', text_position='below'):
        self.text = text
        self.text_position = text_position

    def close(self):
        # Safely close the UI
        self.root.quit()
