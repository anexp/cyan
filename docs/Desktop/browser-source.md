# Browser


## Chromium

https://chromium.googlesource.com/chromium/src/+/main/docs/linux/build_instructions.md

Install depot_tools

Clone the depot_tools repository:
```sh
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
```
Add depot_tools to the beginning of your PATH (you will probably want to put this in your ~/.bashrc or ~/.zshrc). Assuming you cloned depot_tools to /path/to/depot_tools:
```sh
export PATH="/path/to/depot_tools:$PATH"
```
When cloning depot_tools to your home directory do not use ~ on PATH, otherwise gclient runhooks will fail to run. Rather, you should use either $HOME or the absolute path:
```sh
export PATH="${HOME}/depot_tools:$PATH"
```
Get the code

Create a chromium directory for the checkout and change to it (you can call this whatever you like and put it wherever you like, as long as the full path has no spaces):
```sh
mkdir ~/chromium && cd ~/chromium
```
Run the fetch tool from depot_tools to check out the code and its dependencies.
```sh
fetch --nohooks chromium
```
If you don't want the full repo history, you can save a lot of time by adding the `--no-history` flag to fetch.

Expect the command to take 30 minutes on even a fast connection, and many hours on slower ones.

If you've already installed the build dependencies on the machine (from another checkout, for example), you can omit the --nohooks flag and fetch will automatically execute gclient runhooks at the end.

When fetch completes, it will have created a hidden .gclient file and a directory called src in the working directory. The remaining instructions assume you have switched to the src directory:
```sh
cd src
```
Install additional build dependencies

Once you have checked out the code, and assuming you're using Ubuntu, run build/install-build-deps.sh
```sh
./build/install-build-deps.sh
```
You may need to adjust the build dependencies for other distros. There are some notes at the end of this document, but we make no guarantees for their accuracy.
Run the hooks

Once you've run install-build-deps at least once, you can now run the Chromium-specific hooks, which will download additional binaries and other things you might need:
```sh
gclient runhooks
```
Optional: You can also install API keys if you want your build to talk to some Google services, but this is not necessary for most development and testing purposes.
Setting up the build

Chromium uses Ninja as its main build tool along with a tool called GN to generate .ninja files. You can create any number of build directories with different configurations. To create a build directory, run:

```sh
gn gen out/Default
```

You only have to run this once for each new build directory, Ninja will update the build files as needed.
You can replace Default with another name, but it should be a subdirectory of out.
For other build arguments, including release settings, see GN build configuration. The default will be a debug component build matching the current host operating system and CPU.
For more info on GN, run gn help on the command line or read the quick start guide.




## Brave

```sh
git clone https://github.com/brave/brave-browser.git
cd brave-browser
npm i
npm run init
npm run build
npm run start
```
