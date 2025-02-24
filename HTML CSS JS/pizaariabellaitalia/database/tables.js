import { db } from "./db.js"

async function criarTabelas() {
    await db.run(`CREATE TABLE IF NOT EXISTS cardapio (
        tipo TEXT,
        id TEXT PRIMARY KEY,
        titulo TEXT,
        img TEXT,
        descricao TEXT,
        valor REAL
        )
    `);

    await db.run(`CREATE TABLE IF NOT EXISTS cadastro (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        password TEXT
        )
    `);
}
criarTabelas().then(() => console.log("Tabela criada"));
