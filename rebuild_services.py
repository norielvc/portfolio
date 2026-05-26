import re

with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\n', '\n')

# ─── 1. NEW SOLAR SYSTEM COVER BLOCK ────────────────────────────────────────
NEW_COVER = '''            <!-- COVER STATE: Orbital Animation -->
            <div class="services-cover" id="services-cover">
                <div class="svc-cover-text">
                    <p class="svc-eyebrow">WHAT I DO</p>
                    <h2 class="svc-cover-title">Services<br/><em>&amp; Skills</em></h2>
                    <p class="svc-cover-sub">From infrastructure to interfaces &mdash; I build it end to end.</p>
                    <button class="svc-explore-btn" onclick="openServicesView()">
                        <span>Explore Services</span>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M7 7h10v10"/></svg>
                    </button>
                </div>

                <!-- Orbital SVG Animation — 800×800 viewBox, 9 planets -->
                <div class="svc-orbital-wrapper">
                    <!-- Floating planet pin tooltip -->
                    <div class="planet-pin" id="planet-pin">
                        <div class="planet-pin-label" id="planet-pin-label"></div>
                        <div class="planet-pin-stem"></div>
                        <div class="planet-pin-dot"></div>
                    </div>

                    <svg id="svc-solar-svg" class="svc-orbital-svg" viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <!-- Circular path for each orbit: M cx,cy-r A r,r 0 1 1 cx-0.01,cy-r Z -->
                            <path id="orb0" d="M 400,345 A 55,55  0 1 1 399.99,345  Z"/>
                            <path id="orb1" d="M 400,310 A 90,90  0 1 1 399.99,310  Z"/>
                            <path id="orb2" d="M 400,275 A 125,125 0 1 1 399.99,275 Z"/>
                            <path id="orb3" d="M 400,240 A 160,160 0 1 1 399.99,240 Z"/>
                            <path id="orb4" d="M 400,195 A 205,205 0 1 1 399.99,195 Z"/>
                            <path id="orb5" d="M 400,150 A 250,250 0 1 1 399.99,150 Z"/>
                            <path id="orb6" d="M 400,115 A 285,285 0 1 1 399.99,115 Z"/>
                            <path id="orb7" d="M 400,85  A 315,315 0 1 1 399.99,85  Z"/>
                            <path id="orb8" d="M 400,55  A 345,345 0 1 1 399.99,55  Z"/>
                        </defs>

                        <!-- 9 Orbit rings -->
                        <circle cx="400" cy="400" r="55"  fill="none" stroke="rgba(26,26,26,0.12)" stroke-width="1"/>
                        <circle cx="400" cy="400" r="90"  fill="none" stroke="rgba(26,26,26,0.10)" stroke-width="1"/>
                        <circle cx="400" cy="400" r="125" fill="none" stroke="rgba(26,26,26,0.09)" stroke-width="1"/>
                        <circle cx="400" cy="400" r="160" fill="none" stroke="rgba(26,26,26,0.08)" stroke-width="1"/>
                        <circle cx="400" cy="400" r="205" fill="none" stroke="rgba(26,26,26,0.07)" stroke-width="1"/>
                        <circle cx="400" cy="400" r="250" fill="none" stroke="rgba(26,26,26,0.06)" stroke-width="1"/>
                        <circle cx="400" cy="400" r="285" fill="none" stroke="rgba(26,26,26,0.05)" stroke-width="1"/>
                        <circle cx="400" cy="400" r="315" fill="none" stroke="rgba(26,26,26,0.05)" stroke-width="1"/>
                        <circle cx="400" cy="400" r="345" fill="none" stroke="rgba(26,26,26,0.04)" stroke-width="1"/>

                        <!-- Sun -->
                        <circle cx="400" cy="400" r="28" fill="#1a1a1a" class="svc-sun"/>
                        <circle cx="400" cy="400" r="40" fill="rgba(26,26,26,0.07)" class="svc-sun-pulse"/>
                        <circle cx="400" cy="400" r="56" fill="rgba(26,26,26,0.03)" class="svc-sun-pulse2"/>

                        <!-- Planet 1: Mercury — Web Development -->
                        <circle id="planet-0" r="5"  fill="#1a1a1a" class="svc-planet">
                            <animateMotion dur="5s" repeatCount="indefinite">
                                <mpath href="#orb0"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 2: Venus — SaaS Development -->
                        <circle id="planet-1" r="7"  fill="#2a2a2a" class="svc-planet">
                            <animateMotion dur="9s" repeatCount="indefinite">
                                <mpath href="#orb1"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 3: Earth — Business Automation -->
                        <circle id="planet-2" r="7.5" fill="#333333" class="svc-planet">
                            <animateMotion dur="14s" repeatCount="indefinite">
                                <mpath href="#orb2"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 4: Mars — Responsive Design -->
                        <circle id="planet-3" r="6"  fill="#444444" class="svc-planet">
                            <animateMotion dur="22s" repeatCount="indefinite">
                                <mpath href="#orb3"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 5: Jupiter — Database Solutions -->
                        <circle id="planet-4" r="14" fill="#2d2d2d" class="svc-planet">
                            <animateMotion dur="48s" repeatCount="indefinite">
                                <mpath href="#orb4"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 6: Saturn — AI-Powered Dev (has ring) -->
                        <g id="planet-5" class="svc-planet">
                            <animateMotion dur="70s" repeatCount="indefinite">
                                <mpath href="#orb5"/>
                            </animateMotion>
                            <ellipse rx="16" ry="5" cx="0" cy="0" fill="none" stroke="#666" stroke-width="2" transform="rotate(-25)"/>
                            <circle r="9" fill="#3a3a3a"/>
                        </g>

                        <!-- Planet 7: Uranus — IT Infrastructure -->
                        <circle id="planet-6" r="8"  fill="#555555" class="svc-planet">
                            <animateMotion dur="90s" repeatCount="indefinite">
                                <mpath href="#orb6"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 8: Neptune — Security & DevOps -->
                        <circle id="planet-7" r="8"  fill="#666666" class="svc-planet">
                            <animateMotion dur="115s" repeatCount="indefinite">
                                <mpath href="#orb7"/>
                            </animateMotion>
                        </circle>

                        <!-- Planet 9: Pluto — Mobile Development -->
                        <circle id="planet-8" r="4"  fill="#999999" class="svc-planet">
                            <animateMotion dur="140s" repeatCount="indefinite">
                                <mpath href="#orb8"/>
                            </animateMotion>
                        </circle>
                    </svg>

                    <!-- 9 label tags — each maps to a planet -->
                    <div class="svc-orbit-labels">
                        <span class="svc-orbit-label active" data-planet="0">WEB DEV</span>
                        <span class="svc-orbit-label" data-planet="1">SAAS</span>
                        <span class="svc-orbit-label" data-planet="2">AUTOMATION</span>
                        <span class="svc-orbit-label" data-planet="3">DESIGN</span>
                        <span class="svc-orbit-label" data-planet="4">DATABASE</span>
                        <span class="svc-orbit-label" data-planet="5">AI-POWERED</span>
                        <span class="svc-orbit-label" data-planet="6">IT INFRA</span>
                        <span class="svc-orbit-label" data-planet="7">SECURITY</span>
                        <span class="svc-orbit-label" data-planet="8">MOBILE</span>
                    </div>
                </div>
            </div>'''

