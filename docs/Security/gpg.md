# gpg

List keys:
```sh
gpg --list-secret-keys
gpg --list-keys
```

Generate keys:
```sh
gpg --full-generate-key
```
OR
```sh
gpg --gen-key
```

Export/Import keys:

```sh
gpg --export -a Melvin > melvin_public.key
gpg --import melvin_public.key
gpg --export-secret-keys Melvin > melvin-private-key.key
gpg --import melvin-private-key.key
```

Encrypt & Decrypt
```sh
gpg -e -r "Melvin" users.csv
gpg --always-trust -e -r "Melvin" users.csv

gpg -d users.csv.gpg
gpg --batch --passphrase demo users.csv.gpg
```
