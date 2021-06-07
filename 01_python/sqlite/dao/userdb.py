# userdb.py Control 역할
import sqlite3

from frame.sqlitedao import SqliteDao
from sql.sql import Sql
from vo.uservo import UserVO


class UserDB(SqliteDao):
    def __init__(self, dbName):
        super().__init__(dbName);
    def insert(self, u):
        cc = self.getConn();
        cc['cursor'].execute(Sql.insert_userdb,
                             (u.getId(),u.getPwd(),u.getName())
                             );
        cc['con'].commit();
        self.close(cc);
        print('%s 등록 되었습니다.' % u);
    def delete(self,id):
        print('%s 삭제 되었습니다.' % id);
    def update(self, u):
        print('%s 수정 되었습니다.' % u);
    def select(self, id):
        result = None;
        cc = self.getConn();
        cc['cursor'].execute(Sql.select_userdb , (id,));
        obj = cc['cursor'].fetchone();
        result = UserVO(obj[0],obj[1],obj[2]);
        self.close(cc);
        return result;
    def selectall(self):
        results = [];
        cc = self.getConn();
        cc['cursor'].execute(Sql.selectall_userdb);
        all = cc['cursor'].fetchall();
        for u in all:
            rs = UserVO(u[0],u[1],u[2]);
            results.append(rs);
        self.close(cc);
        return results;





