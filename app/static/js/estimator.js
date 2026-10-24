/**
 * Estimator Engine
 * Handles interactive selection, live filtering of projects by framework,
 * real-time multi-currency calculation (KES, USD, EUR), live palette swatch preview,
 * and automatic specification prefill into contact form.
 */

document.addEventListener('DOMContentLoaded', () => {
    // State
    const state = {
        currency: 'KES', // Default is KES
        rates: {
            KES: 129.85,
            USD: 1.0,
            EUR: 0.8911
        },
        symbols: {
            KES: 'KSh ',
            USD: '$',
            EUR: '€'
        },
        framework: 'django',
        project: null,
        frontend: null,
        database: null,
        addons: [],
        palette: null,
        uiTier: null,
        devops: []
    };

    // DOM Elements
    const currencyPills = document.querySelectorAll('.currency-pill');
    const summaryCurrencySelect = document.getElementById('summaryCurrencySelect');
    const frameworkCards = document.querySelectorAll('.framework-card');
    const activeFrameworkLabel = document.getElementById('activeFrameworkLabel');
    const projectsGrid = document.getElementById('projectsGrid');
    const frontendCards = document.querySelectorAll('#frontendGrid .option-pill-card');
    const databaseCards = document.querySelectorAll('#databaseGrid .option-pill-card');
    const addonCheckboxes = document.querySelectorAll('.addon-input');
    const tierCards = document.querySelectorAll('.tier-card');
    const paletteCards = document.querySelectorAll('.palette-swatch-card');
    const devopsCheckboxes = document.querySelectorAll('.devops-input');

    // Summary Elements
    const sumBackend = document.getElementById('sumBackend');
    const sumProject = document.getElementById('sumProject');
    const sumFrontend = document.getElementById('sumFrontend');
    const sumDatabase = document.getElementById('sumDatabase');
    const sumPalette = document.getElementById('sumPalette');
    const sumAddonsCount = document.getElementById('sumAddonsCount');
    const sumDevopsCount = document.getElementById('sumDevopsCount');
    const grandTotalBuild = document.getElementById('grandTotalBuild');
    const grandTotalMonthly = document.getElementById('grandTotalMonthly');
    const btnRequestQuote = document.getElementById('btnRequestQuote');

    // Palette Banner Elements
    const bannerColorBar = document.getElementById('bannerColorBar');
    const bannerPaletteName = document.getElementById('bannerPaletteName');
    const bannerPaletteMood = document.getElementById('bannerPaletteMood');

    // Format Number with commas
    function formatNumber(num) {
        return Math.round(num).toLocaleString('en-US');
    }

    // Format Currency
    function formatMoney(amountKes, amountUsd, amountEur) {
        if (state.currency === 'KES') {
            return 'KSh ' + formatNumber(amountKes);
        } else if (state.currency === 'USD') {
            return '$' + formatNumber(amountUsd);
        } else {
            return '€' + formatNumber(amountEur);
        }
    }

    // Set Currency
    function setCurrency(curr) {
        if (!['KES', 'USD', 'EUR'].includes(curr)) return;
        state.currency = curr;

        // Sync pills
        currencyPills.forEach(p => {
            if (p.dataset.curr === curr) {
                p.classList.add('active');
            } else {
                p.classList.remove('active');
            }
        });

        // Sync summary select
        if (summaryCurrencySelect) {
            summaryCurrencySelect.value = curr;
        }

        // Update all price badges in the page
        document.querySelectorAll('[data-kes]').forEach(el => {
            const attrName = 'data-' + curr.toLowerCase();
            if (el.getAttribute(attrName)) {
                el.textContent = el.getAttribute(attrName);
            }
        });

        recalculateTotal();
    }

    // Currency Switcher Listeners
    currencyPills.forEach(pill => {
        pill.addEventListener('click', () => {
            setCurrency(pill.dataset.curr);
        });
    });

    if (summaryCurrencySelect) {
        summaryCurrencySelect.addEventListener('change', (e) => {
            setCurrency(e.target.value);
        });
    }

    // Step Wizard Switcher: Show one step at a time!
    function goToStep(stepId) {
        const targetCard = document.getElementById(stepId);
        if (!targetCard) return;

        // Hide all step cards, show the target step card
        document.querySelectorAll('.step-card').forEach(card => {
            card.classList.remove('active-step');
        });
        targetCard.classList.add('active-step');

        // Update top stepper indicators
        document.querySelectorAll('.step-item[data-step-target]').forEach(item => {
            if (item.dataset.stepTarget === stepId) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });

        // Scroll cleanly to the step top
        const estimatorSection = document.querySelector('.estimator-section');
        if (estimatorSection) {
            estimatorSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    // Top Stepper Navigation - Click directly to jump to any step
    const stepperItems = document.querySelectorAll('.step-item[data-step-target]');
    stepperItems.forEach(item => {
        item.addEventListener('click', () => {
            goToStep(item.dataset.stepTarget);
        });
    });

    // Next / Previous Step Buttons
    document.addEventListener('click', (e) => {
        const nextBtn = e.target.closest('[data-next-step]');
        if (nextBtn) {
            goToStep(nextBtn.dataset.nextStep);
            return;
        }

        const prevBtn = e.target.closest('[data-prev-step]');
        if (prevBtn) {
            goToStep(prevBtn.dataset.prevStep);
            return;
        }

        const submitBtn = e.target.closest('#btnStep6Submit');
        if (submitBtn) {
            if (btnRequestQuote) btnRequestQuote.click();
            return;
        }
    });

    // Step 1: Framework Selection
    frameworkCards.forEach(card => {
        card.addEventListener('click', () => {
            frameworkCards.forEach(c => {
                c.classList.remove('selected');
                const btn = c.querySelector('.select-fw-btn');
                if (btn) btn.textContent = 'Select ' + c.dataset.framework.toUpperCase();
            });
            card.classList.add('selected');
            const btn = card.querySelector('.select-fw-btn');
            if (btn) btn.textContent = 'Selected Backend';

            state.framework = card.dataset.framework;
            const fwTitle = card.querySelector('.framework-name').textContent.split('/')[0].trim();
            if (activeFrameworkLabel) {
                activeFrameworkLabel.textContent = fwTitle;
            }
            if (sumBackend) {
                sumBackend.textContent = fwTitle;
            }

            filterProjectsByFramework(state.framework);
            recalculateTotal();

            // Seamlessly take user directly to Step 2!
            setTimeout(() => {
                goToStep('step2');
            }, 180);
        });
    });

    // Step 2: Filter Projects by Framework
    function filterProjectsByFramework(fwId) {
        const allProjectCards = projectsGrid.querySelectorAll('.project-option-card');
        let firstVisible = null;

        allProjectCards.forEach(card => {
            if (card.dataset.framework === fwId) {
                card.style.display = 'block';
                if (!firstVisible) firstVisible = card;
            } else {
                card.style.display = 'none';
            }
        });

        // Select first visible project if current selected project is hidden
        if (firstVisible) {
            selectProject(firstVisible);
        }
    }

    // Select Project
    function selectProject(card) {
        const allProjectCards = projectsGrid.querySelectorAll('.project-option-card');
        allProjectCards.forEach(c => c.classList.remove('active'));
        card.classList.add('active');

        state.project = {
            id: card.dataset.id,
            name: card.dataset.name,
            priceKes: parseFloat(card.dataset.priceKes),
            priceUsd: parseFloat(card.dataset.priceUsd),
            priceEur: parseFloat(card.dataset.priceEur),
            monthlyKes: parseFloat(card.dataset.monthlyKes) || 0,
            monthlyUsd: parseFloat(card.dataset.monthlyUsd) || 0,
            monthlyEur: parseFloat(card.dataset.monthlyEur) || 0
        };

        if (sumProject) {
            sumProject.textContent = state.project.name;
        }

        recalculateTotal();
    }

    // Project Option Card Clicks
    projectsGrid.addEventListener('click', (e) => {
        const card = e.target.closest('.project-option-card');
        if (card) {
            selectProject(card);
        }
    });

    // Step 3A: Frontend Option Clicks
    frontendCards.forEach(card => {
        card.addEventListener('click', () => {
            frontendCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');

            state.frontend = {
                id: card.dataset.id,
                name: card.dataset.name,
                priceKes: parseFloat(card.dataset.priceKes),
                priceUsd: parseFloat(card.dataset.priceUsd),
                priceEur: parseFloat(card.dataset.priceEur)
            };

            if (sumFrontend) {
                sumFrontend.textContent = state.frontend.name.split('(')[0].trim();
            }

            recalculateTotal();
        });
    });

    // Step 3B: Database Option Clicks
    databaseCards.forEach(card => {
        card.addEventListener('click', () => {
            databaseCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');

            state.database = {
                id: card.dataset.id,
                name: card.dataset.name,
                priceKes: parseFloat(card.dataset.priceKes),
                priceUsd: parseFloat(card.dataset.priceUsd),
                priceEur: parseFloat(card.dataset.priceEur)
            };

            if (sumDatabase) {
                sumDatabase.textContent = state.database.name.split('(')[0].trim();
            }

            recalculateTotal();
        });
    });

    // Step 4: Add-on Checkboxes
    addonCheckboxes.forEach(chk => {
        chk.addEventListener('change', () => {
            updateAddonsState();
            recalculateTotal();
        });
    });

    function updateAddonsState() {
        state.addons = [];
        addonCheckboxes.forEach(chk => {
            if (chk.checked) {
                state.addons.push({
                    id: chk.dataset.id,
                    name: chk.dataset.name,
                    priceKes: parseFloat(chk.dataset.priceKes),
                    priceUsd: parseFloat(chk.dataset.priceUsd),
                    priceEur: parseFloat(chk.dataset.priceEur)
                });
            }
        });

        if (sumAddonsCount) {
            sumAddonsCount.textContent = state.addons.length === 0 ? 'None' : `${state.addons.length} selected`;
        }
    }

    // Step 5: UI Styling Tier Clicks
    tierCards.forEach(card => {
        card.addEventListener('click', () => {
            tierCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');

            state.uiTier = {
                id: card.dataset.id,
                name: card.dataset.name,
                priceKes: parseFloat(card.dataset.priceKes),
                priceUsd: parseFloat(card.dataset.priceUsd),
                priceEur: parseFloat(card.dataset.priceEur)
            };

            recalculateTotal();
        });
    });

    // Step 5: Palette Selection & Live Swatch Tinting
    paletteCards.forEach(card => {
        card.addEventListener('click', () => {
            paletteCards.forEach(c => c.classList.remove('selected'));
            card.classList.add('selected');

            state.palette = {
                id: card.dataset.id,
                name: card.dataset.name,
                mood: card.dataset.mood,
                primary: card.dataset.primary,
                secondary: card.dataset.secondary,
                accent: card.dataset.accent,
                soft: card.dataset.soft,
                bg: card.dataset.bg
            };

            // Update Preview Banner
            if (bannerPaletteName) bannerPaletteName.textContent = state.palette.name;
            if (bannerPaletteMood) bannerPaletteMood.textContent = state.palette.mood;
            if (sumPalette) sumPalette.textContent = state.palette.name;

            if (bannerColorBar) {
                bannerColorBar.querySelector('.c-primary').style.backgroundColor = state.palette.primary;
                bannerColorBar.querySelector('.c-secondary').style.backgroundColor = state.palette.secondary;
                bannerColorBar.querySelector('.c-accent').style.backgroundColor = state.palette.accent;
                bannerColorBar.querySelector('.c-soft').style.backgroundColor = state.palette.soft;
                bannerColorBar.querySelector('.c-bg').style.backgroundColor = state.palette.bg;
            }
        });
    });

    // Step 6: DevOps Checkboxes
    devopsCheckboxes.forEach(chk => {
        chk.addEventListener('change', () => {
            updateDevopsState();
            recalculateTotal();
        });
    });

    function updateDevopsState() {
        state.devops = [];
        devopsCheckboxes.forEach(chk => {
            if (chk.checked) {
                state.devops.push({
                    id: chk.dataset.id,
                    name: chk.dataset.name,
                    priceKes: parseFloat(chk.dataset.priceKes),
                    priceUsd: parseFloat(chk.dataset.priceUsd),
                    priceEur: parseFloat(chk.dataset.priceEur)
                });
            }
        });

        if (sumDevopsCount) {
            sumDevopsCount.textContent = state.devops.length === 0 ? 'None' : `${state.devops.length} package(s)`;
        }
    }

    // Master Recalculate Function
    function recalculateTotal() {
        let totalKes = 0;
        let totalUsd = 0;
        let totalEur = 0;

        let monthlyKes = 0;
        let monthlyUsd = 0;
        let monthlyEur = 0;

        // Base Project
        if (state.project) {
            totalKes += state.project.priceKes;
            totalUsd += state.project.priceUsd;
            totalEur += state.project.priceEur;

            monthlyKes += state.project.monthlyKes;
            monthlyUsd += state.project.monthlyUsd;
            monthlyEur += state.project.monthlyEur;
        }

        // Frontend
        if (state.frontend) {
            totalKes += state.frontend.priceKes;
            totalUsd += state.frontend.priceUsd;
            totalEur += state.frontend.priceEur;
        }

        // Database
        if (state.database) {
            totalKes += state.database.priceKes;
            totalUsd += state.database.priceUsd;
            totalEur += state.database.priceEur;
        }

        // Add-ons
        state.addons.forEach(a => {
            totalKes += a.priceKes;
            totalUsd += a.priceUsd;
            totalEur += a.priceEur;
        });

        // UI Tier
        if (state.uiTier) {
            totalKes += state.uiTier.priceKes;
            totalUsd += state.uiTier.priceUsd;
            totalEur += state.uiTier.priceEur;
        }

        // DevOps
        state.devops.forEach(d => {
            totalKes += d.priceKes;
            totalUsd += d.priceUsd;
            totalEur += d.priceEur;
        });

        // Render Grand Totals
        if (grandTotalBuild) {
            grandTotalBuild.textContent = formatMoney(totalKes, totalUsd, totalEur);
        }

        if (grandTotalMonthly) {
            grandTotalMonthly.textContent = formatMoney(monthlyKes, monthlyUsd, monthlyEur) + ' / mo';
        }
    }

    // Initialize Default Selections
    function initDefaults() {
        // Set initial frontend
        const activeFe = document.querySelector('#frontendGrid .option-pill-card.selected') || frontendCards[0];
        if (activeFe) {
            state.frontend = {
                id: activeFe.dataset.id,
                name: activeFe.dataset.name,
                priceKes: parseFloat(activeFe.dataset.priceKes),
                priceUsd: parseFloat(activeFe.dataset.priceUsd),
                priceEur: parseFloat(activeFe.dataset.priceEur)
            };
        }

        // Set initial database
        const activeDb = document.querySelector('#databaseGrid .option-pill-card.selected') || databaseCards[0];
        if (activeDb) {
            state.database = {
                id: activeDb.dataset.id,
                name: activeDb.dataset.name,
                priceKes: parseFloat(activeDb.dataset.priceKes),
                priceUsd: parseFloat(activeDb.dataset.priceUsd),
                priceEur: parseFloat(activeDb.dataset.priceEur)
            };
        }

        // Set initial UI tier
        const activeTier = document.querySelector('.tier-card.selected') || tierCards[0];
        if (activeTier) {
            state.uiTier = {
                id: activeTier.dataset.id,
                name: activeTier.dataset.name,
                priceKes: parseFloat(activeTier.dataset.priceKes),
                priceUsd: parseFloat(activeTier.dataset.priceUsd),
                priceEur: parseFloat(activeTier.dataset.priceEur)
            };
        }

        // Set initial palette
        const activePal = document.querySelector('.palette-swatch-card.selected') || paletteCards[0];
        if (activePal) {
            state.palette = {
                id: activePal.dataset.id,
                name: activePal.dataset.name,
                mood: activePal.dataset.mood,
                primary: activePal.dataset.primary,
                secondary: activePal.dataset.secondary,
                accent: activePal.dataset.accent,
                soft: activePal.dataset.soft,
                bg: activePal.dataset.bg
            };
            if (bannerColorBar) {
                bannerColorBar.querySelector('.c-primary').style.backgroundColor = state.palette.primary;
                bannerColorBar.querySelector('.c-secondary').style.backgroundColor = state.palette.secondary;
                bannerColorBar.querySelector('.c-accent').style.backgroundColor = state.palette.accent;
                bannerColorBar.querySelector('.c-soft').style.backgroundColor = state.palette.soft;
                bannerColorBar.querySelector('.c-bg').style.backgroundColor = state.palette.bg;
            }
        }

        // Initialize swatch circles from data-color
        document.querySelectorAll('.swatch-circle[data-color]').forEach(circle => {
            circle.style.backgroundColor = circle.dataset.color;
        });

        updateAddonsState();
        updateDevopsState();
        filterProjectsByFramework(state.framework);
        setCurrency('KES'); // Default to Kenyan Shillings
    }

    initDefaults();

    // Request Quote Handler - Generate structured specification and send to /contact
    if (btnRequestQuote) {
        btnRequestQuote.addEventListener('click', () => {
            const specLines = [
                `Hi Laban, I configured a custom project estimate via your portfolio pricing calculator:`,
                ``,
                `--- [PROJECT SPECIFICATION] ---`,
                `• Core Backend: ${state.framework.toUpperCase()}`,
                `• System/Deliverable: ${state.project ? state.project.name : 'Not selected'}`,
                `• Frontend Framework: ${state.frontend ? state.frontend.name : 'Default'}`,
                `• Database & Storage: ${state.database ? state.database.name : 'Default'}`,
                `• UI Color Theme: ${state.palette ? state.palette.name + ' (' + state.palette.mood + ')' : 'Default'}`,
                `• Styling Engineering: ${state.uiTier ? state.uiTier.name : 'Standard'}`,
                `• DevOps & Deployment: ${state.devops.length > 0 ? state.devops.map(d => d.name).join(', ') : 'None'}`,
                `• Selected Add-ons: ${state.addons.length > 0 ? state.addons.map(a => a.name).join(', ') : 'None'}`,
                ``,
                `• Estimated One-Time Build: ${grandTotalBuild.textContent}`,
                `• Estimated Monthly Service/Maintenance: ${grandTotalMonthly.textContent}`,
                `-------------------------------`,
                ``,
                `Please let me know your availability for a kick-off discussion!`
            ];

            const messageText = encodeURIComponent(specLines.join('\n'));
            window.location.href = `/contact?spec=${messageText}`;
        });
    }
});
