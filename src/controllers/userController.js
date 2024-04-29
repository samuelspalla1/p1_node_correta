const User = require('../models/User');

exports.getAllUsers = async (req, res) => {
    try {
        const users = await User.find();
        res.status(200).json(users);
    } catch (error) {
        res.status(400).json({message: error.message})
    }
};


exports.getSingleUser = async (req, res) => {
    try {
        const userId = req.params.id;
        const user = await User.findById(userId);
        if (!user) {
            return res.status(404).json({ message: 'Usuário não encontrado' });
        }
        res.status(200).json(user);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};


exports.createUser = async (req, res) => {
    try {
        console.log('Dados recebidos no corpo da solicitação:', req.body);

        const newUser = new User(req.body);
        await newUser.save();

        console.log('Novo usuário salvo no banco de dados:', newUser);

        res.status(201).json(newUser);
    } catch (error) {
        console.error('Erro ao criar novo usuário:', error);
        res.status(400).json({message: error.message});
    }
};

exports.updateUser = async (req, res) => {
    const { id } = req.params;
    try {
        const updatedUser = await User.findByIdAndUpdate(id, req.body, { new: true });
        res.status(200).json(updatedUser);
    } catch (error) {
        res.status(400).json({message: error.message});
    }
};

exports.deleteUser = async (req, res) => {
    const { id } = req.params;
    try {
        await User.findByIdAndDelete(id);
        res.status(204).send();
    } catch (error) {
        res.status(400).json({message: error.message});
    }
};