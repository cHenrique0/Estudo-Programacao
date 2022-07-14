import { Pool } from "pg";

const connectionString =
  "postgres://kjdmjddr:VPJlLCUyeqjQTXIE1A_-YP0H7fELBjRY@kesavan.db.elephantsql.com/kjdmjddr";
const db = new Pool({ connectionString });

export default db;
