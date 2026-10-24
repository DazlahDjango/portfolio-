"""
catalogue_data.py
Contains structured projects, frameworks, databases, frontend systems,
add-ons, CSS color palettes, and DevOps tiers based on catalogue.txt.
Exchange Rates: 1 USD ≈ 129.85 KES ≈ 0.8911 EUR
"""

CURRENCIES = {
    "KES": {"symbol": "KSh", "rate_from_usd": 129.85, "prefix": "KSh "},
    "USD": {"symbol": "$", "rate_from_usd": 1.0, "prefix": "$"},
    "EUR": {"symbol": "€", "rate_from_usd": 0.8911, "prefix": "€"},
}

FRAMEWORKS = {
    "django": {
        "id": "django",
        "name": "Django / Django REST Framework",
        "badge": "Batteries-Included & Enterprise Grade",
        "tagline": "The premier Python framework for secure, scalable business backends and complex SaaS systems.",
        "icon": "shield-check",
        "what_is": (
            "Django is a high-level, batteries-included Python web framework designed to help you build reliable, "
            "secure, and robust applications rapidly. It includes an Object-Relational Mapper (ORM), built-in "
            "authentication, security protections against CSRF/SQL injection, automated database migrations, "
            "and a production-grade admin dashboard out of the box."
        ),
        "why_choose": [
            "Includes built-in user authentication, session security, and permissions.",
            "World-class administrative dashboard ready without writing custom CRUD screens.",
            "Native support for multi-tenancy, complex relational schemas, and audit logs.",
            "Pairs seamlessly with Django REST Framework (DRF) for React, Vue, Next.js, and mobile clients."
        ],
        "best_for": "SaaS platforms, ERP, CRM, School/Hospital Management, Portals & High-Security APIs."
    },
    "flask": {
        "id": "flask",
        "name": "Flask / Python Microframework",
        "badge": "Lightweight, Flexible & Agile",
        "tagline": "A minimalist, un-opinionated Python framework offering total architectural freedom.",
        "icon": "zap",
        "what_is": (
            "Flask is a lightweight WSGI microframework for Python. It provides the core essentials — routing, "
            "request handling, and Jinja2 templating — while giving the developer total freedom to hand-pick "
            "their preferred database ORM (SQLAlchemy), authentication method, and service architecture without unnecessary bloat."
        ),
        "why_choose": [
            "Extremely fast footprint and rapid prototyping speed.",
            "Total control over architecture, libraries, and microservice layout.",
            "Ideal for clean REST APIs, dashboards, client portals, and web services.",
            "Deployable with minimal server resource consumption."
        ],
        "best_for": "Custom business websites, MVPs, focused APIs, dashboards & utilities."
    },
    "fastapi": {
        "id": "fastapi",
        "name": "FastAPI",
        "badge": "Modern, High-Speed & Asynchronous",
        "tagline": "Modern, high-performance async framework with automatic OpenAPI docs and type validation.",
        "icon": "cpu",
        "what_is": (
            "FastAPI is a modern, high-performance web framework for building APIs with Python 3.8+ based on standard "
            "Python type hints and Starlette/Pydantic. It offers performance comparable to NodeJS and Go, with "
            "built-in asynchronous I/O and interactive Swagger documentation generated automatically."
        ),
        "why_choose": [
            "Native asynchronous Python (async/await) for high-concurrency workloads.",
            "Automatic interactive documentation (Swagger / OpenAPI) with zero setup.",
            "Strict runtime data validation via Pydantic.",
            "The top industry choice for AI models, ML inference, and vector search endpoints."
        ],
        "best_for": "AI/ML inference APIs, real-time data pipelines, high-throughput microservices."
    },
    "node": {
        "id": "node",
        "name": "Node.js / Express / NestJS",
        "badge": "Full-Stack JavaScript Ecosystem",
        "tagline": "Event-driven, high-concurrency backend powered by the JavaScript/TypeScript runtime.",
        "icon": "terminal",
        "what_is": (
            "Node.js is an open-source, cross-platform JavaScript runtime environment that executes code outside "
            "a web browser. Using Express or NestJS (TypeScript enterprise framework), it allows developers to share "
            "code, schemas, and models seamlessly between the frontend and backend."
        ),
        "why_choose": [
            "Same language (JS/TS) across both client and server.",
            "Non-blocking event loop ideal for real-time WebSockets and instant messaging.",
            "Massive ecosystem of NPM packages and serverless compatibility."
        ],
        "best_for": "Real-time chat, collaborative apps, streaming, and full-stack TypeScript projects."
    }
}

