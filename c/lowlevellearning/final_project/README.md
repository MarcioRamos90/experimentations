

to create the initial file
```
command echo -ne "LLAD\x00\x01\x00\x00\x00\x00\x00\x0c" > mynewdb.db

```

if we run `xxd mynewdb.db`:

```
00000000: 4c4c 4144 0001 0000 0000 000c            LLAD........
```

first four bytes represents our file type

```
00000000: |[4c4c 4144]| 0001 0000 0000 000c        |[LLAD]|........
```

the another two byte represents the version

```
00000000: 4c4c 4144 |[0001]| 0000 0000 000c        LLAD........
```

the anothe two bytes are the number of employess

```
00000000: 4c4c 4144 0001 |[0000]| 0000 000c        LLAD........
```

and the last 4 bytes represents the lenght of the current file, in this case 12 bytes

```
00000000: 4c4c 4144 0001 0000 |[0000 000c]|        LLAD........
```