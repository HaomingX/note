### c语言的具体结构

简单来说，一个C程序就是由若干`头文件`和`函数`组成。

### 良好习惯之规范

1.一个说明或一个语句占一行**，例如：包含头文件、一个可执行语句结束都需要**换行**。**

**2.函数体内的语句要有明显**缩进**，**通常以按一下Tab键为一个缩进**。

3.括号要**成对写**，如果需要删除的话也要**成对删除**。

4.当一句可执行语句结束的时候末尾需要有**分号**。

5.代码中所有符号均为**英文半角符号**。

### 有名有姓的C(标识符)

C语言规定，标识符可以是字母`(A～Z，a～z)`、数字`(0～9)`、下划线`_`组成的字符串，并且第一个字符必须是**字母或下划线**。

### 在定义中不允许连续赋值，如`int a=b=c=5;`是不合法的。

![数据类型分类](https://img-blog.csdnimg.cn/img_convert/e671d31452bcdbb9621d33f817b61349.png)

最常用的：

![整型,实型,字符型](https://img-blog.csdnimg.cn/img_convert/6ea6373cf0ab35bd9e20e241315c32d4.png)

注：**C语言中不存在字符串变量，字符串只能存在字符数组中,**这个后面会讲。

整型：

![整型](https://img-blog.csdnimg.cn/img_convert/50d855eadf4a2f953989d0090545a38d.png)

浮点型：

![浮点型](https://img-blog.csdnimg.cn/img_convert/ba3adb33221ba262997156095e8e5b64.png)

### 自动类型转换

数据类型存在自动转换的情况.
自动转换发生在**不同数据类型**运算时，在编译的时候**自动完成**。

![自动转换](https://img-blog.csdnimg.cn/img_convert/cfb12365d13ecd8566a481b7e46155b4.png)

### 强制类型转换

强制类型转换是通过**定义类型转换运算**来实现的。其一般形式为：

```c
(数据类型) (表达式)
```

**在使用强制转换时应注意以下问题：**

1. 数据类型和表达式都必须加括号, 如把`(int)(x/2+y)`写成`(int)x/2+y`则成了把`x`转换成`int`型之后再除`2`再与`y`相加了。
2. **转换后不会改变原数据的类型及变量值，只在本次运算中临时性转换**（表达式值）。
3. 强制转换后的运算结果**不遵循四舍五入**原则。

### 运算符号

C语言中运算符:

※ 算术运算符 ※ 赋值运算符 ※ 关系运算符 ※ 逻辑运算符 ※ 三目运算符

#### 三目运算符

C语言中的三目运算符：`?:`，其格式为：表达式1 ? 表达式2 : 表达式3; （if-else语言）、

运算级

![运算符的优先级](https://img-blog.csdnimg.cn/img_convert/20e9c2e337b881c67d216afe05a275fd.png)

### 循环

break语句与continue语句的区别是:

> break是跳出当前整个循环，continue是结束本次循环开始下一次循环。

### switch-case

![switch](https://img-blog.csdnimg.cn/img_convert/0b65fc0b70d0627398270200874ed4f6.png)

1.在case后的各常量表达式的值不能相同，否则会出现错误。
2.在case子句后如果没有break;会一直往后执行**一直到遇到break;**才会跳出switch语句。
3.switch后面的表达式语句只能是整型或者字符类型。
4.在case后，允许有多个语句，**可以不用{}**括起来。
5.各case和default子句的先后顺序可以变动，而不会影响程序执行结果。
6.default子句可以省略不用。

### 臭名远扬之goto语句

C语言中也有这样的语句，就是`goto`语句，goto语句是一种**无条件分支**语句:

goto 语句标号;

![mark](https://img-blog.csdnimg.cn/img_convert/2850dd78567005e8047055159bbbcffe.png)

### 函数

```c
//定义
类型 函数名(函数参数){
    内容
    return 对应类型变量;（空不返回）
}
//声明
eg:void hanshu(int,int);
注：void函数中如果有return语句，该语句**只能起到结束函数运行的功能。其格式为: return;
//调用
eg:hanshu(5,6);
```

#### 形参和实参

- **形参**是在定义函数名和函数体的时候使用的参数,目的是用来接收调用该函数时传入的参数。
- **实参**是在调用时传递该函数的参数。
- **形参**只有在被调用时才分配内存单元，在调用结束时，即刻释放所分配的内存单元。因此，形参只有在函数内部有效。
- 实参可以是常量、变量、表达式、函数等。
- 在参数传递时，实参和形参在数量上，类型上，顺序上应严格一致，否则会发生**类型不匹配**的错误。

### 递归函数

![递归](https://img-blog.csdnimg.cn/img_convert/af48c62987c6e36901f78576139e4b69.png)

递归最重要的思想：**不要死磕递归过程，而是应该把前面过程都当成已知，通过写递推表达式来完成递归代码**。

### 局部与全局

C语言中的变量，按作用域范围可分为两种，即**局部变量**和**全局变量**。

***局部变量***也称为内部变量。局部变量是在函数内作定义说明的。其作用域仅限于函数内， 离开该函数后再使用这种变量是非法的。在复合语句中也可定义变量，其作用域只在复合语句范围内。**函数内部有与全局变量名称相同的变量全局变量会被隐藏；（更小的地方会隐藏更大的地方的变量）；**

##### ***全局变量***也称为外部变量，它是在函数外部定义的变量。它不属于哪一个函数，它属于一个源程序文件。其作用域是整个源程序。**全局变量未初始化会被赋予0值，指针赋予null；**

![](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202021-10-09%20155759.png)

### 变量存储类别

C语言根据变量的生存周期来划分，可以分为**静态存储方式**和**动态存储方式**。

静态存储方式：是指在程序运行期间分配固定的存储空间的方式。静态存储区中存放了在整个程序执行过程中都存在的变量，如全局变量。

![](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202021-10-09%20155347.png)

![](https://haoming2003.oss-cn-hangzhou.aliyuncs.com/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202021-10-09%20155700.png)

动态存储方式：是指在程序运行期间根据需要进行动态的分配存储空间的方式。动态存储区中存放的变量是根据程序运行的需要而建立和释放的，通常包括：函数形式参数；自动变量；函数调用时的现场保护和返回地址等。

C语言中**存储类别**又分为四类：

自动（auto）、
静态（static）、
寄存器的（register）
外部的（extern）

1、用关键字auto定义的变量为自动变量，auto可以省略，auto不写则隐含定为“自动存储类别”，属于动态存储方式。如：![auto](https://img-blog.csdnimg.cn/img_convert/ce56abb2380367008122be0e9f7db54e.png)

2、用static修饰的为静态变量，如果定义在函数内部的，称之为静态局部变量；如果定义在函数外部，称之为静态外部变量。如下为静态局部变量：

![static](https://img-blog.csdnimg.cn/img_convert/6dee6dc3aabecd7add027c03a868a3bc.png)

注意：静态局部变量属于静态存储类别，在**静态存储区内**分配存储单元，在程序整个运行期间都不释放；**静态局部变量在编译时赋初值，即只赋初值一次**；如果在定义局部变量时不赋初值的话，则对静态局部变量来说，**编译时自动赋初值0（对数值型变量）或空字符（对字符变量）**。

3、为了提高效率，C语言允许将局部变量得值放在CPU中的寄存器中，这种变量叫“寄存器变量”，用关键字register作声明。例如：

![register](https://img-blog.csdnimg.cn/img_convert/70ab0f3e683ea2a572ed2aab7bbde323.png)

注意：只有局部自动变量和形式参数可以作为寄存器变量；一个计算机系统中的寄存器数目有限，不能定义任意多个寄存器变量；**局部静态变量不能定义为寄存器变量。**

4、用extern声明的的变量是外部变量，外部变量的意义是某函数可以调用在该函数之后定义的变量。如：![extern](https://img-blog.csdnimg.cn/img_convert/71ecff3d41fc366a1c008d2e37ae9bc0.png)

### 内部函数与外部函数

在C语言中不能被其他源文件调用的函数称谓内部函数 ，内部函数由static关键字来定义，因此又被称谓静态函数，形式为：

```c
static [数据类型] 函数名([参数])
```

这里的static是对函数的作用范围的一个限定，**限定该函数只能在其所处的源文件中使用**，因此**在不同文件中出现相同的函数名称的内部函数是没有问题的。**
在C语言中能被其他源文件调用的函数称谓外部函数 ，外部函数由extern关键字来定义，形式为：

```c
extern [数据类型] 函数名([参数])
```

C语言规定，在没有指定函数的作用范围时，系统会默认认为是外部函数，因此当需要定义外部函数时extern也可以省略。

### 数组

```c
//声明
数据类型 数组名称[长度];
//初始化（三种）
1.数据类型 数组名称[长度n] = {元素1,元素2…元素n};
2.数据类型 数组名称[] = {元素1,元素2…元素n};
3.数据类型 数组名称[长度n];
数组名称[0] = 元素1; 数组名称[1] = 元素2; 数组名称[n-1] = 元素n;//常利用循环
//当然也能用memset函数初始化数组
```

注意：

```c
1.数组的下标均以0开始；
2.数组在初始化的时候，数组内元素的个数不能大于声明的数组长度；
注：如果采用第一种初始化方式，元素个数小于数组的长度时，多余的数组元素初始化为0；
3.在声明数组后没有进行初始化的时候，静态（static）和外部（extern）类型的数组元素初始化元素为0，自动（auto）类型的数组的元素初始化值不确定(但一定要初始化)。
```

### 数组的遍历(循环)

注意以下几点：

1. 最好**避免出现数组越界访问**，循环变量最好不要超出数组的长度.
2. **C语言的数组长度一经声明，长度就是固定，无法改变**，并且**C语言并不提供计算数组长度的方法**。

#### 数组作为函数参数

1.整个数组当作函数参数，即把**数组名称传入函数**中。

2.数组中的元素当作函数参数，即把数组中的参数传入函数中。

注意：

1. 数组名作为函数实参传递时，函数定义处作为接收参数的数组类型形参既可以指定长度也可以不指定长度。
2. 数组元素作为函数实参传递时，数组元素类型必须与形参数据类型一致。

### 字符串和字符数组

**字符串概念：** 
C语言中字符串就是用双引号括起来的任意字符序列，在字符串中同时也可以包括转义字符，它是以’\0’为结尾的字符数组 
如”helloworld”; 
char *string = “helloworld”; 
**字符数组：** 
用来存放字符的数组，字符数组中每个元素存放一个字符，数组元素的类型为char类型,初始化字符数组的时候最好以’\0’结尾， 
‘\0’是结束符号 
如：char string []= “helloworld”; 
char array [] = {‘h’,’e’,’l’,’l’,’o’,’w’,’o’,’r’,’l’,’d’,’\0’}; 
char array [] = {“helloworld”};

注意：使用字符串初始化字符数组的时候，它比用字符逐个赋值要多占用一个字节，用于存放’\0’,同时字符数组的长度不会去计算’\0’,但是数组占有的字节数会将’\0’算上，是由系统自行来进行处理的

注：**NULL==‘\0’**

**字符数组的输入输出：** 
**注意：输出的时候只要是遇到’\0’符号的时候，就会停止输出** 
\1. 通过循环来将字符数组逐个输入输出 
\2. 将整个字符串一次性进行输出或输入，C语言允许用数组名进行输入一个字符数组,如:

```c
        char a[10];
        scanf("%s",a);
        char b []  = "girl";
        printf("%s",b);
```





```c
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
 
char global_array[5];//全局变量会初始化
int main(int argc,char *argv[]){
    char local_array[5];//局部变量是不会进行初始化的
    char array1[] = {'h','e','l','l','o',' ','w','o','r','l','d','\0'};
    char array2[] = "hello world";
    char array3[] = {"hello world"};
 
    char array4[5] = "helloworld";  
    char array5[20] = "helloworld";
 
    //char  array[6] = {'\0'};初始化类型
    //char array6[10];
    //memset(array6,0,sizeof(array6));//使用memset来对字符数组进行初始化
 
    //字节的长度比字符串的长度要多1
    printf("array1:%s sizeof array1:%d,strlen array1:%d\n",array1,sizeof(array1),strlen(array1));
    printf("array2:%s sizeof array2:%d,strlen array2:%d\n",array2,sizeof(array2),strlen(array2));
    printf("array3:%s sizeof array3:%d,strlen array3:%d\n",array3,sizeof(array3),strlen(array3));
    printf("array4:%s sizeof array4:%d,strlen array4:%d\n",array4,sizeof(array4),strlen(array4));
    printf("array5:%s sizeof array5:%d,strlen array5:%d\n",array5,sizeof(array5),strlen(array5));
 
    char array6[10];
    memset(array6,0,sizeof(array6));//使用memset来对字符数组进行初始化，也可以用来对内存进行初始化
    printf("input a string:\n");//尽量不要数组越界，因为在C 语言中，数组超出其操作内存的范围，不会判错，但是这种是及其不安全的，因为操作的内存很
有可能是其他函数操作的内存
    //scanf("%s",array6);使用scanf读取内容，但是其是不会判断字符串的长度的,空格也会退出
    //fgets可以从文件读取，也可以从标准输入进行读取，使用stdin,使用fgets读取字符串的时候，只能读取字符(数组长度-1)个字符,解决了scanf的问题，同时
也解决了输入空格的问题。
    fgets(array6,sizeof(array6),stdin);
    printf("%s\n",array6);
    return 0;
}
```

输出结果为: 
array1:hello world sizeof array1:12,strlen array1:11 
array2:hello world sizeof array2:12,strlen array2:11 
array3:hello world sizeof array3:12,strlen array3:11 
array4:hello sizeof array4:5,strlen array4:5 
array5:helloworld sizeof array5:20,strlen array5:10

从上面的array4和array5我们可以看出，如果制定数组的长度，那么此时我们输出的字符串是按照数组的长度来进行输出的 
1:如果数组长度大于字符串的长度的时候 ，这个时候，输出是完整的，数组长度为定义的长度，字符串长度是数组中字符的长度 
2:**如果数组长度小于字符串长度的时候，输出是不完整的 ，数组长度这个时候是定义的长度，处处的字符长度也为定义的长度，字符串的长度同样也是定义的长度**

实战注意： 
尽量不要对字符数组长度进行定义，应该把这个长度交给系统来进行分配 
**一般情况下使用memset来对内存进行初始化** 
**一般情况下我们使用fgets来进行字符数组的初始化，而不用scanf,因为fgets很好的解决了输入越界的问题以及数组的空格问题**

下面这个案例就是通过字符数组来计算一句话中单词的平均长度:

```c
#include<stdio.h>
#include<string.h>
 
 
int main(void)
{
    int letter = 0;
    int word_count = 0;
    int flag = 0;
    char array[30] = {'\0'};
    printf("Please input a sentence!\n");
    fgets(array,sizeof(array),stdin);
    int n = strlen(array);
    int i = 0;
    for(i = 0 ; i< n ; i++){
        char  ch  = array[i];
        if(ch == '\n')
            break;
        if(ch == ' '|| ch =='\t'){
            flag = 0;
        }else if(!flag && ch != ' '  && ch != '\t'){
            word_count ++ ;
            flag = 1;
        }
        if(ch != ' '&& ch!='\t'){
            letter++;
        }
    }   
    printf("Average word length:%.1f\n",(float)letter/word_count);
    return 0;
}
```

#### 字符串函数

1.**strlen()获取字符串的长度**，在字符串长度中是不包括‘\0’而且汉字和字母的长度是不一样的。比如：![strlen](https://img-blog.csdnimg.cn/img_convert/caaf3a5678332e230fc40c899fe596c3.png)

注：sizeof是整个容器的大小

2.strcmp()在比较的时候会把字符串先转换成ASCII码再进行比较,返回的结果为0表示s1和s2的ASCII码相等,返回结果为1表示s1比s2的ASCII码大,返回结果为-1表示s1比s2的ASCII码小，例如：![strcmp](https://img-blog.csdnimg.cn/img_convert/5a4a8abb1a10673115829dc157a2bdb8.png)

**注：最多比较到第一个不同的地方一定能分出大小**

3.strcpy()拷贝之后会覆盖原来字符串且不能对字符串常量进行拷贝，比如：

![strcpy](https://img-blog.csdnimg.cn/img_convert/d5f9c993acd5f39994115c3faa6edde8.png)

4.strcat在使用时s1与s2指的内存空间不能重叠，且s1要有足够的空间来容纳要复制的字符串，如：![strcat](https://img-blog.csdnimg.cn/img_convert/ead9e0c88b6b814c9f14db58214f702a.png)

5.strstr得到相同字串。

6.str*chr*函数功能为在一个串中查找给定字符的第一个匹配之处。

### 多维数组用指针实现

```c
//普通实现
int a[5][6];
//指针实现
int*a[10]//指针数组
a[0]=(int*)malloc(num*sizeof(int));
...
```







补充：

1.在scanf中随意使用\n，表示忽略一切空白符直至下一个非空白符出现。

2.用"%*c"(空字符，不存储字符的字符)滤掉回车;

3.字符ASCII码直接比较就是了，同时数组与数字的比较也需要用S[1]<='0'这种方法

4.EOF（-1）表示文件末尾

5.

1. \t \r \n都是转义字符，空格就是单纯的空格，输入时可以输入空格
2. \t 的意思是 ：水平制表符。将当前位置移到下一个tab位置。
3. \r 的意思是： 回车。将当前位置移到本行的开头。
4. \n 的意思是：回车换行。将当前位置移到下一行的开头。
5. \f的意思是：换页。将当前位置移到下一页的开头。

