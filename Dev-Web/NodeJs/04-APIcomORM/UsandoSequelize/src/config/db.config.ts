import dotenv from "dotenv";

dotenv.config();

export const dbConfig = {
  HOST: <string>process.env.DB_HOST,
  PORT: <string>process.env.DB_PORT,
  USER: <string>process.env.DB_USER,
  PASSWORD: <string>process.env.DB_PASSWORD,
  DB: <string>process.env.DB_NAME,
  DIALECT: process.env.DB_DIALECT,
  POOL: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000,
  },
};
