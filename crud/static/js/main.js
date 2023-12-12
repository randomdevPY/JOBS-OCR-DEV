(async function() {
    const sContent = document.querySelectorAll('.devops-ar span');
    const pElement = document.querySelector('.devops-ar');

    await new Promise((resolve) => {
        sContent.forEach((span, i) => {
            setTimeout(() => {
                span.style.color = '#75aadb';
                if (i !== sContent.length - 1) {
                    setTimeout(() => {
                        span.style.color = 'initial';
                    }, 350);
                }
                if (i === sContent.length - 1) {
                    resolve();
                }
            }, i * 350);
        });
    });

    pElement.classList.add('animate__animated', 'animate__pulse');
})();