// importando Router para definir novas rotas e alguns tipos do express
import { Router, Request, Response, NextFunction } from "express";

const usersRoute = Router();

// GET de todos os usuários
usersRoute.get(
  "/users",
  (request: Request, response: Response, next: NextFunction) => {
    const users = [{ userName: "Teste" }];
    response.status(200).send(users);
  }
);

// GET por id de usuário
usersRoute.get(
  "/users/:uuid",
  (request: Request, response: Response, next: NextFunction) => {
    // pegando o id digitado na url do navegador
    const uuid = request.params.uuid;
    response.status(200).send({ uuid });
  }
);

export default usersRoute;