SYSTEM_PROJECTS = [
    # --- DJANGO PROJECTS ---
    {
        "id": "django-ecommerce",
        "framework": "django",
        "name": "E-Commerce & Digital Marketplace",
        "scope": "Product catalog, multi-category navigation, cart, checkout, order tracking, admin stock control.",
        "prices": {"usd": 1200, "kes": 155820, "eur": 1069},
        "monthly": {"usd": 29, "kes": 3766, "eur": 26},
        "recommended_frontend": ["react", "nextjs", "django-templates"],
        "recommended_db": ["postgres", "mysql"]
    },
    {
        "id": "django-saas-mvp",
        "framework": "django",
        "name": "Multi-Tenant SaaS Foundation",
        "scope": "Tenant isolation, organization accounts, subscription tier limits, role permissions, billing portal.",
        "prices": {"usd": 1488, "kes": 193217, "eur": 1326},
        "monthly": {"usd": 27, "kes": 3506, "eur": 24},
        "recommended_frontend": ["react", "nextjs", "vue"],
        "recommended_db": ["postgres"]
    },
    {
        "id": "django-school-mgmt",
        "framework": "django",
        "name": "School & Campus Management System",
        "scope": "Student & teacher records, admissions, fee tracking, timetable, attendance, grade reporting portal.",
        "prices": {"usd": 1800, "kes": 233730, "eur": 1604},
        "monthly": {"usd": 38, "kes": 4934, "eur": 34},
        "recommended_frontend": ["react", "django-templates", "htmx"],
        "recommended_db": ["postgres"]
    },
    {
        "id": "django-clinic-mgmt",
        "framework": "django",
        "name": "Hospital & Clinic Administration System",
        "scope": "Patient health records, doctor appointments, diagnosis notes, triage, prescription & billing history.",
        "prices": {"usd": 2232, "kes": 289825, "eur": 1989},
        "monthly": {"usd": 44, "kes": 5713, "eur": 39},
        "recommended_frontend": ["react", "django-templates", "vue"],
        "recommended_db": ["postgres"]
    },
    {
        "id": "django-pos-inventory",
        "framework": "django",
        "name": "Point-of-Sale (POS) & Stock Inventory",
        "scope": "Barcode checkout, cash/MPesa tender, low-stock alerts, supplier reorders, shift reconciliation.",
        "prices": {"usd": 1776, "kes": 230614, "eur": 1583},
        "monthly": {"usd": 25, "kes": 3246, "eur": 22},
        "recommended_frontend": ["react", "vue", "django-templates"],
        "recommended_db": ["postgres", "mysql"]
    },
    {
        "id": "django-crm-portal",
        "framework": "django",
        "name": "Customer Relationship Management (CRM)",
        "scope": "Lead management pipeline, customer communications log, deal stages, tasks, automated email alerts.",
        "prices": {"usd": 2232, "kes": 289825, "eur": 1989},
        "monthly": {"usd": 41, "kes": 5324, "eur": 37},
        "recommended_frontend": ["react", "nextjs", "htmx"],
        "recommended_db": ["postgres"]
    },
    {
        "id": "django-property-mgmt",
        "framework": "django",
        "name": "Real Estate & Rental Management Portal",
        "scope": "Tenant onboarding, lease tracking, automated rent invoices, maintenance tickets, owner reporting.",
        "prices": {"usd": 2016, "kes": 261778, "eur": 1796},
        "monthly": {"usd": 44, "kes": 5713, "eur": 39},
        "recommended_frontend": ["react", "nextjs", "django-templates"],
        "recommended_db": ["postgres"]
    },
    {
        "id": "django-mobile-api",
        "framework": "django",
        "name": "Django REST API for Mobile Application",
        "scope": "DRF endpoints, JWT token authentication, push notification triggers, profile sync, media uploads.",
        "prices": {"usd": 1344, "kes": 174518, "eur": 1198},
        "monthly": {"usd": 27, "kes": 3506, "eur": 24},
        "recommended_frontend": ["flutter", "react-native"],
        "recommended_db": ["postgres"]
    },

    # --- FLASK PROJECTS ---
    {
        "id": "flask-business-web",
        "framework": "flask",
        "name": "Custom Corporate Website & Inquiry Engine",
        "scope": "High-speed multi-page corporate website, dynamic services showcase, contact dispatch with Brevo.",
        "prices": {"usd": 650, "kes": 84402, "eur": 579},
        "monthly": {"usd": 15, "kes": 1948, "eur": 13},
        "recommended_frontend": ["jinja2-vanilla", "htmx"],
        "recommended_db": ["sqlite", "postgres"]
    },
    {
        "id": "flask-rest-api",
        "framework": "flask",
        "name": "Flask High-Efficiency REST API Starter",
        "scope": "JWT security, modular blueprints, SQLAlchemy models, rate-limiting, JSON serialization.",
        "prices": {"usd": 728, "kes": 94531, "eur": 649},
        "monthly": {"usd": 16, "kes": 2078, "eur": 14},
        "recommended_frontend": ["react", "vue"],
        "recommended_db": ["postgres", "mysql"]
    },
    {
        "id": "flask-user-portal",
        "framework": "flask",
        "name": "Client Portal & Authentication Hub",
        "scope": "Secure login, password resets, session management, role protection, customer document downloads.",
        "prices": {"usd": 806, "kes": 104659, "eur": 718},
        "monthly": {"usd": 17, "kes": 2207, "eur": 15},
        "recommended_frontend": ["react", "jinja2-vanilla", "htmx"],
        "recommended_db": ["postgres"]
    },
    {
        "id": "flask-inventory-tracker",
        "framework": "flask",
        "name": "Lightweight Inventory & Asset Tracker",
        "scope": "Product SKU indexing, stock intake, audit logs, supplier list, CSV export and low stock notices.",
        "prices": {"usd": 884, "kes": 114787, "eur": 788},
        "monthly": {"usd": 18, "kes": 2337, "eur": 16},
        "recommended_frontend": ["vue", "htmx", "jinja2-vanilla"],
        "recommended_db": ["postgres", "sqlite"]
    },
    {
        "id": "flask-booking-system",
        "framework": "flask",
        "name": "Appointment Booking & Calendar Scheduler",
        "scope": "Service selection, calendar availability slots, client booking form, email confirmation dispatches.",
        "prices": {"usd": 962, "kes": 124916, "eur": 857},
        "monthly": {"usd": 15, "kes": 1948, "eur": 13},
        "recommended_frontend": ["react", "vue", "jinja2-vanilla"],
        "recommended_db": ["postgres"]
    },
    {
        "id": "flask-reporting-dash",
        "framework": "flask",
        "name": "Business Analytics & KPI Dashboard",
        "scope": "Data aggregation, interactive charts, date-range filters, Excel and PDF report downloads.",
        "prices": {"usd": 884, "kes": 114787, "eur": 788},
        "monthly": {"usd": 15, "kes": 1948, "eur": 13},
        "recommended_frontend": ["react", "vue"],
        "recommended_db": ["postgres", "clickhouse"]
    },

    # --- FASTAPI PROJECTS ---
    {
        "id": "fastapi-crud-service",
        "framework": "fastapi",
        "name": "High-Concurrency Async CRUD Microservice",
        "scope": "Async SQLAlchemy, Pydantic type schemas, OpenAPI documentation, automated unit tests.",
        "prices": {"usd": 950, "kes": 123358, "eur": 847},
        "monthly": {"usd": 20, "kes": 2597, "eur": 18},
        "recommended_frontend": ["react", "vue"],
        "recommended_db": ["postgres"]
    },
    {
        "id": "fastapi-ml-inference",
        "framework": "fastapi",
        "name": "Machine Learning & AI Inference API",
        "scope": "Scikit-Learn/PyTorch model loader, real-time predictions, batch endpoint, request validation.",
        "prices": {"usd": 1064, "kes": 138160, "eur": 948},
        "monthly": {"usd": 24, "kes": 3116, "eur": 21},
        "recommended_frontend": ["react", "nextjs"],
        "recommended_db": ["postgres", "redis"]
    },
    {
        "id": "fastapi-vector-rag",
        "framework": "fastapi",
        "name": "Semantic Vector Search & RAG Knowledge API",
        "scope": "Text embedding pipeline, pgvector or Qdrant search, LLM context synthesis, document QA.",
        "prices": {"usd": 1178, "kes": 152963, "eur": 1050},
        "monthly": {"usd": 26, "kes": 3376, "eur": 23},
        "recommended_frontend": ["react", "nextjs"],
        "recommended_db": ["pgvector", "qdrant"]
    },

    # --- NODE / EXPRESS PROJECTS ---
    {
        "id": "node-realtime-chat",
        "framework": "node",
        "name": "Real-Time Chat & Collaboration Backend",
        "scope": "Socket.io websockets, presence indicators, chat rooms, message persistence, file sharing.",
        "prices": {"usd": 1364, "kes": 177115, "eur": 1215},
        "monthly": {"usd": 29, "kes": 3766, "eur": 26},
        "recommended_frontend": ["react", "nextjs", "vue"],
        "recommended_db": ["postgres", "redis", "mongodb"]
    },
    {
        "id": "node-express-rest",
        "framework": "node",
        "name": "Express.js REST API Architecture",
        "scope": "JWT auth, express-validator, Prisma ORM, CORS, Winston logging, health monitoring.",
        "prices": {"usd": 1100, "kes": 142835, "eur": 980},
        "monthly": {"usd": 25, "kes": 3246, "eur": 22},
        "recommended_frontend": ["react", "nextjs", "vue"],
        "recommended_db": ["postgres", "mongodb"]
    }
]

