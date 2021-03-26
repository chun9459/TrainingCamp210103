# 要求三：基本的 SQL 指令
# 1. 使用 INSERT 指令新增一筆資料到 user 資料表中，這筆資料的 username 和 password 欄位必須是 ply。接著繼續新增至少 4 筆隨意的資料。
     INSERT INTO user VALUES
    -> (NULL, "Wendy", "ply", "ply", NOW());
    ![image](https://user-images.githubusercontent.com/76869260/112659900-d5996700-8e8f-11eb-916d-a86ae1694a5b.png)
    
     INSERT INTO user VALUES
    -> (NULL, "Stacy", "6610W", "qsqs", 20011208142159),
    -> (NULL, "Elly", "6610K", "QSSQ", 20160819070513),
    -> (NULL, "Leon", "6610J", "FMFM", 20200130151142),
    -> (NULL, "Katherina", "6610S", "fmmf", 20120909090909);
    ![image](https://user-images.githubusercontent.com/76869260/112660456-6f611400-8e90-11eb-8701-0c0b11890680.png)


# 2. 使用 SELECT 指令取得所有在 user 資料表中的使用者資料。
    SELECT * FROM user;
    ![image](https://user-images.githubusercontent.com/76869260/112660510-80118a00-8e90-11eb-863a-67bb5d3f9cb9.png)


# 3. 使用 SELECT 指令取得 user 資料表中總共有幾筆資料。
    SELECT COUNT(*) FROM user;
    ![image](https://user-images.githubusercontent.com/76869260/112660635-9e778580-8e90-11eb-9315-0100da46a1a4.png)


# 4. 使用 SELECT 指令取得所有在 user 資料表中的使用者資料，並按照 time 欄位，由近到遠排序。
     SELECT * FROM user ORDER BY time DESC;
     ![image](https://user-images.githubusercontent.com/76869260/112660909-ef877980-8e90-11eb-9d3a-366ab0118c73.png)


# 5. 使用 SELECT 指令取得 user 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。
    SELECT * FROM user ORDER BY time DESC LIMIT 1,3;
    ![image](https://user-images.githubusercontent.com/76869260/112700969-4d848300-8eca-11eb-935c-4d1b3a3a7d8c.png)


# 6. 使用 SELECT 指令取得欄位 username 是 ply 的使用者資料。
     SELECT * FROM user WHERE username="ply";
    ![image](https://user-images.githubusercontent.com/76869260/112661990-1db98900-8e92-11eb-8c60-ff16f8a7d3a6.png)


# 7. 使用 SELECT 指令取得欄位 username 是 ply、且欄位 password 也是 ply 的資料。
    SELECT * FROM user WHERE username="ply" AND password="ply";
    ![image](https://user-images.githubusercontent.com/76869260/112662279-77ba4e80-8e92-11eb-84f5-0a23148d0465.png)


# 8. 使用 UPDATE 指令更新欄位 username 是 ply 的使用者資料，將資料中的 name 欄位改成【丁滿】。
    UPDATE user SET name="丁滿" WHERE username="ply";
    ![image](https://user-images.githubusercontent.com/76869260/112663263-940abb00-8e93-11eb-8b88-b94a963f15f4.png)


# 9. 使用 DELETE 指令刪除所有在 user 資料表中的資料。
    DELETE FROM user;
    ![image](https://user-images.githubusercontent.com/76869260/112663732-20b57900-8e94-11eb-9b2d-ce6b8586115a.png)

