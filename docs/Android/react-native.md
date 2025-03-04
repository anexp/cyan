# React Native

Ref :-

1. [Build and Debug apk](https://medium.com/geekculture/react-native-generate-apk-debug-and-release-apk-4e9981a2ea51)


### Getting Started

Install react native globally
```sh
sudo npm i -g react-native
```

Initialize project
```sh
npx react-native init AwesomeProject
```
### Generate apk

Go to android directory
```sh
cd android
```

For debug
```sh
./gradlew assembleDebug
```

For release
```sh
./gradlew assembleRelease
```



