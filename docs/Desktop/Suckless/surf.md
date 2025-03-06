# Surf

### Cannot open local files by default

Ref :-
1. [Debian Bug report](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=926393)

This is apparmor issue 

modify /etc/apparmor.d/local/usr.bin.surf

according to apparmor

Add this line
```
# Allow read access to .html, .css, and .js files inside $HOME
@{HOME}/**/*.md r,
@{HOME}/**/*.html r,
@{HOME}/**/*.css r,
@{HOME}/**/*.js r,
```


