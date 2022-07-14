import db from "../database/db";
import User from "../models/user.model";

class UserRepository {
  async findAllUsers(): Promise<User[]> {
    const query = `
      SELECT uuid, username
      FROM application_user
    `;
    // destructuring para pegar apenas as linhas da tabela e armazenando na const users
    const { rows: users } = await db.query<User>(query);
    return users || [];
  }

  async findUserById(uuid: string): Promise<User> {
    const query = `
      SELECT uuid, username
      FROM application_user
      WHERE uuid = $1
    `;
    // o elemento do array será substituido no $1 do WHERE na query
    const where = [uuid];
    const {
      rows: [user],
    } = await db.query<User>(query, where);
    return user || null;
  }
}

export default new UserRepository();
