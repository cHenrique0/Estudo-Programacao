// importando Router para definir novas rotas e alguns tipos do express
import { Router, Request, Response, NextFunction } from "express";
// importando constantes do status code
import { StatusCodes } from "http-status-codes";
import userRepository from "../repositories/user.repository";

// Opcional: criar minha propria constante com o status code
// const OK = StatusCodes.OK;

const usersRoute = Router();

// GET all users
usersRoute.get(
  "/users",
  async (request: Request, response: Response, next: NextFunction) => {
    const users = await userRepository.findAllUsers();
    response.status(StatusCodes.OK).send(users);
  }
);

// GET user by ID
usersRoute.get(
  "/users/:uuid",
  async (request: Request, response: Response, next: NextFunction) => {
    // pegando o id digitado na url do navegador
    const uuid = request.params.uuid;
    const user = await userRepository.findUserById(uuid);
    response.status(StatusCodes.OK).send(user);
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