# ─── 2. NEW DETAIL VIEW WITH 9 CARDS ────────────────────────────────────────
NEW_DETAIL = '''            <!-- DETAIL STATE: Cards Grid -->
            <div class="services-detail" id="services-detail">
                <div class="svc-detail-header">
                    <button class="svc-back-btn" onclick="closeServicesView()">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
                        <span>Back</span>
                    </button>
                    <h2 class="svc-detail-title">Services <em>&amp; Skills</em></h2>
                </div>
                <div class="services-grid">
                    <div class="service-card">
                        <div class="service-icon">
                            <svg class="svc-icon-svg" viewBox="0 0 60 60" fill="none">
                                <rect x="8" y="14" width="44" height="32" rx="4" class="icon-path"/>
                                <line x1="8" y1="22" x2="52" y2="22" class="icon-path"/>
                                <circle cx="14" cy="18" r="2" class="icon-dot"/>
                                <circle cx="21" cy="18" r="2" class="icon-dot"/>
                                <line x1="20" y1="34" x2="40" y2="34" class="icon-path svc-path-anim"/>
                                <line x1="20" y1="41" x2="33" y2="41" class="icon-path svc-path-anim"/>
                            </svg>
                        </div>
                        <h3>Web Development</h3>
                        <p>Full-featured business websites with modern design and functionality</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon">
                            <svg class="svc-icon-svg" viewBox="0 0 60 60" fill="none">
                                <path d="M30 10 Q50 18 50 30 Q50 48 30 52 Q10 48 10 30 Q10 18 30 10Z" class="icon-path"/>
                                <circle cx="30" cy="30" r="8" class="icon-path"/>
                                <line x1="30" y1="10" x2="30" y2="22" class="icon-path svc-path-anim"/>
                                <line x1="30" y1="38" x2="30" y2="50" class="icon-path svc-path-anim"/>
                            </svg>
                        </div>
                        <h3>SaaS Development</h3>
                        <p>Scalable software-as-a-service platforms for enterprise and government</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon">
                            <svg class="svc-icon-svg" viewBox="0 0 60 60" fill="none">
                                <circle cx="30" cy="30" r="10" class="icon-path"/>
                                <circle cx="30" cy="30" r="18" class="icon-path" style="stroke-dasharray:5 4"/>
                                <line x1="14" y1="14" x2="20" y2="20" class="icon-path svc-path-anim"/>
                                <line x1="46" y1="46" x2="40" y2="40" class="icon-path svc-path-anim"/>
                                <line x1="46" y1="14" x2="40" y2="20" class="icon-path svc-path-anim"/>
                            </svg>
                        </div>
                        <h3>Business Automation</h3>
                        <p>Paperless systems and workflow automation for companies</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon">
                            <svg class="svc-icon-svg" viewBox="0 0 60 60" fill="none">
                                <rect x="18" y="10" width="24" height="40" rx="4" class="icon-path"/>
                                <line x1="23" y1="20" x2="37" y2="20" class="icon-path svc-path-anim"/>
                                <line x1="23" y1="28" x2="37" y2="28" class="icon-path svc-path-anim"/>
                                <circle cx="30" cy="42" r="2.5" class="icon-dot"/>
                            </svg>
                        </div>
                        <h3>Responsive Design</h3>
                        <p>Mobile-first approach ensuring perfect experience on all devices</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon">
                            <svg class="svc-icon-svg" viewBox="0 0 60 60" fill="none">
                                <ellipse cx="30" cy="18" rx="16" ry="6" class="icon-path"/>
                                <path d="M14 18 V30 Q14 36 30 36 Q46 36 46 30 V18" class="icon-path svc-path-anim"/>
                                <path d="M14 30 V42 Q14 48 30 48 Q46 48 46 42 V30" class="icon-path svc-path-anim"/>
                            </svg>
                        </div>
                        <h3>Database Solutions</h3>
                        <p>Efficient database design and optimization for your applications</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon">
                            <svg class="svc-icon-svg" viewBox="0 0 60 60" fill="none">
                                <path d="M30 8 L34 22 L48 22 L37 31 L41 45 L30 36 L19 45 L23 31 L12 22 L26 22 Z" class="icon-path"/>
                                <circle cx="30" cy="26" r="3.5" class="icon-dot"/>
                            </svg>
                        </div>
                        <h3>AI-Powered Development</h3>
                        <p>Leveraging modern AI tools for rapid, efficient development</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon">
                            <svg class="svc-icon-svg" viewBox="0 0 60 60" fill="none">
                                <rect x="10" y="20" width="40" height="26" rx="3" class="icon-path"/>
                                <line x1="18" y1="30" x2="30" y2="30" class="icon-path svc-path-anim"/>
                                <line x1="18" y1="37" x2="26" y2="37" class="icon-path svc-path-anim"/>
                                <path d="M30 20 V12 Q30 8 34 8 L42 8 Q46 8 46 12 V20" class="icon-path svc-path-anim"/>
                            </svg>
                        </div>
                        <h3>IT Infrastructure</h3>
                        <p>Enterprise-grade server, network, and cloud architecture setup</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon">
                            <svg class="svc-icon-svg" viewBox="0 0 60 60" fill="none">
                                <path d="M30 8 L50 16 L50 30 Q50 44 30 52 Q10 44 10 30 L10 16 Z" class="icon-path"/>
                                <polyline points="22,30 28,36 40,24" class="icon-path svc-path-anim"/>
                            </svg>
                        </div>
                        <h3>Security &amp; DevOps</h3>
                        <p>Secure pipelines, threat mitigation, and CI/CD automation</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon">
                            <svg class="svc-icon-svg" viewBox="0 0 60 60" fill="none">
                                <rect x="18" y="8" width="24" height="44" rx="5" class="icon-path"/>
                                <line x1="24" y1="17" x2="36" y2="17" class="icon-path svc-path-anim"/>
                                <circle cx="30" cy="44" r="2.5" class="icon-dot"/>
                            </svg>
                        </div>
                        <h3>Mobile Development</h3>
                        <p>Cross-platform mobile apps built for speed and reliability</p>
                    </div>
                </div>
            </div>'''

