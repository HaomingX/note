## C++语法

### 一、bool类型

为什么存在？只占一个字节，有时候可以优化程序，而且对于只有T,F时很直观

```c++
#include <iostream>
using namespace std;

int main(){
    //bool是一种数据类型
    //只表示真和假;非0为真(true),0为假(false);ture(1),false(0);
    bool is=true;
    is=false;
    is++;//为真，所以is为true(1)
    is=3.14//为真，所以is为true(1)
    return 0;
}
```

### 二、内联函数

定义: 当函数被声明为内联函数之后, 编译器会将其内联展开, 而不是按通常的函数调用机制进行调用.
优点: 当函数体比较小的时候, 内联该函数可以令目标代码更加高效. 对于存取函数以及其它函数体比较短, 性能关键的函数, 鼓励使用内联.
缺点: 滥用内联将导致程序变慢. 内联可能使目标代码量或增或减, 这取决于内联函数的大小. 内联非常短小的存取函数通常会减少代码大小, 但内联一个相当大的函数将戏剧性的增加代码大小. 现代处理器由于更好的利用了指令缓存, 小巧的代码往往执行更快。

```c++
//eg:
int add(int m,int n);//申明
//当然申明前也可以放，关键字 inline 必须与函数定义体放在一起才能使函数成为内联，仅将 inline 放在函数声明前面不起任何作用。
inline int add(int m,int n)//定义
{
    return m+n;
}
//语法
inline 返回值类型 函数名 (形参表)
{
    函数体;
}
```

结论：

1.不要内联超过十行的函数

2.不要内联带循环，switch的函数，不要内联递归函数和虚函数

3.不要使用过多的内联函数

### 三、函数重载

##### 一、定义

函数重载是一种特殊情况，C++允许在同一作用域中声明几个类似的同名函数，这些同名函数的形参列表（**参数个数，类型，顺序**）**至少一个不同**，常用来处理实现功能类似数据类型不同的问题。

- **函数名称必须相同**。
- **参数列表必须不同（个数不同、类型不同、参数排列顺序不同等）。**
- **函数的返回类型可以相同也可以不相同。**
- **仅仅返回类型不同不足以成为函数的重载。**

在C++中不仅函数可以重载，运算符也可以重载。例如： 运算符<<,>>。既可以做移位运算符，也可以做输出，输入运算符。

```c++
//eg:
#include<iostream>
using namespace std;
 
int Add(int a, int b)
{
	return a + b;
}
 
double Add(double a, double b)
{
	return a + b;
}
 
float Add(float a, float b)
{
	return a + b;
}
int main()
{
	cout<<Add(1,2)<<endl;
	cout<<Add(3.5, 4.5)<<endl;
	cout << Add(2.22, 3.33) << endl;
	return 0;
}
```

##### 二、可能的问题-二义性

精确匹配：

```c++
#include<iostream>
#include "string.h"
using namespace std;

void MyCout(long n)
{
    cout << "参数为长整形！" << endl;
}

void MyCout(int n)
{
    cout << "参数为整形！" << endl;
}

int main()
{
    long a = 100;
    int b = 200;
    MyCout(a);
    MyCout(b);
    system("pause");
    return 0;
}
```

多个匹配导致二义性

```c++
#include<iostream>
#include "string.h"
using namespace std;

void MyCout(double n)
{
    cout << "参数为整形！" << endl;
}

void MyCout(char n)
{
    cout << "参数为字符指针！" << endl;
}

void MyCout(unsigned int n)
{
    cout << "参数为double！" << endl;
}

int main()
{
    int a=100;
    MyCout(a);
    system("pause");
    return 0;
}
```

解决方案：**在使用函数重载时推荐使用精准匹配进行函数重载，以便避免出现二义性！避免使用如int\*和char\*这样的难以辨识的参数作为重载区分**

### 四、函数参数缺省

##### 一、定义 

有一些参数的值在每次函数调用时都相同，书写这样的语句会使人厌烦。C++语言采用参数的缺省值使书写变得简洁（在编译时，缺省值由编译器自动插入）。 

##### 二、内容

```c++
int add(int x,int y=10); //函数声明
int add(int x,int y  /*= 10*/) 一般讲函数定义时的
{
 return x+y;
}
/*如果在函数声明的时候设置了缺省参数的值，那么在函数定义的时候就不能在设置缺省参数了
需要注意的有：
默认的缺省只可以从右到左缺省，不可以缺省左边的参数，或者中间的参数
调用缺省参数的函数是从左往右初始化值的*/
```

