(() => {
const themeToggle = document.getElementById('theme-toggle');
const html = document.documentElement;
const en = html.lang === 'en';
const dataLabels = {
    'Recibido': 'Received', 'Diagnosticado': 'Diagnosed',
    'Presupuesto enviado': 'Estimate sent', 'Presupuesto aceptado': 'Estimate accepted',
    'Reparando': 'Repairing', 'Esperando pieza': 'Waiting for part',
    'Listo': 'Ready', 'Entregado': 'Delivered',
    'Móvil': 'Mobile phone', 'Portátil': 'Laptop', 'Sobremesa': 'Desktop computer',
    'Ordenador': 'Desktop computer', 'Consola': 'Console', 'Otro': 'Other',
};
window.openRepairTranslate = value => en ? (dataLabels[value] || value) : value;

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        const current = html.getAttribute('data-theme');
        const next = current === 'light' ? 'dark' : 'light';
        html.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
    });
}

const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('nav-links');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
        });
    });
}

const formNuevaEntrada = document.querySelector('.form-nueva-entrada');
if (formNuevaEntrada) {
    formNuevaEntrada.addEventListener('submit', (e) => {
        const telefono = document.getElementById('telefono').value.trim();
        const email = document.getElementById('email').value.trim();

        if (!telefono && !email) {
            e.preventDefault();
            alert(en ? 'Enter at least one contact detail (phone or email).' : 'Indica al menos un dato de contacto (teléfono o email).');
        }
    });
}

const telefonoInput = document.getElementById('telefono');
const nombreInput = document.getElementById('nombre');
const emailInput = document.getElementById('email');

if (telefonoInput) {
    let timeout;
    telefonoInput.addEventListener('input', () => {
        clearTimeout(timeout);
        const q = telefonoInput.value.trim();
        if (q.length < 3) return;

        timeout = setTimeout(() => {
            fetch(`/api/buscar-cliente?q=${encodeURIComponent(q)}`)
                .then(res => res.json())
                .then(data => {
                    if (data.length > 0) {
                        const c = data[0];
                        if (nombreInput) nombreInput.value = c.nombre;
                        if (emailInput && c.email) emailInput.value = c.email;
                    }
                });
        }, 300);
    });
}
})();
