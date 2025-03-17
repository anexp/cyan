# GDB


Example .gdbinit
```
# GDB INIT

# https://sourceware.org/gdb/current/onlinedocs/gdb.html/TUI-Keys.html
# Ctrl + L to clear/redraw screen
# `shell cls` command also clears screen
# Ctrl + X + A to toggle TUI mode

# completely disable debuginfod
set debuginfod enabled off
set pagination off
set confirm off
# One way to see the GDB output history in TUI mode is to enable logging:
set trace-commands on
set logging overwrite on
set logging enabled on
# and then tail the log in another shell:
# cd where/gdb/is/running
# tail -f gdb.txt

# See `help skip` for info

skip -rfu ^std::.*
skip -rfu ^__gnu_debug::.*
skip -fu __interceptor_freopen
skip -fu __ubsan::__ubsan_handle_dynamic_type_cache_miss
skip -fu __interceptor___isoc99_scanf
skip -fu __interceptor_printf


# Increase cmd window height
wh cmd +3
wh cmd +3


#custom commands
define my1
s
bt f
end

define my2
n
bt f
end
```
