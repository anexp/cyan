# Invidious

Ref :-
1. [Installation via docker](https://docs.invidious.io/installation/#docker-compose-method-production)
2. [Config variables](https://github.com/iv-org/invidious/blob/master/config/config.example.yml)


Change port ip

```
ports:
     # - "127.0.0.1:3000:3000"
     - "3000:3000"
```


Change INVIDIOUS_CONFIG

```
hmac_key: "PUT_SOME_RANDOM_STRING"
external_port: 3000
domain: invidious.tld
https_only: true
statistics_enabled: true
captcha_enabled: false
```
