# 要求⼆：建立資料庫和資料表

#### 1. 建立⼀個新的資料庫，取名字為 website。

#### 2. 在資料庫中，建立會員資料表，取名字為 member。資料表必須包含以下欄位設定：

![](./Screenshot%20from%202022-10-17%2019-07-49.png)

# 要求三：SQL CRUD

#### ●使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。

![](./Screenshot%20from%202022-10-17%2017-02-56.png)

#### ● 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。

![](./Screenshot%20from%202022-10-17%2017-03-16.png)


#### ● 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

![](./Screenshot%20from%202022-10-17%2017-07-28.png)


#### ● 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )

![](./Screenshot%20from%202022-10-17%2017-16-40.png)


#### ● 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。

![](./Screenshot%20from%202022-10-17%2017-17-14.png)


#### ● 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

![](./Screenshot%20from%202022-10-17%2017-17-14.png)


#### ● 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

![](./Screenshot%20from%202022-10-17%2019-23-45.png)

# 要求四：SQL Aggregate Functions

#### ● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

![](./Screenshot%20from%202022-10-17%2017-22-09.png)


#### ● 取得 member 資料表中，所有會員 follower_count 欄位的總和。

![](./Screenshot%20from%202022-10-17%2017-24-25.png)


#### ● 取得 member 資料表中，所有會員 follower_count 欄位的平均數

![](./Screenshot%20from%202022-10-17%2017-24-41.png)


# 要求五：SQL JOIN (Optional)

#### 1. 在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message。資料表中必須包含以下欄位設定：

![](./Screenshot%20from%202022-10-17%2017-56-58.png)

![](./Screenshot%20from%202022-10-17%2018-00-26.png)

#### ● 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。

![](./Screenshot%20from%202022-10-17%2018-12-55.png)

#### ● 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。

![](./Screenshot%20from%202022-10-17%2018-13-54.png)


#### ● 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。

![](./Screenshot%20from%202022-10-17%2018-19-35.png)
