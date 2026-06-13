import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Briefly AI", page_icon="🚀", layout="centered")

# 2. Premium Styling
st.markdown("""
    <style>
    .main-title {font-size: 42px !important; font-weight: 800; text-align: center; margin-bottom: 10px;}
    .sub-title {font-size: 20px !important; text-align: center; color: #666; margin-bottom: 40px;}
    .feature-box {padding: 20px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown("<div class='main-title'>Turn 1 Video or Article into 2 Weeks of Premium Content</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Drop a link. Get a complete LinkedIn, X, and Newsletter distribution kit in 60 seconds.</div>", unsafe_allow_html=True)

# 4. The Interactive Core UI (The Illusion)
source_url = st.text_input("🔗 Paste your YouTube, Podcast, or Article URL here:", placeholder="https://..." )

col1, col2 = st.columns(2)
with col1:
    tone = st.selectbox("Select Writing Tone", ["Thought Leader / Authoritative", "Casual Storyteller", "Data-Driven Analyst"])
with col2:
    output_length = st.select_slider("Output Depth", options=["Short & Punchy", "Balanced", "Deep Dive"])

# 5. The Golden Trap (The Smoke Test Button)
if st.button("✨ Generate My Distribution Kit", type="primary", use_container_width=True):
    if not source_url:
        st.warning("Please paste a URL first!")
    else:
        # Step into the conversion funnel
        st.success("⚡ URL analyzed! Your optimized multi-channel content kit is ready.")
        
        # Display blurred placeholder text to simulate real data loading behind a wall
        st.markdown("### 🔒 Previewing Your Generated Content Assets...")
        st.info("💡 Our AI found 4 massive talking points in your source link. Unlock the full text below:")
        
        st.markdown("""
        <div class='feature-box' style='filter: blur(4px); opacity: 0.5;'>
        <strong>LinkedIn Post Asset:</strong><br>
        How we scaled our operations by 400% without hiring a single manager...
        </div>
        """, unsafe_allow_html=True)
        
        # The Actionable Conversion Form
        with st.form("conversion_form"):
            st.markdown("### 🚀 Claim Your Content Kit")
            st.write("We are currently in Early-Bird Beta. Lock in your lifetime account today for a flat 70% off.")
            
            user_email = st.text_input("Enter your business email:")
            submit_payment = st.form_submit_button("💳 Unlock My Kit Now ($29/mo)")
            
            if submit_payment:
                if "@" in user_email:
                    # Redirect them straight to your Stripe Payment Link
                    st.markdown("""
                        <meta http-equiv="refresh" content="0; url=https://buy.stripe.com/mock_link_replace_with_yours" />
                        <script>window.location.href = 'https://buy.stripe.com/mock_link_replace_with_yours';</script>
                    """, unsafe_allow_html=True)
                    st.info("Redirecting you securely to Stripe Checkout...")
                else:
                    st.error("Please enter a valid email address.")

# 6. Trust Signals / Proof Section
st.markdown("---")
st.markdown("### Why Top Creators Choose Briefly")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**Zero Fluff**\n\nAI frameworks optimized for human engagement, not robotic jargon.")
with c2:
    st.markdown("**Cross-Platform**\n\nPerfect formatting hooks for LinkedIn, X threads, and email.")
with c3:
    st.markdown("**Pure Speed**\n\nGo from a raw ideas/videos to a fully loaded content calendar in minutes.")
