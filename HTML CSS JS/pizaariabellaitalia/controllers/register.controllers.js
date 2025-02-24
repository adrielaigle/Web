import { db } from "../database/db.js"

async function obterRegistros(req, res) {
    const cadastro = await db.all("SELECT * FROM cadastro")
    return res.status(200).json(cadastro)
}

export {
    obterRegistros
}