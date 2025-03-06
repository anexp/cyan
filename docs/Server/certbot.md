# Certbot

### List certificates
```sh
sudo certbot certificates
```

### Renew
```sh
sudo certbot renew
```

### Wild card  SSL certificate 
```sh
sudo certbot -d "*.subdomain.domain.tld" --manual --preferred-challenges dns certonly  --agree-tos
```
Without email
```sh
sudo certbot -d "*.subdomain.domain.tld" --manual --preferred-challenges dns certonly  --agree-tos --register-unsafely-without-email
```


### Check if a TXT record is visible  
Go to [Google Toolbox](https://toolbox.googleapps.com/apps/dig/#TXT/_acme-challenge.subdomain.domain.tld)



####  Mentioned in the web articles
href : https://r.je/guide-lets-encrypt-certificate-for-local-development  
however `--server` flag is not needed

```sh
sudo certbot -d example.org --server https://acme-v02.api.letsencrypt.org/directory --manual --preferred-challenges dns certonly
```