### 五、引用

```c++
int y=3;
int &x=y;
//引用实际上就是变量的别名,x，y两个变量使用的是同一片内存
```

```c++
 int& zhangsan; //不行，引用必须初始化，要知道是给谁取别名嘛
//给一个别名取别名之后是可以再给别名进行取别名的
//也可以给同一个变量取多个别名
int&a=x;
int& b=a;
引用初始化后不能更改
例如：
int x=y=10;
int &a=x;
a=y; //这样只是改变x的值，并不是改变a的引用
不可以出现两个&& 没有引用的引用     &&a; //错误
引用是不占内存的,引用用作函数参数，是不会进行拷贝，提高了程序的效率
/*指针和引用的不同之处：
指针变量是占用内存的，但是引用是完全不占内存的，和原来的变量是用的同一片内存，有指针的引用，没有引用的指针*/
```

将函数返回值使用引用：

```c++
int& fun(int& x,int &y)
{
//Int temp=5;
//Return temp; 不可以，函数引用不可以返回一个临时变量，因为函数执行完之后，临时变量就被释放掉了，那么变量都没有了，还需要给谁起别名呢，给鬼吗
    X=x+5;
    return x; 那么为什么这样可以呢,因为x是一个引用，不是一个局部变量
}
//函数的引用必须返回的是一个有效的空间。
```

### 六、new和delete

```c++
//使用new动态申请内存：
   int *p=new int;
   int *p==new int(666); //将*P初始化为666，之所以可以这样写是因为构造函数的原因
```

```c++
//申请数组：
   int *p=new int[10];
   int *pArr=new int[10]{0,1,2,3,4,5,6,7,8,9}; //初始化申请的数组
```

```c++
//释放内存：
  delete p;
  P=nullptr; 
  delete[] pArr;

//如果delete一个内存之后，再来一次delete这是很危险的，你如果在后面申请到同一个地址的内存，那么刚申请就被释放掉了，就会出现非法操作现象
```

### 七、命名空间

#include<iostream>     //输入输出流  cout <<   cin >>

Using namespace std;   //这是使用的系统中的名字叫做std的命名空间

##### 一、如何定义命名空间

Namespace    zhangsan

{
//可以定义变量、函数、类、结构体，都行

Int age;

}

##### 二、使用命名空间中的变量

第一种  zhangsan::变量名

第二种 using  zhangsan::变量名

表示从这句话开始，以下所有的该变量都是使用zhangsan中的变量 ，并且不可以重新定义

第三种 using namespace  zhangsan（放在局部）;

表示从这句话开始使用的变量会在zhangsan命名空间中找

第四种 将using namaspace zhangsan;语句直接放在全局中（最正常的人使用）

::   限定符表示后面的变量是属于哪个空间中的

如果在命名空间中有一个fun()函数，然后还有一个全局的函数fun()那么，并且还有 using namaspace zhangsan;这一句话，这时你如果在main函数中调用fun();的话肯定是不行的，因为编译器会不知道你要使用的是哪一个的fun()

那么你可以这样使用全局中的fun()函数

::fun(); //::  作用说明是全局的

这样使用命名空间中的fun()函数

Zhangsan::fun();

注意：命名空间不可以在局部进行定义，可以在局部进行使用

另外还需要注意的是局部中定义的变量和全局命名空间（指的是using namespace zhangsan;这句话放在了主函数外边）中的是不冲突的，编译器会采取就近原则进行使用

在一个程序中是可以使用多个命名空间的，但是要注意尽量避免不要连续声明多个命名空间，因为可能会出现冲突

##### 三、命名空间的嵌套：

#####  四、命名空间的合并：

可以定义重复名字的命名空间，这样就会将两个合成一个进行处理

```c++
namespace {
   int age=10;
}
这样的就是全局命名空间和static是类似的，只可以在当前文件中使用
如何使用全局命名空间中的变量：
Cout<<age<<endl;或者cout<<::age<<endl;
那么如果在来一个全局变量
 int age=30;
这样的也是可以的，因为全局命名空间中的age在{}之中的，和全局变量age并不冲突
但是在使用的时候必须加上限定符::并且使用的是全局的age，不是namespace中的age,吧并且namespace中的age是无法再被访问
```



