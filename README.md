# Vouch Coverage Recommender - Streamlit App

A user-friendly, interactive tool that provides personalized insurance coverage recommendations for Vouch Insurance clients.

## Features

- ✅ 11 targeted questions to understand your business
- ✅ Smart recommendations based on Vouch's underwriting guidelines
- ✅ Vouch-branded design (Dark Blue, Light Green, Taupe color palette)
- ✅ Priority-based coverage organization (Essential, Recommended, Optional)
- ✅ Mobile-responsive interface
- ✅ Easy deployment to Streamlit Cloud

## Quick Start

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Open your browser:**
   The app will automatically open at `http://localhost:8501`

### Deploy to Streamlit Cloud (Free)

1. **Create a GitHub repository:**
   - Go to https://github.com/new
   - Create a new repository (e.g., `vouch-coverage-recommender`)
   - Upload these files:
     - `streamlit_app.py`
     - `requirements.txt`
     - `README.md`

2. **Deploy to Streamlit Cloud:**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Connect your GitHub account
   - Select your repository
   - Set main file path: `streamlit_app.py`
   - Click "Deploy"

3. **Your app will be live at:**
   `https://[your-app-name].streamlit.app`

## File Structure

```
vouch-coverage-recommender/
├── streamlit_app.py      # Main application file
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Customization

### Update Coverage Logic
Edit the calculation functions in `streamlit_app.py`:
- `get_gl_limits()`
- `get_cyber_limits()`
- `get_eo_limits()`
- `get_do_limits()`
- `get_epl_limits()`

### Modify Questions
Update the `questions` list in `streamlit_app.py` to add/remove questions or change options.

### Adjust Branding
Modify the CSS in the `st.markdown()` section to change colors, fonts, or styling.

## Coverage Types Included

- **General Liability (GL)** - Third-party bodily injury and property damage
- **Cyber Liability** - Data breaches and network security failures
- **Errors & Omissions (E&O)** - Professional mistakes and negligence
- **Directors & Officers (D&O)** - Leadership protection
- **Employment Practices Liability (EPL)** - Wrongful termination and discrimination
- **Business Personal Property (BPP)** - Physical assets coverage
- **Media Liability** - Copyright and content claims (when applicable)
- **Hired & Non-Owned Auto (HNOA)** - Vehicle coverage (when applicable)
- **Employee Benefits Liability (EBL)** - Benefit program errors

## Support

For questions or issues:
- Email: [your-email@vouch.us]
- Internal Slack: #product-marketing

## License

Internal use only - Vouch Insurance
