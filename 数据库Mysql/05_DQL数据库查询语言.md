# DQL数据查询语言

## 创建数据库
create database db_2;

use db_2;

## 创建学生、班级、教师的数据表
```SQL
-- 教师表
create table teacher(
t_id int primary key auto_increment,
t_name varchar(20) not null,
t_sex varchar(4) check(t_sex = '男' || t_sex = '女'),
t_age int check(t_age >= 20 && t_age <= 60)
)auto_increment = 100;

insert into teacher(t_name,t_sex,t_age) values("小威","男",28),("靓靓","女",20),
	("丸子","女",23),("易木","男",27),("龙卷风","男",30),("桃子","女",21),
    ("robert","男",40),("可达","男",28),("荔枝","女",22),("教主","男",29);
```

```SQL
-- 班级表
create table class(
c_id int primary key auto_increment,
c_name varchar(30) not null,
c_tid int, -- 班级的任课老师/班主任老师
c_stunum int default 0, -- 班级学生人数
constraint for_CT foreign key(c_tid)
 references teacher(t_id) on update cascade
)auto_increment = 100;

insert into class(c_name,c_tid) values("C语言",101),
	("C++",103),("数据结构",106),("数据库",100),("Win32",NULL),
    ("游戏开发",107),("QT",NULL),("Linux服务器",NULL);
```

```SQL
-- 学生表
create table student(
s_id int primary key auto_increment,
s_name varchar(20) not null,
s_cid int, -- 学生属于哪个班级
s_sex varchar(4) check(s_sex = '男'||s_sex = '女'),
s_age int check(s_age >= 18 && s_age <= 40),
constraint for_SC foreign key(s_cid)
 references class(c_id) on update cascade
)auto_increment = 1000;

insert into student(s_name,s_cid,s_sex,s_age) values("陈小皮",100,'男',20),
	("吉利服",103,'男',20),("张益达",100,'男',20),("萌萌",103,'女',20),
	("晓东",101,'男',20),("小蔡",null,'男',21),("小玉",102,'女',21),
	("阿雪",103,'女',21),("如花",null,'女',25),("似玉",null,'女',24),
	("小桂子",null,'男',22),("小强子",101,'男',23),("小吴",102,'男',24),
    ("小花",100,'女',23),("小丸子",null,'女',20),("小红",101,'女',21);
```



# 一、查询语句的基本格式select
```SQL
-- 查询所有学生的所有信息

SELECT * FROM db_2.student;
	-- select * from student; -- 有使用数据库的情况下，可以省略数据库名
	-- * 代表查询所有属性（字段）
```



```SQL
-- 查询所有学生的指定数据

select s_id,s_name from student;
```



# 二、条件查询where

## 1、关系运算符（>，<，>=，<=，=，!=(<>)）
```SQL
select s_id,s_name from student where s_id <= 1010;
	-- 在where子句之后加上查询条件
select s_id,s_name from student where s_id <> 1010;
	-- <>是不等于符号（也可以用!=）
```



## 2、逻辑运算符（&&(and/AND)，||(or/OR)）
```SQL
select s_id,s_name from student where s_id >= 1003 && s_id <= 1011;

select s_id,s_name from student where s_id = 1005 || s_name = '小吴';
```



## 3、范围查询（连续范围内：数字、字母）
```SQL
-- between……and……：在……之间

select s_id,s_name from student where s_id between 1003 and 1011;
	-- not between……and……：不在……之间
select s_id,s_name from student where s_id not between 1003 and 1011;
```



## 4、集合范围查询（使用不连续范围，自定义范围）
```SQL
-- in：在集合范围内查询

select s_id,s_name from student where s_id in(900,1000,1011,666,"abc",1012,111,1015);
	-- not in：在集合范围外查询
select s_id,s_name from student where s_name not in(123,"小哈","陈小皮","萌萌","abc",1012,11.11,"小红");
```



