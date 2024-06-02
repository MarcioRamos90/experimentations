# Libraries

A library is a piece of code that is portable as either a static object or a shared object.

## Static Object

A static object, static library, or `.a` file is a set of intermediate ELF files that are compiled into your program at compile time. The benefit of a static object is that the code is transported inside your final product, you don't need to ship additional libraries. The downside is that your binary will increase in size as code is not shared amongst other processes.

### Compiling

```
# compiling the library 
gcc -o libteehee.o -c ./lib.c 
ar rcs libteehee.a libteehee.o

# adding the library to a project 
gcc -o main main.c libteehee.a -Ilibtee
```

## Shared Object

A shared object, shared library, or `.so` file is a compiled ELF file that is linked into your program at run time. The benefit of a shared object is that the code is transported outside your final product meaning your ELF will be smaller without the duplicated code inside. However, this means that for your code to run, you will need to install the library in the system root library directory, such as `/lib` or `/usr/lib`

```
# compiling the library 
gcc -o -shared libteehee.so ./lib.c 

# adding the library to a project 
gcc -o main main.c -Ilibtee -lteehee -L$(pwd)
