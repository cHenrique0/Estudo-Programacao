import { NextFunction, Request, Response } from "express";
import JWT from "jsonwebtoken";
import ForbiddenError from "../models/errors/forbidden.error.model";

async function bearerAuthMiddleware(
  request: Request,
  response: Response,
  next: NextFunction
) {
  try {
    const authHeader = request.headers["authorization"];
    if (!authHeader) {
      throw new ForbiddenError("Credenciais não informadas");
    }

    const [authType, token] = authHeader.split(" ");
    if (authType !== "Bearer" || !token) {
      throw new ForbiddenError("Tipo de autenticação ou token inválido");
    }

    const tokenPayload = JWT.verify(token, "my_secret_key");

    if (typeof tokenPayload !== "object" || !tokenPayload.sub) {
      throw new ForbiddenError("Token inválido!");
    }

    const user = { uuid: tokenPayload.sub, username: tokenPayload.username };
    request.user = user;
    next();
  } catch (error) {
    next(error);
  }
}

export default bearerAuthMiddleware;