## 5、字符串模糊匹配like（只适用于字符串等文本类型）
```SQL
-- like：像……一样，类似于……

-- 通配符'%'：匹配任意多个字符
	-- 查询姓名以'小'字开头以任意多个字符结尾的学生信息
select * from student where s_name like '小%';
	-- 查询姓名中包含'小'字的学生信息
select * from student where s_name like '%小%';
-- 通配符'_'：匹配任意一个字符
	-- 查询姓名以'小'字开头以任意一个字符结尾的学生信息
select * from student where s_name like '小_';
-- 通配符'%'和通配符'_'配合使用
	-- 查询姓名以'小'字开头以任意多个字符结尾并且至少要有三个字的学生信息
select * from student where s_name like '小__%';
```



## 6、分页查询limit
```SQL
select * from student limit 5;
	-- 查询学生表中前5条数据
	-- 相当于：select * from student limit 0,5;
select * from student limit 2,6;
	-- 查询学生表中从第3（编号为2）条数据开始的后6条数据
```



## 7、查询结构排序order by
```SQL
-- order by：查询排序（默认升序排列）
	-- 查询学生信息按年龄从小到大排列
select * from student order by s_age;
-- order by <属性名> desc：查询排序（降序排列）
	-- 查询学生信息按年龄从大到小排列
select * from student order by s_age desc;
```



## 8、分组查询group by
```SQL
-- 对学生年龄进行分组查询

select * from student group by s_age;
	-- 对学生性别进行分组查询
select * from student group by s_sex;
	-- 单纯的分组查询意义不大（可以理解成为去除某个属性的重复值）

-- 分组查询一般用于分组之后的处理或计算（求和、最大值、最小值、平均值、统计等）
	-- 如：分组统计
    -- 分别统计学生中男女生的人数
select s_sex,count(s_id) from student group by s_sex;
	-- count为统计函数
	-- 分别统计班级学生人数
select s_cid,count(s_id) from student group by s_cid;

-- 分组之后的条件筛选
	-- 分别统计班级学生人数
-- select s_cid,count(s_id) from student group by s_cid where s_cid is not null;
	-- 分组之后无法使用where子句进行条件筛选，只能使用having子句
select s_cid,count(s_id) from student group by s_cid having s_cid is not null;
    -- having的查询效率比where低

select s_cid,count(s_id) from student where s_cid is not null group by s_cid;
	-- 能够在分组之前进行条件筛选的，就尽量在分组之前用where筛选完成后再分组
```



# 三、DQL多表查询
## 1、交叉连接
### ① 交叉连接的基本格式
```SQL
-- 查询所有学生所在班级的班级名称

select student.s_id,student.s_name,class.c_name from student,class;
```



### ② 笛卡尔积
```SQL
select student.*,class.* from student,class;
-- 笛卡尔积：连接查询多个表格所有数据都相互匹配一次，形成一个包含所有可能情况的临时数据表
-- 笛卡尔积非常影响查询性能，会降低查询效率，所以要尽量避免产生笛卡尔积
	-- 交叉连接会产生笛卡尔积
-- 查询语句查询出的数据表被称为临时结果集（临时表），不是真实存在的数据表，而是存在内存中的临时数据
```



### ③ 带条件的交叉连接
```SQL
-- 查询所有学生所在班级的班级名称

select student.*,class.* from student,class 
	where student.s_cid = class.c_id; -- 等值连接：外键值 = 主键值
```



## 2、内连接inner join
### ① 内连接的基本格式
```SQL
-- 查询所有学生所在班级的班级名称

select student.*,class.* from student inner join class 
	on student.s_cid = class.c_id; -- 等值连接：外键值 = 主键值
-- 相同条件下，内连接和交叉连接的查询效果一致
```



### ② 不带条件的内连接
```SQL
-- 查询所有学生所在班级的班级名称

select student.*,class.* from student inner join class;
```



### ③ 内连接和交叉连接的区别
```SQL
-- 内连接不产生笛卡尔积
-- 内连接的查询效率比交叉连接要高很多
```

## 3、外连接
```SQL
-- 外连接是对内连接查询结果的补全（查询结果的完全展示）
	-- 外连接会显示内连接中没有关联匹配的数据（没有匹配的用null代替）

-- ① 左外连接left join（左连接）
select student.s_id,student.s_name,class.c_name from student left join class
	on student.s_cid = class.c_id;
    
select student.s_id,student.s_name,class.c_name from class left join student
	on student.s_cid = class.c_id;

-- ② 右外连接right join（右连接）
select student.s_id,student.s_name,class.c_name from student right join class
	on student.s_cid = class.c_id;

select student.s_id,student.s_name,class.c_name from class right join student
	on student.s_cid = class.c_id;

-- ① 全外连接full join（全连接）
select student.s_id,student.s_name,class.c_name from student full join class
	on student.s_cid = class.c_id;
-- MySQL不支持全连接
```



