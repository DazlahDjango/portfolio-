"""
Services you offer. These are what clients see on the Services page.
"""

SERVICES = [
    {
        "title": "Custom Software Development",
        "icon": "code",
        "description": (
            "Full-stack web applications built with Django or Flask, backed by PostgreSQL. "
            "From single-tenant tools to multitenant SaaS platforms with role-based access control."
        ),
        "features": [
            "Requirements → design → build → deploy",
            "REST APIs with DRF",
            "Authentication & RBAC",
            "Payment gateway integration (PayStack)",
        ],
    },
    {
        "title": "AI & Machine Learning Integration",
        "icon": "brain",
        "description": (
            "Add intelligence to your existing systems — predictive features, automation, "
            "and data-driven decision support — without rebuilding from scratch."
        ),
        "features": [
            "ML model integration into web apps",
            "Data analysis & reporting",
            "Custom automation pipelines",
            "Model deployment & monitoring",
        ],
    },
    {
        "title": "Network Design & Configuration",
        "icon": "network",
        "description": (
            "Complete network architecture and configuration for offices, campuses, "
            "and small data centers — Cisco and MikroTik, designed for reliability and scale."
        ),
        "features": [
            "Network topology design",
            "Router, switch, and MikroTik configuration",
            "Subnetting & IP address planning",
            "On-site troubleshooting & optimization",
        ],
    },
    {
        "title": "IT Infrastructure & Hardware Management",
        "icon": "server",
        "description": (
            "End-to-end management of server rooms, computer labs, and hardware fleets — "
            "including setup, maintenance, and emergency recovery."
        ),
        "features": [
            "Server room setup & management",
            "Computer lab deployment & maintenance",
            "Hardware diagnostics & repair",
            "OS installation & system recovery",
        ],
    },
    {
        "title": "Virtualization & Docker",
        "icon": "container",
        "description": (
            "Containerize and virtualize your infrastructure for consistency, portability, "
            "and cost efficiency — from dev environments to production stacks."
        ),
        "features": [
            "Docker container setup",
            "Multi-service orchestration",
            "Virtualized dev environments",
            "Deployment automation",
        ],
    },
    {
        "title": "Technical Consulting",
        "icon": "spark",
        "description": (
            "Not sure what you need? I'll assess your current systems and give you an honest, "
            "practical roadmap — whether you hire me for the build or not."
        ),
        "features": [
            "System audit & recommendations",
            "Architecture planning",
            "Tool & stack selection",
            "Technical documentation",
        ],
    },
]