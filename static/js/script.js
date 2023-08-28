var alertElement = document.getElementById('auto-hide-alert');

if (alertElement) {
    setTimeout(function () {
        alertElement.classList.remove('show');
        alertElement.style.display = 'none';
    }, 2000);
}