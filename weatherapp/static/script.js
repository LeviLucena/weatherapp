// Enhanced JavaScript for Weather App

document.addEventListener('DOMContentLoaded', function() {
    const estadoSelect = document.getElementById('estado');
    const municipioSelect = document.getElementById('municipio');
    const form = document.querySelector('form');

    // Add loading state to form submission
    form.addEventListener('submit', function() {
        const submitBtn = document.querySelector('.btn-submit');
        submitBtn.innerHTML = '<i class="bi bi-arrow-repeat spinner-icon"></i> Carregando...';
        submitBtn.disabled = true;
    });

    // Handle state selection change
    estadoSelect.addEventListener('change', function () {
        const codigoUf = this.value;
        
        if (!codigoUf) {
            municipioSelect.innerHTML = '<option value="" disabled selected>Selecione um município</option>';
            return;
        }

        municipioSelect.innerHTML = '<option disabled selected>Carregando...</option>';
        municipioSelect.disabled = true;

        fetch(`/municipios/${codigoUf}`)
            .then(response => response.json())
            .then(data => {
                municipioSelect.innerHTML = '<option value="" disabled selected>Selecione um município</option>';
                data.forEach(municipio => {
                    const option = document.createElement('option');
                    option.value = municipio;
                    option.textContent = municipio;
                    municipioSelect.appendChild(option);
                });
                municipioSelect.disabled = false;
            })
            .catch(error => {
                console.error('Erro ao carregar municípios:', error);
                municipioSelect.innerHTML = '<option disabled selected>Erro ao carregar municípios</option>';
                municipioSelect.disabled = false;
            });
    });

    // Initialize with selected state if exists
    if (estadoSelect.value) {
        estadoSelect.dispatchEvent(new Event('change'));
    }

    // Add animation to cards when they appear
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 150 * index);
    });

    // Add hover effect to forecast cards
    const forecastCards = document.querySelectorAll('.forecast-card');
    forecastCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.03)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
});

// Add spinner animation for loading states
const style = document.createElement('style');
style.textContent = `
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .spinner-icon {
        animation: spin 1s linear infinite;
        display: inline-block;
    }
`;
document.head.appendChild(style);