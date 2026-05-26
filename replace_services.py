import re

with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', encoding='utf-8') as f:
    content = f.read()

# Normalize line endings
content_lf = content.replace('\r\n', '\n')

NEW_SECTION = '''    <!-- Services Section -->
    <section id="services" class="services">
        <div class="services-inner">

            <!-- COVER STATE: Orbital Animation -->
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

                <!-- Orbital SVG Animation -->
                <div class="svc-orbital-wrapper">
                    <svg class="svc-orbital-svg" viewBox="0 0 500 360" xmlns="http://www.w3.org/2000/svg">
                        <ellipse cx="250" cy="180" rx="220" ry="88" fill="none" stroke="rgba(26,26,26,0.09)" stroke-width="1.2"/>
                        <ellipse cx="250" cy="180" rx="155" ry="62" fill="none" stroke="rgba(26,26,26,0.07)" stroke-width="1"/>
                        <ellipse cx="250" cy="180" rx="88" ry="35" fill="none" stroke="rgba(26,26,26,0.05)" stroke-width="1"/>
                        <circle cx="250" cy="180" r="22" fill="#1a1a1a" class="svc-sun"/>
                        <circle cx="250" cy="180" r="34" fill="rgba(26,26,26,0.06)" class="svc-sun-pulse"/>
                        <circle cx="250" cy="180" r="48" fill="rgba(26,26,26,0.03)" class="svc-sun-pulse2"/>
                        <g class="orb-ring-1"><circle cx="250" cy="118" r="11" fill="#1a1a1a"/></g>
                        <g class="orb-ring-2"><circle cx="405" cy="180" r="14" fill="#2a2a2a"/></g>
                        <g class="orb-ring-3"><circle cx="95" cy="180" r="10" fill="#444444"/></g>
                        <g class="orb-ring-1b"><circle cx="162" cy="135" r="8" fill="#666666"/></g>
                        <g class="orb-ring-2b"><circle cx="470" cy="210" r="7" fill="#888888"/></g>
                        <g class="orb-ring-3b"><circle cx="338" cy="215" r="9" fill="#aaaaaa"/></g>
                    </svg>
                    <div class="svc-orbit-labels">
                        <span class="svc-orbit-label active">WEB DEV</span>
                        <span class="svc-orbit-label">SAAS</span>
                        <span class="svc-orbit-label">AUTOMATION</span>
                        <span class="svc-orbit-label">DESIGN</span>
                        <span class="svc-orbit-label">DATABASE</span>
                        <span class="svc-orbit-label">AI-POWERED</span>
                    </div>
                </div>
            </div>

            <!-- DETAIL STATE: Cards Grid -->
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
                </div>
            </div>

        </div>
    </section>'''

# Use regex to find and replace the services section
pattern = r'    <!-- Services Section -->.*?</section>'
new_content = re.sub(pattern, NEW_SECTION, content_lf, flags=re.DOTALL)

if new_content == content_lf:
    print("ERROR: Pattern not found, no replacement made")
else:
    # Write back with original line endings
    with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\index.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(new_content)
    print("SUCCESS: Services section replaced")
