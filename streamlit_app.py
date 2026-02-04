import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Vouch Coverage Recommender",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Vouch branding
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'DM Sans', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0F1C2C 0%, #1A5745 100%);
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
    }
    
    .vouch-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.75rem;
        background: linear-gradient(135deg, #3BE0AD 0%, #1A5745 100%);
        padding: 0.75rem 1.5rem;
        border-radius: 50px;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(59, 224, 173, 0.3);
    }
    
    .vouch-logo {
        color: #0F1C2C;
        font-size: 1.1rem;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #EFF4E4 0%, #3BE0AD 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        color: #EFF4E4;
        font-size: 1.1rem;
        opacity: 0.85;
        margin-bottom: 2rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #3BE0AD 0%, #1A5745 100%);
        color: #0F1C2C;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 24px rgba(59, 224, 173, 0.5);
    }
    
    .stRadio > div {
        background: rgba(239, 244, 228, 0.05);
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid rgba(239, 244, 228, 0.1);
    }
    
    .stRadio > label {
        color: #EFF4E4 !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }
    
    .stRadio > div > div > label {
        color: #EFF4E4 !important;
        padding: 1rem !important;
        border-radius: 10px;
        background: rgba(239, 244, 228, 0.05) !important;
        border: 2px solid rgba(239, 244, 228, 0.1) !important;
        margin-bottom: 0.5rem !important;
        transition: all 0.3s ease;
    }
    
    .stRadio > div > div > label:hover {
        background: rgba(59, 224, 173, 0.15) !important;
        border-color: #3BE0AD !important;
    }
    
    div[data-testid="stMetric"] {
        background: rgba(239, 244, 228, 0.05);
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid rgba(239, 244, 228, 0.1);
    }
    
    div[data-testid="stMetricLabel"] {
        color: #EFF4E4 !important;
        font-weight: 600 !important;
    }
    
    div[data-testid="stMetricValue"] {
        color: #3BE0AD !important;
        font-weight: 700 !important;
    }
    
    .coverage-card {
        background: rgba(239, 244, 228, 0.05);
        border: 1px solid rgba(239, 244, 228, 0.1);
        border-radius: 16px;
        padding: 1.75rem;
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .coverage-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
        border-color: rgba(59, 224, 173, 0.3);
    }
    
    .coverage-title {
        color: #EFF4E4;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .coverage-limit {
        background: rgba(59, 224, 173, 0.2);
        color: #3BE0AD;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-size: 0.875rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 0.75rem;
    }
    
    .coverage-limit-recommended {
        background: rgba(255, 193, 100, 0.2);
        color: #FFC164;
    }
    
    .coverage-limit-optional {
        background: rgba(239, 244, 228, 0.2);
        color: #EFF4E4;
    }
    
    .coverage-description {
        color: #EFF4E4;
        opacity: 0.8;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 0.75rem;
    }
    
    .coverage-note {
        background: rgba(59, 224, 173, 0.1);
        border: 1px solid rgba(59, 224, 173, 0.3);
        border-radius: 8px;
        padding: 0.75rem;
        color: #EFF4E4;
        font-size: 0.85rem;
        opacity: 0.9;
    }
    
    .section-header {
        color: #EFF4E4;
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .priority-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        display: inline-block;
    }
    
    .priority-essential {
        background: #3BE0AD;
    }
    
    .priority-recommended {
        background: #FFC164;
    }
    
    .priority-optional {
        background: #EFF4E4;
        opacity: 0.5;
    }
    
    .stProgress > div > div {
        background: linear-gradient(90deg, #3BE0AD 0%, #1A5745 100%);
    }
    
    .stProgress > div {
        background: rgba(239, 244, 228, 0.1);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Coverage calculation functions
def get_revenue_index(revenue):
    revenue_map = {
        '$0-$1M': 0, '$1M-$2M': 1, '$2M-$5M': 2, '$5M-$10M': 3, 'Over $10M': 4
    }
    return revenue_map.get(revenue, 0)

def get_gl_limits(answers):
    rev_idx = get_revenue_index(answers.get('revenue'))
    product_type = answers.get('productType')
    vertical = answers.get('vertical')
    
    high_risk = vertical in ['Fintech & Web3', 'Healthcare & Life Sciences']
    
    if product_type == 'Hardware / Physical Products':
        limits = [
            ['$1M/$2M', '$2M/$4M + PCO', '$2M/$4M + PCO', '$4M/$8M + PCO', '$4M/$8M + PCO'],
            ['$1M/$2M', '$2M/$4M + PCO', '$2M/$4M + PCO', '$4M/$8M + PCO', '$4M/$8M + PCO'],
            ['$1M/$2M + $2M Umbrella', '$2M/$4M + PCO', '$2M/$4M + PCO', '$4M/$8M + PCO', '$4M/$8M + PCO']
        ]
        return limits[2 if high_risk else 1][rev_idx]
    elif product_type == 'Professional Services':
        if high_risk:
            return ['$1M/$2M + $2M Umbrella', '$2M/$4M + PCO', '$2M/$4M + PCO', '$4M/$8M + PCO', '$4M/$8M + PCO'][rev_idx]
        return ['$1M/$2M', '$2M/$4M + PCO', '$2M/$4M + PCO', '$4M/$8M + PCO', '$4M/$8M + PCO'][rev_idx]
    else:
        return ['$1M/$2M', '$1M/$2M', '$2M/$4M', '$4M/$8M', '$4M/$8M'][rev_idx]

def get_cyber_limits(answers):
    rev_idx = get_revenue_index(answers.get('revenue'))
    product_type = answers.get('productType')
    vertical = answers.get('vertical')
    pii_records = answers.get('piiRecords', '0-100K')
    
    pii_map = {'0-100K': 0, '100K-1M': 1, '1M-2M': 2, '2M-5M': 3, 'Over 5M': 4}
    pii_idx = pii_map.get(pii_records, 0)
    
    if product_type == 'Hardware / Physical Products':
        limits = [
            ['$1M/$1M', '$1M/$1M', '$2M/$2M', '$2M/$2M', '$3M/$3M+'],
            ['$1M/$1M', '$1M/$1M', '$2M/$2M', '$2M/$2M', '$3M/$3M+'],
            ['$1M/$1M', '$2M/$2M', '$3M/$3M', '$5M/$5M+', '$5M/$5M+'],
            ['$1M/$1M', '$2M/$2M', '$3M/$3M', '$5M/$5M+', '$5M/$5M+'],
            ['$1M/$1M', '$2M/$2M', '$3M/$3M', '$5M/$5M+', '$5M/$5M+']
        ]
        return limits[pii_idx][rev_idx]
    elif vertical in ['Fintech & Web3', 'Healthcare & Life Sciences']:
        limits = [
            ['$1M/$1M', '$2M/$2M', '$2M/$2M', '$5M/$5M', '$5M/$5M+'],
            ['$1M/$1M', '$2M/$2M', '$2M/$2M', '$5M/$5M', '$5M/$5M+'],
            ['$1M/$1M', '$2M/$2M', '$3M/$3M', '$5M/$5M+', '$5M/$5M+'],
            ['$1M/$1M', '$2M/$2M', '$3M/$3M', '$5M/$5M+', '$5M/$5M+'],
            ['$1M/$1M', '$2M/$2M', '$3M/$3M', '$5M/$5M+', '$5M/$5M+']
        ]
        return limits[pii_idx][rev_idx]
    else:
        limits = [
            ['$1M/$1M', '$1M/$1M', '$2M/$2M', '$2M/$2M', '$3M/$3M'],
            ['$1M/$1M', '$2M/$2M', '$2M/$2M', '$2M/$2M', '$3M/$3M+'],
            ['$1M/$1M', '$2M/$2M', '$3M/$3M', '$5M/$5M+', '$5M/$5M+'],
            ['$1M/$1M', '$2M/$2M', '$3M/$3M', '$5M/$5M+', '$5M/$5M+'],
            ['$1M/$1M', '$2M/$2M', '$3M/$3M', '$5M/$5M+', '$5M/$5M+']
        ]
        return limits[pii_idx][rev_idx]

def get_eo_limits(answers):
    rev_idx = get_revenue_index(answers.get('revenue'))
    product_type = answers.get('productType')
    customer_type = answers.get('customerType')
    
    if product_type == 'Hardware / Physical Products':
        if customer_type == 'B2C (Business to Consumer)':
            return ['$1M/$1M', '$1M/$1M', '$2M/$2M', '$3M/$3M', '$3M/$3M+'][rev_idx]
        return ['$1M', '$1M', '$1M', '$2M', '$5M'][rev_idx]
    else:
        return ['$1M', '$1M', '$2M', '$3M', '$5M'][rev_idx]

def get_do_limits(answers):
    cap_raised = answers.get('capitalRaised')
    cap_map = {'$0-$1M': 0, '$1M-$2M': 1, '$2M-$5M': 2, '$5M-$10M': 3, '$10M-$20M': 4, 'Over $20M': 5}
    cap_idx = cap_map.get(cap_raised, 0)
    
    vertical = answers.get('vertical')
    product_type = answers.get('productType')
    
    is_regulated = vertical in ['Fintech & Web3', 'Healthcare & Life Sciences']
    
    if is_regulated:
        if product_type == 'Hardware / Physical Products':
            return ['$1M', '$1M', '$2M', '$2M', '$3M', '$5M'][cap_idx]
        elif product_type == 'Professional Services':
            return ['$1M', '$1M', '$1M', '$2M', '$3M', '$5M'][cap_idx]
        elif vertical == 'Healthcare & Life Sciences':
            return ['$1M', '$1M', '$2M', '$3M', '$3M', '$3M'][cap_idx]
        else:
            return ['$1M', '$1M', '$2M', '$3M', '$3M', '$5M'][cap_idx]
    else:
        if product_type == 'Hardware / Physical Products':
            return ['$1M', '$1M', '$1M', '$2M', '$2M', '$5M'][cap_idx]
        elif product_type == 'Professional Services':
            return ['$1M', '$1M', '$1M', '$2M', '$2M', '$5M'][cap_idx]
        else:
            return ['$1M', '$1M', '$1M', '$2M', '$2M', '$5M'][cap_idx]

def get_epl_limits(answers):
    employee_count = answers.get('employeeCount')
    emp_map = {'1-5': 0, '6-10': 1, '11-20': 2, '21-50': 3, 'Over 50': 4}
    emp_idx = emp_map.get(employee_count, 0)
    
    state = answers.get('stateLocation')
    
    if state == 'California':
        return ['$1M', '$1M', '$2M', '$2M', '$2M+'][emp_idx]
    elif state == 'NY, IL, NJ, MA, or WA':
        return ['$1M', '$1M', '$1M', '$2M', '$2M+'][emp_idx]
    else:
        return ['$1M', '$1M', '$1M', '$2M', '$2M+'][emp_idx]

def get_bpp_limits(answers):
    asset_value = answers.get('assetValue', '$0-$10K')
    asset_map = {
        '$0-$10K': '$10K',
        '$10K-$25K': '$25K',
        '$25K-$50K': '$50K',
        '$50K-$100K': '$100K',
        '$100K-$150K': '$150K',
        '$150K-$250K': '$250K',
        '$250K-$500K': '$500K',
        '$500K-$1M': '$1M'
    }
    return asset_map.get(asset_value, '$10K')

def get_media_limits(answers):
    audience_reach = answers.get('audienceReach')
    if not audience_reach or audience_reach == 'Not applicable':
        return None
    
    reach_map = {
        '0-100K': '$1M',
        '100K-1M': '$1M',
        '1M-5M': '$2M',
        '5M-25M': '$3M',
        'Over 25M': '$5M'
    }
    return reach_map.get(audience_reach)

def calculate_recommendations(answers):
    recs = {}
    
    # General Liability
    recs['gl'] = {
        'name': 'General Liability',
        'limit': get_gl_limits(answers),
        'description': 'Covers third-party bodily injury, property damage, and personal injury claims.',
        'priority': 'essential',
        'notes': 'Includes Products-Completed Operations (PCO) coverage' if answers.get('productType') in ['Hardware / Physical Products', 'Professional Services'] or answers.get('vertical') == 'Healthcare & Life Sciences' else None
    }
    
    # Cyber Liability
    recs['cyber'] = {
        'name': 'Cyber Liability',
        'limit': get_cyber_limits(answers),
        'description': 'Protects against data breaches, network security failures, and privacy violations.',
        'priority': 'essential',
        'notes': f"Based on {answers.get('piiRecords', '0-100K')} PII records" if answers.get('piiRecords', '0-100K') != '0-100K' else None
    }
    
    # E&O
    recs['eo'] = {
        'name': 'Errors & Omissions (E&O)',
        'limit': get_eo_limits(answers),
        'description': 'Coverage for professional mistakes, negligence, and failure to deliver services.',
        'priority': 'essential' if answers.get('customerType') == 'B2B (Business to Business)' else 'recommended',
        'notes': 'Critical for B2B contracts and vendor requirements' if answers.get('customerType') == 'B2B (Business to Business)' else None
    }
    
    # D&O
    cap_val = int(answers.get('capitalRaised', '$0-$1M').split('-')[0].replace('$', '').replace('M', '').replace('Over ', '').replace('+', ''))
    recs['do'] = {
        'name': 'Directors & Officers (D&O)',
        'limit': get_do_limits(answers),
        'description': 'Protects leadership from lawsuits alleging mismanagement or breach of duty.',
        'priority': 'essential' if cap_val > 5 else 'recommended',
        'notes': 'Enhanced limits recommended for regulated industries' if answers.get('vertical') in ['Fintech & Web3', 'Healthcare & Life Sciences'] else None
    }
    
    # EPL
    emp_val = int(answers.get('employeeCount', '1-5').split('-')[0])
    recs['epl'] = {
        'name': 'Employment Practices Liability (EPL)',
        'limit': get_epl_limits(answers),
        'description': 'Covers claims of wrongful termination, discrimination, and harassment.',
        'priority': 'essential' if emp_val > 5 else 'recommended',
        'notes': 'California requires higher limits due to employee-friendly laws' if answers.get('stateLocation') == 'California' else None
    }
    
    # BPP
    recs['bpp'] = {
        'name': 'Business Personal Property',
        'limit': get_bpp_limits(answers),
        'description': 'Covers physical assets like equipment, furniture, and inventory at your locations.',
        'priority': 'recommended'
    }
    
    # Media Liability
    media_limit = get_media_limits(answers)
    if media_limit:
        recs['media'] = {
            'name': 'Media Liability',
            'limit': media_limit,
            'description': 'Protects against copyright infringement, defamation, and content-related claims.',
            'priority': 'recommended',
            'notes': f"Based on {answers.get('audienceReach')} audience reach"
        }
    
    # Hired & Non-Owned Auto
    if answers.get('travelingEmployees') == 'Yes':
        recs['hnoa'] = {
            'name': 'Hired & Non-Owned Auto',
            'limit': '$1M',
            'description': 'Covers employee use of personal or rental vehicles for business purposes.',
            'priority': 'recommended'
        }
    
    # Employee Benefits Liability
    recs['ebl'] = {
        'name': 'Employee Benefits Liability',
        'limit': '$1M/$2M',
        'description': 'Covers errors in administering employee benefit programs.',
        'priority': 'optional'
    }
    
    return recs

# Questions
questions = [
    {
        'id': 'revenue',
        'question': 'What is your annual revenue?',
        'options': ['$0-$1M', '$1M-$2M', '$2M-$5M', '$5M-$10M', 'Over $10M']
    },
    {
        'id': 'vertical',
        'question': 'Which vertical best describes your company?',
        'options': ['Fintech & Web3', 'Healthcare & Life Sciences', 'Consumer Marketplaces', 'Enterprise Software / SaaS', 'Other']
    },
    {
        'id': 'productType',
        'question': 'What do you primarily make or sell?',
        'options': ['Software / Digital Products', 'Hardware / Physical Products', 'Professional Services']
    },
    {
        'id': 'customerType',
        'question': 'Who are your primary customers?',
        'options': ['B2B (Business to Business)', 'B2C (Business to Consumer)', 'Both B2B and B2C']
    },
    {
        'id': 'piiRecords',
        'question': 'How many PII (Personally Identifiable Information) records do you handle?',
        'options': ['0-100K', '100K-1M', '1M-2M', '2M-5M', 'Over 5M']
    },
    {
        'id': 'capitalRaised',
        'question': 'How much capital have you raised (including debt)?',
        'options': ['$0-$1M', '$1M-$2M', '$2M-$5M', '$5M-$10M', '$10M-$20M', 'Over $20M']
    },
    {
        'id': 'employeeCount',
        'question': 'How many full-time employees do you have?',
        'options': ['1-5', '6-10', '11-20', '21-50', 'Over 50']
    },
    {
        'id': 'stateLocation',
        'question': 'Where is your primary business location?',
        'options': ['California', 'NY, IL, NJ, MA, or WA', 'Other State']
    },
    {
        'id': 'assetValue',
        'question': 'What is the total value of your business assets (equipment, furniture, inventory)?',
        'options': ['$0-$10K', '$10K-$25K', '$25K-$50K', '$50K-$100K', '$100K-$150K', '$150K-$250K', '$250K-$500K', '$500K-$1M']
    },
    {
        'id': 'audienceReach',
        'question': 'What is your content/media audience reach? (Optional)',
        'options': ['Not applicable', '0-100K', '100K-1M', '1M-5M', '5M-25M', 'Over 25M']
    },
    {
        'id': 'travelingEmployees',
        'question': 'Do your employees travel for work or use personal vehicles for business?',
        'options': ['Yes', 'No']
    }
]

# Header
st.markdown("""
<div class="main-header">
    <div class="vouch-badge">
        <span class="vouch-logo">🛡️ VOUCH</span>
    </div>
    <h1 class="main-title">Coverage Recommender</h1>
    <p class="subtitle">Get personalized insurance recommendations in minutes</p>
</div>
""", unsafe_allow_html=True)

# Main content
if st.session_state.step < len(questions):
    # Progress bar
    progress = (st.session_state.step + 1) / len(questions)
    st.progress(progress)
    col1, col2 = st.columns(2)
    with col1:
        st.caption(f"Question {st.session_state.step + 1} of {len(questions)}")
    with col2:
        st.caption(f"{int(progress * 100)}% Complete")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Current question
    current_q = questions[st.session_state.step]
    
    # Radio buttons for options
    answer = st.radio(
        current_q['question'],
        current_q['options'],
        key=f"q_{st.session_state.step}"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.step > 0:
            if st.button("← Back"):
                st.session_state.step -= 1
                st.rerun()
    
    with col3:
        if st.button("Next →" if st.session_state.step < len(questions) - 1 else "Get Results"):
            st.session_state.answers[current_q['id']] = answer
            st.session_state.step += 1
            st.rerun()

else:
    # Calculate recommendations
    recommendations = calculate_recommendations(st.session_state.answers)
    
    # Filter by priority
    essential = {k: v for k, v in recommendations.items() if v['priority'] == 'essential'}
    recommended = {k: v for k, v in recommendations.items() if v['priority'] == 'recommended'}
    optional = {k: v for k, v in recommendations.items() if v['priority'] == 'optional'}
    
    # Display results
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">Your Coverage Recommendations</h1>
        <p class="subtitle">Based on your responses, here's your tailored insurance package</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Essential Coverage
    st.markdown("""
    <div class="section-header">
        <span class="priority-dot priority-essential"></span>
        Essential Coverage
    </div>
    """, unsafe_allow_html=True)
    
    for key, coverage in essential.items():
        st.markdown(f"""
        <div class="coverage-card">
            <h3 class="coverage-title">{coverage['name']}</h3>
            <div class="coverage-limit">{coverage['limit']}</div>
            <p class="coverage-description">{coverage['description']}</p>
            {f'<div class="coverage-note">💡 {coverage["notes"]}</div>' if coverage.get('notes') else ''}
        </div>
        """, unsafe_allow_html=True)
    
    # Recommended Coverage
    if recommended:
        st.markdown("""
        <div class="section-header">
            <span class="priority-dot priority-recommended"></span>
            Recommended Coverage
        </div>
        """, unsafe_allow_html=True)
        
        for key, coverage in recommended.items():
            st.markdown(f"""
            <div class="coverage-card">
                <h3 class="coverage-title">{coverage['name']}</h3>
                <div class="coverage-limit coverage-limit-recommended">{coverage['limit']}</div>
                <p class="coverage-description">{coverage['description']}</p>
                {f'<div class="coverage-note">💡 {coverage["notes"]}</div>' if coverage.get('notes') else ''}
            </div>
            """, unsafe_allow_html=True)
    
    # Optional Coverage
    if optional:
        st.markdown("""
        <div class="section-header">
            <span class="priority-dot priority-optional"></span>
            Optional Coverage
        </div>
        """, unsafe_allow_html=True)
        
        for key, coverage in optional.items():
            st.markdown(f"""
            <div class="coverage-card">
                <h3 class="coverage-title">{coverage['name']}</h3>
                <div class="coverage-limit coverage-limit-optional">{coverage['limit']}</div>
                <p class="coverage-description">{coverage['description']}</p>
                {f'<div class="coverage-note">💡 {coverage["notes"]}</div>' if coverage.get('notes') else ''}
            </div>
            """, unsafe_allow_html=True)
    
    # Action buttons
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🔄 Start Over"):
            st.session_state.step = 0
            st.session_state.answers = {}
            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center; padding: 2rem; background: rgba(239, 244, 228, 0.05); border-radius: 16px; border: 1px solid rgba(239, 244, 228, 0.1);">
            <p style="color: #EFF4E4; font-size: 1.1rem; margin-bottom: 1rem;">Ready to secure your coverage?</p>
            <p style="color: #EFF4E4; opacity: 0.7; font-size: 0.95rem; margin-bottom: 1.5rem;">
                Connect with a Vouch advisor to get a quote and customize your policy
            </p>
            <a href="https://vouch.us" target="_blank" style="
                display: inline-block;
                padding: 0.875rem 2rem;
                background: #3BE0AD;
                color: #0F1C2C;
                text-decoration: none;
                border-radius: 10px;
                font-size: 1rem;
                font-weight: 700;
            ">Get Started with Vouch</a>
        </div>
        """, unsafe_allow_html=True)
