
// Importando o express
import express from "express";
// Importando alguns tipos do express
import { Request, Response, NextFunction } from "express";
import usersRoute from "./routes/users.route";

// criando uma instância do express
const app = express();
// variavel para armazenar a porta que será usada pelo express
const port = 3000;

// definindo uma rota experimental para testar o funcionamento
app.get('/status', (request: Request, response: Response, next: NextFunction) => {
  response.status(200).send({
    "msg": "a GET request"
  });
});

// Usando as rotas criadas em ./routes
app.use(usersRoute);

// Fazendo o express ouvir a porta para iniciar o servidor
app.listen(port, () => {
  console.log(`App listening on port: ${port}`);
});