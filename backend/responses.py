import re

# ─────────────────────────────────────────────
# TOPIC CATALOGUE  (shown as quick-select chips)
# ─────────────────────────────────────────────
TOPICS = [
    {"id": "what_is_churn",        "label": "What is customer churn?"},
    {"id": "churn_signals",        "label": "Key churn signals in neobanks"},
    {"id": "churn_rate",           "label": "How to calculate churn rate"},
    {"id": "ltv_definition",       "label": "What is LTV?"},
    {"id": "ltv_formula",          "label": "LTV formula for neobanks"},
    {"id": "ltv_vs_cac",           "label": "LTV vs CAC ratio"},
    {"id": "ml_models",            "label": "ML models for churn prediction"},
    {"id": "features",             "label": "Top predictive features"},
    {"id": "data_sources",         "label": "Data sources needed"},
    {"id": "retention_tactics",    "label": "Retention tactics"},
    {"id": "segment_strategy",     "label": "Segmentation strategy"},
    {"id": "model_evaluation",     "label": "Evaluating model performance"},
    {"id": "real_time",            "label": "Real-time intervention systems"},
    {"id": "ltv_segments",         "label": "LTV-based customer segments"},
    {"id": "revenue_impact",       "label": "Revenue impact of churn"},
]

# ─────────────────────────────────────────────
# ANSWER BANK
# ─────────────────────────────────────────────
ANSWERS = {

"what_is_churn": {
    "title": "Customer Churn in Neobanks",
    "body": (
        "Customer churn refers to the rate at which customers stop using a neobank's products "
        "and services over a given period. Unlike traditional banks, neobanks face unique churn "
        "dynamics because switching costs are near zero — opening a new account takes minutes.\n\n"
        "**Types of churn in neobanks:**\n"
        "• **Hard churn** — Customer closes account entirely\n"
        "• **Soft churn** — Account remains open but activity drops to near zero (zombie accounts)\n"
        "• **Product churn** — Customer keeps the account but drops premium features or subscriptions\n"
        "• **Revenue churn** — Customer downgrades, reducing their monetary contribution\n\n"
        "Neobanks typically see soft churn as their biggest challenge: up to 40–60% of signups "
        "become inactive within 90 days. Identifying these early is critical for LTV optimization."
    ),
    "tags": ["churn", "basics", "neobank"]
},

"churn_signals": {
    "title": "Key Churn Signals in Neobanks",
    "body": (
        "Churn rarely happens without warning. Behavioural signals typically appear 30–90 days "
        "before a customer disengages. The most predictive signals are:\n\n"
        "**Transaction Behaviour**\n"
        "• Declining monthly transaction volume (>30% drop vs. 90-day baseline)\n"
        "• Shift from active debit usage to zero transactions\n"
        "• Salary / direct deposit stops appearing\n"
        "• Balance consistently near zero\n\n"
        "**Product Engagement**\n"
        "• App opens drop below once per week\n"
        "• Feature usage regression (stops using savings pots, investments, etc.)\n"
        "• Push notification opt-out or repeated dismissal\n\n"
        "**Support Signals**\n"
        "• Recent complaint or unresolved support ticket\n"
        "• Low CSAT / NPS response\n"
        "• Multiple failed login attempts (possible account abandonment)\n\n"
        "**External Signals**\n"
        "• Opening a competing account (detectable via open-banking data)\n"
        "• Reduced card spend at merchants where neobank was previously dominant"
    ),
    "tags": ["churn", "signals", "features"]
},

"churn_rate": {
    "title": "Calculating Churn Rate",
    "body": (
        "**Monthly Churn Rate (basic)**\n"
        "```\nChurn Rate = (Customers Lost in Period) / (Customers at Start of Period) × 100\n```\n\n"
        "**Example:** 500 churned out of 10,000 → 5% monthly churn\n\n"
        "**Annualised Churn:**\n"
        "```\nAnnual Churn ≈ 1 − (1 − Monthly Churn)^12\n```\n"
        "A 5% monthly churn = ~46% annual churn — that means nearly half your base every year.\n\n"
        "**Revenue Churn Rate** (more actionable for LTV):\n"
        "```\nRevenue Churn = (MRR Lost to Churn) / (MRR at Start) × 100\n```\n\n"
        "**Net Revenue Churn** accounts for expansion revenue:\n"
        "```\nNet Rev Churn = (MRR Lost − MRR Expanded) / MRR at Start × 100\n```\n\n"
        "A negative net revenue churn (expansion > churn) is the holy grail — it means your "
        "existing base grows revenue even as some customers leave.\n\n"
        "**Neobank benchmarks:**\n"
        "• World-class: <2% monthly churn\n"
        "• Healthy: 3–5% monthly churn\n"
        "• Concerning: >7% monthly churn"
    ),
    "tags": ["churn", "metrics", "formula"]
},

"ltv_definition": {
    "title": "Lifetime Value (LTV) for Neobanks",
    "body": (
        "**Lifetime Value (LTV)** — also called Customer Lifetime Value (CLV or CLTV) — is the "
        "total net revenue a neobank expects to earn from a customer throughout the entire "
        "relationship.\n\n"
        "For neobanks, LTV has several distinct revenue streams:\n\n"
        "| Revenue Source | Example |\n"
        "|---|---|\n"
        "| Interchange fees | 0.2–1.5% per card transaction |\n"
        "| Subscription / premium tier | £9.99/month for Metal card |\n"
        "| FX margin | 0.5–2% on currency conversion |\n"
        "| Lending margin | Interest on overdrafts / personal loans |\n"
        "| Savings spread | Difference between deposit rate and investment yield |\n"
        "| Referral programme | Commission from partner products |\n\n"
        "**Why LTV matters more than acquisition count:**\n"
        "Neobanks with high CAC (cost to acquire) must ensure customers stay long enough to "
        "become profitable. A customer acquired for £30 who churns in month 2 generates a net "
        "loss. The payback period analysis — when cumulative revenue exceeds CAC — is the core "
        "financial health metric."
    ),
    "tags": ["ltv", "basics", "revenue"]
},

"ltv_formula": {
    "title": "LTV Formula for Neobanks",
    "body": (
        "**Simple LTV:**\n"
        "```\nLTV = ARPU × Gross Margin % × (1 / Churn Rate)\n```\n\n"
        "Where:\n"
        "• **ARPU** = Average Revenue Per User per month\n"
        "• **Gross Margin %** = Net revenue after direct costs (e.g. card scheme fees)\n"
        "• **1 / Churn Rate** = Average customer lifespan in months\n\n"
        "**Example:**\n"
        "ARPU = £8/month, Gross Margin = 60%, Monthly Churn = 4%\n"
        "```\nLTV = £8 × 0.60 × (1/0.04) = £8 × 0.60 × 25 = £120\n```\n\n"
        "**Discounted LTV (more accurate):**\n"
        "```\nLTV = Σ (Revenue_t − Cost_t) / (1 + Discount Rate)^t\n```\n"
        "Use a 10–15% annual discount rate to account for cost of capital.\n\n"
        "**Predictive LTV (ML-based):**\n"
        "Uses survival models (BG/NBD, Pareto/NBD) or gradient boosting regressors trained on "
        "historical cohort data. These models predict individual-level expected revenue over a "
        "12–36 month horizon, enabling segment-level decision-making.\n\n"
        "**Neobank LTV benchmarks:**\n"
        "• Basic account: £80–£150 LTV\n"
        "• Premium/Metal tier: £400–£900 LTV\n"
        "• SME accounts: £1,200–£4,000 LTV"
    ),
    "tags": ["ltv", "formula", "metrics"]
},

"ltv_vs_cac": {
    "title": "LTV / CAC Ratio",
    "body": (
        "The **LTV:CAC ratio** is the single most important unit economics metric for a neobank.\n\n"
        "```\nLTV:CAC = Customer Lifetime Value / Customer Acquisition Cost\n```\n\n"
        "**Interpretation:**\n"
        "| Ratio | Signal |\n"
        "|---|---|\n"
        "| < 1:1 | You're destroying value — each customer costs more than they return |\n"
        "| 1:1 – 3:1 | Marginal — growth is expensive and fragile |\n"
        "| 3:1 | ✅ Industry benchmark for healthy SaaS / fintech |\n"
        "| > 5:1 | You may be under-investing in growth |\n\n"
        "**CAC components for neobanks:**\n"
        "• Paid social & performance marketing\n"
        "• Referral bonuses (e.g. £50 per referred customer)\n"
        "• App store spend\n"
        "• Onboarding & KYC costs (identity verification APIs)\n"
        "• Card issuance & delivery\n\n"
        "**Improving the ratio:**\n"
        "• **Reduce CAC:** invest in organic / referral channels\n"
        "• **Increase LTV:** upsell to premium, cross-sell lending products, reduce churn\n"
        "• **Segment-specific ratios:** high-LTV segments (SMEs, expats with FX needs) can "
        "justify 3× higher CAC"
    ),
    "tags": ["ltv", "cac", "unit economics"]
},

"ml_models": {
    "title": "ML Models for Churn Prediction",
    "body": (
        "Several model families are used in production churn prediction systems:\n\n"
        "**1. Gradient Boosted Trees (XGBoost / LightGBM)**\n"
        "Most widely deployed for tabular transaction data. Handles missing values natively, "
        "fast to train, highly interpretable via SHAP values. Often the best starting point.\n\n"
        "**2. Logistic Regression (baseline)**\n"
        "Use as a performance floor and for regulatory explainability requirements. Still "
        "competitive when features are well-engineered.\n\n"
        "**3. Survival Models (Cox Proportional Hazards, BG/NBD)**\n"
        "Best for time-to-churn prediction. The BG/NBD (Beta-Geometric / Negative Binomial "
        "Distribution) model is the gold standard for non-contractual settings — exactly where "
        "neobanks operate. Predicts expected transactions and purchase probability per customer.\n\n"
        "**4. Recurrent Neural Networks (LSTM)**\n"
        "Effective when transaction sequences carry temporal patterns. Higher training cost, "
        "harder to explain — use when tabular models plateau.\n\n"
        "**5. Graph Neural Networks**\n"
        "Cutting edge: model customer relationships and referral networks. Useful for detecting "
        "coordinated churn in social clusters.\n\n"
        "**Recommended pipeline:**\n"
        "Start with LightGBM + SHAP → add survival model for time-to-churn → ensemble if needed."
    ),
    "tags": ["ml", "models", "churn"]
},

"features": {
    "title": "Top Predictive Features",
    "body": (
        "Feature engineering is where most predictive power comes from. These features "
        "consistently rank highest in production neobank churn models:\n\n"
        "**Recency / Frequency / Monetary (RFM)**\n"
        "• Days since last transaction (recency)\n"
        "• Transaction count: last 7 / 30 / 90 days\n"
        "• Total spend: last 30 days vs. 90-day average (trend)\n\n"
        "**Account Health**\n"
        "• Average end-of-day balance (last 30 days)\n"
        "• Balance volatility (std dev of daily balance)\n"
        "• Direct deposit present: yes/no\n"
        "• Overdraft usage frequency\n\n"
        "**Product Depth**\n"
        "• Number of active products (savings, investments, loans)\n"
        "• Premium tier: yes/no\n"
        "• Card spend categories (diversity score)\n\n"
        "**Engagement**\n"
        "• App opens per week (7-day rolling average)\n"
        "• Days since last app open\n"
        "• Feature discovery score (# unique features used)\n\n"
        "**Lifecycle**\n"
        "• Account age in days\n"
        "• Months since last product added\n"
        "• Onboarding completion score\n\n"
        "**Customer Support**\n"
        "• Open support tickets: yes/no\n"
        "• CSAT score from last interaction\n"
        "• Complaint in last 30 days: yes/no"
    ),
    "tags": ["features", "ml", "engineering"]
},

"data_sources": {
    "title": "Data Sources Required",
    "body": (
        "A complete churn + LTV system draws from multiple data layers:\n\n"
        "**Core Transactional (Internal)**\n"
        "• Core banking ledger: all debits, credits, balances\n"
        "• Card network data: authorization, settlement, declines\n"
        "• Transfer logs: P2P, direct debits, standing orders\n\n"
        "**Product & Onboarding**\n"
        "• KYC / onboarding funnel events\n"
        "• Product subscription status (premium tier, insurance, etc.)\n"
        "• Referral source and acquisition channel\n\n"
        "**Digital Engagement**\n"
        "• Mobile app event stream (login, feature tap, screen time)\n"
        "• Push notification delivery and open rates\n"
        "• In-app survey responses (NPS, CSAT)\n\n"
        "**Support & CRM**\n"
        "• Zendesk / Intercom ticket history\n"
        "• Chat transcripts (NLP-tagged for sentiment)\n"
        "• Email campaign engagement (open / click rates)\n\n"
        "**External / Open Banking**\n"
        "• Open Banking API: accounts at other banks (with consent)\n"
        "• Credit bureau signals (where regulatory context allows)\n"
        "• Macroeconomic indicators (inflation, unemployment — cohort-level)\n\n"
        "**Infrastructure:**\n"
        "Event streams → Kafka → data lake (S3/BigQuery) → feature store (Feast/Tecton) → ML pipeline"
    ),
    "tags": ["data", "infrastructure", "sources"]
},

"retention_tactics": {
    "title": "Retention Tactics for Neobanks",
    "body": (
        "Once churn risk is identified, interventions must be timely and personalised:\n\n"
        "**Tier 1 — High-risk, high-LTV (act within 24 hours)**\n"
        "• Personal outreach from a dedicated relationship manager (or AI-assisted chat)\n"
        "• Tailored offer: fee waiver, cashback boost, rate upgrade\n"
        "• Root cause resolution: proactively fix any recent service failures\n\n"
        "**Tier 2 — High-risk, medium-LTV (act within 3–7 days)**\n"
        "• Targeted push notification with personalised value reminder\n"
        "• In-app re-engagement campaign (highlight unused features)\n"
        "• Limited-time offer (e.g. '3 months free premium')\n\n"
        "**Tier 3 — Early warning (30–60 day horizon)**\n"
        "• Educational content matched to usage gaps\n"
        "• Gamification nudges (streaks, spending insights)\n"
        "• Cross-sell introduction (if they don't have savings pot — show yield)\n\n"
        "**Structural tactics:**\n"
        "• **Direct deposit lock-in:** Incentivise salary routing — the single best predictor of retention\n"
        "• **Salary advance / BNPL:** Increases switching cost\n"
        "• **Joint accounts / family plans:** Creates network stickiness\n"
        "• **Loyalty programme:** Points or cashback tied to longevity\n\n"
        "**What doesn't work:** Generic discount blasts, win-back emails to hard-churned customers "
        "(cost > recovery), retention offers shown after churn decision is already made."
    ),
    "tags": ["retention", "tactics", "interventions"]
},

"segment_strategy": {
    "title": "Segmentation Strategy",
    "body": (
        "Effective churn and LTV management requires segmenting customers — not treating all "
        "users the same. A two-axis model (Churn Risk × LTV) creates four actionable quadrants:\n\n"
        "```\n"
        "         │  LOW LTV       │  HIGH LTV\n"
        "─────────┼────────────────┼──────────────────\n"
        "LOW RISK │ Nurture        │ Grow & protect\n"
        "─────────┼────────────────┼──────────────────\n"
        "HIGH RISK│ Low priority   │ ⚡ SAVE NOW\n"
        "```\n\n"
        "**Segment definitions:**\n\n"
        "🟢 **Champions** — High LTV, Low Risk\n"
        "Salary banked, premium product, high app engagement. Focus: upsell, referrals, advocacy.\n\n"
        "🟡 **Potential Value** — Low LTV, Low Risk\n"
        "Casual users. Focus: activation — get first salary deposit, introduce savings pot.\n\n"
        "🟠 **At Risk Stars** — High LTV, High Risk\n"
        "Previously active but declining. Focus: immediate personal intervention.\n\n"
        "🔴 **Low Priority** — Low LTV, High Risk\n"
        "Costly to retain and low return. Focus: low-cost automated re-engagement only.\n\n"
        "**Segmentation inputs:** RFM scores, product depth index, churn propensity score (0–1), "
        "predicted 12-month LTV from survival model."
    ),
    "tags": ["segmentation", "strategy", "ltv"]
},

"model_evaluation": {
    "title": "Evaluating Model Performance",
    "body": (
        "Churn models are classification problems with significant class imbalance "
        "(often 5–15% churn rate). Standard accuracy is misleading — use these metrics:\n\n"
        "**Primary Metrics:**\n"
        "• **AUC-ROC:** Overall discrimination power. Target: >0.80 for production deployment\n"
        "• **AUC-PR (Precision-Recall):** More relevant under class imbalance. Target: >0.60\n"
        "• **Lift at top decile:** How much better than random in the top 10% risk score? Target: 3–5×\n\n"
        "**Business Metrics (more important in practice):**\n"
        "• **Revenue saved per £1 of intervention cost** — the ROI of your retention programme\n"
        "• **Precision at operating threshold:** What % of flagged customers actually churned?\n"
        "• **Recall at operating threshold:** What % of churners did you catch?\n\n"
        "**Calibration:**\n"
        "A model that says 80% churn probability should be right ~80% of the time. Use "
        "Platt scaling or isotonic regression to calibrate raw model outputs.\n\n"
        "**Monitoring in production:**\n"
        "• PSI (Population Stability Index) — detect feature drift\n"
        "• Monthly AUC tracking on holdout set\n"
        "• A/B test intervention arms to measure true incremental lift\n"
        "• Retraining cadence: monthly for fast-moving features, quarterly for stable ones"
    ),
    "tags": ["ml", "evaluation", "metrics"]
},

"real_time": {
    "title": "Real-Time Intervention Systems",
    "body": (
        "Churn prediction is only valuable if it triggers timely action. A production-grade "
        "system has three layers:\n\n"
        "**Layer 1 — Scoring Pipeline**\n"
        "• Batch scoring: run nightly on all active customers, update risk scores in feature store\n"
        "• Near-real-time: trigger re-scoring on high-signal events (e.g. salary deposit stops, "
        "app deleted from phone)\n"
        "• Latency target: <5 minutes from event to updated score\n\n"
        "**Layer 2 — Decision Engine**\n"
        "• Rules + model hybrid: model produces score, rules engine applies business constraints\n"
        "  (e.g. 'don't contact customers who complained in last 7 days')\n"
        "• Offer eligibility: map customer segment to approved intervention catalogue\n"
        "• Budget constraints: cap daily intervention volume based on retention budget\n\n"
        "**Layer 3 — Orchestration**\n"
        "• Push to channel: Braze / Iterable for push, email, SMS\n"
        "• CRM alert: flag high-priority cases to human agents in Salesforce / Zendesk\n"
        "• Feedback loop: log intervention outcome → retrain model\n\n"
        "**Tech stack example:**\n"
        "Kafka → Flink (stream processing) → Redis (feature cache) → FastAPI (scoring service) "
        "→ Braze (engagement) → Snowflake (logging)"
    ),
    "tags": ["real-time", "system", "architecture"]
},

"ltv_segments": {
    "title": "LTV-Based Customer Segments",
    "body": (
        "Neobanks use predicted LTV to allocate resources and personalise the experience:\n\n"
        "**Predicted LTV tiers (12-month horizon, typical UK neobank):**\n\n"
        "| Tier | Predicted LTV | % of Base | % of Revenue |\n"
        "|---|---|---|---|\n"
        "| Platinum | >£500 | 5% | 35% |\n"
        "| Gold | £150–£500 | 20% | 40% |\n"
        "| Silver | £50–£150 | 35% | 20% |\n"
        "| Bronze | <£50 | 40% | 5% |\n\n"
        "This 80/20 concentration (25% of customers = 75% of revenue) means churn prevention "
        "ROI is heavily skewed toward Platinum and Gold tiers.\n\n"
        "**LTV drivers by tier:**\n"
        "• **Platinum:** SME owners, frequent international travellers, active investors\n"
        "• **Gold:** Salary banked, premium subscriber, regular saver\n"
        "• **Silver:** Occasional use, primary account elsewhere\n"
        "• **Bronze:** Signed up for bonus, minimal genuine usage\n\n"
        "**Actions by tier:**\n"
        "• Platinum: white-glove service, dedicated support queue\n"
        "• Gold: proactive cross-sell, loyalty rewards\n"
        "• Silver: activation campaigns, feature education\n"
        "• Bronze: low-cost nurture only, sunset if dormant >180 days"
    ),
    "tags": ["ltv", "segments", "strategy"]
},

"revenue_impact": {
    "title": "Revenue Impact of Churn",
    "body": (
        "Churn has a compounding negative effect on neobank revenue. Here's how to quantify it:\n\n"
        "**Direct Revenue Loss:**\n"
        "```\nAnnual Revenue Lost = Monthly Churners × Avg LTV × 12\n```\n\n"
        "**Example:** 1,000 monthly churners × £120 LTV = £1.44M annual revenue at risk\n\n"
        "**Replacement Cost:**\n"
        "To maintain customer count with 5% monthly churn, you must acquire 5% new customers "
        "every month — just to stand still. At £30 CAC:\n"
        "```\nReplacement Spend = 0.05 × 10,000 customers × £30 = £15,000/month = £180K/year\n```\n\n"
        "**Churn Reduction ROI:**\n"
        "Reducing churn from 5% to 4% monthly on a 10,000-customer base:\n"
        "• Saves 100 customers/month\n"
        "• At £120 LTV = £12,000 revenue protected monthly\n"
        "• Plus £3,000 CAC replacement savings\n"
        "• = £180K annual value from 1 percentage point improvement\n\n"
        "**Neobank industry insight:**\n"
        "Studies show improving churn by just 5% can increase profits by 25–95% (Bain & Co), "
        "as existing customers cost 5–7× less to serve than newly acquired ones.\n\n"
        "This is why investing £50K–£200K in a churn prediction system typically delivers "
        "10–50× ROI in the first 12 months for a neobank with >50K customers."
    ),
    "tags": ["revenue", "roi", "impact"]
},

}

