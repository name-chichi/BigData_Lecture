# userdb.py Control 역할
import sqlite3

from itemvo import ItemVO
from sql import Sql


class ItemDB:

    def __init__(self, dbName):
        self.__dbName = dbName;
    def getConn(self):
        con = sqlite3.connect(self.__dbName);
        cursor = con.cursor();
        return {'con':con,'cursor':cursor};
    def close(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close();
        if cc['con'] != None:
            cc['con'].close();
    def makeTable(self):
        cc = self.getConn();
        cc['cursor'].execute(Sql.make_itemdb);
        cc['con'].commit();
        self.close(cc);

    def insert(self, item):
        cc = self.getConn();
        cc['cursor'].execute(Sql.insert_itemdb,(item.getName(),item.getPrice()));
        cc['con'].commit();
        self.close(cc);
        print('%s 등록 되었습니다.' % item);
    def delete(self,id):
        cc = self.getConn();
        cc['cursor'].execute(Sql.delete_itemdb, (id,));
        cc['con'].commit();
        self.close(cc);
        print('%d 삭제 되었습니다.' % id);
    def update(self, item):
        cc = self.getConn();
        cc['cursor'].execute(Sql.update_itemdb, (item.getName(), item.getPrice(), item.getId()));
        cc['con'].commit();
        self.close(cc);
        print('%s 수정 되었습니다.' % item);
    def select(self, id):
        # 해당 id 의 데이터를 가지고 와서 itemvo를 만들어서 리턴한다.
        result = None;
        cc = self.getConn();
        cc['cursor'].execute(Sql.select_itemdb,(id,));
        obj = cc['cursor'].fetchone();
        result = ItemVO(obj[0],obj[1],obj[2],obj[3]);
        self.close(cc);
        return result;
    def selectall(self):
        results = [];
        cc = self.getConn();
        cc['cursor'].execute(Sql.selectall_itemdb);
        objs = cc['cursor'].fetchall();
        for obj in objs:
            result = ItemVO(obj[0], obj[1], obj[2], obj[3]);
            results.append(result);
        self.close(cc);
        return results;





