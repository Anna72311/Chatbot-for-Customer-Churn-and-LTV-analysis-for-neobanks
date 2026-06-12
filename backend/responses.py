import re

# ─────────────────────────────────────────────────────────────────
# TOPIC LABELS  (per language)
# ─────────────────────────────────────────────────────────────────
TOPIC_LABELS = {
    "en": [
        {"id": "what_is_churn",      "label": "What is customer churn?"},
        {"id": "churn_signals",      "label": "Key churn signals in neobanks"},
        {"id": "churn_rate",         "label": "How to calculate churn rate"},
        {"id": "ltv_definition",     "label": "What is LTV?"},
        {"id": "ltv_formula",        "label": "LTV formula for neobanks"},
        {"id": "ltv_vs_cac",         "label": "LTV vs CAC ratio"},
        {"id": "ml_models",          "label": "ML models for churn prediction"},
        {"id": "features",           "label": "Top predictive features"},
        {"id": "data_sources",       "label": "Data sources needed"},
        {"id": "retention_tactics",  "label": "Retention tactics"},
        {"id": "segment_strategy",   "label": "Segmentation strategy"},
        {"id": "model_evaluation",   "label": "Evaluating model performance"},
        {"id": "real_time",          "label": "Real-time intervention systems"},
        {"id": "ltv_segments",       "label": "LTV-based customer segments"},
        {"id": "revenue_impact",     "label": "Revenue impact of churn"},
    ],
    "hi": [
        {"id": "what_is_churn",      "label": "ग्राहक चर्न क्या है?"},
        {"id": "churn_signals",      "label": "नियोबैंक में चर्न के संकेत"},
        {"id": "churn_rate",         "label": "चर्न दर की गणना कैसे करें"},
        {"id": "ltv_definition",     "label": "LTV क्या है?"},
        {"id": "ltv_formula",        "label": "नियोबैंक के लिए LTV फ़ॉर्मूला"},
        {"id": "ltv_vs_cac",         "label": "LTV बनाम CAC अनुपात"},
        {"id": "ml_models",          "label": "चर्न पूर्वानुमान के लिए ML मॉडल"},
        {"id": "features",           "label": "शीर्ष पूर्वानुमान विशेषताएँ"},
        {"id": "data_sources",       "label": "आवश्यक डेटा स्रोत"},
        {"id": "retention_tactics",  "label": "प्रतिधारण रणनीतियाँ"},
        {"id": "segment_strategy",   "label": "सेगमेंटेशन रणनीति"},
        {"id": "model_evaluation",   "label": "मॉडल प्रदर्शन मूल्यांकन"},
        {"id": "real_time",          "label": "रियल-टाइम हस्तक्षेप प्रणाली"},
        {"id": "ltv_segments",       "label": "LTV-आधारित ग्राहक खंड"},
        {"id": "revenue_impact",     "label": "चर्न का राजस्व पर प्रभाव"},
    ],
    "fr": [
        {"id": "what_is_churn",      "label": "Qu'est-ce que l'attrition client ?"},
        {"id": "churn_signals",      "label": "Signaux d'attrition dans les neobanques"},
        {"id": "churn_rate",         "label": "Comment calculer le taux d'attrition"},
        {"id": "ltv_definition",     "label": "Qu'est-ce que la LTV ?"},
        {"id": "ltv_formula",        "label": "Formule LTV pour les neobanques"},
        {"id": "ltv_vs_cac",         "label": "Ratio LTV / CAC"},
        {"id": "ml_models",          "label": "Modèles ML pour prédire l'attrition"},
        {"id": "features",           "label": "Principales variables prédictives"},
        {"id": "data_sources",       "label": "Sources de données nécessaires"},
        {"id": "retention_tactics",  "label": "Tactiques de rétention"},
        {"id": "segment_strategy",   "label": "Stratégie de segmentation"},
        {"id": "model_evaluation",   "label": "Évaluation des performances du modèle"},
        {"id": "real_time",          "label": "Systèmes d'intervention en temps réel"},
        {"id": "ltv_segments",       "label": "Segments clients basés sur la LTV"},
        {"id": "revenue_impact",     "label": "Impact de l'attrition sur les revenus"},
    ],
}

# backward compat — default English
TOPICS = TOPIC_LABELS["en"]