FRONTEND_OPTIONS = [
    {
        "id": "react",
        "name": "React Single Page Application (SPA)",
        "badge": "Rich Interactivity",
        "desc": "Component-based, highly reactive UI with TanStack Query and state management.",
        "prices": {"usd": 400, "kes": 51940, "eur": 356}
    },
    {
        "id": "nextjs",
        "name": "Next.js (React + Server-Side Rendering)",
        "badge": "SEO & Performance",
        "desc": "Ultra-fast SSR and static optimization, best for public marketing + web applications.",
        "prices": {"usd": 550, "kes": 71418, "eur": 490}
    },
    {
        "id": "vue",
        "name": "Vue.js Business UI",
        "badge": "Clean & Intuitive",
        "desc": "Lightweight, responsive frontend with Pinia state management and modular views.",
        "prices": {"usd": 350, "kes": 45448, "eur": 312}
    },
    {
        "id": "htmx",
        "name": "HTMX + Modern CSS",
        "badge": "Lean & Lightning Fast",
        "desc": "Dynamic server-driven interactions without heavy client JS bundles. Super stable.",
        "prices": {"usd": 200, "kes": 25970, "eur": 178}
    },
    {
        "id": "django-templates",
        "name": "Native Server Templates (Django/Jinja)",
        "badge": "Built-In Baseline",
        "desc": "Clean HTML5, custom responsive CSS, minimal overhead, included in base build.",
        "prices": {"usd": 0, "kes": 0, "eur": 0}
    },
    {
        "id": "flutter",
        "name": "Flutter Cross-Platform Mobile App",
        "badge": "iOS & Android",
        "desc": "Single codebase compiled into native iOS and Android mobile applications.",
        "prices": {"usd": 900, "kes": 116865, "eur": 802}
    }
]

