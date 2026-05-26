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
    # DARKENED: increased from 0.06 to 0.12 opacity
    return f'<ellipse cx="{CX}" cy="{CY}" rx="{r}" ry="{ry:.1f}" fill="none" stroke="rgba(26,26,26,0.15)" stroke-width="1"/>'

planets_data = [
    {"r": 80,  "dur": 5,   "size": 7},
    {"r": 120, "dur": 9,   "size": 9},
    {"r": 160, "dur": 14,  "size": 10},
    {"r": 200, "dur": 22,  "size": 8},
    {"r": 290, "dur": 48,  "size": 22}, # Jupiter
    {"r": 360, "dur": 70,  "size": 16}, # Saturn
    {"r": 420, "dur": 90,  "size": 14}, # Uranus
    {"r": 460, "dur": 115, "size": 14}, # Neptune
    {"r": 495, "dur": 140, "size": 6},  # Pluto
]

NEW_DEFS = f'''
                            <!-- Elliptical Paths -->
                            {''.join([make_ellipse_path(f"orb{i}", d["r"]) for i, d in enumerate(planets_data)])}
                            
                            <!-- VECTOR 3D GRADIENT (Harder, cleaner look) -->
                            <radialGradient id="vectorSphere" cx="30%" cy="30%" r="70%" fx="30%" fy="30%">
                                <stop offset="0%" stop-color="#888888"/> <!-- Light Gray Highlight -->
                                <stop offset="60%" stop-color="#333333"/> <!-- Mid Gray -->
                                <stop offset="100%" stop-color="#111111"/> <!-- Dark Gray Shadow -->
                            </radialGradient>
                            
                            <radialGradient id="sunGrad" cx="50%" cy="50%" r="50%">
                                <stop offset="0%" stop-color="#fffbe6"/>
                                <stop offset="70%" stop-color="#fdf5c4"/>
                                <stop offset="100%" stop-color="#f0e68c"/> <!-- Slightly darker edge for recognition -->
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
    # DARKENED asteroids
    opacity = random.uniform(0.15, 0.5)
    asteroids.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size:.1f}" fill="rgba(26,26,26,{opacity:.2f})"/>')

NEW_RINGS = '\n'.join([make_orbit_circle(d["r"]) for d in planets_data])
ASTEROID_BELT = f'<g class="asteroid-belt">{" ".join(asteroids)}</g>'

PLANETS_HTML = ""
for i, d in enumerate(planets_data):
    start_offset = -random.uniform(0, d["dur"])
    
    if i == 5: # Saturn
        PLANETS_HTML += f'''
                        <!-- Planet 6: Saturn (Vector 3D) -->
                        <g id="planet-5" class="svc-planet">
                            <animateMotion dur="{d["dur"]}s" begin="{start_offset:.2f}s" repeatCount="indefinite">
                                <mpath href="#orb5"/>
                            </animateMotion>
                            <ellipse rx="28" ry="9" cx="0" cy="0" fill="none" stroke="rgba(0,0,0,0.2)" stroke-width="3" transform="rotate(-25)"/>
                            <circle r="{d["size"]}" fill="url(#vectorSphere)"/>
                        </g>'''
    else:
        PLANETS_HTML += f'''
                        <!-- Planet {i+1} (Vector 3D) -->
                        <circle id="planet-{i}" r="{d["size"]}" fill="url(#vectorSphere)" class="svc-planet">
                            <animateMotion dur="{d["dur"]}s" begin="{start_offset:.2f}s" repeatCount="indefinite">
                                <mpath href="#orb{i}"/>
                            </animateMotion>
                        </circle>'''

# Technical Grid Lines - DARKENED
NEW_SVG = f'''                    <svg id="svc-solar-svg" class="svc-orbital-svg" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
                        <defs>
{NEW_DEFS}
                        </defs>

                        <!-- Background Technical Grid (Darker) -->
                        <line x1="0" y1="500" x2="1000" y2="500" stroke="rgba(26,26,26,0.06)" stroke-dasharray="4 4"/>
                        <line x1="500" y1="0" x2="500" y2="1000" stroke="rgba(26,26,26,0.06)" stroke-dasharray="4 4"/>

                        <!-- 9 Orbit rings -->
{NEW_RINGS}

                        <!-- Asteroid Belt -->
{ASTEROID_BELT}

                        <!-- Sun (More defined) -->
                        <circle cx="500" cy="500" r="38" fill="url(#sunGrad)" stroke="rgba(255,250,200,0.5)" stroke-width="1" class="svc-sun"/>
                        <circle cx="500" cy="500" r="54" fill="rgba(255,250,200,0.1)" class="svc-sun-pulse"/>
                        <circle cx="500" cy="500" r="75" fill="rgba(255,250,200,0.05)" class="svc-sun-pulse2"/>

{PLANETS_HTML}
                    </svg>'''

pattern = r'<svg id="svc-solar-svg".*?</svg>'
new_content = re.sub(pattern, NEW_SVG, content, flags=re.DOTALL)

if new_content == content:
    print("FAIL: SVG pattern not found")
else:
    with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(new_content)
    print("SUCCESS: Darkened lines and updated planets to Vector 3D style")
