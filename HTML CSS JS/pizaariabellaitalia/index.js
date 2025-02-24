import express from "express"
import { cardapioRouter } from "./routes/cardapio.routes.js";
import { registerRouter } from "./routes/register.routes.js";

const app = express();

app.use(express.static("public"))
app.use(express.json())

app.use(cardapioRouter);
app.use(registerRouter);

app.get("/hello", (req, res) => {
    return res.status(200).json({ "mensagem": "Olá mundo" })
})

app.listen(55555, () => {
    console.log("Servidor foi iniciado na porta 55555")
})