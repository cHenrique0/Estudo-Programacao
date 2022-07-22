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
app.get("/", (req: Request, res: Response) => {
  res.sendStatus(StatusCodes.OK);
});

app.listen(PORT, () => {
  console.log(`Application listening on port: ${PORT}`);
  console.log(`> ${[allowedOrigins]}`);
});