## 4、多表连接查询
```SQL
-- 查询所有学生所在班级的班级名称，以及对应班级的任课老师
select student.s_id,student.s_name,class.c_name,teacher.t_name
	from student left join class on student.s_cid = class.c_id
	left join teacher on class.c_tid = teacher.t_id;
-- 只有存在外键联系的表格连接查询才有意义
-- 多表连接查询最好不要涉及到4个表以上的连接（不包括4个表），这样查询效率很低，是数据库设计的问题
-- 表的连接很吃查询性能
```



## 5、别名的使用as
```SQL
-- 查询所有学生所在班级的班级名称，以及对应班级的任课老师
select S.s_id as 学号,S.s_name as 学生姓名,C.c_name as 班级名称,T.t_name as 任课老师
	from student as S left join class as C on S.s_cid = C.c_id
	left join teacher as T on C.c_tid = T.t_id;
	-- 可以使用关键字as给属性名和表名取别名
    -- 给数据表取别名可以减少表名的解析时间，从而提高查询效率

-- 关键字as可以省略
select S.s_id 学号,S.s_name 学生姓名,C.c_name 班级名称,T.t_name 任课老师
	from student S left join class C on S.s_cid = C.c_id
	left join teacher T on C.c_tid = T.t_id;
```



## 四、补充

## SQL UNION 操作符

UNION 操作符用于合并两个或多个 SELECT 语句的结果集。

请注意，UNION 内部的 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每条 SELECT 语句中的列的顺序必须相同。

### SQL UNION 语法

```sql
SELECT column_name(s) FROM table_name1
UNION
SELECT column_name(s) FROM table_name2
```

**注释：**默认地，UNION 操作符选取不同的值。如果允许重复的值，请使用 UNION ALL。

### SQL UNION ALL 语法

```sql
SELECT column_name(s) FROM table_name1
UNION ALL
SELECT column_name(s) FROM table_name2
```

另外，UNION 结果集中的列名总是等于 UNION 中第一个 SELECT 语句中的列名。

下面的例子中使用的原始表：

Employees_China:

| E_ID | E_Name         |
| :--- | :------------- |
| 01   | Zhang, Hua     |
| 02   | Wang, Wei      |
| 03   | Carter, Thomas |
| 04   | Yang, Ming     |

Employees_USA:

| E_ID | E_Name         |
| :--- | :------------- |
| 01   | Adams, John    |
| 02   | Bush, George   |
| 03   | Carter, Thomas |
| 04   | Gates, Bill    |

## 使用 UNION 命令

实例

列出所有在中国和美国的不同的雇员名：

```sql
SELECT E_Name FROM Employees_China
UNION
SELECT E_Name FROM Employees_USA
```

结果

| E_Name         |
| :------------- |
| Zhang, Hua     |
| Wang, Wei      |
| Carter, Thomas |
| Yang, Ming     |
| Adams, John    |
| Bush, George   |
| Gates, Bill    |

**注释：**这个命令无法列出在中国和美国的所有雇员。在上面的例子中，我们有两个名字相同的雇员，他们当中只有一个人被列出来了。UNION 命令只会选取不同的值。

UNION ALL

UNION ALL 命令和 UNION 命令几乎是等效的，不过 UNION ALL 命令会列出所有的值。

```sql
SQL Statement 1
UNION ALL
SQL Statement 2
```

## 使用 UNION ALL 命令

实例：

列出在中国和美国的所有的雇员：

```sql
SELECT E_Name FROM Employees_China
UNION ALL
SELECT E_Name FROM Employees_USA
```

结果

| E_Name         |
| :------------- |
| Zhang, Hua     |
| Wang, Wei      |
| Carter, Thomas |
| Yang, Ming     |
| Adams, John    |
| Bush, George   |
| Carter, Thomas |
| Gates, Bill    |