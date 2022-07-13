// importando Router para definir novas rotas e alguns tipos do express
import { Router, Request, Response, NextFunction } from "express";
// importando constantes do status code
import { StatusCodes } from "http-status-codes";

// Opcional: criar minha propria constante com o status code
// const OK = StatusCodes.OK;

const usersRoute = Router();

// GET all users
usersRoute.get(
  "/users",
  (request: Request, response: Response, next: NextFunction) => {
    const users = [{ userName: "Teste" }];
    response.status(StatusCodes.OK).send(users);
  }
);

// GET user by ID
usersRoute.get(
  "/users/:uuid",
  (request: Request, response: Response, next: NextFunction) => {
    // pegando o id digitado na url do navegador
    const uuid = request.params.uuid;
    response.status(StatusCodes.OK).send({ uuid });
  }
);

// POST user(create)
usersRoute.post(
  "/users",
  (request: Request, response: Response, next: NextFunction) => {
    const newUser = request.body;
    response.status(StatusCodes.CREATED).send(newUser);
  }
);

// PUT user(update)
usersRoute.put(
  "/users/:uuid",
  (request: Request, response: Response, next: NextFunction) => {
    const uuid = request.params.uuid;
    response.status(StatusCodes.OK).send({ uuid });
  }
);

// DELETE user
usersRoute.delete(
  "/users/:uuid",
  (request: Request, response: Response, next: NextFunction) => {
    response.sendStatus(StatusCodes.OK);
  }
);

export default usersRoute;