# ─────────────────────────────────────────────────────────────────
# ANSWERS  (English)
# ─────────────────────────────────────────────────────────────────
ANSWERS_EN = {

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
        "• Multiple failed login attempts\n\n"
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
        "A 5% monthly churn = ~46% annual churn.\n\n"
        "**Revenue Churn Rate:**\n"
        "```\nRevenue Churn = (MRR Lost to Churn) / (MRR at Start) × 100\n```\n\n"
        "**Net Revenue Churn:**\n"
        "```\nNet Rev Churn = (MRR Lost − MRR Expanded) / MRR at Start × 100\n```\n\n"
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
        "**Lifetime Value (LTV)** is the total net revenue a neobank expects to earn from a "
        "customer throughout the entire relationship.\n\n"
        "For neobanks, LTV has several distinct revenue streams:\n\n"
        "| Revenue Source | Example |\n"
        "|---|---|\n"
        "| Interchange fees | 0.2–1.5% per card transaction |\n"
        "| Subscription / premium tier | £9.99/month for Metal card |\n"
        "| FX margin | 0.5–2% on currency conversion |\n"
        "| Lending margin | Interest on overdrafts / personal loans |\n"
        "| Savings spread | Difference between deposit rate and investment yield |\n"
        "| Referral programme | Commission from partner products |\n\n"
        "**Why LTV matters:** A customer acquired for £30 who churns in month 2 generates a net "
        "loss. The payback period — when cumulative revenue exceeds CAC — is the core "
        "financial health metric."
    ),
    "tags": ["ltv", "basics", "revenue"]
},
"ltv_formula": {
    "title": "LTV Formula for Neobanks",
    "body": (
        "**Simple LTV:**\n"
        "```\nLTV = ARPU × Gross Margin % × (1 / Churn Rate)\n```\n\n"
        "**Example:** ARPU = £8/month, Gross Margin = 60%, Monthly Churn = 4%\n"
        "```\nLTV = £8 × 0.60 × (1/0.04) = £120\n```\n\n"
        "**Discounted LTV:**\n"
        "```\nLTV = Σ (Revenue_t − Cost_t) / (1 + Discount Rate)^t\n```\n"
        "Use a 10–15% annual discount rate.\n\n"
        "**Predictive LTV (ML-based):**\n"
        "Uses survival models (BG/NBD, Pareto/NBD) or gradient boosting regressors trained on "
        "historical cohort data.\n\n"
        "**Neobank LTV benchmarks:**\n"
        "• Basic account: £80–£150\n"
        "• Premium/Metal tier: £400–£900\n"
        "• SME accounts: £1,200–£4,000"
    ),
    "tags": ["ltv", "formula", "metrics"]
},
"ltv_vs_cac": {
    "title": "LTV / CAC Ratio",
    "body": (
        "```\nLTV:CAC = Customer Lifetime Value / Customer Acquisition Cost\n```\n\n"
        "| Ratio | Signal |\n"
        "|---|---|\n"
        "| < 1:1 | Destroying value |\n"
        "| 1:1 – 3:1 | Marginal — fragile growth |\n"
        "| 3:1 | ✅ Industry benchmark |\n"
        "| > 5:1 | Under-investing in growth |\n\n"
        "**CAC components:** Paid social, referral bonuses, app store spend, KYC costs, card issuance.\n\n"
        "**Improving the ratio:**\n"
        "• Reduce CAC: invest in organic / referral channels\n"
        "• Increase LTV: upsell to premium, cross-sell lending, reduce churn\n"
        "• Segment-specific ratios: high-LTV segments justify 3× higher CAC"
    ),
    "tags": ["ltv", "cac", "unit economics"]
},
"ml_models": {
    "title": "ML Models for Churn Prediction",
    "body": (
        "**1. Gradient Boosted Trees (XGBoost / LightGBM)**\n"
        "Most widely deployed. Handles missing values natively, highly interpretable via SHAP.\n\n"
        "**2. Logistic Regression (baseline)**\n"
        "Use for regulatory explainability. Still competitive with good feature engineering.\n\n"
        "**3. Survival Models (Cox / BG/NBD)**\n"
        "Best for time-to-churn. BG/NBD is gold standard for non-contractual neobank settings.\n\n"
        "**4. Recurrent Neural Networks (LSTM)**\n"
        "Effective for temporal transaction sequences. Higher cost, harder to explain.\n\n"
        "**5. Graph Neural Networks**\n"
        "Cutting edge: models customer referral networks to detect coordinated churn.\n\n"
        "**Recommended pipeline:**\n"
        "Start with LightGBM + SHAP → add survival model for time-to-churn → ensemble if needed."
    ),
    "tags": ["ml", "models", "churn"]
},
"features": {
    "title": "Top Predictive Features",
    "body": (
        "**Recency / Frequency / Monetary (RFM)**\n"
        "• Days since last transaction\n"
        "• Transaction count: last 7 / 30 / 90 days\n"
        "• Total spend trend vs. 90-day average\n\n"
        "**Account Health**\n"
        "• Average end-of-day balance (last 30 days)\n"
        "• Balance volatility (std dev of daily balance)\n"
        "• Direct deposit present: yes/no\n"
        "• Overdraft usage frequency\n\n"
        "**Product Depth**\n"
        "• Number of active products\n"
        "• Premium tier: yes/no\n"
        "• Card spend category diversity score\n\n"
        "**Engagement**\n"
        "• App opens per week (7-day rolling average)\n"
        "• Days since last app open\n"
        "• Feature discovery score\n\n"
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
        "**Core Transactional (Internal)**\n"
        "• Core banking ledger: all debits, credits, balances\n"
        "• Card network data: authorization, settlement, declines\n"
        "• Transfer logs: P2P, direct debits, standing orders\n\n"
        "**Product & Onboarding**\n"
        "• KYC / onboarding funnel events\n"
        "• Product subscription status\n"
        "• Referral source and acquisition channel\n\n"
        "**Digital Engagement**\n"
        "• Mobile app event stream (login, feature tap, screen time)\n"
        "• Push notification open rates\n"
        "• In-app survey responses (NPS, CSAT)\n\n"
        "**Support & CRM**\n"
        "• Ticket history and chat transcripts (NLP-tagged)\n"
        "• Email campaign engagement\n\n"
        "**Infrastructure:**\n"
        "Event streams → Kafka → data lake (S3/BigQuery) → feature store (Feast/Tecton) → ML pipeline"
    ),
    "tags": ["data", "infrastructure", "sources"]
},
"retention_tactics": {
    "title": "Retention Tactics for Neobanks",
    "body": (
        "**Tier 1 — High-risk, high-LTV (act within 24 hours)**\n"
        "• Personal outreach from relationship manager\n"
        "• Tailored offer: fee waiver, cashback boost, rate upgrade\n"
        "• Proactively fix any recent service failures\n\n"
        "**Tier 2 — High-risk, medium-LTV (act within 3–7 days)**\n"
        "• Targeted push notification with personalised value reminder\n"
        "• In-app re-engagement campaign\n"
        "• Limited-time offer (e.g. '3 months free premium')\n\n"
        "**Tier 3 — Early warning (30–60 day horizon)**\n"
        "• Educational content matched to usage gaps\n"
        "• Gamification nudges (streaks, spending insights)\n"
        "• Cross-sell introduction\n\n"
        "**Structural tactics:**\n"
        "• Direct deposit lock-in — the single best predictor of retention\n"
        "• Salary advance / BNPL increases switching cost\n"
        "• Joint accounts / family plans create network stickiness\n"
        "• Loyalty programme tied to longevity"
    ),
    "tags": ["retention", "tactics", "interventions"]
},
"segment_strategy": {
    "title": "Segmentation Strategy",
    "body": (
        "A two-axis model (Churn Risk × LTV) creates four actionable quadrants:\n\n"
        "```\n"
        "         │  LOW LTV       │  HIGH LTV\n"
        "─────────┼────────────────┼──────────────────\n"
        "LOW RISK │ Nurture        │ Grow & protect\n"
        "─────────┼────────────────┼──────────────────\n"
        "HIGH RISK│ Low priority   │ ⚡ SAVE NOW\n"
        "```\n\n"
        "🟢 **Champions** — High LTV, Low Risk: upsell, referrals, advocacy.\n"
        "🟡 **Potential Value** — Low LTV, Low Risk: activation campaigns.\n"
        "🟠 **At Risk Stars** — High LTV, High Risk: immediate personal intervention.\n"
        "🔴 **Low Priority** — Low LTV, High Risk: low-cost automated re-engagement only."
    ),
    "tags": ["segmentation", "strategy", "ltv"]
},
"model_evaluation": {
    "title": "Evaluating Model Performance",
    "body": (
        "**Primary Metrics (class-imbalance aware):**\n"
        "• **AUC-ROC:** Overall discrimination. Target: >0.80\n"
        "• **AUC-PR (Precision-Recall):** Better under imbalance. Target: >0.60\n"
        "• **Lift at top decile:** Target: 3–5× over random\n\n"
        "**Business Metrics:**\n"
        "• Revenue saved per £1 of intervention cost\n"
        "• Precision at operating threshold\n"
        "• Recall at operating threshold\n\n"
        "**Calibration:**\n"
        "Use Platt scaling or isotonic regression. A score of 80% should be right ~80% of the time.\n\n"
        "**Production monitoring:**\n"
        "• PSI (Population Stability Index) — detect feature drift\n"
        "• Monthly AUC on holdout set\n"
        "• A/B test intervention arms to measure true incremental lift\n"
        "• Retrain monthly (fast features) / quarterly (stable features)"
    ),
    "tags": ["ml", "evaluation", "metrics"]
},
"real_time": {
    "title": "Real-Time Intervention Systems",
    "body": (
        "**Layer 1 — Scoring Pipeline**\n"
        "• Batch scoring: nightly on all active customers\n"
        "• Near-real-time: re-score on high-signal events (salary deposit stops, app deleted)\n"
        "• Latency target: <5 minutes from event to updated score\n\n"
        "**Layer 2 — Decision Engine**\n"
        "• Rules + model hybrid: model score + business constraints\n"
        "• Offer eligibility: map segment to approved intervention catalogue\n"
        "• Budget constraints: cap daily intervention volume\n\n"
        "**Layer 3 — Orchestration**\n"
        "• Push to channel: Braze / Iterable for push, email, SMS\n"
        "• CRM alert for human agents (Salesforce / Zendesk)\n"
        "• Feedback loop: log outcome → retrain model\n\n"
        "**Tech stack:**\n"
        "Kafka → Flink → Redis → FastAPI → Braze → Snowflake"
    ),
    "tags": ["real-time", "system", "architecture"]
},
"ltv_segments": {
    "title": "LTV-Based Customer Segments",
    "body": (
        "| Tier | Predicted LTV | % of Base | % of Revenue |\n"
        "|---|---|---|---|\n"
        "| Platinum | >£500 | 5% | 35% |\n"
        "| Gold | £150–£500 | 20% | 40% |\n"
        "| Silver | £50–£150 | 35% | 20% |\n"
        "| Bronze | <£50 | 40% | 5% |\n\n"
        "This 80/20 concentration means churn prevention ROI is heavily skewed toward Platinum and Gold.\n\n"
        "**Actions by tier:**\n"
        "• Platinum: white-glove service, dedicated support queue\n"
        "• Gold: proactive cross-sell, loyalty rewards\n"
        "• Silver: activation campaigns, feature education\n"
        "• Bronze: low-cost nurture, sunset if dormant >180 days"
    ),
    "tags": ["ltv", "segments", "strategy"]
},
"revenue_impact": {
    "title": "Revenue Impact of Churn",
    "body": (
        "**Direct Revenue Loss:**\n"
        "```\nAnnual Revenue Lost = Monthly Churners × Avg LTV × 12\n```\n"
        "Example: 1,000 churners × £120 LTV = £1.44M/year at risk\n\n"
        "**Replacement Cost:**\n"
        "```\nReplacement Spend = Churn Rate × Customers × CAC × 12\n```\n"
        "5% monthly churn on 10K customers at £30 CAC = £180K/year just to stand still.\n\n"
        "**Churn Reduction ROI:**\n"
        "Reducing churn from 5% to 4% on 10,000 customers:\n"
        "• Saves 100 customers/month × £120 LTV = £12,000/month protected\n"
        "• Plus £3,000 CAC savings = **£180K annual value** from 1 percentage point\n\n"
        "Improving churn by 5% can increase profits by 25–95% (Bain & Co). "
        "Investing £50K–£200K in a churn system typically delivers 10–50× ROI in year one."
    ),
    "tags": ["revenue", "roi", "impact"]
},
}

