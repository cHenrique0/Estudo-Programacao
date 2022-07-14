import db from "../database/db";
import User from "../models/user.model";

class UserRepository {
  async findAllUsers(): Promise<User[]> {
    const select = `
      SELECT uuid, username
      FROM application_user
    `;
    // destructuring para pegar apenas as linhas da tabela e armazenando na const users
    const { rows: users } = await db.query<User>(select);
    return users || [];
  }

  async findUserById(uuid: string): Promise<User> {
    const select = `
      SELECT uuid, username
      FROM application_user
      WHERE uuid = $1
    `;
    // o elemento do array será substituido no $1 do WHERE na query
    const where = [uuid];
    const {
      rows: [user],
    } = await db.query<User>(select, where);
    return user || null;
  }

  async create(user: User): Promise<string> {
    const insert = `
      INSERT INTO application_user(
        username,
        password
      )
      VALUES ($1, crypt($2, $3))
      RETURNING uuid
    `;
    const values = [user.username, user.password, "chva81425078"];

    const {
      rows: [newUser],
    } = await db.query<{ uuid: string }>(insert, values);

    return newUser.uuid;
  }

  async update(user: User): Promise<void> {
    const update = `
      UPDATE application_user
      SET
        username = $1,
        password = crypt($2, $3)
      WHERE uuid = $4
      RETURNING uuid
    `;
    const values = [user.username, user.password, "chva81425078", user.uuid];
    await db.query(update, values);
  }

  async remove(uuid: string): Promise<void> {
    const deleteQuery = `
      DELETE FROM application_user
      WHERE uuid=$1
    `;
    const where = [uuid];
    await db.query(deleteQuery, where);
  }
}

export default new UserRepository();
