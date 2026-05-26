# Portfolio Website - Full Stack Developer

An elegant, modern portfolio website showcasing your work as a Full Stack Developer.

## Features

- **Responsive Design** - Works perfectly on all devices
- **Smooth Animations** - Engaging scroll animations and transitions
- **Modern UI** - Clean, professional design with orange accent color
- **Typing Animation** - Dynamic title animation on hero section
- **Project Showcase** - Display your 5 completed projects
- **Contact Form** - Easy way for clients to reach you
- **Mobile Navigation** - Hamburger menu for mobile devices

## Sections

1. **Home/Hero** - Introduction with your photo and key information
2. **About** - Your background and skills overview
3. **Services** - What you offer to clients
4. **Projects** - Showcase of your 5 completed projects
5. **Resume** - Experience and skills with progress bars
6. **Contact** - Contact form and social links

## Customization Guide

### 1. Personal Information

Edit `index.html` and replace:
- `Your Name` - Your actual name
- `your.email@example.com` - Your email
- `+1 234 567 8900` - Your phone number
- `Your City, Country` - Your location

### 2. Profile Photo

Replace the placeholder image:
```html
<img src="https://via.placeholder.com/400x500" alt="Profile" id="profile-img">
```

Change to:
```html
<img src="your-photo.jpg" alt="Your Name" id="profile-img">
```

### 3. Projects

For each project card, update:
- Project image (`src="your-project-image.jpg"`)
- Project title
- Project description
- Technology tags
- Project link (`href="your-project-url"`)

### 4. Skills

Update the skill bars in the Resume section with your actual skills and percentages.

### 5. Social Links

Update the social media links in the contact section:
```html
<a href="https://github.com/yourusername"><i class="fab fa-github"></i></a>
<a href="https://linkedin.com/in/yourusername"><i class="fab fa-linkedin"></i></a>
<a href="https://twitter.com/yourusername"><i class="fab fa-twitter"></i></a>
```

### 6. Colors

To change the color scheme, edit `styles.css`:
```css
:root {
    --primary-color: #FF8C42; /* Change this to your preferred color */
    --secondary-color: #2C3E50;
}
```

### 7. Resume Download

Add your resume PDF and update the link:
```html
<a href="your-resume.pdf" class="btn btn-primary" download>
```

## Technologies Used

- HTML5
- CSS3 (with CSS Grid and Flexbox)
- Vanilla JavaScript
- Font Awesome Icons

## How to Use

1. Download all files (index.html, styles.css, script.js)
2. Customize the content as described above
3. Add your photos and project images
4. Open `index.html` in a browser to preview
5. Deploy to your hosting service (GitHub Pages, Netlify, Vercel, etc.)

## Deployment Options

### GitHub Pages (Free)
1. Create a GitHub repository
2. Upload your files
3. Go to Settings > Pages
4. Select main branch and save
5. Your site will be live at `https://yourusername.github.io/repository-name`

### Netlify (Free)
1. Sign up at netlify.com
2. Drag and drop your folder
3. Your site is live instantly

### Vercel (Free)
1. Sign up at vercel.com
2. Import your GitHub repository
3. Deploy with one click

## Tips for Success

1. **Use Professional Photos** - High-quality, professional headshot
2. **Showcase Real Projects** - Add screenshots and live links
3. **Keep It Updated** - Regularly add new projects
4. **SEO Optimization** - Add meta tags for better search visibility
5. **Performance** - Optimize images for faster loading
6. **Analytics** - Add Google Analytics to track visitors

## Contact Form Setup

The contact form currently shows an alert. To make it functional:

1. **Using Formspree (Easy)**
   - Sign up at formspree.io
   - Get your form endpoint
   - Update form action: `<form action="https://formspree.io/f/your-id" method="POST">`

2. **Using EmailJS (Free)**
   - Sign up at emailjs.com
   - Follow their integration guide
   - Update the JavaScript in script.js

3. **Backend Integration**
   - Create your own backend API
   - Update the form submission handler in script.js

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License

Free to use for personal and commercial projects.

---

**Good luck with your portfolio! Remember to highlight your AI-assisted development skills as a modern advantage.**
