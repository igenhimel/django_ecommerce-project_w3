setTimeout(function() {
    var alertElement = document.getElementById('auto-hide-alert');
    if (alertElement) {
    alertElement.classList.remove('show');
    alertElement.style.display = 'none';
    }
}, 2000);