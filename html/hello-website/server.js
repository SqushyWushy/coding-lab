const express = require('express');
const app  = express();
const PORT = 3000;

app.use(express.static('.'));
app.use(express.json());

const emails = [];

app.post('/submit-email', (req, res) => {
    const email = req.body.email;
    if (!email) {
        return res.status(400).json({ message: "No email received." });
    }

    emails.push(email);
    console.log("New email:", email);
    res.json({ message: "Thanks! Your email was received."});
});

app.listen(PORT, () => {
    console.log(`Backend is running at http://localhost:${PORT}`);
});

