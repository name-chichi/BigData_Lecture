class Sql:
    make_itemdb = '''  
        CREATE  TABLE  IF  NOT  EXISTS  ITEMDB (
          ID INTEGER  PRIMARY KEY  AUTOINCREMENT,
          NAME  TEXT,
          PRICE  REAL,
          REGDATE   TIMESTAMP  DEFAULT  CURRENT_TIMESTAMP
        ) 
    ''';
    insert_itemdb = '''  
        INSERT  INTO  ITEMDB (NAME,PRICE) VALUES  (?,?) 
    ''';
    update_itemdb = '''  
        UPDATE  ITEMDB  SET  NAME=?,  PRICE=?  WHERE ID=? 
    ''';
    delete_itemdb = '''  
        DELETE   FROM  ITEMDB  WHERE  ID = ? 
    ''';
    select_itemdb = '''   
        SELECT  *  FROM  ITEMDB  WHERE  ID = ?
    ''';
    selectall_itemdb = '''   
        SELECT  * FROM  ITEMDB
    ''';







