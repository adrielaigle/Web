import { db } from "../database/db.js"

async function obterCardapio(req, res) {
    const cardapio = await db.all("SELECT * FROM cardapio")
    return res.status(200).json(cardapio)
}

export {
    obterCardapio
}