# ─────────────────────────────────────────────────────────────────
# ANSWERS  (Hindi)
# ─────────────────────────────────────────────────────────────────
ANSWERS_HI = {

"what_is_churn": {
    "title": "नियोबैंक में ग्राहक चर्न",
    "body": (
        "ग्राहक चर्न वह दर है जिस पर ग्राहक एक निश्चित अवधि में नियोबैंक की सेवाओं का उपयोग बंद कर देते हैं। "
        "पारंपरिक बैंकों के विपरीत, नियोबैंक में स्विचिंग कॉस्ट लगभग शून्य है — नया खाता खोलने में सिर्फ मिनट लगते हैं।\n\n"
        "**नियोबैंक में चर्न के प्रकार:**\n"
        "• **हार्ड चर्न** — ग्राहक खाता पूरी तरह बंद कर देता है\n"
        "• **सॉफ्ट चर्न** — खाता खुला रहता है लेकिन गतिविधि लगभग शून्य (ज़ॉम्बी खाते)\n"
        "• **प्रोडक्ट चर्न** — खाता रखता है पर प्रीमियम सुविधाएँ छोड़ देता है\n"
        "• **रेवेन्यू चर्न** — ग्राहक डाउनग्रेड करता है, योगदान कम होता है\n\n"
        "नियोबैंक के लिए सॉफ्ट चर्न सबसे बड़ी चुनौती है: साइनअप में से 40–60% ग्राहक 90 दिनों में निष्क्रिय हो जाते हैं। "
        "इन्हें जल्दी पहचानना LTV अनुकूलन के लिए महत्वपूर्ण है।"
    ),
    "tags": ["churn", "basics", "neobank"]
},
"churn_signals": {
    "title": "नियोबैंक में चर्न के प्रमुख संकेत",
    "body": (
        "चर्न शायद ही बिना चेतावनी के होता है। व्यवहार संबंधी संकेत आमतौर पर ग्राहक के जाने से 30–90 दिन पहले दिखाई देते हैं:\n\n"
        "**लेनदेन व्यवहार**\n"
        "• मासिक लेनदेन में गिरावट (90-दिन के आधार से >30% कम)\n"
        "• डेबिट उपयोग से शून्य लेनदेन की ओर बदलाव\n"
        "• वेतन / डायरेक्ट डिपॉज़िट का रुकना\n"
        "• बैलेंस लगातार शून्य के करीब\n\n"
        "**प्रोडक्ट एंगेजमेंट**\n"
        "• ऐप ओपन सप्ताह में एक बार से कम\n"
        "• फ़ीचर उपयोग में कमी (सेविंग्स पॉट, निवेश बंद करना)\n"
        "• पुश नोटिफिकेशन ऑप्ट-आउट\n\n"
        "**सपोर्ट संकेत**\n"
        "• हालिया शिकायत या अनसुलझी टिकट\n"
        "• कम CSAT / NPS स्कोर\n\n"
        "**बाहरी संकेत**\n"
        "• प्रतिस्पर्धी बैंक में खाता खोलना (ओपन बैंकिंग डेटा से पता चलता है)\n"
        "• उन मर्चेंट पर कार्ड खर्च में कमी जहाँ पहले नियोबैंक का उपयोग था"
    ),
    "tags": ["churn", "signals", "features"]
},
"churn_rate": {
    "title": "चर्न दर की गणना",
    "body": (
        "**मासिक चर्न दर (बुनियादी)**\n"
        "```\nचर्न दर = (अवधि में खोए ग्राहक) / (अवधि की शुरुआत में ग्राहक) × 100\n```\n\n"
        "**उदाहरण:** 10,000 में से 500 गए → 5% मासिक चर्न\n\n"
        "**वार्षिक चर्न:**\n"
        "```\nवार्षिक चर्न ≈ 1 − (1 − मासिक चर्न)^12\n```\n"
        "5% मासिक = ~46% वार्षिक चर्न\n\n"
        "**रेवेन्यू चर्न दर:**\n"
        "```\nरेवेन्यू चर्न = (MRR हानि) / (शुरुआती MRR) × 100\n```\n\n"
        "**नियोबैंक बेंचमार्क:**\n"
        "• विश्व स्तरीय: <2% मासिक चर्न\n"
        "• स्वस्थ: 3–5% मासिक चर्न\n"
        "• चिंताजनक: >7% मासिक चर्न"
    ),
    "tags": ["churn", "metrics", "formula"]
},
"ltv_definition": {
    "title": "नियोबैंक के लिए लाइफटाइम वैल्यू (LTV)",
    "body": (
        "**लाइफटाइम वैल्यू (LTV)** वह कुल शुद्ध राजस्व है जो एक नियोबैंक किसी ग्राहक से पूरे संबंध के दौरान अर्जित करने की उम्मीद रखता है।\n\n"
        "नियोबैंक के LTV के प्रमुख राजस्व स्रोत:\n\n"
        "| राजस्व स्रोत | उदाहरण |\n"
        "|---|---|\n"
        "| इंटरचेंज फ़ीस | प्रति कार्ड लेनदेन 0.2–1.5% |\n"
        "| सब्सक्रिप्शन / प्रीमियम | ₹999/माह मेटल कार्ड |\n"
        "| FX मार्जिन | करेंसी कन्वर्जन पर 0.5–2% |\n"
        "| लेंडिंग मार्जिन | ओवरड्राफ्ट / पर्सनल लोन ब्याज |\n"
        "| सेविंग्स स्प्रेड | डिपॉज़िट दर और निवेश यील्ड का अंतर |\n\n"
        "**LTV क्यों मायने रखती है:** ₹1,000 में अर्जित ग्राहक यदि महीने 2 में चला जाए तो शुद्ध हानि होती है। "
        "पेबैक पीरियड — जब संचयी राजस्व CAC से अधिक हो — मुख्य वित्तीय स्वास्थ्य मेट्रिक है।"
    ),
    "tags": ["ltv", "basics", "revenue"]
},
"ltv_formula": {
    "title": "नियोबैंक के लिए LTV फ़ॉर्मूला",
    "body": (
        "**सरल LTV:**\n"
        "```\nLTV = ARPU × सकल मार्जिन % × (1 / चर्न दर)\n```\n\n"
        "**उदाहरण:** ARPU = ₹800/माह, मार्जिन = 60%, मासिक चर्न = 4%\n"
        "```\nLTV = ₹800 × 0.60 × 25 = ₹12,000\n```\n\n"
        "**डिस्काउंटेड LTV:**\n"
        "```\nLTV = Σ (Revenue_t − Cost_t) / (1 + Discount Rate)^t\n```\n"
        "10–15% वार्षिक डिस्काउंट दर का उपयोग करें।\n\n"
        "**प्रेडिक्टिव LTV (ML-आधारित):**\n"
        "ऐतिहासिक कोहॉर्ट डेटा पर BG/NBD सर्वाइवल मॉडल या ग्रेडिएंट बूस्टिंग रिग्रेसर का उपयोग।\n\n"
        "**नियोबैंक LTV बेंचमार्क:**\n"
        "• बेसिक खाता: ₹8,000–₹15,000\n"
        "• प्रीमियम/मेटल: ₹40,000–₹90,000\n"
        "• SME खाते: ₹1,20,000–₹4,00,000"
    ),
    "tags": ["ltv", "formula", "metrics"]
},
"ltv_vs_cac": {
    "title": "LTV / CAC अनुपात",
    "body": (
        "```\nLTV:CAC = ग्राहक लाइफटाइम वैल्यू / ग्राहक अधिग्रहण लागत\n```\n\n"
        "| अनुपात | संकेत |\n"
        "|---|---|\n"
        "| < 1:1 | मूल्य नष्ट हो रहा है |\n"
        "| 1:1 – 3:1 | सीमांत — विकास नाजुक |\n"
        "| 3:1 | ✅ उद्योग बेंचमार्क |\n"
        "| > 5:1 | विकास में कम निवेश |\n\n"
        "**CAC घटकों में शामिल:** पेड सोशल, रेफरल बोनस, ऐप स्टोर खर्च, KYC लागत, कार्ड जारी करना।\n\n"
        "**अनुपात सुधारने के तरीके:**\n"
        "• CAC घटाएं: ऑर्गेनिक / रेफरल चैनलों में निवेश करें\n"
        "• LTV बढ़ाएं: प्रीमियम अपसेल, लेंडिंग क्रॉस-सेल, चर्न कम करें\n"
        "• उच्च-LTV सेगमेंट 3× अधिक CAC को उचित ठहरा सकते हैं"
    ),
    "tags": ["ltv", "cac", "unit economics"]
},
"ml_models": {
    "title": "चर्न पूर्वानुमान के लिए ML मॉडल",
    "body": (
        "**1. ग्रेडिएंट बूस्टेड ट्री (XGBoost / LightGBM)**\n"
        "सबसे अधिक उपयोग किया जाने वाला। SHAP के माध्यम से व्याख्यायोग्य, मिसिंग वैल्यू को नेटिवली हैंडल करता है।\n\n"
        "**2. लॉजिस्टिक रिग्रेशन (बेसलाइन)**\n"
        "नियामक व्याख्यायोग्यता के लिए। अच्छे फ़ीचर इंजीनियरिंग के साथ प्रतिस्पर्धी।\n\n"
        "**3. सर्वाइवल मॉडल (Cox / BG/NBD)**\n"
        "चर्न-टू-टाइम के लिए सर्वश्रेष्ठ। BG/NBD नॉन-कॉन्ट्रैक्चुअल नियोबैंक सेटिंग के लिए गोल्ड स्टैंडर्ड।\n\n"
        "**4. रिकरेंट न्यूरल नेटवर्क (LSTM)**\n"
        "टेम्पोरल ट्रांजेक्शन सीक्वेंस के लिए प्रभावी। समझाना कठिन।\n\n"
        "**5. ग्राफ न्यूरल नेटवर्क**\n"
        "रेफरल नेटवर्क में समन्वित चर्न का पता लगाने के लिए।\n\n"
        "**अनुशंसित पाइपलाइन:**\n"
        "LightGBM + SHAP → सर्वाइवल मॉडल → आवश्यकता अनुसार एन्सेम्बल"
    ),
    "tags": ["ml", "models", "churn"]
},
"features": {
    "title": "शीर्ष पूर्वानुमान विशेषताएँ",
    "body": (
        "**रिसेंसी / फ्रीक्वेंसी / मॉनेटरी (RFM)**\n"
        "• अंतिम लेनदेन के बाद के दिन\n"
        "• लेनदेन की संख्या: पिछले 7 / 30 / 90 दिन\n"
        "• 90-दिन के औसत की तुलना में खर्च प्रवृत्ति\n\n"
        "**खाता स्वास्थ्य**\n"
        "• औसत दिन-अंत बैलेंस (पिछले 30 दिन)\n"
        "• बैलेंस अस्थिरता\n"
        "• डायरेक्ट डिपॉज़िट: हाँ/नहीं\n"
        "• ओवरड्राफ्ट उपयोग की आवृत्ति\n\n"
        "**प्रोडक्ट गहराई**\n"
        "• सक्रिय उत्पादों की संख्या\n"
        "• प्रीमियम टियर: हाँ/नहीं\n"
        "• कार्ड खर्च श्रेणी विविधता स्कोर\n\n"
        "**एंगेजमेंट**\n"
        "• सप्ताह में ऐप ओपन (7-दिन रोलिंग औसत)\n"
        "• अंतिम ऐप ओपन के बाद के दिन\n"
        "• फ़ीचर डिस्कवरी स्कोर\n\n"
        "**ग्राहक सहायता**\n"
        "• खुली टिकट: हाँ/नहीं\n"
        "• अंतिम इंटरैक्शन का CSAT स्कोर\n"
        "• पिछले 30 दिनों में शिकायत: हाँ/नहीं"
    ),
    "tags": ["features", "ml", "engineering"]
},
"data_sources": {
    "title": "आवश्यक डेटा स्रोत",
    "body": (
        "**मूल लेनदेन डेटा (आंतरिक)**\n"
        "• कोर बैंकिंग लेजर: सभी डेबिट, क्रेडिट, बैलेंस\n"
        "• कार्ड नेटवर्क डेटा: ऑथराइज़ेशन, सेटलमेंट, डिक्लाइन\n"
        "• ट्रांसफर लॉग: P2P, डायरेक्ट डेबिट, स्टैंडिंग ऑर्डर\n\n"
        "**प्रोडक्ट और ऑनबोर्डिंग**\n"
        "• KYC / ऑनबोर्डिंग फनल इवेंट\n"
        "• प्रोडक्ट सब्सक्रिप्शन स्थिति\n"
        "• रेफरल स्रोत और अधिग्रहण चैनल\n\n"
        "**डिजिटल एंगेजमेंट**\n"
        "• मोबाइल ऐप इवेंट स्ट्रीम\n"
        "• पुश नोटिफिकेशन ओपन रेट\n"
        "• इन-ऐप सर्वे (NPS, CSAT)\n\n"
        "**सपोर्ट और CRM**\n"
        "• टिकट इतिहास और चैट ट्रांसक्रिप्ट\n"
        "• ईमेल कैम्पेन एंगेजमेंट\n\n"
        "**इन्फ्रास्ट्रक्चर:**\n"
        "Kafka → डेटा लेक (S3/BigQuery) → फ़ीचर स्टोर → ML पाइपलाइन"
    ),
    "tags": ["data", "infrastructure", "sources"]
},
"retention_tactics": {
    "title": "प्रतिधारण रणनीतियाँ",
    "body": (
        "**टियर 1 — उच्च जोखिम, उच्च LTV (24 घंटे में कार्रवाई)**\n"
        "• रिलेशनशिप मैनेजर से व्यक्तिगत संपर्क\n"
        "• कस्टमाइज़्ड ऑफर: फ़ीस माफी, कैशबैक बूस्ट, रेट अपग्रेड\n"
        "• हालिया सेवा विफलताओं को सक्रिय रूप से ठीक करें\n\n"
        "**टियर 2 — उच्च जोखिम, मध्यम LTV (3–7 दिन में)**\n"
        "• व्यक्तिगत पुश नोटिफिकेशन\n"
        "• इन-ऐप री-एंगेजमेंट कैम्पेन\n"
        "• सीमित समय का ऑफर (जैसे '3 महीने मुफ्त प्रीमियम')\n\n"
        "**टियर 3 — शुरुआती चेतावनी (30–60 दिन)**\n"
        "• उपयोग के अंतराल के अनुसार शैक्षिक सामग्री\n"
        "• गेमिफिकेशन नज (स्ट्रीक, खर्च की जानकारी)\n"
        "• क्रॉस-सेल परिचय\n\n"
        "**संरचनात्मक रणनीतियाँ:**\n"
        "• वेतन डिपॉज़िट लॉक-इन — प्रतिधारण का सबसे अच्छा संकेतक\n"
        "• सैलरी एडवांस / BNPL स्विचिंग कॉस्ट बढ़ाता है\n"
        "• संयुक्त खाते / फैमिली प्लान नेटवर्क स्टिकीनेस बनाते हैं"
    ),
    "tags": ["retention", "tactics", "interventions"]
},
"segment_strategy": {
    "title": "सेगमेंटेशन रणनीति",
    "body": (
        "दो-अक्ष मॉडल (चर्न जोखिम × LTV) चार एक्शनेबल चतुर्भुज बनाता है:\n\n"
        "```\n"
        "         │  कम LTV        │  उच्च LTV\n"
        "─────────┼────────────────┼──────────────────\n"
        "कम जोखिम│ पोषण करें      │ बढ़ाएं और बचाएं\n"
        "─────────┼────────────────┼──────────────────\n"
        "उच्च जोखम│ कम प्राथमिकता │ ⚡ अभी बचाएं\n"
        "```\n\n"
        "🟢 **चैंपियन** — उच्च LTV, कम जोखिम: अपसेल, रेफरल, एडवोकेसी।\n"
        "🟡 **संभावित मूल्य** — कम LTV, कम जोखिम: एक्टिवेशन कैम्पेन।\n"
        "🟠 **जोखिम में स्टार** — उच्च LTV, उच्च जोखिम: तत्काल व्यक्तिगत हस्तक्षेप।\n"
        "🔴 **कम प्राथमिकता** — कम LTV, उच्च जोखिम: केवल कम लागत वाला ऑटोमेटेड री-एंगेजमेंट।"
    ),
    "tags": ["segmentation", "strategy", "ltv"]
},
"model_evaluation": {
    "title": "मॉडल प्रदर्शन मूल्यांकन",
    "body": (
        "**प्राथमिक मेट्रिक्स:**\n"
        "• **AUC-ROC:** समग्र भेदभाव। लक्ष्य: >0.80\n"
        "• **AUC-PR:** क्लास इम्बैलेंस में बेहतर। लक्ष्य: >0.60\n"
        "• **टॉप डेसाइल पर लिफ्ट:** लक्ष्य: रैंडम से 3–5× बेहतर\n\n"
        "**बिज़नेस मेट्रिक्स:**\n"
        "• ₹1 हस्तक्षेप लागत पर बचाया गया राजस्व\n"
        "• ऑपरेटिंग थ्रेशोल्ड पर प्रिसिजन और रिकॉल\n\n"
        "**कैलिब्रेशन:**\n"
        "Platt स्केलिंग या isotonic regression का उपयोग करें।\n\n"
        "**प्रोडक्शन मॉनिटरिंग:**\n"
        "• PSI (पॉपुलेशन स्टेबिलिटी इंडेक्स) — फ़ीचर ड्रिफ्ट\n"
        "• होल्डआउट सेट पर मासिक AUC ट्रैकिंग\n"
        "• ट्रू इन्क्रीमेंटल लिफ्ट मापने के लिए A/B टेस्ट\n"
        "• रीट्रेनिंग: तेज़ फ़ीचर के लिए मासिक, स्थिर के लिए तिमाही"
    ),
    "tags": ["ml", "evaluation", "metrics"]
},
"real_time": {
    "title": "रियल-टाइम हस्तक्षेप प्रणाली",
    "body": (
        "**परत 1 — स्कोरिंग पाइपलाइन**\n"
        "• बैच स्कोरिंग: सभी सक्रिय ग्राहकों पर रात में\n"
        "• नियर-रियल-टाइम: उच्च-सिग्नल इवेंट पर री-स्कोर\n"
        "• लेटेंसी लक्ष्य: इवेंट से अपडेटेड स्कोर तक <5 मिनट\n\n"
        "**परत 2 — डिसीजन इंजन**\n"
        "• नियम + मॉडल हाइब्रिड: मॉडल स्कोर + बिज़नेस बाधाएं\n"
        "• ऑफर पात्रता: सेगमेंट को अनुमोदित हस्तक्षेप से जोड़ें\n"
        "• बजट बाधाएं: दैनिक हस्तक्षेप वॉल्यूम सीमित करें\n\n"
        "**परत 3 — ऑर्केस्ट्रेशन**\n"
        "• चैनल पर पुश: Braze / Iterable (पुश, ईमेल, SMS)\n"
        "• मानव एजेंट के लिए CRM अलर्ट\n"
        "• फीडबैक लूप: परिणाम लॉग करें → मॉडल रीट्रेन करें\n\n"
        "**टेक स्टैक:**\n"
        "Kafka → Flink → Redis → FastAPI → Braze → Snowflake"
    ),
    "tags": ["real-time", "system", "architecture"]
},
"ltv_segments": {
    "title": "LTV-आधारित ग्राहक खंड",
    "body": (
        "| टियर | अनुमानित LTV | आधार का % | राजस्व का % |\n"
        "|---|---|---|---|\n"
        "| प्लेटिनम | >₹50,000 | 5% | 35% |\n"
        "| गोल्ड | ₹15,000–₹50,000 | 20% | 40% |\n"
        "| सिल्वर | ₹5,000–₹15,000 | 35% | 20% |\n"
        "| ब्रॉन्ज़ | <₹5,000 | 40% | 5% |\n\n"
        "यह 80/20 सांद्रता का अर्थ है कि चर्न रोकने का ROI प्लेटिनम और गोल्ड में केंद्रित है।\n\n"
        "**टियर अनुसार कार्रवाई:**\n"
        "• प्लेटिनम: व्हाइट-ग्लव सेवा, समर्पित सहायता\n"
        "• गोल्ड: प्रोएक्टिव क्रॉस-सेल, लॉयल्टी रिवॉर्ड\n"
        "• सिल्वर: एक्टिवेशन कैम्पेन\n"
        "• ब्रॉन्ज़: 180 दिन निष्क्रिय रहने पर सनसेट"
    ),
    "tags": ["ltv", "segments", "strategy"]
},
"revenue_impact": {
    "title": "चर्न का राजस्व पर प्रभाव",
    "body": (
        "**प्रत्यक्ष राजस्व हानि:**\n"
        "```\nवार्षिक हानि = मासिक चर्न × औसत LTV × 12\n```\n"
        "उदाहरण: 1,000 चर्न × ₹12,000 LTV = ₹1.44 करोड़/वर्ष जोखिम में\n\n"
        "**प्रतिस्थापन लागत:**\n"
        "```\nप्रतिस्थापन खर्च = चर्न दर × ग्राहक × CAC × 12\n```\n"
        "10,000 ग्राहकों पर 5% मासिक चर्न + ₹3,000 CAC = ₹18 लाख/वर्ष सिर्फ स्थिर रहने के लिए\n\n"
        "**चर्न कमी ROI:**\n"
        "5% से 4% चर्न कम करने पर:\n"
        "• 100 ग्राहक/माह × ₹12,000 LTV = ₹12 लाख/माह सुरक्षित\n"
        "• + ₹3 लाख CAC बचत = **1 प्रतिशत अंक से ₹1.8 करोड़ वार्षिक मूल्य**\n\n"
        "चर्न में 5% सुधार से मुनाफे में 25–95% वृद्धि हो सकती है (Bain & Co)।"
    ),
    "tags": ["revenue", "roi", "impact"]
},
}

