import pandas as pd
import re
import streamlit as st

def classify_review(review):
    # Define keywords for each category
    process_keywords = [
        'smooth', 'seamless', 'process', 'efficient', 'straightforward', 'hassle-free', 'user-friendly',
        'convenient', 'fast', 'prompt', 'timely', 'organized', 'structured', 'streamlined',
        'consistent', 'transparent', 'informative', 'clear', 'secure', 'reliable', 'accurate',
        'personalized', 'tailored', 'flexible', 'adaptable', 'responsive', 'accessible',
        'compliant', 'ethical', 'trustworthy', 'confidential', 'supportive', 'value-added',
        'cost-effective', 'comprehensive', 'end-to-end', 'customer-focused', 'needs-based',
        'intuitive', 'logical', 'well-documented', 'standardized', 'repeatable', 'scalable',
        'agile', 'data-driven', 'insightful', 'proactive', 'preventive', 'continuous improvement',
        'innovative', 'transformative', 'sustainable', 'resilient', 'risk-aware', 'compliant',
        'auditable', 'traceable', 'measurable', 'transparent', 'accountable', 'collaborative',
        'workflow', 'procedure', 'protocol', 'methodology', 'approach', 'technique', 'strategy',
        'framework', 'lifecycle', 'transition', 'migration', 'implementation', 'execution', 'delivery',
        'simple', 'easy', 'slow', 'disorganized', 'inefficient', 'confusing', 'outdated', 
        'cumbersome', 'rigid', 'error-prone', 'bureaucratic', 'redundant', 'inconsistent', 'unresponsive'
    ]
    technology_keywords = [
        'intuitive', 'invalid', 'pin', 'user-friendly', 'modern', 'advanced', 'innovative', 'cutting-edge',
        'reliable', 'efficient', 'fast', 'responsive', 'secure', 'robust', 'stable',
        'integrated', 'seamless', 'accessible', 'mobile-friendly', 'omnichannel', 'personalized',
        'customizable', 'interactive', 'intelligent', 'automated', 'self-service', 'convenient',
        'informative', 'transparent', 'real-time', 'data-driven', 'analytical', 'insightful',
        'scalable', 'flexible', 'adaptable', 'future-proof', 'compatibility', 'interoperability',
        'cloud-based', 'virtualized', 'resilient', 'fault-tolerant', 'privacy-compliant',
        'contextual', 'predictive', 'cognitive', 'conversational', 'natural language', 'voice-enabled',
        'multi-modal', 'immersive', 'augmented', 'virtual', 'blockchain-powered', 'distributed',
        'decentralized', 'sustainable', 'energy-efficient', 'eco-friendly', 'ethical', 'transparent',
        'accountable', 'inclusive', 'accessible', 'register', 'buggy', 'glitchy', 'glitch',
        'app', 'application', 'mobile app', 'android app', 'ios app', 'website', 'web app', 'portal',
        'platform', 'interface', 'dashboard', 'chatbot', 'virtual assistant', 'voice assistant',
        'bug', 'download', 'attachment', 'load', 'crashing', 'install', 'reinstall', 'code', 'error',
        'rin', 'hack', 'hacking', 'scam', 'login', 'log', 'notification', 'track', 'location', 'offline',
        'pdf', 'image', 'upload', 'photo', 'click', 'slow', 'unresponsive', 'insecure', 'complicated',
        'hard-to-use', 'malfunction', 'fail', 'downtime'
    ]
    people_keywords = [
        'friendly', 'knowledgeable', 'helpful', 'patient', 'attentive', 'empathetic', 'responsive',
        'professional', 'courteous', 'communicative', 'efficient', 'dedicated', 'well-trained',
        'reliable', 'accessible', 'multilingual', 'personable', 'understanding', 'supportive',
        'experienced', 'reassuring', 'proactive', 'approachable', 'caring', 'compassionate',
        'trustworthy', 'accommodating', 'service-minded', 'respectful', 'polite', 'empowering',
        'motivating', 'encouraging', 'engaging', 'clear communication', 'problem-solving',
        'situational awareness', 'emotional intelligence', 'customer-centric', 'culturally aware',
        'adaptive', 'resilient', 'collaborative', 'team-oriented', 'passionate', 'committed',
        'accountable', 'ethical', 'transparent', 'authentic', 'they', 'he', 'man', 'lady', 'she',
        'rude', 'incompetent', 'unhelpful', 'impatient', 'inattentive', 'insensitive', 'unresponsive',
        'unprofessional', 'discourteous', 'uncommunicative', 'inefficient', 'careless', 'untrained',
        'unreliable', 'inaccessible', 'uninformed', 'impersonal', 'unsupportive', 'inexperienced',
        'dismissive', 'passive', 'unapproachable', 'uncaring', 'untrustworthy', 'inflexible',
        'condescending', 'demotivating', 'discouraging', 'disengaging', 'unclear communication',
        'problem-ignoring', 'situationally unaware', 'emotionally unintelligent', 'self-centered',
        'culturally insensitive', 'rigid', 'fragile', 'uncooperative', 'individualistic', 'apathetic',
        'uncommitted', 'unaccountable', 'unethical', 'opaque', 'inauthentic'
    ]

    # Convert review to string and then to lowercase for case-insensitive matching
    review = str(review).lower()

    # Check for process-related keywords
    for keyword in process_keywords:
        if keyword in review:
            return "Process"

    # Check for technology-related keywords
    for keyword in technology_keywords:
        if keyword in review:
            return "Technology"

    # Check for people-related keywords
    for keyword in people_keywords:
        if keyword in review:
            return "People"

    # If no keywords found, return "Unknown"
    return "Unknown"

st.title('Customer Review Labeling App')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    reviews_df = pd.read_csv(uploaded_file)

    # Convert the 'Review' column to string data type
    reviews_df['Review'] = reviews_df['Review'].astype(str)

    # Apply the classify_review function to the 'Review' column
    reviews_df['Label'] = reviews_df['Review'].apply(classify_review)

    # Display the labeled reviews
    st.write(reviews_df)

    # Allow the user to download the labeled reviews
    st.download_button(
        label="Download labeled reviews as CSV",
        data=reviews_df.to_csv(index=False),
        file_name='labeled_reviews.csv',
        mime='text/csv'
    )
else:
    st.write("Please upload a CSV file to get started.")
