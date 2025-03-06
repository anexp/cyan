# Diskpart


list disk
list par
list vol

convert gpt

create par efi size=100
create par primary


sel disk 0
sel par 1

format fs=fat32 quick
format fs=ntfs quick


```ps1
sel par 1
assign letter=g:
```

```ps1
sel par 2
assign letter=c:
```