# ─────────────────────────────────────────────
# KEYWORD → TOPIC MATCHING
# ─────────────────────────────────────────────
KEYWORD_MAP = {
    "what_is_churn":    ["what is churn", "define churn", "churn mean", "customer churn", "what does churn"],
    "churn_signals":    ["signal", "warning", "indicator", "detect churn", "early warning", "signs of churn", "churn sign"],
    "churn_rate":       ["calculate churn", "churn rate", "churn formula", "measure churn", "churn metric", "how to measure"],
    "ltv_definition":   ["what is ltv", "lifetime value", "clv", "cltv", "ltv mean", "define ltv", "what is customer lifetime"],
    "ltv_formula":      ["ltv formula", "calculate ltv", "compute ltv", "ltv calculation", "ltv model", "ltv equation"],
    "ltv_vs_cac":       ["ltv cac", "cac", "acquisition cost", "unit economics", "ltv to cac", "ratio"],
    "ml_models":        ["model", "algorithm", "xgboost", "lightgbm", "random forest", "machine learning", "predict churn", "ml", "neural"],
    "features":         ["feature", "variable", "input", "predictor", "column", "attribute", "data point"],
    "data_sources":     ["data source", "dataset", "data need", "what data", "data require", "kafka", "pipeline"],
    "retention_tactics":["retain", "retention", "keep customer", "prevent churn", "reduce churn", "tactic", "strategy to keep", "win back"],
    "segment_strategy": ["segment", "segmentation", "group customer", "cluster", "tier", "persona"],
    "model_evaluation": ["evaluate", "auc", "precision", "recall", "metric", "performance", "accuracy", "roc", "f1"],
    "real_time":        ["real time", "real-time", "live", "instant", "trigger", "event", "stream", "production", "deploy"],
    "ltv_segments":     ["ltv segment", "ltv tier", "platinum", "gold", "silver", "bronze", "ltv group", "value segment"],
    "revenue_impact":   ["revenue", "impact", "cost of churn", "roi", "profit", "financial", "money", "dollar", "pound"],
}

