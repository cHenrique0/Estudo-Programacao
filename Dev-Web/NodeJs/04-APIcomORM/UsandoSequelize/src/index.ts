import express, { Request, Response } from "express";
import cors, { CorsOptions } from "cors";
import { StatusCodes } from "http-status-codes";

const app = express();
const PORT = 5000;
const allowedOrigins = [`http://localhost:${PORT}`];
const options: CorsOptions = {
  origin: allowedOrigins,
};

app.use(cors(options));

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rota de teste
app.get("/", (req: Request, res: Response): Response => {
  return res.status(StatusCodes.OK).send({
    message: "Exemplo de API usando Sequelize",
  });
});

const start = async (): Promise<void> => {
  try {
    app.listen(PORT, () => {
      console.log(`Application listening on port: ${PORT}`);
      console.log(`> ${[allowedOrigins]}`);
    });
  } catch (error) {
    console.log(error);
    process.exit(1);
  }
};

start();
