# Exercise


## Debugger setup

(NOTE: only one person can be connected to the debugger at once)

1. Install `py3tftp` (`pip3 install py3ftp`)
2. Navigate in terminal to the directory containing `gdb-server7`
3. Execute `python3 -m py3tftp`
4. Attach to UART shell on router (`sudo screen /dev/ttyUSB0 115200`)
5. In UART shell navigate to `/var/tmp`
6. Execute `tftp -g -r ./gdbserver-7 192.168.0.100:9069`
7. Execute `./gdbserver-7 --attach host:2345 320`
8. On your machine connect to the server by first executing `gdb-multiarch <path-to-httpd>`
9. When within gdb execute `target remote 192.168.0.1:2345`

You should now be connected in gdb to the router, and be debugging the http server.


This is a useful cheatsheet for gdb - https://gabriellesc.github.io/teaching/resources/GDB-cheat-sheet.pdf

if you have GEF installed, to print hexdumps of memory use:
```
hexdump byte <ADDRESS/REGISTER> --size <HEXDUMP_SIZE>
```

## Questions

The goal of this exercise is to understand how `http_cgi_main` works, and how it processes requests. This will be split into several smaller exercises.

This is a sample POST request sent to the server:

```
POST http://192.168.0.1/cgi?1&1&1

[IGD_DEV_INFO#0,0,0,0,0,0#0,0,0,0,0,0]0,4
modelName
description
X_TP_isFD
X_TP_ProductVersion
[ETH_SWITCH#0,0,0,0,0,0#0,0,0,0,0,0]1,1
numberOfVirtualPorts
[MULTIMODE#0,0,0,0,0,0#0,0,0,0,0,0]2,1
mode
[/cgi/info#0,0,0,0,0,0#0,0,0,0,0,0]3,0
```

### 1

Sample:
```
[IGD_DEV_INFO#0,0,0,0,0,0#0,0,0,0,0,0]0,4
```

#### a
```
[IGD_DEV_INFO#0,0,0,0,0,0#0,0,0,0,0,0]<X>,<Y>
```

In the above line, what do X and Y represent?

#### b

In the following request body what should A, B, C, D, E, and F be?

```
[/cgi/info#0,0,0,0,0,0#0,0,0,0,0,0]<A>,<B>
[IGD_DEV_INFO#0,0,0,0,0,0#0,0,0,0,0,0]<C>,<D>
description
X_TP_ProductVersion
X_TP_isFD
[ETH_SWITCH#0,0,0,0,0,0#0,0,0,0,0,0]<E>,<F>
numberOfVirtualPorts
```

### 2

````
http://192.168.0.1/cgi?1&1&1
````

#### a

What do the query parameters represent in the code?

#### b 

```
[<X>#0,0,0,0,0,0#0,0,0,0,0,0]0,4
```

If you are not logged in what possible values can X be?
