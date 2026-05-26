import re

with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\n', '\n')

# The new orbital SVG block (9 planets, each with a circular orbit path using animateMotion)
NEW_SVG_BLOCK = '''                <!-- Orbital SVG Animation -->
                <div class="svc-orbital-wrapper">
                    <svg class="svc-orbital-svg" viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg">
                        <!-- Define circular orbit paths for animateMotion -->
                        <defs>
                            <path id="orb0" d="M 300,255 A 45,45 0 1 1 299.9,255 Z"/>
                            <path id="orb1" d="M 300,230 A 70,70 0 1 1 299.9,230 Z"/>
                            <path id="orb2" d="M 300,205 A 95,95 0 1 1 299.9,205 Z"/>
                            <path id="orb3" d="M 300,180 A 120,120 0 1 1 299.9,180 Z"/>
                            <path id="orb4" d="M 300,145 A 155,155 0 1 1 299.9,145 Z"/>
                            <path id="orb5" d="M 300,112 A 188,188 0 1 1 299.9,112 Z"/>
                            <path id="orb6" d="M 300,82 A 218,218 0 1 1 299.9,82 Z"/>
                            <path id="orb7" d="M 300,55 A 245,245 0 1 1 299.9,55 Z"/>
                            <path id="orb8" d="M 300,32 A 268,268 0 1 1 299.9,32 Z"/>
                        </defs>

                        <!-- Orbit rings (circles) -->
                        <circle cx="300" cy="300" r="45"  fill="none" stroke="rgba(26,26,26,0.10)" stroke-width="1"/>
                        <circle cx="300" cy="300" r="70"  fill="none" stroke="rgba(26,26,26,0.09)" stroke-width="1"/>
                        <circle cx="300" cy="300" r="95"  fill="none" stroke="rgba(26,26,26,0.08)" stroke-width="1"/>
                        <circle cx="300" cy="300" r="120" fill="none" stroke="rgba(26,26,26,0.07)" stroke-width="1"/>
                        <circle cx="300" cy="300" r="155" fill="none" stroke="rgba(26,26,26,0.06)" stroke-width="1"/>
                        <circle cx="300" cy="300" r="188" fill="none" stroke="rgba(26,26,26,0.06)" stroke-width="1"/>
                        <circle cx="300" cy="300" r="218" fill="none" stroke="rgba(26,26,26,0.05)" stroke-width="1"/>
                        <circle cx="300" cy="300" r="245" fill="none" stroke="rgba(26,26,26,0.05)" stroke-width="1"/>
                        <circle cx="300" cy="300" r="268" fill="none" stroke="rgba(26,26,26,0.04)" stroke-width="1"/>

                        <!-- Sun / Core -->
                        <circle cx="300" cy="300" r="22" fill="#1a1a1a" class="svc-sun"/>
                        <circle cx="300" cy="300" r="32" fill="rgba(26,26,26,0.08)" class="svc-sun-pulse"/>
                        <circle cx="300" cy="300" r="44" fill="rgba(26,26,26,0.04)" class="svc-sun-pulse2"/>

                        <!-- Planet 1: Mercury (orbit r=45, 5s) -->
                        <circle r="4" fill="#1a1a1a">
                            <animateMotion dur="5s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#orb0"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 2: Venus (orbit r=70, 9s) -->
                        <circle r="5.5" fill="#2a2a2a">
                            <animateMotion dur="9s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#orb1"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 3: Earth (orbit r=95, 14s) -->
                        <circle r="6" fill="#333333">
                            <animateMotion dur="14s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#orb2"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 4: Mars (orbit r=120, 20s) -->
                        <circle r="5" fill="#555555">
                            <animateMotion dur="20s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#orb3"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 5: Jupiter (orbit r=155, 45s) - largest -->
                        <circle r="11" fill="#3a3a3a">
                            <animateMotion dur="45s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#orb4"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 6: Saturn (orbit r=188, 65s) — with ring -->
                        <g>
                            <animateMotion dur="65s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#orb5"/>
                            </animateMotion>
                            <ellipse rx="13" ry="4" cx="0" cy="0" fill="none" stroke="#666666" stroke-width="1.5" transform="rotate(-20)"/>
                            <circle r="7" fill="#4a4a4a"/>
                        </g>

                        <!-- Planet 7: Uranus (orbit r=218, 85s) -->
                        <circle r="6.5" fill="#606060">
                            <animateMotion dur="85s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#orb6"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 8: Neptune (orbit r=245, 110s) -->
                        <circle r="6.5" fill="#707070">
                            <animateMotion dur="110s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#orb7"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 9: Pluto (orbit r=268, 130s) - smallest -->
                        <circle r="3" fill="#999999">
                            <animateMotion dur="130s" repeatCount="indefinite" rotate="auto">
                                <mpath href="#orb8"/>
                            </animateMotion>
                        </circle>
                    </svg>
                    <div class="svc-orbit-labels">
                        <span class="svc-orbit-label active">WEB DEV</span>
                        <span class="svc-orbit-label">SAAS</span>
                        <span class="svc-orbit-label">AUTOMATION</span>
                        <span class="svc-orbit-label">DESIGN</span>
                        <span class="svc-orbit-label">DATABASE</span>
                        <span class="svc-orbit-label">AI-POWERED</span>
                    </div>
                </div>'''

# Replace from "<!-- Orbital SVG Animation -->" to "</div>" closing the wrapper
pattern = r'<!-- Orbital SVG Animation -->.*?</div>\s*</div>\s*</div>\s*<!-- DETAIL STATE'
replacement = NEW_SVG_BLOCK + '\n            </div>\n\n            <!-- DETAIL STATE'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if new_content == content:
    print("ERROR: Pattern not found")
else:
    with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(new_content)
    print("SUCCESS: Solar system rebuilt with 9 planets on circular orbits")