```c++
//如果有这样的命名空间：
namaspace    zhangsan
{
	int age = 1;
	namespace   lisi
	{
		int age = 2;
		namespace  wangwu
		{
			int age = 3;
		}
	}
}
那么就需要一步一步的进行访问：
访问wangwu中的age  zhangsan::lisi::wangwu::age;
或者这样：
namespace  MM=zhangsan::lisi::wagnwu;
MM::age;
注意不可以使用typedef zhangsan::lisi::wangwu;因为typedef只可以重定义数据类型
```

##### 五、补充

```c++
上课补充：
//命名空间有什么用？
管理代码
//是什么，如何使用，在什么地方使用？
{}花括号分为两种：第一种定义域，第二种 作用域
作用域分号可加可不加，定义域必须加分号
命名空间使用的是作用域式的花括号,分号可加可不加
```

### 八、cin和cout

##### 一、使用

```c++
输入输出：
Int  i =  0x123; //虽然0x123是16进制数，但是cout<<默认的是按10进制数来输出的
使用cout<<输出16进制数
Cout<<hex<<i; //这样输出的就是0x123了

使用cout按不同的进制进行输出（设置一次始终有效）：

16进制：hex

10进制：dec

8进制：oct
没有二进制
注意：在函数中使用的cout也是已经被设置之后的cout，因为cout是一个对象，在一个地方设置好之后，其他地方的该对象肯定也被改变了
    
设置cout的输出样式：
//设置打印得宽度：
Cout.width(5); （一次有效）

//设置默认的填充字符：（一次有效）不可以在右边填充
Cout.fill(‘$’);

//设置精度： （始终有效）
Cout.precision(5); 设置精度为5包括整数部分，尾部的0不会打印，如果不足5位，只会打印原数

```

##### 二、打印特殊设置

```c++
打印特殊设置：（始终有效）
//打印true或false
cout.setf(ios_base::boolpha);

//设置打印小数点之后的0
Cout.setf(ios_base::showpoint);

//打印正整数数之前的+号：
Cout.setf(ios_base::showpos);

//打印16进制之前的0x：
Cout.setf(ios_base::showbase);
```

### 九、类string//未整理

1. 概述
string是C++标准库的一个重要的部分，主要用于字符串处理。可以使用输入输出流方式直接进行string操作，也可以通过文件等手段进行string操作。同时，C++的算法库对string类也有着很好的支持，并且string类还和c语言的字符串之间有着良好的接口。

2. 常见用法
2.1 string转换为char*
方法一：使用 c_str() 方法，代码（stringsimple.cpp）如下：