# ─────────────────────────────────────────────────────────────────
# ANSWERS  (French)
# ─────────────────────────────────────────────────────────────────
ANSWERS_FR = {

"what_is_churn": {
    "title": "L'attrition client dans les neobanques",
    "body": (
        "L'attrition (ou churn) désigne le taux auquel les clients cessent d'utiliser les produits "
        "et services d'une neobanque sur une période donnée. Contrairement aux banques traditionnelles, "
        "les neobanques font face à une dynamique d'attrition unique car les coûts de changement sont "
        "quasi nuls — ouvrir un nouveau compte prend quelques minutes.\n\n"
        "**Types d'attrition dans les neobanques :**\n"
        "• **Attrition dure** — Le client ferme complètement son compte\n"
        "• **Attrition douce** — Le compte reste ouvert mais l'activité tombe à quasi zéro (comptes zombies)\n"
        "• **Attrition produit** — Le client garde le compte mais abandonne les fonctionnalités premium\n"
        "• **Attrition de revenus** — Le client rétrograde, réduisant sa contribution monétaire\n\n"
        "Les neobanques voient souvent l'attrition douce comme leur principal défi : jusqu'à 40–60% "
        "des inscrits deviennent inactifs dans les 90 jours. Les identifier tôt est crucial pour l'optimisation LTV."
    ),
    "tags": ["churn", "basics", "neobank"]
},
"churn_signals": {
    "title": "Signaux d'attrition clés dans les neobanques",
    "body": (
        "L'attrition survient rarement sans avertissement. Les signaux comportementaux apparaissent "
        "généralement 30 à 90 jours avant le départ du client :\n\n"
        "**Comportement transactionnel**\n"
        "• Baisse du volume mensuel (>30% vs. base 90 jours)\n"
        "• Passage d'une utilisation active à zéro transaction\n"
        "• Arrêt du virement salaire / prélèvement direct\n"
        "• Solde constamment proche de zéro\n\n"
        "**Engagement produit**\n"
        "• Ouvertures d'app inférieures à une fois par semaine\n"
        "• Régression d'utilisation (arrêt épargne, investissements)\n"
        "• Désactivation des notifications push\n\n"
        "**Signaux support**\n"
        "• Réclamation récente ou ticket non résolu\n"
        "• Faible score CSAT / NPS\n\n"
        "**Signaux externes**\n"
        "• Ouverture d'un compte concurrent (détectable via open banking)\n"
        "• Baisse des dépenses carte là où la neobanque était dominante"
    ),
    "tags": ["churn", "signals", "features"]
},
"churn_rate": {
    "title": "Calcul du taux d'attrition",
    "body": (
        "**Taux d'attrition mensuel (basique)**\n"
        "```\nTaux = (Clients perdus) / (Clients en début de période) × 100\n```\n\n"
        "**Exemple :** 500 perdus sur 10 000 → 5% d'attrition mensuelle\n\n"
        "**Attrition annualisée :**\n"
        "```\nAttrition annuelle ≈ 1 − (1 − Attrition mensuelle)^12\n```\n"
        "5% mensuel = ~46% annuel\n\n"
        "**Taux d'attrition des revenus :**\n"
        "```\nAttrition revenus = (MRR perdu) / (MRR initial) × 100\n```\n\n"
        "**Benchmarks neobanques :**\n"
        "• Excellence : <2% d'attrition mensuelle\n"
        "• Sain : 3–5% d'attrition mensuelle\n"
        "• Préoccupant : >7% d'attrition mensuelle"
    ),
    "tags": ["churn", "metrics", "formula"]
},
"ltv_definition": {
    "title": "Valeur Vie Client (LTV) pour les neobanques",
    "body": (
        "La **Valeur Vie Client (LTV)** est le revenu net total qu'une neobanque s'attend à générer "
        "avec un client tout au long de leur relation.\n\n"
        "Sources de revenus LTV pour les neobanques :\n\n"
        "| Source de revenus | Exemple |\n"
        "|---|---|\n"
        "| Frais d'interchange | 0,2–1,5% par transaction carte |\n"
        "| Abonnement / premium | 9,99€/mois carte Metal |\n"
        "| Marge FX | 0,5–2% sur conversion de devises |\n"
        "| Marge crédit | Intérêts découvert / prêts |\n"
        "| Spread épargne | Différence taux dépôt / rendement |\n\n"
        "**Pourquoi la LTV compte :** Un client acquis pour 30€ qui part au 2e mois génère une perte nette. "
        "La période de remboursement — quand les revenus cumulés dépassent le CAC — est la métrique de santé financière principale."
    ),
    "tags": ["ltv", "basics", "revenue"]
},
"ltv_formula": {
    "title": "Formule LTV pour les neobanques",
    "body": (
        "**LTV simple :**\n"
        "```\nLTV = ARPU × Marge brute % × (1 / Taux d'attrition)\n```\n\n"
        "**Exemple :** ARPU = 8€/mois, Marge = 60%, Attrition mensuelle = 4%\n"
        "```\nLTV = 8€ × 0,60 × 25 = 120€\n```\n\n"
        "**LTV actualisée :**\n"
        "```\nLTV = Σ (Revenus_t − Coûts_t) / (1 + Taux d'actualisation)^t\n```\n"
        "Utiliser un taux d'actualisation annuel de 10–15%.\n\n"
        "**LTV prédictive (ML) :**\n"
        "Modèles de survie BG/NBD ou régresseurs gradient boosting entraînés sur données cohortes.\n\n"
        "**Benchmarks LTV neobanques :**\n"
        "• Compte basique : 80–150€\n"
        "• Niveau premium/Metal : 400–900€\n"
        "• Comptes PME : 1 200–4 000€"
    ),
    "tags": ["ltv", "formula", "metrics"]
},
"ltv_vs_cac": {
    "title": "Ratio LTV / CAC",
    "body": (
        "```\nLTV:CAC = Valeur Vie Client / Coût d'Acquisition Client\n```\n\n"
        "| Ratio | Signal |\n"
        "|---|---|\n"
        "| < 1:1 | Destruction de valeur |\n"
        "| 1:1 – 3:1 | Marginal — croissance fragile |\n"
        "| 3:1 | ✅ Benchmark industrie |\n"
        "| > 5:1 | Sous-investissement en croissance |\n\n"
        "**Composantes du CAC :** Publicité sociale, bonus parrainage, App Store, KYC, émission carte.\n\n"
        "**Améliorer le ratio :**\n"
        "• Réduire le CAC : canaux organiques / parrainage\n"
        "• Augmenter la LTV : upsell premium, cross-sell crédit, réduire l'attrition\n"
        "• Segments haute LTV justifient un CAC 3× plus élevé"
    ),
    "tags": ["ltv", "cac", "unit economics"]
},
"ml_models": {
    "title": "Modèles ML pour la prédiction d'attrition",
    "body": (
        "**1. Arbres à gradient boosté (XGBoost / LightGBM)**\n"
        "Le plus déployé en production. Interprétable via SHAP, gère les valeurs manquantes nativement.\n\n"
        "**2. Régression logistique (baseline)**\n"
        "Pour l'explicabilité réglementaire. Compétitif avec un bon feature engineering.\n\n"
        "**3. Modèles de survie (Cox / BG/NBD)**\n"
        "Idéal pour prédire le délai avant attrition. BG/NBD est le standard pour les neobanques.\n\n"
        "**4. Réseaux de neurones récurrents (LSTM)**\n"
        "Efficace pour les séquences temporelles de transactions. Difficile à expliquer.\n\n"
        "**5. Réseaux de neurones graphiques**\n"
        "Détecte l'attrition coordonnée dans les réseaux de parrainage.\n\n"
        "**Pipeline recommandé :**\n"
        "LightGBM + SHAP → modèle de survie → ensemble si nécessaire"
    ),
    "tags": ["ml", "models", "churn"]
},
"features": {
    "title": "Principales variables prédictives",
    "body": (
        "**Récence / Fréquence / Montant (RFM)**\n"
        "• Jours depuis la dernière transaction\n"
        "• Nombre de transactions : 7 / 30 / 90 derniers jours\n"
        "• Tendance dépenses vs. moyenne 90 jours\n\n"
        "**Santé du compte**\n"
        "• Solde moyen en fin de journée (30 jours)\n"
        "• Volatilité du solde\n"
        "• Virement salaire : oui/non\n"
        "• Fréquence d'utilisation du découvert\n\n"
        "**Profondeur produit**\n"
        "• Nombre de produits actifs\n"
        "• Niveau premium : oui/non\n"
        "• Score de diversité des dépenses carte\n\n"
        "**Engagement**\n"
        "• Ouvertures app par semaine (moyenne glissante 7 jours)\n"
        "• Jours depuis la dernière ouverture app\n"
        "• Score de découverte de fonctionnalités\n\n"
        "**Support client**\n"
        "• Ticket ouvert : oui/non\n"
        "• Score CSAT de la dernière interaction\n"
        "• Réclamation dans les 30 derniers jours : oui/non"
    ),
    "tags": ["features", "ml", "engineering"]
},
"data_sources": {
    "title": "Sources de données nécessaires",
    "body": (
        "**Transactionnel de base (interne)**\n"
        "• Grand livre bancaire : débits, crédits, soldes\n"
        "• Données réseau carte : autorisation, règlement, refus\n"
        "• Journaux de transfert : P2P, prélèvements, virements permanents\n\n"
        "**Produit & Onboarding**\n"
        "• Événements KYC / tunnel d'onboarding\n"
        "• Statut abonnement produit\n"
        "• Source de parrainage et canal d'acquisition\n\n"
        "**Engagement digital**\n"
        "• Flux d'événements app mobile\n"
        "• Taux d'ouverture des notifications push\n"
        "• Réponses aux sondages in-app (NPS, CSAT)\n\n"
        "**Support & CRM**\n"
        "• Historique tickets et transcriptions chat\n"
        "• Engagement campagnes email\n\n"
        "**Infrastructure :**\n"
        "Kafka → data lake (S3/BigQuery) → feature store (Feast/Tecton) → pipeline ML"
    ),
    "tags": ["data", "infrastructure", "sources"]
},
"retention_tactics": {
    "title": "Tactiques de rétention pour les neobanques",
    "body": (
        "**Niveau 1 — Risque élevé, LTV élevée (agir sous 24h)**\n"
        "• Prise de contact personnelle par un gestionnaire de relation\n"
        "• Offre sur mesure : exonération de frais, boost cashback, upgrade de taux\n"
        "• Résolution proactive des incidents de service récents\n\n"
        "**Niveau 2 — Risque élevé, LTV moyenne (3–7 jours)**\n"
        "• Notification push personnalisée avec rappel de valeur\n"
        "• Campagne de réengagement in-app\n"
        "• Offre limitée dans le temps (ex. '3 mois premium offerts')\n\n"
        "**Niveau 3 — Alerte précoce (30–60 jours)**\n"
        "• Contenu éducatif adapté aux lacunes d'utilisation\n"
        "• Nudges de gamification (séries, insights dépenses)\n"
        "• Introduction cross-sell\n\n"
        "**Tactiques structurelles :**\n"
        "• Domiciliation salaire — meilleur prédicteur de rétention\n"
        "• Avance salaire / BNPL augmente le coût de changement\n"
        "• Comptes joints / plans famille créent de la fidélité réseau"
    ),
    "tags": ["retention", "tactics", "interventions"]
},
"segment_strategy": {
    "title": "Stratégie de segmentation",
    "body": (
        "Un modèle à deux axes (Risque d'attrition × LTV) crée quatre quadrants actionnables :\n\n"
        "```\n"
        "          │  LTV FAIBLE    │  LTV ÉLEVÉE\n"
        "──────────┼────────────────┼──────────────────\n"
        "FAIBLE    │ Nourrir        │ Développer et\n"
        "RISQUE    │                │ protéger\n"
        "──────────┼────────────────┼──────────────────\n"
        "RISQUE    │ Basse priorité │ ⚡ SAUVER MAINTENANT\n"
        "ÉLEVÉ     │                │\n"
        "```\n\n"
        "🟢 **Champions** — LTV élevée, faible risque : upsell, parrainage, advocacy.\n"
        "🟡 **Valeur potentielle** — LTV faible, faible risque : campagnes d'activation.\n"
        "🟠 **Stars à risque** — LTV élevée, risque élevé : intervention personnelle immédiate.\n"
        "🔴 **Basse priorité** — LTV faible, risque élevé : réengagement automatisé à faible coût uniquement."
    ),
    "tags": ["segmentation", "strategy", "ltv"]
},
"model_evaluation": {
    "title": "Évaluation des performances du modèle",
    "body": (
        "**Métriques principales (déséquilibre de classes) :**\n"
        "• **AUC-ROC :** Discrimination globale. Cible : >0,80\n"
        "• **AUC-PR :** Meilleur sous déséquilibre. Cible : >0,60\n"
        "• **Lift au top décile :** Cible : 3–5× vs. aléatoire\n\n"
        "**Métriques métier :**\n"
        "• Revenus sauvegardés par € de coût d'intervention\n"
        "• Précision et rappel au seuil opérationnel\n\n"
        "**Calibration :**\n"
        "Platt scaling ou régression isotonique. Un score de 80% doit être correct ~80% du temps.\n\n"
        "**Surveillance en production :**\n"
        "• PSI (Population Stability Index) — détecter la dérive des features\n"
        "• Suivi AUC mensuel sur jeu de test\n"
        "• A/B test des bras d'intervention pour mesurer le lift incrémental\n"
        "• Réentraînement mensuel (features rapides) / trimestriel (stables)"
    ),
    "tags": ["ml", "evaluation", "metrics"]
},
"real_time": {
    "title": "Systèmes d'intervention en temps réel",
    "body": (
        "**Couche 1 — Pipeline de scoring**\n"
        "• Scoring batch : chaque nuit sur tous les clients actifs\n"
        "• Quasi temps réel : re-scoring sur événements à fort signal\n"
        "• Latence cible : <5 minutes de l'événement au score mis à jour\n\n"
        "**Couche 2 — Moteur de décision**\n"
        "• Hybride règles + modèle : score + contraintes métier\n"
        "• Éligibilité offre : mapper le segment au catalogue d'interventions\n"
        "• Contraintes budgétaires : plafonner le volume d'interventions quotidien\n\n"
        "**Couche 3 — Orchestration**\n"
        "• Push canal : Braze / Iterable pour push, email, SMS\n"
        "• Alerte CRM pour agents humains (Salesforce / Zendesk)\n"
        "• Boucle de retour : logger les résultats → réentraîner le modèle\n\n"
        "**Stack technique :**\n"
        "Kafka → Flink → Redis → FastAPI → Braze → Snowflake"
    ),
    "tags": ["real-time", "system", "architecture"]
},
"ltv_segments": {
    "title": "Segments clients basés sur la LTV",
    "body": (
        "| Niveau | LTV prédite | % de la base | % des revenus |\n"
        "|---|---|---|---|\n"
        "| Platine | >500€ | 5% | 35% |\n"
        "| Or | 150–500€ | 20% | 40% |\n"
        "| Argent | 50–150€ | 35% | 20% |\n"
        "| Bronze | <50€ | 40% | 5% |\n\n"
        "Cette concentration 80/20 signifie que le ROI de prévention d'attrition est concentré sur Platine et Or.\n\n"
        "**Actions par niveau :**\n"
        "• Platine : service premium, file de support dédiée\n"
        "• Or : cross-sell proactif, récompenses fidélité\n"
        "• Argent : campagnes d'activation, éducation fonctionnalités\n"
        "• Bronze : nurture à faible coût, suppression si inactif >180 jours"
    ),
    "tags": ["ltv", "segments", "strategy"]
},
"revenue_impact": {
    "title": "Impact de l'attrition sur les revenus",
    "body": (
        "**Perte de revenus directe :**\n"
        "```\nPerte annuelle = Churners mensuels × LTV moyenne × 12\n```\n"
        "Exemple : 1 000 churners × 120€ LTV = 1,44M€/an à risque\n\n"
        "**Coût de remplacement :**\n"
        "```\nDépense remplacement = Taux attrition × Clients × CAC × 12\n```\n"
        "5% mensuel sur 10 000 clients à 30€ CAC = 180K€/an juste pour rester à niveau.\n\n"
        "**ROI réduction attrition :**\n"
        "Passer de 5% à 4% sur 10 000 clients :\n"
        "• 100 clients/mois × 120€ LTV = 12 000€/mois protégés\n"
        "• + 3 000€ économies CAC = **180K€ de valeur annuelle** par point de % gagné\n\n"
        "Améliorer l'attrition de 5% peut augmenter les bénéfices de 25–95% (Bain & Co)."
    ),
    "tags": ["revenue", "roi", "impact"]
},
}

