// Importando o express
import express from "express";
// Importando alguns tipos do express
import { Request, Response, NextFunction } from "express";
// importando constantes do status code
import { StatusCodes } from "http-status-codes";
// importando as rotas do usuário
import usersRoute from "./routes/users.route";

// criando uma instância do express
const app = express();
// variavel para armazenar a porta que será usada pelo express
const port = 3000;

/* Configurações da aplicação */
app.use(express.json()); // middleware para o express interpretar o content-type da resquest como json
app.use(express.urlencoded({ extended: true }));

/* Configurações de rotas */
app.use(usersRoute); // rotas do usuário

// definindo uma rota experimental para testar o funcionamento
app.get(
  "/status",
  (request: Request, response: Response, next: NextFunction) => {
    response.status(StatusCodes.OK).send({
      msg: "A GET request to test",
    });
  }
);

/* Inicialização do servidor */
app.listen(port, () => {
  console.log(`App listening on port: ${port}`);
});