```c++
#include <string>
#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    string strOutput = "Hello World";
cout << "[cout] strOutput is: " << strOutput << endl;
 
// string 转换为 char*
const char* pszOutput = strOutput.c_str();

printf("[printf] strOutput is: %s\n", pszOutput);
 
return 0;
}
```
编译并执行上述代码，结果如下：

 ![img](https://img-blog.csdn.net/20180529171716402?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpaXRkYXI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70) 

上述代码执行结果说明：

cout 可直接输出 string 类的对象的内容；
使用 c_str() 方法转换 string 类型到 char* 类型时，需要为char*添加 const 关键字；
printf() 函数不能直接打印 string 类的对象的内容，可以通过将 string 转换为 char* 类型，再使用 printf() 函数打印。
2.1.1 data()方法与c_str()方法
data()方法与c_str()方法相似，都返回 const char* 类型。两者区别和联系如下：

在C++98版本中，c_str()返回 const char* 类型，返回的字符串会以空字符（null character）结尾；
在C++98版本中，data()返回 const char* 类型，返回的字符串不以空字符（null character）结尾；
在C++11版本中，c_str()与data()用法相同（Both string::data and string::c_str are synonyms and return the same value.）
2.2 计算string长度、string字符串比较
示例代码如下：

```c++
#include <string>
#include <iostream>

#define HELLOSTR "Hello World"

using namespace std;

int main()
{
    string strOutput = "Hello World";
int nLen = strOutput.length();
 
cout << "the length of strOutput is: " << nLen << endl;
 
if (0 == strOutput.compare(HELLOSTR))
{
    cout << "strOutput equal with macro HELLOSTR" << endl;
}
 
return 0;
}

```
编译并执行上述代码，结果如下：

```c++
[root@node1 /opt/liitdar/mydemos/simples]# ./stringsimple2 
the length of strOutput is: 11
strOutput equal with macro HELLOSTR
[root@node1 /opt/liitdar/mydemos/simples]# 
```

上述代码执行结果说明：

string类型可直接使用 length() 方法计算字符串长度，该方法计算结果为字符串的实际长度，如本例中"Hello World"字符串的长度为11；
string类型可使用 compare(const string& str) 方法进行字符串比较。
2.3 string对象判空
可使用 empty() 方法对string类型的对象进行判空，如下：

    if (str2.empty())
    {
        cout << "str2 is empty." << endl;
    }
2.4 char*、char[]转换为string
将 char*、char[] 转换为 string 类型时，直接进行赋值操作，将 char*、char[] 的变量赋值给 string 对象即可。

说明：这里所说的“赋值”操作，实际上是将 char*、char[] 定义的字符串的首地址赋值给 string 对象了。

示例代码（stringtochar.cpp）如下：

```c++
#include <string>
#include <iostream>

using namespace std;

int main()
{
    const char* pszName = "liitdar";
    char pszCamp[] = "alliance";
string strName;
string strCamp;
 
strName = pszName;
strCamp = pszCamp;
 
cout << "strName is: " << strName << endl;
cout << "strCamp is: " << strCamp << endl;
 
return 0;
}

```
 编译并执行上述代码，结果如下：

![img](https://img-blog.csdn.net/20180709093415439?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpaXRkYXI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70) 

2.5 string类的find方法
使用string类的find方法，在字符串中检索自字符串是否存在。

2.5.1 用法
用法如下：

size_t find (const string& str, size_t pos = 0) const;
size_t find (const char* s, size_t pos = 0) const;
size_t find (const char* s, size_t pos, size_t n) const;
size_t find (char c, size_t pos = 0) const;
2.5.2 返回值
find函数返回值：

The position of the first character of the first match. If no matches were found, the function returns string::npos.

size_t is an unsigned integral type (the same as member type string::size_type).

2.5.3 示例代码
find方法的示例代码（string_find_test1.cpp）如下：

```c++
#include <string>
#include <iostream>

using namespace std;

int main()
{
    // 待检索的字符串
    string strOutput = "|0|1|2|";
    // 需要检索的子串
    string strObj = "|1|";
// 子串位于字符串中的位置
size_t nLoc = strOutput.find(strObj);
// 如果检索到子串在字符串中，则打印子串的位置
if (nLoc != string::npos)
{
    cout << "nLoc is: " << nLoc << endl;
}
 
return 0;
}
```
编译并执行上述代码，结果如下：

![img](https://img-blog.csdn.net/20180821151551816?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpaXRkYXI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70) 

2.6 string类的insert方法
使用string类的insert方法，向字符串中插入字符（串）。官方的定义如下：

Inserts additional characters into the string right before the character indicated by pos (or p).

2.6.1 用法

![1639197816069](C:\Users\Π\AppData\Roaming\Typora\typora-user-images\1639197816069.png)

2.6.2 示例代码
insert方法的示例代码（string_insert_test1.cpp）如下：

```c++
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string strDemo = "I am";
strDemo.insert(4, " good.");
 
cout << "strDemo is: " << strDemo << endl;
 
return 0;
 }
```


编译并执行上述代码，结果如下：

 ![img](https://img-blog.csdnimg.cn/20190108090050486.png) 

2.7 int类型转为string类的方法
这里介绍两种常见的 int 类型转换为 string 类的方法，示例代码如下：

```c++
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

int main()
{
    // 方法1
    int nNum1 = 123;
    stringstream ss;
ss << nNum1;
string strTest1 = ss.str();
cout << "strTest1 is: " << strTest1 << endl;
 
/*
string strTest2;
strTest2 << ss;     // stringstream 未定义 << 操作符，故此句报错
cout << "strTest2 is: " << strTest2 << endl;
*/
 
string strTest3;
ss >> strTest3;
cout << "strTest3 is: " << strTest3 << endl;
 
// 方法2
int nNum2 = 456;
string strTest4;
strTest4 = to_string(nNum2);    // C++11 标准
cout << "strTest4 is: " << strTest4 << endl;
 
return 0;
}
```
编译并执行上述代码，结果如下：

 ![img](https://img-blog.csdnimg.cn/20190313112439858.png) 

### 十、补充

1.三目运算符的值是变量，可修改，可赋值

2.函数必须有返回类型

3.const 是真的常量

4.