DATABASE_OPTIONS = [
    {
        "id": "postgres",
        "name": "PostgreSQL (Recommended)",
        "badge": "Enterprise Relational",
        "desc": "ACID compliance, schema constraints, JSONB support, row-level security and high reliability.",
        "prices": {"usd": 150, "kes": 19478, "eur": 134}
    },
    {
        "id": "mysql",
        "name": "MySQL / MariaDB",
        "badge": "Standard Relational",
        "desc": "High compatibility with standard hosting setups, reliable transactional storage.",
        "prices": {"usd": 120, "kes": 15582, "eur": 107}
    },
    {
        "id": "sqlite",
        "name": "SQLite (Local-First / Lightweight)",
        "badge": "Zero Configuration",
        "desc": "Self-contained serverless SQL database engine, included by default with no extra cost.",
        "prices": {"usd": 0, "kes": 0, "eur": 0}
    },
    {
        "id": "redis",
        "name": "Redis In-Memory Data Store",
        "badge": "Caching & Queues",
        "desc": "Lightning-fast caching, user session management, and rate-limiting queue layer.",
        "prices": {"usd": 180, "kes": 23373, "eur": 160}
    },
    {
        "id": "pgvector",
        "name": "pgvector / Vector Database",
        "badge": "AI & Semantic Search",
        "desc": "Vector embeddings storage for semantic similarity search and AI document retrieval.",
        "prices": {"usd": 250, "kes": 32463, "eur": 223}
    },
    {
        "id": "mongodb",
        "name": "MongoDB Document Store",
        "badge": "NoSQL / JSON",
        "desc": "Flexible document storage for unstructured catalogues, logs, and rapid schema shifts.",
        "prices": {"usd": 160, "kes": 20776, "eur": 143}
    }
]

