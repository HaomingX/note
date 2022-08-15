# DDL与DML

## 一、数据定义语言DML

### 1、数据库的创建和使用

#### ① 创建数据库
```sql
CREATE DATABASE test;
	-- 创建一个数据库，名称为test

CREATE DATABASE TEST;
	-- 不允许创建同名数据库
	-- SQL语言不区分大小写（除字符串中以外）

CREATE DATABASE test default charset utf8;
	-- 创建一个数据库，名称为test，并设置默认字符集为utf8
```



#### ② 查看当前数据库服务中所有的数据库
```sql
SHOW DATABASES;
```



#### ③ 数据库的删除
```sql
DROP DATABASE test;
DROP DATABASE db_1;
DROP DATABASE db_2;
```

#### ④ 数据库的使用
```sql
CREATE DATABASE db_1;
USE db_1;
	-- 只有进入了数据库，才能在当前数据库中创建数据表等数据库对象
```

### 2、数据表的创建和格式的修改

#### ① 数据表的创建
```sql
CREATE TABLE people( -- 保存人的信息的数据库
p_id int, -- 编号
p_name char(20), -- 姓名
p_gender char(4), -- 性别
p_age int -- 年龄
);
```



#### ② 数据表的删除
```sql
DROP TABLE people;
```

#### ③ 修改表名称
```sql
RENAME table people to people_tb;
```

#### ④ 查看表结构
```sql
DESC people_tb;
SHOW COLUMNS FROM people_tb;
```

#### ⑤ 增加表中列
```sql
ALTER TABLE people_tb ADD p_birthday date;
```

#### ⑥ 删除表中列
```sql
ALTER TABLE people_tb DROP COLUMN p_age;
```

#### ⑦ 修改属性列的数据类型
```sql
ALTER TABLE people_tb MODIFY COLUMN p_name varchar(30);
```

#### ⑧ 修改列名称
```sql
ALTER TABLE people_tb CHANGE COLUMN p_birthday 出生年月 date;
-- 很少用到表结构的修改，一般都是在创建表时就要定义完成，严格要求，而不是创建完毕之后再修改
```

## 二、数据操纵语言DML

### 1、表数据的插入insert
```sql
-- ① 向数据表中指定的属性列插入数据
INSERT INTO people_tb(p_id,p_name) value(1,"徐浩铭");
	-- 属性名的顺序要与插入数据的顺序保持一致，没有给定数据的属性默认为空null

-- ② 向数据表中所有属性列插入数据
INSERT INTO people_tb(p_id,p_name,p_gender,出生年月) value(2,"彭承旭",'男','2020-02-02');
	-- SQL语言没有单个字符类型，只有字符串类型，所以''单引号和""双引号都表示字符串
INSERT INTO people_tb value(2,"徐旭",'男','2003-05-09');
	-- 不给定属性名的插入就是默认为所有属性插入数据

-- ③ 插入多条数据
INSERT INTO people_tb(p_id,p_name) values(3,"小明"),(4,"小王"),(5,"小李");
```



### 2、表数据的修改update
```sql
-- ① 修改所有数据
UPDATE people_tb set p_gender = "男";
	-- 不带条件的修改，默认修改指定字段的所有数据

-- ② 条件修改
UPDATE people_tb set p_gender = "女" where p_id = 5;

-- ③ 多条件修改
UPDATE people_tb set p_gender = "女" where p_id = 5 && p_name = "小李";
	-- 逻辑运算符&&(and/AND)、||(or/OR)
UPDATE people_tb set 出生年月 = "2000-01-01" where p_id = 4 || p_name = "小李";

-- 如果发现数据更新错误，又没有语法错误，错误提示safe update等，那就是没有关闭安全检查，默认不允许修改数据
-- 关闭安全检查：编辑菜单->首选项->SQL Editor->Safe updates->勾去掉->重启workbench
```

![image-20220313010756261](C:\Users\Π\AppData\Roaming\Typora\typora-user-images\image-20220313010756261.png)

### 3、表数据的删除delete
```sql
-- ① 删除表中所有数据
DELETE FROM people_tb;

-- ② 条件删除
DELETE FROM people_tb where p_id = 4;

-- ③ 多条件删除
DELETE FROM people_tb where p_id = 4 or p_name = "小明";
```

