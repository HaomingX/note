## 一、windows编程

我们之前编程常用的”黑屏“叫控制台应用程序(Win32 Console Application)，也称DOS程序（或MS-DOS程序）。DOS是早期的命令式操作系统，很难做出漂亮的界面，除了开发人员，”黑屏“对普通用户很不友好。

带界面的程序叫Windows应用程序(Win32 Application)。Windows是一款现代操作系统，带有丰富的交互界面，使用简单，无需记忆繁杂的命令。

C语言只是一种工具，需要与Windows系统结合，借助Windows提供的函数才能开发出漂亮的程序。

## 二、Windows API的概念

在C语言中，使用fopen()函数可以打开一个文件，感觉非常简单。文件保存在硬盘上，要经过复杂的处理才能显示，这些细节对我们来说是透明的，由操作系统完成。也就是说，我们调用fopen()函数来通知操作系统，让操作系统打开一个文件。

那么，我们如何告诉操作系统打开文件呢？

看似简单的操作到底层都非常复杂，打开文件首先要扫描硬盘，找到文件的位置，然后从文件中读取一部分数据，将数据放进I/O缓冲区，放进内存；这些数据都是0、1序列，还要对照ASCII表或Unicode表”翻译“成字符，再在显示器上显示出来。这个过程如果要让程序员来完成，那简直是噩梦！

怎么办呢？Windows想了一个很好的办法，它预先把这些复杂的操作写在一个函数里面，编译成动态链接库(DLL)，随Windows一起发布，程序员只需要简单地调用这些函数就可以完成复杂的工作，让编程变得简单有趣。

这些封装好的函数，叫做 API(Application Programming Interface)，即应用程序编程接口。

API 函数以C语言的形式向外暴露，可以通过C语言直接调用。

除了函数，Windows 还预先定义了很多数据类型（使用C语言的 typedef 关键字定义）。广义上来说，这些数据类型也是 API 的一部分。

API 屏蔽了很多细节，大大简化了程序员的工作，这就是操作系统的威力，不但让普通用户使用方便，也让程序员如释重负。

在Windows上运行的程序（包括MS-DOS程序），本质上都是通过调用Windows API来完成功能的，包括QQ、360、VC6.0等，别看这些团队牛，也不可能从底层做起，那简直不可想象。

C语言也一样，也是调用Windows API，fopen() 函数就是通过调用 CreateFile() 函数实现的。CreateFile() 是Windows API中的一个函数，可以用来打开或创建文件。

通常所说的 SDK 编程就是直接调用API 函数进行编程。SDK 是 Software Development Kit 的缩写，即软件开发工具包。

Windows API 函数成千上万，详细了解每一个函数的用法是不可能的，也是完全没有必要的。只需知道哪些功能由哪些API 函数提供就行了，等使用它们时再去查阅帮助文件。

带界面的程序的专业称呼是GUI程序。GUI 是 Graphical User Interface 的简写，即图形用户界面。接下来将使用 Windows API 来编写GUI程序，编程语言为C语言。

## 三、第一个真正的windows程序

编写Windows程序，首先要包含 windows.h 头文件。windows.h 还包含了其他一些Windows头文件，例如：

- windef.h：基本类型定义
- winbase.h：内核函数
- wingdi.h：用户接口函数
- winuser.h： 图形设备接口函数


这些头文件定义了Windows的所有数据类型、函数原型、数据结构和符号常量，也就是说，所有的Windows API都在这些头文件中声明。

在C语言中，程序都是“黑屏”的，称为控制台程序(Console Application)。这套教程要讲的是带界面的Windows程序(Windows Application)，也称为GUI程序(GUI Application)。

