 **C++与Java的语法区别**

首先，两个大的不同是主函数和怎样编译的不同，接下来是许多小的区别。

**main 函数
C++**
//自由浮动的函数
int main( int argc, char* argv[])
{
  printf( "Hello, world" );
}
**Java**
// 每个函数都必须是一个类的一部分;当java <class>运行是一个特定类的主函数会被调用
// (因此你可以让每个类都有一个main函数，这在写单元测试是很有用)
class HelloWorld
{
  public static void main(String args[])
  {
    System.out.println( "Hello, World" );
  }
}


**类的声明**
除了 Java 不要求用分号外几乎是相同的。
**C++**
  class Bar {};

**Java**
  class Bar {}
  **方法声明**
  都相同的, 除了在Java,方法必须总是 某个类的一部分并且可能public/private/protected 作为修饰
**构造函数和析构函数
**构造函数都是相同的 (即类的名字), Java没有准确意义上的的析构函数**静态成员函数和变量**
方法声明是相同的, 但 Java 提供静态初始化块来来初始化静态变量 (不需要在源文件中声明):
class Foo
{
  static private int x;
  // 静态初始化块
  { x = 5; }
}
**对象的声明**
**C++**
  // 在栈中
  myClass x;

  //或者在堆中
  myClass *x = new myClass;

**Java
**  // 总是在对堆中声明
  myClass x = new myClass();

**继  承**
**C++
**  class Foo : public Bar
  { ... };

**Java
**  class Foo extends Bar
  { ... }

**访问级别 (abstraction barriers)
C++**
  public:
    void foo();
    void bar();

**Java
**  public void foo();
  public void bar();

**虚函数**
**C++**
  virtual int foo(); // 或者非虚函数写作 int foo();

**Java**
  // 函数默认的就是虚函数; 用final关键字防止重载
  int foo(); // 或者, final int foo();
**内存管理
**大体上是相同的--new 来分配， 但是 Java没有 delete，因为它有垃圾回收器。**NULL vs null**
**C++**
  // 初始化一个指针为 NULL
  int *x = NULL;

**Java**
  // 编译器将捕获使用未初始化的引用
  //但是如果你因需要初始化一个引用而赋一个null，那么这是无效的
  myClass x = null;

**布尔型**
Java有一点罗嗦: 你必须写 boolean而不止是 bool.
**C++**
  **bool foo;
****Java**
   boolean foo;
**常  量**
**C++**
  const int x = 7;

**Java**
  final int x = 7;

**抛异常**
首先，Java在编译器强制抛异常—如果你的方法可能会抛异常你必需明确报告
**C++**
   int foo() throw (IOException)
**Java**
   int foo() throws IOException
**数   组**
**C++**
  int x[10];
  // 或
  int *x = new x[10];
  // 使用 x,然后归还内存
  delete[] x;

**Java
**  int[] x = new int[10];
  // 使用 x, 内存有垃圾回收器回收或
  //或在程序生命周期尽头归还给系统

**集合和迭代器
C++**
迭代器是类的成员。范围的开始是<容器>.begin(), 结束是 <容器>.end()。 用++ 操作符递增, 用 *操作符访。 
  vector myVec;
  for ( vector<int>::iterator itr = myVec.begin();
     itr != myVec.end();
     ++itr )
  {
    cout << *itr;
  }

**Java**
迭代器只是一个接口。 范围的开始是 <集合>.iterator，你必须用itr.hasNext()来查看是否到达集合尾。 使用itr.next()(是在C++中使用操作符++ 和*操作的结合)来获得下一个元素。 
  ArrayList myArrayList = new ArrayList();
  Iterator itr = myArrayList.iterator();
  while ( itr.hasNext() )
  {
    System.out.println( itr.next() );
  }

  // 或, 在Java 5中
  ArrayList myArrayList = new ArrayList();
  for( Object o : myArrayList ) {
    System.out.println( o );
  }


**抽象类**
**C++
**  // 只需要包含一个纯虚函数
  class Bar { public: virtual void foo() = 0; };

**Java**
  // 语法上允许显示的声明!
  abstract class Bar { public abstract void foo(); }

  // 或者你也可以声明一个接口
  interface Bar { public void foo(); }

  // 然后让一个类继承这个接口:
  class Chocolate implements Bar
  {
    public void foo() { /* do something */ }
  }

**引用 vs 指针**
**C++**
  //引用不可改变,通过使用指针来获得更多的灵活性
  int bar = 7, qux = 6;
  int& foo = bar;

**Java**
  // 引用是可变的，仅存储对象地址;
  //没有指针类型
  myClass x;
  x.foo(); // error, x is a null ``pointer''

  // 注意你要总是用 . 来访问域

**编 译**
**C++**
   // 编译
  g++ foo.cc -o outfile
  // 运行
  ./outfile

**Java
**  // 编译foo.java文件中的类成<classname>.class  javac foo.java
  // 通过调用<classname>中的静态main方法来运行
  java <classname>

**注  释**
两种语言是一样的 (// 和 /* */ 可以用)