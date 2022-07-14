// Importando o express
import express from "express";
// importando as rotas
import usersRoute from "./routes/users.route";
import statusRoute from "./routes/status.route";

// criando uma instância do express
const app = express();
// variavel para armazenar a porta que será usada pelo express
const port = 3000;

/* Configurações da aplicação */
app.use(express.json()); // middleware para o express interpretar o content-type da resquest como json
app.use(express.urlencoded({ extended: true }));

/* Configurações de rotas */
app.use(statusRoute); // rotas de status do servidor
app.use(usersRoute); // rotas do usuário

/* Inicialização do servidor */
app.listen(port, () => {
  console.log(`App listening on port: ${port}`);
});
