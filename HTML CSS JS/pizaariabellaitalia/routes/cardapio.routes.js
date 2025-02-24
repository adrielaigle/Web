import { Router } from 'express';
import { db } from '../database/db.js';
import { obterCardapio } from '../controllers/cardapio.controllers.js';

export const cardapioRouter = Router();

cardapioRouter.get('/api/cardapio', obterCardapio);

async function isIDcadastrado(id) {
    const cardapio = await db.all("SELECT * FROM cardapio");
    for (let x = 0; x < cardapio.length; x++) {
        if (cardapio[x].id === id) {
            return true;
        }
    }
    return false;
}

cardapioRouter.post('/api/cardapio', async (req, res) => {
    const cardapio = await db.all("SELECT * FROM cardapio WHERE id=?", [req.body.id]);
    if (cardapio[0]) {
        return res.status(400).json({ mensagem: "Pizza já cadastrada" });
    } else {
        await db.run(
            `INSERT INTO cardapio (tipo, id, titulo, descricao, valor) VALUES (?,?,?,?,?)`,
            [req.body.tipo, req.body.id, req.body.titulo, req.body.descricao, req.body.valor]
        );
        return res.status(201).json({ "mensagem": "Pizza cadastrada com sucesso" });
    }
});

cardapioRouter.patch('/api/cardapio/:id', async (req, res) => {
    const id = +req.params.id;
    const nome = req.body.nome;
    const cardapio = await db.all("SELECT * FROM cardapio");

    if (await isIDcadastrado(id)) {
        await db.run(`UPDATE cardapio SET titulo = ? WHERE id = ?`, [nome, id])
        return res.status(200).json({ mensagem: "Pizza atualizada com sucesso" });
    } else {
        return res.status(404).json({ mensagem: "Pizza não encontrada" });
    }
});