ADDON_MODULES = [
    {
        "id": "payment-mpesa-stripe",
        "name": "Payment Gateway (M-Pesa / Stripe / Paystack)",
        "desc": "Automated STK push, callback validation, transaction logging, and receipt dispatch.",
        "prices": {"usd": 280, "kes": 36358, "eur": 249}
    },
    {
        "id": "brevo-email-sms",
        "name": "Transactional Email & SMS Integration (Brevo / Twilio)",
        "desc": "Automated order alerts, client welcomes, verification codes, and deliverability setup.",
        "prices": {"usd": 180, "kes": 23373, "eur": 160}
    },
    {
        "id": "celery-redis-workers",
        "name": "Asynchronous Task Workers (Celery + Redis)",
        "desc": "Non-blocking background jobs: PDF generation, scheduled emails, and long imports.",
        "prices": {"usd": 250, "kes": 32463, "eur": 223}
    },
    {
        "id": "mfa-rbac-security",
        "name": "Two-Factor Auth (MFA) & Role-Based Permissions",
        "desc": "Granular roles (Admin, Manager, Staff, Client), TOTP authentication, and audit trails.",
        "prices": {"usd": 240, "kes": 31164, "eur": 214}
    },
    {
        "id": "ai-rag-chatbot",
        "name": "AI Assistant & Curated Knowledge RAG Bot",
        "desc": "Interactive FAQ chatbot trained on your company files and documents with cited sources.",
        "prices": {"usd": 400, "kes": 51940, "eur": 356}
    },
    {
        "id": "excel-pdf-export",
        "name": "Automated PDF Invoices & Excel Data Exports",
        "desc": "One-click styled PDF invoices, receipts, and structured Excel reporting downloads.",
        "prices": {"usd": 150, "kes": 19478, "eur": 134}
    }
]