# ─────────────────────────────────────────────────────────────────
# ANSWER MAP BY LANGUAGE
# ─────────────────────────────────────────────────────────────────
ANSWERS_BY_LANG = {
    "en": ANSWERS_EN,
    "hi": ANSWERS_HI,
    "fr": ANSWERS_FR,
}

# ─────────────────────────────────────────────────────────────────
# KEYWORD MAP  (language-aware)
# ─────────────────────────────────────────────────────────────────
KEYWORD_MAP_EN = {
    "what_is_churn":     ["what is churn", "define churn", "churn mean", "customer churn", "what does churn"],
    "churn_signals":     ["signal", "warning", "indicator", "detect churn", "early warning", "signs of churn"],
    "churn_rate":        ["calculate churn", "churn rate", "churn formula", "measure churn", "churn metric"],
    "ltv_definition":    ["what is ltv", "lifetime value", "clv", "cltv", "ltv mean", "define ltv"],
    "ltv_formula":       ["ltv formula", "calculate ltv", "compute ltv", "ltv calculation", "ltv model"],
    "ltv_vs_cac":        ["ltv cac", "cac", "acquisition cost", "unit economics", "ltv to cac", "ratio"],
    "ml_models":         ["model", "algorithm", "xgboost", "lightgbm", "machine learning", "predict churn", "ml", "neural"],
    "features":          ["feature", "variable", "input", "predictor", "attribute"],
    "data_sources":      ["data source", "dataset", "data need", "what data", "kafka", "pipeline"],
    "retention_tactics": ["retain", "retention", "keep customer", "prevent churn", "reduce churn", "tactic"],
    "segment_strategy":  ["segment", "segmentation", "group customer", "cluster", "tier"],
    "model_evaluation":  ["evaluate", "auc", "precision", "recall", "metric", "performance", "accuracy"],
    "real_time":         ["real time", "real-time", "live", "instant", "trigger", "stream", "production"],
    "ltv_segments":      ["ltv segment", "ltv tier", "platinum", "gold", "silver", "bronze"],
    "revenue_impact":    ["revenue", "impact", "cost of churn", "roi", "profit", "financial"],
}

