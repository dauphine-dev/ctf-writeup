# SECCON CTF Quals - 2019

## Rev / 383 - 7w1n5

> Hi, we are brothers! Can you catch our flag??
> 
> * [Brother1](./Brother1)
> * [Brother2](./Brother2)


### Solution

By [@jaidTw](https://github.com/jaidTw)

Credits to [@HexRabbit](https://blog.hexrabbit.io)

題目給了兩個靜態執行檔，乍看之下輸出相同：
```
$ ./Brother1
Let's start analysis! :)
$ ./Brother2
Let's start analysis! :)
```
試著`strace`會發現程式一直`exec`自己，而且`Brother1`還會`fork`出`ps`, `grep`, `tr`等等。
```
root@46ecc8ec88c7:/mnt/7w1n5# strace -f 2>&1 ./Brother1 | grep execve
execve("./Brother1", ["./Brother1"], 0x7ffc4c336378 /* 17 vars */) = 0
execve("/bin/bash", ["./Brother1", "-c", "exec './Brother1' \"$@\"", "./Brother1"], 0xfedd70 /* 18 vars */) = 0
execve("/mnt/7w1n5/Brother1", ["./Brother1"], 0x564da9ddc570 /* 18 vars */) = 0
execve("/bin/bash", ["./Brother1", "-c", "                                "..., "./Brother1"], 0x7fffc5ce47e8 /* 17 vars */) = 0
[pid   940] execve("/bin/ps", ["ps", "-a"], 0x55d4c41a15d0 /* 17 vars */ <unfinished ...>
[pid   940] <... execve resumed> )      = 0
[pid   941] execve("/bin/grep", ["grep", "-v", "grep"], 0x55d4c41a15d0 /* 17 vars */ <unfinished ...>
[pid   941] <... execve resumed> )      = 0
[pid   942] execve("/bin/grep", ["grep", "-e", "gdb", "-e", " r2", "-q"], 0x55d4c41a15d0 /* 17 vars */ <unfinished ...>
[pid   942] <... execve resumed> )      = 0
[pid   972] execve("/usr/bin/tr", ["tr", "A-Za-z", "N-ZA-Mn-za-m"], 0x55d4c41a15d0 /* 17 vars */ <unfinished ...>
[pid   972] <... execve resumed> )      = 0
[pid   971] execve("/bin/date", ["date", "+xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"...], 0x55d4c41a15d0 /* 17 vars */ <unfinished ...>
$ strace -f 2>&1 ./Brother2 | grep execve
execve("./Brother2", ["./Brother2"], 0x7ffc9b72b7f8 /* 17 vars */) = 0
execve("/bin/bash", ["./Brother2", "-c", "exec '/usr/bin/strace' \"$@\"", "./Brother2"], 0x149cd70 /* 18 vars */) = 0
execve("/usr/bin/strace", ["/usr/bin/strace"], 0x556be1bb85a0 /* 18 vars */) = 0
```
逆向程式本身會發現大量呼叫`arc4(buf, len)`根據table `stte`來對`buf`進行解密，因此用gdb追著看每次`arc4()`結束後的buffer，可以發現`Brother1`的`0x6be167`在解密後會是
```
pwndbg> p (char*)0x6be178
$2 = 0x6be178 <data+216> "#!/bin/bash\necho \"Let's start analysis! :)\"\nps -a|grep -v grep|grep -e gdb -e \" r2\" -q && echo \"No no no no no\" && exit 1\necho Close! So close! >/dev/null\nfor I in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15\ndo\n  date +", 'x' <repeats 770 times>, "SECCON{Which_do_yo|tr A-Za-z N-ZA-Mn-za-m >/dev/null & # base64になっている\ndone\necho Close! So close! >/dev/null\n"
```
而`Brother2`的會是
```
#!/bin/bash\necho \"Let's start analysis! :)\"\nps -a|grep -v grep|grep -e gdb -e \" r2\" -q && echo \"No no no no no\" && exit 1\necho Close! So close! >/dev/null\nfor I in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15\ndo\n  date +", 'x' <repeats 770 times>, "u_like_Bin_or_TxT}|tr A-Za-z N-ZA-Mn-za-m >/dev/null & # base64になっている\ndone\necho Close! So close! >/dev/null\n
```
將兩段中的flag片段組合就行
```
SECCON{Which_do_you_like_Bin_or_TxT}
```