# Replace the entire services-inner content
pattern = r'<!-- COVER STATE.*?</div>\s*\n\s*</div>\s*\n\s*</div>\s*\n\s*</section>'
replacement = NEW_COVER + '\n\n' + NEW_DETAIL + '\n\n        </div>\n    </section>'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if new_content == content:
    print("ERROR: Pattern not found, trying alternate...")
    # Fallback: replace from services-inner opening to closing
    start_marker = '            <!-- COVER STATE: Orbital Animation -->'
    end_marker = '        </div>\n    </section>'
    
    start_idx = content.find(start_marker)
    end_idx = content.rfind('        </div>\n    </section>', 0, content.find('<!-- Projects Section'))
    
    if start_idx == -1 or end_idx == -1:
        print(f"start={start_idx}, end={end_idx}")
        print("FAIL: Could not locate markers")
    else:
        new_content = content[:start_idx] + NEW_COVER + '\n\n' + NEW_DETAIL + '\n\n        </div>\n    </section>' + content[end_idx + len('        </div>\n    </section>'):]
        with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', 'w', encoding='utf-8', newline='\r\n') as f:
            f.write(new_content)
        print("SUCCESS via fallback")
else:
    with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(new_content)
    print("SUCCESS: 9-planet solar system with labels rebuilt")