KEYWORD_MAP_HI = {
    "what_is_churn":     ["चर्न क्या", "चर्न का मतलब", "ग्राहक चर्न", "चर्न परिभाषा"],
    "churn_signals":     ["संकेत", "चेतावनी", "चर्न के संकेत", "पहचान", "चर्न पहचान"],
    "churn_rate":        ["चर्न दर", "गणना", "चर्न फ़ॉर्मूला", "दर मापना"],
    "ltv_definition":    ["ltv क्या", "लाइफटाइम वैल्यू", "ltv का मतलब", "ग्राहक मूल्य"],
    "ltv_formula":       ["ltv फ़ॉर्मूला", "ltv गणना", "ltv कैसे"],
    "ltv_vs_cac":        ["cac", "अधिग्रहण लागत", "ltv cac", "अनुपात"],
    "ml_models":         ["मॉडल", "एल्गोरिदम", "मशीन लर्निंग", "ml", "xgboost"],
    "features":          ["विशेषता", "फ़ीचर", "चर", "भविष्यवक्ता"],
    "data_sources":      ["डेटा", "स्रोत", "डेटासेट", "डेटा चाहिए"],
    "retention_tactics": ["प्रतिधारण", "ग्राहक बनाए", "चर्न रोकें", "रणनीति"],
    "segment_strategy":  ["सेगमेंट", "विभाजन", "समूह", "टियर"],
    "model_evaluation":  ["मूल्यांकन", "auc", "प्रिसिजन", "प्रदर्शन", "मेट्रिक"],
    "real_time":         ["रियल टाइम", "लाइव", "तत्काल", "स्ट्रीम"],
    "ltv_segments":      ["ltv खंड", "प्लेटिनम", "गोल्ड", "सिल्वर", "ब्रॉन्ज़"],
    "revenue_impact":    ["राजस्व", "प्रभाव", "roi", "मुनाफा", "वित्तीय"],
}

