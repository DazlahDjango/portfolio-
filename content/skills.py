"""
Skills, grouped by category.
Each category has a name and a list of skills.
Each skill: {"name": "...", "level": 1-5}  (level is optional — shown as dots/bars)
"""

SKILL_CATEGORIES = [
    {
        "name": "Software Engineering",
        "icon": "code",
        "skills": [
            {"name": "Python", "level": 5},
            {"name": "Django", "level": 5},
            {"name": "Flask", "level": 4},
            {"name": "REST APIs (DRF)", "level": 5},
            {"name": "PostgreSQL", "level": 5},
            {"name": "MySQL", "level": 4},
            {"name": "Multitenant Architecture", "level": 4},
            {"name": "RBAC / Authentication", "level": 4},
            {"name": "PayStack Integration", "level": 4},
            {"name": "React (Vite)", "level": 3},
            {"name": "Django Templates / Jinja2", "level": 5},
        ],
    },
    {
        "name": "AI, Data & Machine Learning",
        "icon": "brain",
        "skills": [
            {"name": "Machine Learning", "level": 4},
            {"name": "Data Analysis", "level": 4},
            {"name": "ML Integration in Production Apps", "level": 4},
            {"name": "Python Data Stack (pandas, numpy)", "level": 4},
        ],
    },
    {
        "name": "Networking",
        "icon": "network",
        "skills": [
            {"name": "Network Design (Cisco)", "level": 5},
            {"name": "Router & Switch Configuration", "level": 5},
            {"name": "MikroTik Configuration", "level": 5},
            {"name": "Subnetting & IP Planning", "level": 5},
            {"name": "Network Troubleshooting", "level": 5},
        ],
    },
    {
        "name": "Systems & Infrastructure",
        "icon": "server",
        "skills": [
            {"name": "Docker & Virtualization", "level": 4},
            {"name": "Server Room Management", "level": 5},
            {"name": "Computer Lab Management", "level": 5},
            {"name": "Hardware Diagnostics & Repair", "level": 5},
            {"name": "Windows Administration", "level": 5},
            {"name": "Linux (incl. Kali basics)", "level": 4},
            {"name": "Software Installation & Recovery", "level": 5},
        ],
    },
    {
        "name": "Design & Engineering Tools",
        "icon": "design",
        "skills": [
            {"name": "AutoCAD", "level": 4},
            {"name": "Software Design (UML, diagrams)", "level": 4},
        ],
    },
]