控制台程序以 main() 为入口函数，Windows程序以 WinMain() 为入口函数，动态链接库(DLL)以 DllMain() 为入口函数（请查看 [动态链接库DLL教程](http://c.biancheng.net/cpp/html/2753.html)），不同的入口函数决定了不同类型的程序。

WinMain() 函数的原型为：

```c
int WINAPI WinMain(
    HINSTANCE hInstance,  // 当前窗口句柄
    HINSTANCE hPrevInstance,  // 前一个窗口句柄，Win32下为NULL（Win16留下的废物，目前已弃用）
    LPSTR lpCmdLine,  // 命令行参数
    int nCmdShow  // 窗口显示方式
);
```

先不要急于理解这些参数的含义，我先给大家写一个简单的不带黑屏的、真正的Windows程序：

```c
#include <windows.h>

int WINAPI WinMain(
    HINSTANCE hInstance,
    HINSTANCE hPrevInstance,
    LPSTR lpCmdLine,
    int nCmdShow
){
    // 调用API 函数MessageBox
    int nSelect = MessageBox(NULL, TEXT("你好，欢迎来到这里！"), TEXT("Welcome"), MB_OKCANCEL);
    if(nSelect == IDOK){
        MessageBox(NULL, TEXT("你点击了“确定”按钮"), TEXT("提示"), MB_OK);
    }else{
        MessageBox(NULL, TEXT("你点击了“取消”按钮"), TEXT("提示"), MB_OK);
    }

    return 0;
}
```

编译并运行，会弹出一个对话框，如下所示：
![img](http://c.biancheng.net/cpp/uploads/allimg/150713/1-150G3095500E1.png)

点击“确定”或“取消”按钮，又会弹出一个新的提示框。大家可以亲自运行一下，会有真实的体验。

原来没有`main()`函数，没有`#include <stdio.h>`的C语言程序也是可以运行的！

MessageBox() 函数是众多API中的一个，用于弹出一个指定风格的对话框，其原型为：

```c
int WINAPI MessageBox( HWND hWnd, LPCTSTR lpText, LPCTSTR lpCaption, UINT uType );
```

WINAPI 为宏定义`#define WINAPI __stdcall`，表示函数调用方式，暂时可以不理会，不影响代码编写，只需要知道MessageBox()返回值为 int，表示按下的按钮。有兴趣的读者可以查看：[__stdcall，__cdecl，__pascal，__fastcall的区别](http://c.biancheng.net/cpp/html/2847.html)

参数说明：

- hWnd：该消息框的父窗口句柄，如果此参数为NULL，则该消息框没有拥有父窗口。大家不用急于理解这个参数，后续会详细讲解。
- lpText：消息框的内容。LPCTSTR 是自定义数据类型，等价于 const char *。
- lpCaption：消息框的标题。
- uType：对话框的按钮样式和图标。


uType 支持的按钮样式：

| 按钮                | 含义                                   |
| ------------------- | -------------------------------------- |
| MB_OK               | 默认值，有一个“确认”按钮在里面         |
| MB_YESNO            | 有“是”和“否”两个按钮在里面             |
| MB_ABORTRETRYIGNORE | 有“中止”，“重试”和“跳过”三个按钮在里面 |
| MB_YESNOCANCEL      | 有“是”，“否”和“取消”三个按钮在里面     |
| MB_RETRYCANCEL      | 有“重试”和“取消”两个按钮在里面         |
| MB_OKCANCEL         | 有“确定”和“取消”两个按钮在里面         |


这些按钮都是宏定义：

```c
#define MB_OK                0x00000000L
#define MB_OKCANCEL          0x00000001L
#define MB_ABORTRETRYIGNORE  0x00000002L
#define MB_YESNOCANCEL       0x00000003L
#define MB_YESNO             0x00000004L
#define MB_RETRYCANCEL       0x00000005L
```

你也可以尝试用数字来表示按钮，例如：

```c
MessageBox(NULL, TEXT("你好，欢迎来到C语言中文网！"), TEXT("Welcome"), 1);
```

也会生成与上面相同的对话框。

除了按钮，uType 还支持图标（图标对用户有提醒作用）：

| 图标               | 含义                                                         |
| ------------------ | ------------------------------------------------------------ |
| MB_ICONEXCLAMATION | 一个惊叹号出现在消息框：![img](http://c.biancheng.net/cpp/uploads/allimg/141108/1-14110Q0425B47.png) |
| MB_ICONWARNING     | 一个惊叹号出现在消息框（同上）                               |
| MB_ICONINFORMATION | 一个圆圈中小写字母i组成的图标出现在消息框：![img](http://c.biancheng.net/cpp/uploads/allimg/141108/1-14110Q0431R22.png) |
| MB_ICONASTERISK    | 一个圆圈中小写字母i组成的图标出现在消息框（同上）            |
| MB_ICONQUESTION    | 一个问题标记图标出现在消息框：![img](http://c.biancheng.net/cpp/uploads/allimg/141108/1-14110Q043302b.png) |
| MB_ICONSTOP        | 一个停止消息图标出现在消息框：![img](http://c.biancheng.net/cpp/uploads/allimg/141108/1-14110Q04345J6.png) |
| MB_ICONERROR       | 一个停止消息图标出现在消息框（同上）                         |
| MB_ICONHAND        | 一个停止消息图标出现在消息框（同上）                         |


这些图标也都是宏定义：

```c
#define MB_ICONHAND         0x00000010L
#define MB_ICONQUESTION     0x00000020L
#define MB_ICONEXCLAMATION  0x00000030L
#define MB_ICONASTERISK     0x00000040L
```


如果希望同时定义按钮和图标的样式，可以使用或运算`|`，例如：

```c
MessageBox( NULL,TEXT("你好，欢迎来到C语言中文网！"),TEXT("Welcome"),    MB_OKCANCEL | MB_ICONINFORMATION);
```

会弹出如下的对话框：
![img](http://c.biancheng.net/cpp/uploads/allimg/150713/1-150G3100240611.png)

与上面的对话框相比，多出了一个图标，同时还能听到提示音（Win7 有，XP 和 Win8 读者可以亲自测试）。

大家有没有发现，按钮都是用十六进制的第1位（二进制前4位）来表示，图标都是使用十六进制第2位（二进制第5~8位）来表示，进行或运算，每个位都不会改变，如下图所示：
![img](http://c.biancheng.net/cpp/uploads/allimg/141108/1-14110Q126035L.png)

Windows 通过检测第1位的值来确定按钮的样式，检测第2位的值来确定图标样式。

再看来一下MessageBox() 的返回值。

MessageBox() 返回被按下的按钮，以数字表示，这些数字都被定义成了宏，如下所示：

| 返回值   | 含义                 |
| -------- | -------------------- |
| IDOK     | 用户按下了“确认”按钮 |
| IDCANCEL | 用户按下了“取消”按钮 |
| IDABORT  | 用户按下了“中止”按钮 |
| IDRETRY  | 用户按下了“重试”按钮 |
| IDIGNORE | 用户按下了“忽略”按钮 |
| IDYES    | 用户按下了“是”按钮   |
| IDNO     | 用户按下了“否”按钮   |


对应的宏定义为：

```c
#define IDOK     1
#define IDCANCEL 2
#define IDABORT  3
#define IDRETRY  4
#define IDIGNORE 5
#define IDYES    6
#define IDNO     7
```





## 四、windows数据类型

Windows使用`typedef`或`#define`定了很多新的数据类型，前面几节中我们已经领略到了。它们虽然多，但是都有规律可循，很多都是对C/C++中数据类型的简单加工，而且很容易“见名知意”。要想学习Windows编程，必须要了解常用的数据类型。

如果你对C语言或者C++的数据类型比较熟悉的话，那么对于一些基础的内容这个过程就是慢慢熟悉的过程。

这些数据类型在windows.h头文件中定义：

```c
typedef int                 INT;       /* 整形 */
typedef unsigned int        UINT;      /* 无符号整形 */
typedef unsigned int        *PUINT;    /* 无符号整形指针 */
typedef int                 BOOL;      /* 布尔类型 */
typedef unsigned char       BYTE;      /* 字节 */
typedef unsigned short      WORD;      /* WORD (无符号短整型) */
typedef unsigned long       DWORD;     /* DOUBLE WORD (无符号长整形)*/
typedef float               FLOAT;     /* 浮点型 */
typedef FLOAT               *PFLOAT;   /* 指向float类型指针 */
typedef BOOL near           *PBOOL;    /* 指向布尔类型指针 */
typedef BOOL far            *LPBOOL;
typedef BYTE near           *PBYTE;    /* 指向字节类型指针 */
typedef BYTE far            *LPBYTE;
typedef int near            *PINT;     /* 整形指针 */
typedef int far             *LPINT;
typedef WORD near           *PWORD;    /* 指向WORD类型的指针 */
typedef WORD far            *LPWORD;
typedef long far            *LPLONG;   /* 指向长整形的指针 */
typedef DWORD near          *PDWORD;   /* 指向DWORD类型的指针 */
typedef DWORD far           *LPDWORD;
typedef void far            *LPVOID;   /* 指向void类型的指针 */
typedef CONST void far      *LPCVOID;  /* 指向void类型的常指针 */
```

简单说下，大部分类型都没有什么离奇的地方，可能很多读者会对那个 far 和 near 觉得有疑问，实际上 F12 查看定义会发现他们就定义上方：

```
#define far
#define near
```

看到这里你是否还是有疑问？其实，这个 far 和 near 只是用来标识变量的新旧的（预处理阶段 far 和 near 会被替换成空字符串）。 例如 PINT 和 LPINT 实际上都是 int *，只不过一个是老式写法，一个是新式写法，这都是为了兼容问题。

简单的看下这些数据类型，就可以总结出：但凡是以 “P” 开头的都是指针（pointer）类型（"LP"是老式写法）。撇开这些不谈，那么实际上这些 Windows API 常用的一些数据结构跟我们原本所学的 C/C++ 变量差别就是一个 typedef 而已，基础好的熟悉一下就行了。不过，也不要想得这么简单，Windows 编程还有一些比较复杂的类型比如 HWND、HANDLE 等。

在碰到不熟悉的类型时请熟练的使用 “右键转到定义” 或者 F12。 大家不用太过害怕这些复杂的类型名称，Windows 数据类型并不是内建的数据类型类型，而都是从C类型重定义得到的。

Windows 数据类型名命名的规律

- 无符号类型：一般是以“U”开头，比如“INT”对应的“UINT”。
- 指针类型：其指向的数据类型前加“LP”或“P”，比如指向 DWORD 的指针类型为“LPDWORD”和“PDWORD”。
- 句柄类型：以“H”开头。比如，HWND 是window（WND简写）也就是窗口的句柄，菜单(MENU)类型对应的句柄类型为 “HMENU” 等等。



## 五、宽字符和unicode

在C语言中，我们使用char来定义字符，占用一个字节，最多只能表示128个字符，也就是ASCII码中的字符。计算机起源于美国，char 可以表示所有的英文字符，在以英语为母语的国家完全没有问题。

但是世界上存在很多不同的语言，例如汉语、汉语、日语等有成千上万个字符，需要用多个字节来表示，称之为宽字符(Wide Character)。Unicode 是宽字符编码的一种，已经被现代计算机指定为默认的编码方式，Windows 2000以后的操作系统，包括Windows 2000、XP、Vista、Win7、Win8、Win10、Windows Phone、Windows Server 等（它们统称为 Windows NT）都从底层支持Unicode，存取效率比 char 要高。

更多内容请查看：[ASCII编码与Unicode编码](http://c.biancheng.net/cpp/html/2840.html)

### ①C语言中的宽字符

在C语言中，使用`wchar.h`头文件中的`wchar_t`来定义宽字符，例如：

```c
wchar_t ch = 'A';
```

wchar_t 被定义为`typedef unsigned short wchar_t`，和一个无符号整型一样，占用两个字节。

如果定义宽字符串，需要加前缀`L`，例如：

```c
wchar_t *str = L"C语言中文网";
```

`L`是必须要加的，并且与字符串之间不能有空格，只有这样编译器才知道每个字符占用两个字节。

宽字符示例：

```c
#include <stdio.h>
#include <wchar.h>
int main(){
    char ch = 'A';
    wchar_t wch = 'A';
    char str[] = "C语言中文网";
    wchar_t wstr[] = L"C语言中文网";
    printf("ch=%d, wch=%d, str=%d, wstr=%d\n", sizeof(ch), sizeof(wch), sizeof(str), sizeof(wstr));
    return 0;
}
```

运行结果：
ch=1, wch=2, str=12, wstr=14

wstr 之所以比 str 多两个字节是因为：字符 'C' 占用两个字节，字符串结束标志 '\0' 也占用两个字节。

### ②宽字符串的长度

计算ASCII字符串长度使用 strlen 函数，计算宽字符串长度使用 wcslen 函数：

```c
#include <stdio.h>
#include <wchar.h>
#include <string.h>
int main(){
    char str[] = "C语言中文网";
    wchar_t wstr[] = L"C语言中文网";
    printf("strlen(str)=%d, wcslen(wstr)=%d\n", strlen(str), wcslen(wstr));
    return 0;
}
```

运行结果：
strlen(str)=11, wcslen(wstr)=6

strlen 的运行结果显然不正确，因为它把一个字节作为一个字符计算，而 wcslen 把两个字节作为一个字符计算。

> 注意：wcslen 在 string.h 和 wchar.h 头文件中均有说明。

### ③维护一个版本的源代码

在 Windows NT 以前的操作系统中，甚至包括 Windows 98，对宽字符的支持都不是很好，所以大多情况下使用ASCII编码。Windows NT 推出以后，已经从底层支持了Unicode，所以在 Windows NT 上的程序大多使用Unicode。

如果你希望程序能够在各种版本的Windows操作系统中运行，那么就需要维护两个版本的源代码，ASCII 版和 Unicode 版。ASCII 字符和 Unicode 字符的定义、使用都不一样，要想在一个版本的源代码中做兼容处理会非常困难，要做大量的工作，对程序员来说简直是噩梦。

不过，Windows 又为我们做了一件好事，已经处理了兼容性问题。它是怎么做到的呢？

例如对于字符串，ASCII 中使用 char 来定义，而 Unicode 中使用 wchar_t 来定义，并且需要添加前缀`L`。那么在 windows.h 头文件中（或者是它包含的其他头文件）就这样来处理：

```c
#ifdef UNICODE
typedef wchar_t TCHAR;
#define TEXT(quote) L##quote
#else
typedef char TCHAR
#define TEXT(quote) quote
#endif
```

我们在源码中可以这样来使用：

```c
TCHAR str[] = TEXT("C语言中文网");
```

如果是Unicode版，也就是定义了UNICODE宏，那么上面的语句等价于：

```c
wchar_t str[] = L"C语言中文网";
```

如果是ASCII，也就是没有定义UNICODE宏，那么等价于：

```c
char str[] = "C语言中文网";
```

在Windows中，随处可见这样的处理。虽然现代操作系统都已经支持Unicode，无需再考虑与ASCII的兼容性问题，但是依然要为这些历史问题付出代价。

总结：由于各种各样的原因，我们优先使用Windows定义的数据类型、宏、结构体等，这样编写的程序兼容性较好，不用考虑ASCII和Unicode的问题。但这也带来了一个挑战，就是要熟悉Window定义的数据类型、宏、结构体等。





## 六、与windows编程有关的重要概念

### 窗口

窗口的概念很容易理解，就是我们使用软件时看到的界面。Windows 的核心就是窗口，它是Windows一统PC操作系统市场的杀手锏，如下图所示：

![img](http://c.biancheng.net/cpp/uploads/allimg/150723/1-150H3152122196.png)
图1：记事本程序


我们使用的软件都有自己的窗口，比如 QQ、计算器、记事本等。这些窗口可以包含输入框、下拉菜单、单选按钮、多选按钮、文本区域等各种各样的控件(Controls)，有的甚至还有动画！

窗口、控件、图像、音频视频等都称为资源(Resource)，在程序中都可以使用、创建、添加、修改等。

### 句柄

在Windows编程中，不同窗口、控件、图像等都对应一个唯一的数字（初学者可以理解为 ID），称为句柄(Handle)。通过句柄，程序可以获取对应资源的各种信息，也可以使用、修改、删除该资源。

你可以将句柄理解为学号，你不需要记住学生的姓名、住址、成绩等各种信息，当你需要了解这名学生时，只要去教务处，将学号（句柄）告诉那里的工作人员(Windows)，他就能够帮你找到这个学生。

句柄屏蔽了很多细节，程序员不需要了解背后的机制。例如用 CreateFile() 函数创建文件后会返回一个文件句柄，然后通过这个句柄就可以读写、删除该文件，而不需要了解Windows是如何将句柄与文件关联起来的，也不需要了解句柄到底保存了哪些信息，Windows 是闭源的，这些背后的细节只有微软知道。

### Windows的消息机制

在一般的编程中，我们都是通过 API 函数来调用系统功能，让操作系统来帮我们完成很多工作，例如调用 CreateFile() 函数，操作系统会帮我们创建一个文件，而不需要我们参与任何工作，非常方便。

反过来，操作系统也会“偷懒”，会调用我们程序中的函数，让我们自己处理某些事情。例如用户敲击键盘，操作系统会首先收到通知，但它并不会处理，而是调用程序中的函数，告诉程序用户敲击了键盘，你自己处理好了；如果程序不处理，操作系统才会进行默认的操作。

当然，这不能理解为操作系统“偷懒”，而是给我们一个机会，让我们自行处理某些事情，从而使程序更加灵活和健壮，也让程序员有了更多发挥的空间。

用户敲击键盘、点击鼠标、拖动窗口、选择菜单、输入文字等所有的操作都称为事件(Event)。这与我们平时理解的“事件”是类似的，都表示发生了某些情况，好的或者坏的。

当有事件发生时，Windows 会生成一条消息(Message)，告诉程序发生了什么事情。这与我们平时理解的“消息”是类似，都表示一种传递信息的载体。

那么，Windows 是如何通过消息将发生的事件通知给应用程序的呢？

每当事件发生时，Windows 会生成一条消息，并放到一个由系统维护的队列中。然后，程序会自己从这个队列中获取消息并分析，调用事件处理函数（处理事件的代码也就在这个函数中），对用户的操作进行响应。

> 队列是一种先进先出的数据结构，不明白的请自行Google或百度。

注意：Windows 向队列中分派消息和应用程序从队列中获取消息并不是同步的，Windows 不管队列中有没有消息，不管应用程序有没有处理完毕，只要有事件发生，就会将消息丢进队列，什么时候处理完毕是应用程序的事。

可见，消息是连接 Windows 和应用程序的纽带，Windows 通过消息告诉应用程序发生了什么，应用程序通过消息知道该做什么。

### 消息结构体

消息其实是一个结构体，名字为 MSG，定义为：

```c
typedef struct tagMSG {
    HWND hwnd;
    UINT message;
    WPARAM wParam;
    LPARAM lParam;
    DWORD time;
    POINT pt;
} MSG;
```

Windows 向队列中投递消息，其实就是将一个类型为 MSG 的结构体变量丢进队列。

MSG 结构体中各成员变量的含义如下：
1) hwnd表示消息所属的窗口。用户一般是在程序的窗口下进行操作，所以一个消息一般都是与某个窗口相关联的。例如在某个活动窗口中按下鼠标左键，产生的按键消息就是发给该窗口的。

2) message表示消息类型，是一个数值。在Windows中，消息是由一个数值来表示的，不同类型的消息对应不同的数值。但是由于数值不便于记忆，所以Windows将消息对应的数值定义为WM_XXX宏（WM是Window Message的缩写）的形式，XXX 对应某种消息的英文拼写的大写形式。例如，鼠标左键按下消息是WM_LBUTTONDOWN，键盘按下消息是WM_KEYDOWN，字符消息是WM_CHAR，等等。在程序中我们通常都是以WM_XXX宏的形式来使用消息的。

3) 第三、第四个成员变量wParam和lParam，用于指定消息的附加信息。例如，当我们收到一个字符消息的时候，message成员变量的值就是WM_CHAR，但用户到底输入的是什么字符，那么就由wParam和lParam来说明。wParam、lParam表示的信息随消息的不同而不同。

4) 最后两个变量分别表示消息投递到消息队列中的时间和鼠标的当前位置。