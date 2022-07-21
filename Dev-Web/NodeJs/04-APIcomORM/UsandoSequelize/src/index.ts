import express, { Request, Response } from "express";
import { StatusCodes } from "http-status-codes";

const app = express();
const PORT = 5000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Rota de teste
app.get("/", (req: Request, res: Response) => {
  res.sendStatus(StatusCodes.OK);
});

app.listen(PORT, () => {
  console.log(`Application listening on port: ${PORT}`);
  console.log(`> http://localhost:${PORT}/`);
});