DEVOPS_OPTIONS = [
    {
        "id": "docker-full",
        "name": "Docker & Multi-Container Compose Setup",
        "badge": "Portability & Reliability",
        "desc": "Multi-stage Dockerfile, docker-compose orchestration (App + Postgres + Redis + Nginx).",
        "prices": {"usd": 200, "kes": 25970, "eur": 178}
    },
    {
        "id": "vps-nginx-ssl",
        "name": "Production Linux VPS Deployment & SSL Hardening",
        "badge": "Live Server Launch",
        "desc": "Ubuntu VPS setup, Nginx reverse proxy, automated Let's Encrypt SSL, UFW firewall & fail2ban.",
        "prices": {"usd": 250, "kes": 32463, "eur": 223}
    },
    {
        "id": "cicd-github-actions",
        "name": "CI/CD Pipeline (GitHub Actions Automation)",
        "badge": "Automated Deploy",
        "desc": "Automated test runs, linting checks, and seamless zero-downtime deployment on push.",
        "prices": {"usd": 180, "kes": 23373, "eur": 160}
    },
    {
        "id": "backup-disaster-recovery",
        "name": "Automated Daily Backups & Disaster Recovery",
        "badge": "Data Safety",
        "desc": "Automated encrypted database dumps sent to S3/Cloud storage with retention policy.",
        "prices": {"usd": 160, "kes": 20776, "eur": 143}
    }
]

