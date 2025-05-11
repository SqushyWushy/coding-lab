function handleClick() {
    alert("You clicked the button!");
}

function submitEmail() {
    const emailInput = document.getElementById('email-input');
    const responseMessage = document.getElementById('response-message');

    fetch('/submit-email',  {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: emailInput.value })
    })
    .then(res => res.json())
    .then(data => {
        responseMessage.textContent = data.message;
        emailInput.value = '';
    })
    .catch(() => {
        responseMessage.textContent = "Something went wrong.";
    });
}
