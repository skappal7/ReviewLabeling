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

def categorize_review(review):
    billing_keywords = ['invoice', 'payment', 'bill', 'charge', 'refund', 'credit', 'debit', 'balance', 'overdue', 'fee', 'statement', 'account', 'transaction', 'receipt', 'pay', 'finance', 'cost', 'expense', 'price', 'amount', 'due', 'overcharge', 'undercharge', 'billing cycle']
    technical_support_keywords = ['tech support', 'technical', 'troubleshoot', 'error', 'issue', 'bug', 'glitch', 'malfunction', 'repair', 'fix', 'installation', 'setup', 'connectivity', 'network', 'software', 'hardware', 'reboot', 'reset', 'upgrade', 'update', 'compatibility', 'diagnostics', 'assistance', 'support']
    account_management_keywords = ['account', 'profile', 'login', 'password', 'username', 'registration', 'sign up', 'sign in', 'subscription', 'renewal', 'cancel', 'deactivate', 'activate', 'update', 'modify', 'personal information', 'user ID', 'credentials', 'security', 'verification', 'access', 'account settings']
    product_information_keywords = ['product', 'feature', 'specification', 'details', 'model', 'version', 'variant', 'description', 'availability', 'stock', 'price', 'cost', 'warranty', 'guarantee', 'manual', 'guide', 'brochure', 'catalog', 'options', 'selection', 'usage', 'demo', 'sample']
    service_inquiry_keywords = ['service', 'inquiry', 'information', 'details', 'availability', 'schedule', 'appointment', 'booking', 'reservation', 'timing', 'location', 'facility', 'feature', 'benefit', 'offer', 'package', 'plan', 'subscription', 'contract', 'agreement', 'terms']
    complaints_feedback_keywords = ['complaint', 'issue', 'problem', 'dissatisfaction', 'feedback', 'suggestion', 'review', 'criticism', 'concern', 'trouble', 'negative experience', 'poor service', 'bad', 'unhappy', 'unsatisfied', 'resolved', 'unresolved', 'escalate', 'escalation', 'grievance', 'refund', 'compensation']
    sales_renewals_keywords = ['sales', 'purchase', 'buy', 'order', 'renew', 'renewal', 'contract', 'agreement', 'deal', 'discount', 'offer', 'promo', 'pricing', 'cost', 'quote', 'billing', 'payment', 'subscription', 'trial', 'demo', 'upgrade', 'conversion', 'checkout', 'transaction']
    shipping_delivery_keywords = ['shipping', 'delivery', 'dispatch', 'shipment', 'package', 'courier', 'tracking', 'track', 'status', 'estimated delivery', 'delay', 'lost', 'damaged', 'return', 'replacement', 'logistics', 'freight', 'parcel', 'order', 'receive', 'warehouse', 'logistics', 'carrier']
    returns_exchanges_keywords = ['return', 'exchange', 'replacement', 'refund', 'credit', 'policy', 'terms', 'conditions', 'process', 'procedure', 'defective', 'damaged', 'wrong item', 'incorrect', 'sent', 'receive', 'receipt', 'product', 'package', 'return label', 'authorization', 'approval', 'inspection']
    general_inquiry_keywords = ['general', 'inquiry', 'question', 'ask', 'information', 'details', 'assistance', 'help', 'support', 'contact', 'reach out', 'need', 'want', 'clarify', 'understand', 'query', 'explore', 'guidance', 'advice', 'basic', 'common']

    # Convert review to string and then to lowercase for case-insensitive matching
    review = str(review).lower()

    # Check for billing-related keywords
    for keyword in billing_keywords:
        if keyword in review:
            return "Billing and Payments"

    # Check for technical support-related keywords
    for keyword in technical_support_keywords:
        if keyword in review:
            return "Technical Support"

    # Check for account management-related keywords
    for keyword in account_management_keywords:
        if keyword in review:
            return "Account Management"

    # Check for product information-related keywords
    for keyword in product_information_keywords:
        if keyword in review:
            return "Product Information"

    # Check for service inquiry-related keywords
    for keyword in service_inquiry_keywords:
        if keyword in review:
            return "Service Inquiry"

    # Check for complaints and feedback-related keywords
    for keyword in complaints_feedback_keywords:
        if keyword in review:
            return "Complaints and Feedback"

    # Check for sales and renewals-related keywords
    for keyword in sales_renewals_keywords:
        if keyword in review:
            return "Sales and Renewals"

    # Check for shipping and delivery-related keywords
    for keyword in shipping_delivery_keywords:
        if keyword in review:
            return "Shipping and Delivery"

    # Check for returns and exchanges-related keywords
    for keyword in returns_exchanges_keywords:
        if keyword in review:
            return "Returns and Exchanges"

    # Check for general inquiry-related keywords
    for keyword in general_inquiry_keywords:
        if keyword in review:
            return "General Inquiry"

    # If no keywords found, return "Unknown"
    return "Unknown"

st.title('Review Labeling and Categorization App')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    reviews_df = pd.read_csv(uploaded_file)

    # Convert the 'Review' column to string data type
    reviews_df['Review'] = reviews_df['Review'].astype(str)

    # Apply the classify_review function to the 'Review' column
    reviews_df['Label'] = reviews_df['Review'].apply(classify_review)

    # Apply the categorize_review function to the 'Review' column
    reviews_df['Category'] = reviews_df['Review'].apply(categorize_review)

    # Display the labeled and categorized reviews
    st.write(reviews_df)

    # Allow the user to download the labeled and categorized reviews
    st.download_button(
        label="Download labeled and categorized reviews as CSV",
        data=reviews_df.to_csv(index=False),
        file_name='labeled_categorized_reviews.csv',
        mime='text/csv'
    )
else:
    st.write("Please upload a CSV file to get started.")