DEFAULT_RESPONSE = {
    "title": "Neobank Churn & LTV Assistant",
    "body": (
        "I'm your specialist guide for **customer churn and LTV prediction** in neobanks. "
        "Here are some things I can help you explore:\n\n"
        "• What churn and LTV mean in a neobank context\n"
        "• How to calculate churn rates and LTV\n"
        "• Which ML models to use and how to evaluate them\n"
        "• Key features and data sources for prediction\n"
        "• Retention tactics and real-time intervention systems\n"
        "• Revenue impact and ROI of reducing churn\n\n"
        "Try clicking one of the topic chips above, or type a question like "
        "*'How do I calculate LTV?'* or *'What signals predict churn?'*"
    ),
    "tags": []
}


def get_response(message: str) -> dict:
    """Match user message to best topic and return structured answer."""
    msg_lower = message.lower()

    # Direct topic ID match (from quick-chip clicks)
    if msg_lower.strip() in ANSWERS:
        answer = ANSWERS[msg_lower.strip()]
        return {
            "topic_id": msg_lower.strip(),
            "title": answer["title"],
            "body": answer["body"],
            "tags": answer["tags"],
            "matched": True
        }

    # Keyword matching
    best_topic = None
    best_score = 0

    for topic_id, keywords in KEYWORD_MAP.items():
        score = sum(1 for kw in keywords if kw in msg_lower)
        if score > best_score:
            best_score = score
            best_topic = topic_id

    if best_topic and best_score > 0:
        answer = ANSWERS[best_topic]
        return {
            "topic_id": best_topic,
            "title": answer["title"],
            "body": answer["body"],
            "tags": answer["tags"],
            "matched": True
        }

    # Fallback
    return {
        "topic_id": None,
        "title": DEFAULT_RESPONSE["title"],
        "body": DEFAULT_RESPONSE["body"],
        "tags": DEFAULT_RESPONSE["tags"],
        "matched": False
    }
