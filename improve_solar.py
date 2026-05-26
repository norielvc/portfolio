import re
import random

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
    return f'<ellipse cx="{CX}" cy="{CY}" rx="{r}" ry="{ry:.1f}" fill="none" stroke="rgba(26,26,26,0.06)" stroke-width="1"/>'

# New larger radii
radii = [80, 120, 160, 200, 290, 360, 420, 460, 495]

# Generate Asteroid Belt dots (between Mars [200] and Jupiter [290])
# Radii roughly 230-260
asteroids = []
for _ in range(120):
    r = random.uniform(235, 265)
    angle = random.uniform(0, 360)
    import math
    x = CX + r * math.cos(math.radians(angle))
    y = CY + r * SQUISH * math.sin(math.radians(angle))
    size = random.uniform(0.5, 1.8)
    opacity = random.uniform(0.1, 0.4)
    asteroids.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size:.1f}" fill="rgba(26,26,26,{opacity:.2f})"/>')

NEW_DEFS = '\n'.join([make_ellipse_path(f"orb{i}", r) for i, r in enumerate(radii)])
NEW_RINGS = '\n'.join([make_orbit_circle(r) for r in radii])
ASTEROID_BELT = f'<g class="asteroid-belt">{" ".join(asteroids)}</g>'

# Rebuild the SVG block
NEW_SVG = f'''                    <svg id="svc-solar-svg" class="svc-orbital-svg" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
                        <defs>
{NEW_DEFS}
                        </defs>

                        <!-- Background Technical Grid -->
                        <line x1="100" y1="500" x2="900" y2="500" stroke="rgba(26,26,26,0.03)" stroke-dasharray="4 4"/>
                        <line x1="500" y1="200" x2="500" y2="800" stroke="rgba(26,26,26,0.03)" stroke-dasharray="4 4"/>
                        <circle cx="500" cy="500" r="495" fill="none" stroke="rgba(26,26,26,0.02)"/>

                        <!-- 9 Orbit rings -->
{NEW_RINGS}

                        <!-- Asteroid Belt -->
{ASTEROID_BELT}

                        <!-- Sun -->
                        <circle cx="500" cy="500" r="34" fill="#1a1a1a" class="svc-sun"/>
                        <circle cx="500" cy="500" r="48" fill="rgba(26,26,26,0.06)" class="svc-sun-pulse"/>
                        <circle cx="500" cy="500" r="68" fill="rgba(26,26,26,0.02)" class="svc-sun-pulse2"/>

                        <!-- Planet 1: Mercury -->
                        <circle id="planet-0" r="6" fill="#1a1a1a" class="svc-planet">
                            <animateMotion dur="5s" repeatCount="indefinite"><mpath href="#orb0"/></animateMotion>
                        </circle>
                        <!-- Planet 2: Venus -->
                        <circle id="planet-1" r="8" fill="#2a2a2a" class="svc-planet">
                            <animateMotion dur="9s" repeatCount="indefinite"><mpath href="#orb1"/></animateMotion>
                        </circle>
                        <!-- Planet 3: Earth -->
                        <circle id="planet-2" r="9" fill="#333333" class="svc-planet">
                            <animateMotion dur="14s" repeatCount="indefinite"><mpath href="#orb2"/></animateMotion>
                        </circle>
                        <!-- Planet 4: Mars -->
                        <circle id="planet-3" r="7" fill="#444444" class="svc-planet">
                            <animateMotion dur="22s" repeatCount="indefinite"><mpath href="#orb3"/></animateMotion>
                        </circle>
                        <!-- Planet 5: Jupiter -->
                        <circle id="planet-4" r="18" fill="#2d2d2d" class="svc-planet">
                            <animateMotion dur="48s" repeatCount="indefinite"><mpath href="#orb4"/></animateMotion>
                        </circle>
                        <!-- Planet 6: Saturn -->
                        <g id="planet-5" class="svc-planet">
                            <animateMotion dur="70s" repeatCount="indefinite"><mpath href="#orb5"/></animateMotion>
                            <ellipse rx="22" ry="7" cx="0" cy="0" fill="none" stroke="#666" stroke-width="2" transform="rotate(-25)"/>
                            <circle r="11" fill="#3a3a3a"/>
                        </g>
                        <!-- Planet 7: Uranus -->
                        <circle id="planet-6" r="10" fill="#555555" class="svc-planet">
                            <animateMotion dur="90s" repeatCount="indefinite"><mpath href="#orb6"/></animateMotion>
                        </circle>
                        <!-- Planet 8: Neptune -->
                        <circle id="planet-7" r="10" fill="#666666" class="svc-planet">
                            <animateMotion dur="115s" repeatCount="indefinite"><mpath href="#orb7"/></animateMotion>
                        </circle>
                        <!-- Planet 9: Pluto -->
                        <circle id="planet-8" r="5" fill="#999999" class="svc-planet">
                            <animateMotion dur="140s" repeatCount="indefinite"><mpath href="#orb8"/></animateMotion>
                        </circle>
                    </svg>'''

pattern = r'<svg id="svc-solar-svg".*?</svg>'
new_content = re.sub(pattern, NEW_SVG, content, flags=re.DOTALL)

if new_content == content:
    print("FAIL: SVG pattern not found")
else:
    with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(new_content)
    print("SUCCESS: Improved and scaled up solar system design")
