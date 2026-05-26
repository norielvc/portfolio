import re

html_to_append = """    <!-- Project Modal Structure -->
    <div id="project-modal" class="project-modal">
        <div class="modal-content">
            <button class="modal-close" onclick="closeProjectModal()">x</button>
            
            <div class="modal-visual">
                <div class="mockup-wrapper">
                    <div class="mockup-frame">
                        <img id="modal-main-img" src="" alt="Project Visual" class="modal-main-img">
                    </div>
                </div>
                <div class="modal-gallery" id="modal-gallery">
                    <!-- Gallery thumbs injected by JS -->
                </div>
            </div>
            
            <div class="modal-details">
                <span class="modal-tag">Project</span>
                <h2 id="modal-title" class="modal-title">PROJECT TITLE</h2>
                
                <h4 class="modal-section-title">About</h4>
                <p id="modal-about" class="modal-about">Description goes here.</p>
                
                <a id="modal-launch-link" href="#" target="_blank" class="modal-launch-btn">
                    Launch Project <i class="fas fa-external-link-alt"></i>
                </a>

                <div class="modal-nav">
                    <button class="modal-nav-btn" onclick="prevProject()"><i class="fas fa-arrow-left"></i></button>
                    <button class="modal-nav-btn" onclick="nextProject()"><i class="fas fa-arrow-right"></i></button>
                    <span class="modal-counter"><span id="modal-curr-idx">1</span>/<span id="modal-total-count">4</span></span>
                </div>
            </div>
        </div>
    </div>

    <!-- Contact Section -->
    <section id="contact" class="contact reveal">
        <div class="container">
            <div class="contact-content" style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 40px;">
                <!-- Left: Info Panel -->
                <div class="contact-info-panel">
                    <h2 class="contact-title">Let's Build Something Together</h2>
                    <p class="contact-desc">Whether it's a massive infrastructure project or an innovative web application, I'm ready to bring your vision to life.</p>
                    
                    <div class="contact-status-badge">
                        <span class="contact-status-dot"></span>
                        AVAILABLE FOR FREELANCE & CONTRACT
                    </div>

                    <div class="contact-info-items" style="margin-top: 30px;">
                        <a href="mailto:contact@example.com" class="contact-info-item">
                            <div class="contact-info-icon"><i class="fas fa-envelope"></i></div>
                            <div class="contact-info-text">
                                <span class="contact-info-label">EMAIL ME</span>
                                <span class="contact-info-value">contact@example.com</span>
                            </div>
                            <i class="fas fa-arrow-right contact-info-arrow" style="margin-left: auto;"></i>
                        </a>
                        <div class="contact-divider" style="margin: 15px 0;"></div>
                        <a href="#" class="contact-info-item no-link">
                            <div class="contact-info-icon"><i class="fas fa-map-marker-alt"></i></div>
                            <div class="contact-info-text">
                                <span class="contact-info-label">LOCATION</span>
                                <span class="contact-info-value">Metro Manila, Philippines</span>
                            </div>
                        </a>
                    </div>

                    <div class="contact-socials" style="margin-top: 30px;">
                        <span class="contact-socials-label">SOCIAL PROTOCOLS</span>
                        <div class="contact-social-row" style="margin-top: 10px;">
                            <a href="#" class="contact-social-btn"><i class="fab fa-linkedin-in"></i></a>
                            <a href="#" class="contact-social-btn"><i class="fab fa-github"></i></a>
                            <a href="#" class="contact-social-btn"><i class="fab fa-twitter"></i></a>
                        </div>
                    </div>
                </div>

                <!-- Right: Form Panel -->
                <div class="contact-form-panel">
                    <form id="contact-form" class="contact-form">
                        <div class="contact-form-row">
                            <div class="contact-field">
                                <label for="contact-name">NAME / ID</label>
                                <input type="text" id="contact-name" placeholder="John Doe" required>
                            </div>
                            <div class="contact-field">
                                <label for="contact-email">COMM-LINK (EMAIL)</label>
                                <input type="email" id="contact-email" placeholder="john@example.com" required>
                            </div>
                        </div>
                        <div class="contact-field" style="margin-top: 20px;">
                            <label for="contact-message">TRANSMISSION (MESSAGE)</label>
                            <textarea id="contact-message" rows="5" placeholder="How can I help you?" required></textarea>
                        </div>
                        
                        <div class="contact-form-footer" style="margin-top: 20px; display: flex; justify-content: space-between; align-items: center;">
                            <button type="submit" id="contact-submit" class="contact-submit-btn">
                                <span class="contact-submit-text">INITIATE TRANSMISSION</span>
                                <span class="contact-submit-icon"><i class="fas fa-paper-plane"></i></span>
                                <span class="contact-submit-loading"><i class="fas fa-spinner fa-spin"></i></span>
                            </button>
                            <span class="contact-form-note">Encrypted & Secure</span>
                        </div>
                        <div id="contact-feedback" class="contact-feedback"></div>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content" style="text-align: center; padding: 40px 0; border-top: 1px solid #222; margin-top: 40px;">
                <p class="footer-text">&copy; 2026 Full Stack Developer. All systems nominal.</p>
            </div>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="script.js"></script>
</body>
</html>"""

with open('index.html', 'a', encoding='utf-8') as f:
    f.write(html_to_append)
print("index.html fixed!")
