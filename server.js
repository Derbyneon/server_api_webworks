const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();

app.use(bodyParser.json());

app.post('/subscribe', (req, res) => {
    const email = req.body.email;

    // Lire les emails existants dans le fichier JSON
    let emails = [];
    if (fs.existsSync('emails.json')) {
        const data = fs.readFileSync('emails.json');
        emails = JSON.parse(data);
    }

    // Ajouter le nouvel email
    emails.push({ email });

    // Sauvegarder les emails dans le fichier JSON
    fs.writeFileSync('emails.json', JSON.stringify(emails, null, 2));

    res.json({ message: "Email enregistré avec succès!" });
});

app.listen(3000, () => {
    console.log('Serveur démarré sur le port 3000');
});
