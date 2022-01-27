# WebAssembly

[The WebAssembly Binary Toolkit](https://github.com/WebAssembly/wabt)

Online compiled by the [wat2wasm demo](https://webassembly.github.io/wabt/demo/wat2wasm/)

[WASM Code Explorer](https://wasdk.github.io/wasmcodeexplorer/)

```bash
brew install wasm3
```

```shell
playground/webassembly » wasm3 --repl hello.wasm                                                                                1 ↵
wasm3> how_old 2021 1900
Result: 121
wasm3> 
```

```bash
file hello.wasm
```

Run a Standard Web Server to serve the `index.html`
```bash
python3 -m http.server 10003
```