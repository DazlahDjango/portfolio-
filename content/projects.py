"""
Portfolio projects. Add your own — start with 2-3 solid entries.
For images, drop files into app/static/img/projects/ and set "image" to the filename.
"""

PROJECTS = [
    {
        "title": "Multitenant SaaS Platform",
        "category": "Software",
        "description": (
            "A Django-based multitenant system with per-tenant database isolation, "
            "RBAC, and ML-driven reporting for each tenant."
        ),
        "tech": ["Django", "PostgreSQL", "DRF", "ML"],
        "image": "",  # e.g. "saas.jpg" — leave blank to show a placeholder
        "link": "",
        "repo": "",
    },
    {
        "title": "ML-Powered Analytics Dashboard",
        "category": "AI / Data",
        "description": (
            "An analytics dashboard that predicts trends using trained ML models, "
            "delivered via a Flask API and consumed by a React frontend."
        ),
        "tech": ["Python", "Flask", "React", "scikit-learn"],
        "image": "",
        "link": "",
        "repo": "",
    },
    {
        "title": "Campus Network Design & Deployment",
        "category": "Networking",
        "description": (
            "Designed and configured a full campus network using Cisco and MikroTik "
            "equipment — subnets, routing, VLANs, and access control."
        ),
        "tech": ["Cisco", "MikroTik", "VLAN", "Routing"],
        "image": "",
        "link": "",
        "repo": "",
    },
]