KEYWORD_MAP_FR = {
    "what_is_churn":     ["qu'est-ce que", "attrition", "churn", "définition", "qu est ce"],
    "churn_signals":     ["signal", "indicateur", "signe", "détecter", "avertissement"],
    "churn_rate":        ["calculer", "taux", "formule", "mesurer attrition"],
    "ltv_definition":    ["qu'est-ce que ltv", "valeur vie", "ltv signifie", "définir ltv"],
    "ltv_formula":       ["formule ltv", "calculer ltv", "calcul ltv", "modèle ltv"],
    "ltv_vs_cac":        ["cac", "coût acquisition", "ratio ltv", "unit economics"],
    "ml_models":         ["modèle", "algorithme", "machine learning", "ml", "xgboost", "prédire"],
    "features":          ["variable", "feature", "caractéristique", "prédicteur"],
    "data_sources":      ["source de données", "données", "dataset", "kafka"],
    "retention_tactics": ["rétention", "garder", "fidéliser", "réduire attrition", "tactique"],
    "segment_strategy":  ["segment", "segmentation", "groupe", "cluster", "niveau"],
    "model_evaluation":  ["évaluer", "auc", "précision", "rappel", "performance", "métrique"],
    "real_time":         ["temps réel", "direct", "instantané", "flux", "production"],
    "ltv_segments":      ["segment ltv", "platine", "or", "argent", "bronze", "niveau ltv"],
    "revenue_impact":    ["revenus", "impact", "roi", "profit", "financier"],
}

