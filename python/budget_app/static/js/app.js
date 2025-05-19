// RetroCouple Budget App JavaScript

// Automatically update copyright year
document.addEventListener('DOMContentLoaded', function() {
    // Update current year in footer
    const footerYear = document.querySelector('footer p');
    if (footerYear) {
        const currentYear = new Date().getFullYear();
        footerYear.textContent = footerYear.textContent.replace('{{ now.year }}', currentYear);
    }
});
