import re
import random
import math

with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\n', '\n')

SQUISH = 0.42
CX, CY = 500, 500

def make_ellipse_path(id, r):
    ry = r * SQUISH
    return f'<path id="{id}" d="M {CX},{CY-ry:.1f} A {r},{ry:.1f} 0 1 1 {CX-0.1},{CY-ry:.1f} Z"/>'

def make_orbit_circle(r):
    ry = r * SQUISH
    return f'<ellipse cx="{CX}" cy="{CY}" rx="{r}" ry="{ry:.1f}" fill="none" stroke="rgba(26,26,26,0.12)" stroke-width="1"/>'

# Detailed planet data with realistic color palettes
planets_data = [
    {"r": 80,  "dur": 5,   "size": 7,  "light": "#A5A5A5", "dark": "#4A4A4A"}, # Mercury
    {"r": 120, "dur": 9,   "size": 9,  "light": "#E3BB76", "dark": "#A17431"}, # Venus
    {"r": 160, "dur": 14,  "size": 10, "light": "#4B9CD3", "dark": "#1B4F72"}, # Earth
    {"r": 200, "dur": 22,  "size": 8,  "light": "#E27B58", "dark": "#8E3E26"}, # Mars
    {"r": 290, "dur": 48,  "size": 22, "light": "#D39C7E", "dark": "#935132"}, # Jupiter
    {"r": 360, "dur": 70,  "size": 16, "light": "#C5AB6E", "dark": "#7B652E"}, # Saturn
    {"r": 420, "dur": 90,  "size": 14, "light": "#B2E5F2", "dark": "#4D8C9C"}, # Uranus
    {"r": 460, "dur": 115, "size": 14, "light": "#3E54E8", "dark": "#1A237E"}, # Neptune
    {"r": 495, "dur": 140, "size": 6,  "light": "#968E85", "dark": "#4D4640"}, # Pluto
]

GRADIENTS_HTML = ""
for i, p in enumerate(planets_data):
    GRADIENTS_HTML += f'''
                            <radialGradient id="grad-{i}" cx="30%" cy="30%" r="70%" fx="30%" fy="30%">
                                <stop offset="0%" stop-color="{p["light"]}"/>
                                <stop offset="100%" stop-color="{p["dark"]}"/>
                            </radialGradient>'''

NEW_DEFS = f'''
                            <!-- Elliptical Paths -->
                            {''.join([make_ellipse_path(f"orb{i}", d["r"]) for i, d in enumerate(planets_data)])}
                            
                            <!-- Planet Gradients -->
{GRADIENTS_HTML}
                            
                            <radialGradient id="sunGrad" cx="50%" cy="50%" r="50%">
                                <stop offset="0%" stop-color="#fffbe6"/>
                                <stop offset="60%" stop-color="#ffed85"/>
                                <stop offset="100%" stop-color="#ffd700"/>
                            </radialGradient>
'''

# Asteroid Belt
asteroids = []
for _ in range(130):
    r = random.uniform(235, 265)
    angle = random.uniform(0, 360)
    x = CX + r * math.cos(math.radians(angle))
    y = CY + r * SQUISH * math.sin(math.radians(angle))
    size = random.uniform(0.6, 2.2)
    opacity = random.uniform(0.15, 0.4)
    asteroids.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size:.1f}" fill="rgba(26,26,26,{opacity:.2f})"/>')

NEW_RINGS = '\n'.join([make_orbit_circle(d["r"]) for d in planets_data])
ASTEROID_BELT = f'<g class="asteroid-belt">{" ".join(asteroids)}</g>'

PLANETS_HTML = ""
for i, d in enumerate(planets_data):
    start_offset = -random.uniform(0, d["dur"])
    
    if i == 5: # Saturn
        PLANETS_HTML += f'''
                        <!-- Planet 6: Saturn -->
                        <g id="planet-5" class="svc-planet">
                            <animateMotion dur="{d["dur"]}s" begin="{start_offset:.2f}s" repeatCount="indefinite">
                                <mpath href="#orb5"/>
                            </animateMotion>
                            <ellipse rx="28" ry="9" cx="0" cy="0" fill="none" stroke="rgba(0,0,0,0.12)" stroke-width="2.5" transform="rotate(-25)"/>
                            <circle r="{d["size"]}" fill="url(#grad-5)"/>
                        </g>'''
    else:
        PLANETS_HTML += f'''
                        <!-- Planet {i+1} -->
                        <circle id="planet-{i}" r="{d["size"]}" fill="url(#grad-{i})" class="svc-planet">
                            <animateMotion dur="{d["dur"]}s" begin="{start_offset:.2f}s" repeatCount="indefinite">
                                <mpath href="#orb{i}"/>
                            </animateMotion>
                        </circle>'''

NEW_SVG = f'''                    <svg id="svc-solar-svg" class="svc-orbital-svg" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
                        <defs>
{NEW_DEFS}
                        </defs>

                        <!-- Background Technical Grid -->
                        <line x1="0" y1="500" x2="1000" y2="500" stroke="rgba(26,26,26,0.04)" stroke-dasharray="4 4"/>
                        <line x1="500" y1="0" x2="500" y2="1000" stroke="rgba(26,26,26,0.04)" stroke-dasharray="4 4"/>

                        <!-- 9 Orbit rings -->
{NEW_RINGS}

                        <!-- Asteroid Belt -->
{ASTEROID_BELT}

                        <!-- Sun (High Visibility) -->
                        <circle cx="500" cy="500" r="42" fill="url(#sunGrad)" stroke="rgba(255,215,0,0.3)" stroke-width="2" class="svc-sun"/>
                        <circle cx="500" cy="500" r="58" fill="rgba(255,237,133,0.15)" class="svc-sun-pulse"/>
                        <circle cx="500" cy="500" r="80" fill="rgba(255,237,133,0.05)" class="svc-sun-pulse2"/>

{PLANETS_HTML}
                    </svg>'''

pattern = r'<svg id="svc-solar-svg".*?</svg>'
new_content = re.sub(pattern, NEW_SVG, content, flags=re.DOTALL)

if new_content == content:
    print("FAIL: SVG pattern not found")
else:
    with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(new_content)
    print("SUCCESS: Assigned colors to all planets and improved Sun visibility")
