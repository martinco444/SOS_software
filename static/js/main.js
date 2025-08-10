// Scripts personalizados para SOS Software

document.addEventListener('DOMContentLoaded', function() {
    console.log('SOS Software - Documento cargado');
    
    // Inicializar tooltips de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Inicializar popovers de Bootstrap
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
    
    // Ejemplo de función personalizada
    function saludar() {
        console.log('¡Bienvenido a SOS Software!');
    }
    
    // Llamar a la función de ejemplo
    saludar();
    
    // Ejemplo de manejo de eventos
    document.querySelectorAll('.nav-link').forEach(function(link) {
        link.addEventListener('click', function(e) {
            // Remover la clase active de todos los enlaces
            document.querySelectorAll('.nav-link').forEach(function(el) {
                el.classList.remove('active');
                el.removeAttribute('aria-current');
            });
            
            // Agregar la clase active al enlace clickeado
            this.classList.add('active');
            this.setAttribute('aria-current', 'page');
        });
    });
});