PALETTES = [
    {"id": "p01", "name": "01 Ocean Professional", "primary": "#0B1F3A", "secondary": "#145DA0", "accent": "#2E8BC0", "soft": "#B1D4E0", "bg": "#F4F8FB", "mood": "Trustworthy Corporate"},
    {"id": "p02", "name": "02 Midnight Blue", "primary": "#0A192F", "secondary": "#172A45", "accent": "#64FFDA", "soft": "#8892B0", "bg": "#CCD6F6", "mood": "Developer Modern Dark"},
    {"id": "p03", "name": "03 Corporate Blue", "primary": "#16324F", "secondary": "#245B8F", "accent": "#4C9FCE", "soft": "#D7EAF5", "bg": "#F7FAFC", "mood": "Enterprise Clean"},
    {"id": "p04", "name": "04 Indigo SaaS", "primary": "#312E81", "secondary": "#4338CA", "accent": "#818CF8", "soft": "#C7D2FE", "bg": "#EEF2FF", "mood": "Modern SaaS Standard"},
    {"id": "p05", "name": "05 Purple Gradient", "primary": "#2E1065", "secondary": "#6D28D9", "accent": "#A78BFA", "soft": "#DDD6FE", "bg": "#FAF5FF", "mood": "Creative Tech"},
    {"id": "p06", "name": "06 Emerald Finance", "primary": "#064E3B", "secondary": "#047857", "accent": "#34D399", "soft": "#A7F3D0", "bg": "#ECFDF5", "mood": "Wealth & FinTech"},
    {"id": "p07", "name": "07 Forest Green", "primary": "#12372A", "secondary": "#436850", "accent": "#ADBC9F", "soft": "#FBFADA", "bg": "#F6F7F2", "mood": "Organic & Grounded"},
    {"id": "p08", "name": "08 Teal Modern", "primary": "#134E4A", "secondary": "#0F766E", "accent": "#2DD4BF", "soft": "#99F6E4", "bg": "#F0FDFA", "mood": "Fresh Medical & SaaS"},
    {"id": "p09", "name": "09 Mint Minimal", "primary": "#14532D", "secondary": "#16A34A", "accent": "#86EFAC", "soft": "#DCFCE7", "bg": "#F7FEF9", "mood": "Clean & Crisp"},
    {"id": "p10", "name": "10 Lime Energy", "primary": "#365314", "secondary": "#4D7C0F", "accent": "#A3E635", "soft": "#D9F99D", "bg": "#F7FEE7", "mood": "Vibrant High-Energy"},
    {"id": "p11", "name": "11 Warm Neutral", "primary": "#292524", "secondary": "#57534E", "accent": "#A8A29E", "soft": "#E7E5E4", "bg": "#FAFAF9", "mood": "Architectural Minimal"},
    {"id": "p12", "name": "12 Sandstone", "primary": "#5C4033", "secondary": "#A47148", "accent": "#D8B08C", "soft": "#EAD7C3", "bg": "#FFF9F1", "mood": "Warm Craft"},
    {"id": "p13", "name": "13 Terracotta", "primary": "#7C2D12", "secondary": "#C2410C", "accent": "#FB923C", "soft": "#FED7AA", "bg": "#FFF7ED", "mood": "Artisanal Warmth"},
    {"id": "p14", "name": "14 Sunset", "primary": "#7F1D1D", "secondary": "#DC2626", "accent": "#FB923C", "soft": "#FDE68A", "bg": "#FFFBEB", "mood": "Bold Evening Glow"},
    {"id": "p15", "name": "15 Coral Pop", "primary": "#7F1D1D", "secondary": "#E11D48", "accent": "#FB7185", "soft": "#FECDD3", "bg": "#FFF1F2", "mood": "Playful Consumer"},
    {"id": "p16", "name": "16 Rose Elegance", "primary": "#881337", "secondary": "#BE185D", "accent": "#F472B6", "soft": "#FBCFE8", "bg": "#FDF2F8", "mood": "Luxury Boutique"},
    {"id": "p17", "name": "17 Burgundy Luxury", "primary": "#450A0A", "secondary": "#7F1D1D", "accent": "#B45309", "soft": "#FDE68A", "bg": "#FFFBF5", "mood": "Opulent Premium"},
    {"id": "p18", "name": "18 Gold and Charcoal", "primary": "#18181B", "secondary": "#3F3F46", "accent": "#CA8A04", "soft": "#FDE68A", "bg": "#FAFAF9", "mood": "Exclusive Executive"},
    {"id": "p19", "name": "19 Monochrome", "primary": "#111827", "secondary": "#374151", "accent": "#6B7280", "soft": "#D1D5DB", "bg": "#F9FAFB", "mood": "Timeless Minimalist"},
    {"id": "p20", "name": "20 Slate Dashboard", "primary": "#0F172A", "secondary": "#334155", "accent": "#64748B", "soft": "#CBD5E1", "bg": "#F8FAFC", "mood": "Data Analytic Standard"},
    {"id": "p21", "name": "21 Cyber Neon", "primary": "#09090B", "secondary": "#27272A", "accent": "#22D3EE", "soft": "#E879F9", "bg": "#FAFAFA", "mood": "Futuristic Cyberpunk"},
    {"id": "p22", "name": "22 Dark Terminal", "primary": "#071A0B", "secondary": "#153E20", "accent": "#4ADE80", "soft": "#86EFAC", "bg": "#D1FAE5", "mood": "Hacker Matrix Clean"},
    {"id": "p23", "name": "23 Black and Amber", "primary": "#111111", "secondary": "#292524", "accent": "#F59E0B", "soft": "#FDE68A", "bg": "#FFFDF5", "mood": "Industrial Contrast"},
    {"id": "p24", "name": "24 Arctic", "primary": "#164E63", "secondary": "#0891B2", "accent": "#67E8F9", "soft": "#CFFAFE", "bg": "#F0FDFF", "mood": "Cool & Analytical"},
    {"id": "p25", "name": "25 Sky Light", "primary": "#075985", "secondary": "#0284C7", "accent": "#38BDF8", "soft": "#BAE6FD", "bg": "#F0F9FF", "mood": "Open Cloud Air"},
    {"id": "p26", "name": "26 Ocean Sunset", "primary": "#164E63", "secondary": "#0E7490", "accent": "#F97316", "soft": "#FDBA74", "bg": "#FFF7ED", "mood": "Warm Oceanic"},
    {"id": "p27", "name": "27 Lavender Calm", "primary": "#4C1D95", "secondary": "#7C3AED", "accent": "#C4B5FD", "soft": "#EDE9FE", "bg": "#FAF5FF", "mood": "Soothing Wellness"},
    {"id": "p28", "name": "28 Soft Pastel", "primary": "#64748B", "secondary": "#A5B4FC", "accent": "#FBCFE8", "soft": "#FDE68A", "bg": "#FFFBF5", "mood": "Gentle Friendly"},
    {"id": "p29", "name": "29 Cream and Olive", "primary": "#3F3D2E", "secondary": "#6B705C", "accent": "#A5A58D", "soft": "#FFE8D6", "bg": "#FFFDF8", "mood": "Nordic Ceramic"},
    {"id": "p30", "name": "30 Sage Wellness", "primary": "#344E41", "secondary": "#588157", "accent": "#A3B18A", "soft": "#DAD7CD", "bg": "#F6F7F2", "mood": "Holistic Health"},
    {"id": "p31", "name": "31 Medical Clean", "primary": "#134E4A", "secondary": "#0D9488", "accent": "#5EEAD4", "soft": "#CCFBF1", "bg": "#F0FDFA", "mood": "Clinical Precision"},
    {"id": "p32", "name": "32 Healthcare Blue", "primary": "#1E3A8A", "secondary": "#2563EB", "accent": "#60A5FA", "soft": "#DBEAFE", "bg": "#EFF6FF", "mood": "Hospital Integrity"},
    {"id": "p33", "name": "33 Education Bright", "primary": "#1D4ED8", "secondary": "#F97316", "accent": "#FACC15", "soft": "#BFDBFE", "bg": "#FFFBEB", "mood": "Campus Scholastic"},
    {"id": "p34", "name": "34 Playful Product", "primary": "#4338CA", "secondary": "#EC4899", "accent": "#F59E0B", "soft": "#A7F3D0", "bg": "#FFF7ED", "mood": "Vibrant App Launch"},
    {"id": "p35", "name": "35 African Earth", "primary": "#3E2723", "secondary": "#795548", "accent": "#C17F3A", "soft": "#E5C07B", "bg": "#FFF8E7", "mood": "Rich Heritage"},
    {"id": "p36", "name": "36 Kenyan Flag Inspired", "primary": "#111827", "secondary": "#B91C1C", "accent": "#15803D", "soft": "#D1D5DB", "bg": "#FFFFFF", "mood": "Patriotic & Striking"},
    {"id": "p37", "name": "37 Royal Blue and Gold", "primary": "#172554", "secondary": "#1D4ED8", "accent": "#D4A72C", "soft": "#FDE68A", "bg": "#F8FAFC", "mood": "Prestigious Crown"},
    {"id": "p38", "name": "38 Startup Violet", "primary": "#2E1065", "secondary": "#7C3AED", "accent": "#EC4899", "soft": "#F5D0FE", "bg": "#FDF4FF", "mood": "Venture Tech High-Growth"},
    {"id": "p39", "name": "39 High Contrast Accessible", "primary": "#000000", "secondary": "#1D4ED8", "accent": "#FACC15", "soft": "#E5E7EB", "bg": "#F3F4F6", "mood": "WCAG AAA Accessible"},
    {"id": "p40", "name": "40 Minimal Green SaaS", "primary": "#14532D", "secondary": "#15803D", "accent": "#4ADE80", "soft": "#BBF7D0", "bg": "#F0FDF4", "mood": "Sustainable Growth"}
]

UI_STYLING_TIERS = [
    {
        "id": "theme-standard",
        "name": "Standard Palette Application",
        "desc": "Application of the selected 5-color palette to all headers, buttons, accents, and surfaces.",
        "prices": {"usd": 0, "kes": 0, "eur": 0}
    },
    {
        "id": "theme-custom-design-system",
        "name": "Custom UI Design System & Micro-Animations",
        "desc": "Tailored typography tokens, custom glassmorphism effects, responsive mobile nav & micro-interactions.",
        "prices": {"usd": 250, "kes": 32463, "eur": 223}
    },
    {
        "id": "theme-accessible-audit",
        "name": "WCAG Accessibility & High-Contrast Compliance",
        "desc": "Screen reader aria attributes, color contrast testing, keyboard navigation focus rings.",
        "prices": {"usd": 150, "kes": 19478, "eur": 134}
    }
]
