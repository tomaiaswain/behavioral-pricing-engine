# =====================================================================
# PROJECT 6: BEHAVIORAL PRICE ELASTICITY ENGINE
# =====================================================================

# PHASE 1: MARKET DATA & SCENARIO SETUP
# Base metrics for a standard B2B SaaS product
base_price = 500.00
base_demand = 1000

# We tested a minor price increase last quarter to calculate baseline elasticity
tested_price = 550.00
tested_demand = 950

# Behavioral Shock Scenarios (Multiplier affecting consumer price sensitivity)
# A value > 1.0 means consumers are MORE sensitive to price (Panic/Recession)
# A value < 1.0 means consumers are LESS sensitive (Hype/Competitor Bankrupt)
market_shocks = {
    "Normal Market Conditions": 1.0,
    "Viral Marketing Hype": 0.5,
    "Macroeconomic Recession": 2.5,
    "Major Competitor Bankruptcy": 0.2
}

def calculate_elasticity(p1, d1, p2, d2):
    # Midpoint method for Price Elasticity of Demand (PED)
    pct_change_demand = (d2 - d1) / ((d2 + d1) / 2)
    pct_change_price = (p2 - p1) / ((p2 + p1) / 2)
    return abs(pct_change_demand / pct_change_price)

def run_behavioral_simulation(shock_name, shock_multiplier, target_price_increase):
    print(f"⚙️  [ENGINE] Running Behavioral Shock Simulation: {shock_name}...")
    
    # 1. Calculate historical baseline elasticity
    baseline_ped = calculate_elasticity(base_price, base_demand, tested_price, tested_demand)
    
    # 2. Apply behavioral psychology multiplier
    shocked_ped = baseline_ped * shock_multiplier
    
    # 3. Simulate new demand based on a proposed target price increase
    proposed_price = base_price * (1 + target_price_increase)
    
    # Rearranging elasticity formula to solve for projected demand drop
    # % change demand = Elasticity * % change price
    projected_demand_drop_pct = shocked_ped * target_price_increase
    projected_demand = int(base_demand * (1 - projected_demand_drop_pct))
    
    # Prevent negative demand
    if projected_demand < 0: projected_demand = 0
        
    # 4. Calculate Revenue Impact
    baseline_revenue = base_price * base_demand
    projected_revenue = proposed_price * projected_demand
    revenue_delta = projected_revenue - baseline_revenue
    
    return baseline_ped, shocked_ped, proposed_price, projected_demand, projected_revenue, revenue_delta

# PHASE 3: EXECUTIVE DASHBOARD OUTPUT
def generate_elasticity_report(shock_name, results):
    base_ped, shocked_ped, price, demand, rev, delta = results
    
    print("\n=========================================================")
    print("      BEHAVIORAL ECONOMICS: PRICE SENSITIVITY MODEL      ")
    print("=========================================================")
    print(f"📊 SCENARIO: {shock_name}")
    print("---------------------------------------------------------")
    print(f"🧠 Baseline Elasticity (Historical): {base_ped:.2f}")
    print(f"💥 Adjusted Elasticity (Shocked):    {shocked_ped:.2f}")
    print("---------------------------------------------------------")
    print(f"🎯 PROPOSED STRATEGY: +15% PRICE INCREASE")
    print(f"   -> Target Price:      ${price:,.2f}")
    print(f"   -> Projected Demand:  {demand:,} active licenses")
    print(f"   -> Projected Revenue: ${rev:,.2f}")
    print("---------------------------------------------------------")
    
    if delta > 0:
        print(f"✅ VERDICT: EXECUTABLE. Projected Revenue Gain: +${delta:,.2f}")
    else:
        print(f"⚠️  VERDICT: HIGH RISK. Projected Revenue Loss: ${delta:,.2f}")
    print("=========================================================\n")

# Execute the pipeline: Proposing a 15% price increase across all scenarios
target_increase = 0.15

for scenario, multiplier in market_shocks.items():
    sim_results = run_behavioral_simulation(scenario, multiplier, target_increase)
    generate_elasticity_report(scenario, sim_results)
