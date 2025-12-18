import streamlit as st
import pandas as pd
import datetime

# ==========================================
# ⚙️ Page Configuration
# ==========================================
st.set_page_config(
    page_title="GreenAudit | ESG Reporting Tool",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 🎨 Custom CSS
# ==========================================
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    h1 { color: #2E7D32; }
    .stMetric { background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 📱 Sidebar: Company Profile
# ==========================================
with st.sidebar:
    
    st.image("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=800&q=80", caption="Company HQ")
    
    st.title("GreenAudit")
    st.caption("SME Sustainability Reporting")
    st.divider()
    
    st.header("🏢 Company Profile")
    company_name = st.text_input("Company Name", "Maple Leaf Logistics")
    industry = st.selectbox("Industry Sector", ["Logistics", "Manufacturing", "Retail"])
    
    st.divider()
    st.info("ℹ️ Compliant with **IFRS S2** & **GHG Protocol**.")

# ==========================================
# 🏠 Main Dashboard
# ==========================================
st.title(f"🌿 ESG Carbon Audit: {company_name}")
st.markdown("### Environmental Impact Assessment (Scope 1 & 2)")
st.markdown("---")

# --- Section 1: Data Entry ---
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader("🔥 Scope 1: Direct Emissions")
        st.caption("Fuel combustion from company vehicles.")
        
        st.image("https://cdn-icons-png.flaticon.com/128/1598/1598196.png", width=40)
        fuel_consumption = st.number_input("Diesel Consumption (Liters)", min_value=0.0, value=1200.0)
        gas_consumption = st.number_input("Natural Gas Usage (m³)", min_value=0.0, value=500.0)
        
        FACTOR_FUEL = 2.68
        FACTOR_GAS = 1.90

with col2:
    with st.container(border=True):
        st.subheader("⚡ Scope 2: Indirect Emissions")
        st.caption("Purchased electricity for operations.")
        
        st.image("https://cdn-icons-png.flaticon.com/128/2983/2983973.png", width=40)
        electricity_usage = st.number_input("Electricity Consumption (kWh)", min_value=0.0, value=4500.0)
        
        FACTOR_ELEC = 0.15 

# --- Calculation ---
scope_1 = (fuel_consumption * FACTOR_FUEL) + (gas_consumption * FACTOR_GAS)
scope_2 = (electricity_usage * FACTOR_ELEC)
total_emissions = scope_1 + scope_2

# --- Section 3: Visual Results ---
st.markdown("---")
st.subheader("📊 Audit Results & Visualization")

c1, c2 = st.columns([2, 1])

with c1:
    
    chart_df = pd.DataFrame({
        "Source": ["Fuel (Scope 1)", "Gas (Scope 1)", "Electricity (Scope 2)"],
        "Emissions (kg CO2e)": [fuel_consumption * FACTOR_FUEL, gas_consumption * FACTOR_GAS, scope_2]
    })
    st.bar_chart(chart_df, x="Source", y="Emissions (kg CO2e)", color="#2E7D32")

with c2:
     # (AI Logic Simulation)
    st.write("### Impact Visualization")
    
    if total_emissions > 5000:
        st.error("⚠️ High Impact")
        
        st.image("https://images.unsplash.com/photo-1611273426728-700d07129572?auto=format&fit=crop&w=600&q=80", caption="Current Environmental Stress")
    elif total_emissions > 2000:
        st.warning("⚠️ Moderate Impact")
        
        st.image("https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?auto=format&fit=crop&w=600&q=80", caption="Urban Impact")
    else:
        st.success("✅ Low Impact (Green)")
        
        st.image("https://images.unsplash.com/photo-1501854140884-074bf86ee91c?auto=format&fit=crop&w=600&q=80", caption="Sustainable Operation")

# --- Footer ---
st.markdown("---")
st.caption("Powered by Streamlit | Images by Unsplash")
