const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const User = require('./models/User');
const routes = require('./routes/userRoutes');

const PORT = 3000;
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', (req, res) => {
    res.send('Hello Woooooorld');
});


app.post('/login', async (req, res) => {
    const { email, password } = req.body;
    console.log(req.body);
    try {
        const user = await User.findOne({ email })

        if (!user) {
            res.status(401).send('Usuário não encontrado');
            return;
        }
        //nao consegui fazer uma verificação de senha
        res.redirect('http://127.0.0.1:5000/');
    } catch (error) {
        console.error('Erro ao buscar usuário:', error);
        res.status(500).send('Erro ao buscar usuário no banco de dados');
    }
});





app.get('/login', (req, res) => {
    res.sendFile(__dirname + '/templates/login.html');
});



app.use(routes);

app.listen(PORT, () => {
    console.log(`O servidor está funcionando na porta: ${PORT}`);
});