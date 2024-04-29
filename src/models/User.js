const mongoose = require('mongoose');

const mongoURI = 'mongodb://localhost:27017/trab_node';

mongoose.connect(mongoURI)
    .then(() => console.log('Conectado ao MongoDB'))
    .catch(err => console.error('Erro ao conectar ao MongoDB:', err));


const userSchema = new mongoose.Schema({
    name: String,
    email: { type: String, unique: true },
    password: String,
});

module.exports = mongoose.model("User", userSchema); 