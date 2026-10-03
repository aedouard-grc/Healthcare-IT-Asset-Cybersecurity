# Display recommended GitHub repository structure

from IPython.display import HTML, display

html = """
<div style="
    font-family: 'Courier New', monospace;
    font-size: 14px;
    background: #f6f8fa;
    padding: 20px 24px;
    border-radius: 8px;
    border: 1px solid #d0d7de;
    line-height: 1.6;
    white-space: pre;
    max-width: 720px;
">
<b style="color:#24292f; font-size:15px;">📁 Recommended GitHub Repository Structure</b>

<b style="color:#0969da;">Healthcare-IT-Asset-Cybersecurity/</b>
│
├── <span style="color:#1a7f37;">📄 README.md</span>
│
├── <span style="color:#0969da;">📁 notebooks/</span>
│   └── <span style="color:#1a7f37;">📓 Healthcare_IT_Asset_Cybersecurity_Triage.ipynb</span>
│
├── <span style="color:#0969da;">📁 data/</span>
│   ├── <span style="color:#1a7f37;">📄 healthcare_it_asset_inventory_analyzed.csv</span>
│   ├── <span style="color:#1a7f37;">📄 healthcare_it_asset_triage_report.csv</span>
│   └── <span style="color:#1a7f37;">📄 healthcare_security_dashboard.csv</span>
│
├── <span style="color:#0969da;">📁 screenshots/</span>
│   ├── <span style="color:#1a7f37;">🖼️ asset_inventory.png</span>
│   ├── <span style="color:#1a7f37;">🖼️ vulnerability_analysis.png</span>
│   ├── <span style="color:#1a7f37;">🖼️ risk_analysis.png</span>
│   ├── <span style="color:#1a7f37;">🖼️ triage_dashboard.png</span>
│   ├── <span style="color:#1a7f37;">🖼️ healthcare_it_assets_by_criticality.png</span>
│   ├── <span style="color:#1a7f37;">🖼️ internet_exposed_vs_internal_assets.png</span>
│   ├── <span style="color:#1a7f37;">🖼️ healthcare_it_asset_condition.png</span>
│   ├── <span style="color:#1a7f37;">🖼️ cybersecurity_asset_triage_priority.png</span>
│   ├── <span style="color:#1a7f37;">🖼️ healthcare_it_asset_risk_score.png</span>
│   ├── <span style="color:#1a7f37;">🖼️ healthcare_it_asset_cybersecurity_summary.png</span>
│   ├── <span style="color:#1a7f37;">🖼️ healthcare_it_asset_cybersecurity_dashboard.png</span>
│   └── <span style="color:#1a7f37;">🖼️ recommended_github_repository_structure.png</span>
│
└── <span style="color:#1a7f37;">📄 requirements.txt</span>
</div>
"""

display(HTML(html))