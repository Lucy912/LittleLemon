# ProAI Website - MVP Documentation

## Overview

This is a frontend-only MVP website for ProAI, designed to launch within 2 weeks with a clear message and working Stripe payment links.

**Goal:** A professional, single-page website that clearly communicates ProAI's value proposition and enables direct purchases through Stripe.

---

## 🎯 Key Features

- **Single-page scrolling design** with smooth navigation
- **AI Training Section** with 3 pricing tiers (Starter, Pro, Enterprise)
- **AI Templates Marketplace** with 4 ready-to-use automation templates
- **About & Contact Section** with email and LinkedIn links
- **Fully responsive** design (mobile, tablet, desktop)
- **Professional styling** with ProAI blue (#0070F3)
- **Fast loading** - optimized for under 2 seconds

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Pipenv (or pip)
- MySQL 8.0+ (optional - Django is configured but website is frontend-only)

### Installation

1. **Navigate to the Django project directory:**
   ```bash
   cd littlelemon
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   # or
   pip install -r requirements.txt
   ```

3. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

4. **Open your browser:**
   ```
   http://127.0.0.1:8000/
   ```

That's it! The ProAI website should now be running.

---

## 📝 Customization Guide

### 1. Update Stripe Payment Links

**IMPORTANT:** Replace the placeholder Stripe links with your actual Stripe Checkout URLs.

Open the HTML file: `Static routes assets/templates/index.html`

**AI Training Plans (lines 76, 94, 111):**
```html
<!-- Starter Plan -->
<a href="https://buy.stripe.com/starter" ... >

<!-- Pro Plan -->
<a href="https://buy.stripe.com/pro" ... >

<!-- Enterprise Plan -->
<a href="https://buy.stripe.com/enterprise" ... >
```

Replace with your Stripe Checkout URLs:
```html
<a href="https://buy.stripe.com/test_YOUR_ACTUAL_LINK" ... >
```

**Template Products (lines 136, 151, 166, 181):**
```html
<!-- Email Template -->
<a href="https://buy.stripe.com/template-email" ... >

<!-- Report Template -->
<a href="https://buy.stripe.com/template-report" ... >

<!-- Meeting Template -->
<a href="https://buy.stripe.com/template-meeting" ... >

<!-- Social Template -->
<a href="https://buy.stripe.com/template-social" ... >
```

### 2. Update Contact Information

**Email Address (line 212):**
```html
<a href="mailto:contact@proai.com" ... >
```
Replace `contact@proai.com` with your actual email.

**LinkedIn URL (line 213):**
```html
<a href="https://www.linkedin.com/in/xiangli-proai" ... >
```
Replace with Xiang Li's actual LinkedIn profile URL.

### 3. Customize Content

**Hero Section (lines 43-44):**
- Edit headline and subtitle as needed

**About Section (lines 200-208):**
- Update the company description and mission statement

**Pricing Details:**
- Modify prices, features, and descriptions in the pricing cards

### 4. Replace Placeholder Images

The website currently uses SVG placeholders for template images. Replace these with actual screenshots:

**Location:** `Static routes assets/static/img/`

**Files to replace:**
- `template-email.jpg` - Email automation workflow screenshot
- `template-report.jpg` - Report generator interface
- `template-meeting.jpg` - Meeting notes automation
- `template-social.jpg` - Social media content creator

**Recommended specs:**
- Format: JPG or PNG
- Size: 400x300 pixels (or maintain 4:3 aspect ratio)
- File size: < 100KB each for fast loading

### 5. Update Logo (Optional)

**Current logo:** `Static routes assets/static/img/proai-logo.svg`

Replace with your professional logo if available:
- Recommended size: 120x40 pixels
- Format: SVG (preferred) or PNG with transparent background
- Also update `proai-favicon.png` (32x32 pixels)

---

## 🎨 Design System

### Color Palette
- **Primary Blue:** `#0070F3` (CTAs, links, highlights)
- **Text Dark:** `#1a1a1a` (headings, primary text)
- **Text Gray:** `#666666` (descriptions, secondary text)
- **Background:** `#ffffff` (main), `#f8f9fa` (alternating sections)

### Typography
- **Font:** Inter (Google Fonts)
- **Heading sizes:** 56px (hero), 42px (sections), 24px (cards)
- **Body text:** 16-20px

### Spacing & Layout
- **Max width:** 1200px (centered content)
- **Section padding:** 100px vertical (60px on mobile)
- **Button radius:** 8px with hover effects

---

## 📁 File Structure

```
LittleLemon/
├── Static routes assets/
│   ├── static/
│   │   ├── css/
│   │   │   └── proai-style.css          # Main stylesheet
│   │   └── img/
│   │       ├── proai-logo.svg           # ProAI logo
│   │       ├── proai-favicon.png        # Browser favicon
│   │       ├── template-email.jpg       # Placeholder images
│   │       ├── template-report.jpg
│   │       ├── template-meeting.jpg
│   │       └── template-social.jpg
│   └── templates/
│       └── index.html                   # Main website file
└── littlelemon/                         # Django project
    ├── manage.py
    └── ...
```

---

## ✅ Pre-Launch Checklist

Before launching, ensure you've completed:

- [ ] Updated all Stripe payment links with live/test URLs
- [ ] Changed contact email to your actual address
- [ ] Updated LinkedIn profile URL
- [ ] Replaced placeholder template images with real screenshots
- [ ] Tested all payment links (use Stripe test mode first)
- [ ] Verified email link opens your email client
- [ ] Tested on mobile devices (responsive design)
- [ ] Checked website loads in under 2 seconds
- [ ] Reviewed all content for typos and accuracy
- [ ] Set up Stripe products with correct prices
- [ ] Tested the entire purchase flow

---

## 🔧 Technical Notes

### Django Configuration

The website uses Django as a simple web server. Key settings:

**Settings file:** `littlelemon/littlelemon/settings.py`
- Templates directory: `Static routes assets/templates`
- Static files directory: `Static routes assets/static`

**URL routing:** `littlelemon/littlelemon/urls.py`
- Homepage: `path('', views.index, name='home')`

### Static Files in Development

Django serves static files automatically in development mode (`DEBUG = True`).

For production deployment:
1. Run `python manage.py collectstatic`
2. Configure your web server (nginx/Apache) to serve static files
3. Set `DEBUG = False`
4. Add your domain to `ALLOWED_HOSTS`

---

## 📊 Success Metrics

Track these KPIs after launch:

1. **Clarity Test:** Can visitors understand ProAI within 10 seconds?
2. **Load Speed:** Website loads under 2 seconds on mobile
3. **Conversion:** First purchase within 14 days
4. **Stripe Integration:** All payment links work flawlessly

---

## 🔮 Future Enhancements

Features to add after MVP launch:

- [ ] Blog section for SEO traffic
- [ ] Newsletter subscription form (MailChimp/ConvertKit)
- [ ] Customer testimonials carousel
- [ ] Language switcher (English/Chinese)
- [ ] Embedded AI demo (video or interactive chatbot)
- [ ] Analytics integration (Google Analytics/Plausible)
- [ ] Live chat support widget

---

## 🐛 Troubleshooting

### Static files not loading?

```bash
# Make sure you're in the Django directory
cd littlelemon

# Try running with --insecure flag
python manage.py runserver --insecure
```

### Page not found (404)?

Check that:
1. You're accessing `http://127.0.0.1:8000/` (not `/restaurant/`)
2. The Django server is running
3. Templates directory path is correct in settings.py

### Stripe links not working?

- Verify you've replaced placeholder URLs
- Test in Stripe's test mode first
- Check Stripe dashboard for any errors

---

## 📞 Support

For technical issues with this website:
- Check Django documentation: https://docs.djangoproject.com/
- Stripe integration guide: https://stripe.com/docs/payments/checkout

---

## 📄 License

© 2025 ProAI. All rights reserved.

---

**Built with:** HTML, CSS, JavaScript, Django 4.2
**Launch Timeline:** 2 weeks
**Version:** 0.9 (MVP)
