import { Router } from 'express';
import { db } from '../database/db.js'
import bcrypt from 'bcrypt'
import { obterRegistros } from '../controllers/register.controllers.js';

export const registerRouter = Router();

registerRouter.get('/api/register', obterRegistros);

registerRouter.post('/api/login', async (req, res) => {
    const { username, email, password } = req.body;

    try {
        const existeUserEmail = await db.get("SELECT * FROM cadastro WHERE email = ?", [email]);

        if (!existeUserEmail) {
            return res.status(401).json({ error: "Credenciais Inválidas." });
        }

        const passwordMatch = await bcrypt.compare(password, existeUserEmail.password);

        if (!passwordMatch) {
            return res.status(401).json({ error: "Credenciais Inválidas." });
        }

        res.status(200).json({ message: "Login bem-sucedido" });
    } catch (error) {
        console.error("Erro ao verificar credenciais:", error);
        res.status(500).json({ error: "Erro interno do servidor." });
    }
});

registerRouter.post('/api/register', async (req, res) => {
    const { username, email, password } = req.body;
    try {
        const existeUserEmail = await db.get("SELECT * FROM cadastro WHERE email = ?", [email]);

        if (existeUserEmail) {
            return res.status(409).json({ error: "Já existe um usuário com esse email." })
        }

        const salt = await bcrypt.genSalt(10);
        const hashedSenha = await bcrypt.hash(password, salt);
        console.log(hashedSenha);

        await db.run("INSERT INTO cadastro (name, email, password) VALUES (?, ?, ?)", [username, email, hashedSenha]);
        console.log("Usuário registrado com sucesso"); 

        const usuarioAposInsercao = await db.get("SELECT * FROM cadastro WHERE email = ?", [email]);
        console.log("Depois da inserção, usuário encontrado:", usuarioAposInsercao);
        res.status(201).send("Usuário registrado com sucesso!");
    } catch (error) {
        console.error("Erro ao registrar usuário:", error);
        res.status(500).json({ error: "Erro ao registrar usuário." })
    }
});