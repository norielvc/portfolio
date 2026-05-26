import re

with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\n', '\n')

# Squish factor for the elliptical orbits (matches the tilt in the attachment)
SQUISH = 0.42 

def make_ellipse_path(id, r):
    ry = r * SQUISH
    # Start at the "top" of the squished ellipse: (cx, cy - ry)
    # cx=400, cy=400
    return f'<path id="{id}" d="M 400,{400-ry:.1f} A {r},{ry:.1f} 0 1 1 399.9,{400-ry:.1f} Z"/>'

def make_orbit_circle(r):
    ry = r * SQUISH
    return f'<ellipse cx="400" cy="400" rx="{r}" ry="{ry:.1f}" fill="none" stroke="rgba(26,26,26,0.08)" stroke-width="1"/>'

# radii: 55, 90, 125, 160, 205, 250, 285, 315, 345
radii = [55, 90, 125, 160, 205, 250, 285, 315, 345]

new_defs = '\n'.join([make_ellipse_path(f"orb{i}", r) for i, r in enumerate(radii)])
new_rings = '\n'.join([make_orbit_circle(r) for r in radii])

# Construct the new SVG block
NEW_SVG_START = '''                    <svg id="svc-solar-svg" class="svc-orbital-svg" viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg">
                        <defs>
''' + new_defs + '''
                        </defs>

                        <!-- 9 Orbit rings -->
''' + new_rings + '''

                        <!-- Sun -->
                        <circle cx="400" cy="400" r="28" fill="#1a1a1a" class="svc-sun"/>'''

# We need to replace from <svg id="svc-solar-svg" ... to the Sun
pattern = r'<svg id="svc-solar-svg".*?<!-- Sun -->\s*<circle cx="400" cy="400" r="28" fill="#1a1a1a" class="svc-sun"/>'
new_content = re.sub(pattern, NEW_SVG_START, content, flags=re.DOTALL)

if new_content == content:
    print("FAIL: SVG pattern not found")
else:
    with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(new_content)
    print("SUCCESS: Rebuilt orbits as ellipses")