KEYWORD_MAP_BY_LANG = {
    "en": KEYWORD_MAP_EN,
    "hi": KEYWORD_MAP_HI,
    "fr": KEYWORD_MAP_FR,
}

DEFAULT_BODY = {
    "en": (
        "I'm your specialist guide for **customer churn and LTV prediction** in neobanks. "
        "Select a topic above or ask me anything — model selection, retention tactics, LTV formulas, and more."
    ),
    "hi": (
        "मैं नियोबैंक के लिए **ग्राहक चर्न और LTV पूर्वानुमान** का विशेषज्ञ हूँ। "
        "ऊपर कोई विषय चुनें या कुछ भी पूछें — मॉडल चयन, प्रतिधारण रणनीतियाँ, LTV फ़ॉर्मूला, और अधिक।"
    ),
    "fr": (
        "Je suis votre guide spécialisé pour la **prédiction d'attrition et de LTV** dans les neobanques. "
        "Sélectionnez un sujet ci-dessus ou posez n'importe quelle question — sélection de modèles, tactiques de rétention, formules LTV."
    ),
}
DEFAULT_TITLE = {"en": "NeoBank Churn & LTV Intelligence", "hi": "नियोबैंक चर्न और LTV इंटेलिजेंस", "fr": "Intelligence Attrition & LTV NeoBank"}

# ─────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────
def get_topics(lang: str = "en") -> list:
    return TOPIC_LABELS.get(lang, TOPIC_LABELS["en"])


def get_response(message: str, lang: str = "en") -> dict:
    msg_lower = message.lower().strip()
    answers   = ANSWERS_BY_LANG.get(lang, ANSWERS_EN)
    kw_map    = KEYWORD_MAP_BY_LANG.get(lang, KEYWORD_MAP_EN)

    # Direct topic ID match (chip click)
    if msg_lower in answers:
        a = answers[msg_lower]
        return {"topic_id": msg_lower, "title": a["title"], "body": a["body"], "tags": a["tags"], "matched": True}

    # Keyword matching
    best_topic, best_score = None, 0
    for topic_id, keywords in kw_map.items():
        score = sum(1 for kw in keywords if kw in msg_lower)
        if score > best_score:
            best_score, best_topic = score, topic_id

    if best_topic and best_score > 0:
        a = answers[best_topic]
        return {"topic_id": best_topic, "title": a["title"], "body": a["body"], "tags": a["tags"], "matched": True}

    # Fallback — also try English keywords as a catch-all
    if lang != "en":
        for topic_id, keywords in KEYWORD_MAP_EN.items():
            score = sum(1 for kw in keywords if kw in msg_lower)
            if score > best_score:
                best_score, best_topic = score, topic_id
        if best_topic and best_score > 0:
            a = answers.get(best_topic, ANSWERS_EN[best_topic])
            return {"topic_id": best_topic, "title": a["title"], "body": a["body"], "tags": a["tags"], "matched": True}

    return {
        "topic_id": None,
        "title": DEFAULT_TITLE.get(lang, DEFAULT_TITLE["en"]),
        "body": DEFAULT_BODY.get(lang, DEFAULT_BODY["en"]),
        "tags": [],
        "matched": False
    }
