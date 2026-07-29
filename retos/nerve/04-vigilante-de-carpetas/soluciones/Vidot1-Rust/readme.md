
Mi solucion al reto #4, al final simplemente tome la interfaz que hice anteriormente
para nerve, lo mas nuevo es la interfaz de notify para el manejo de archivos

Estos retos han sido buenos para exponerme mas a hacer cosas con Rust,
y me ha hecho a empezar segregar mi codigo en modulos que igual me sirven para otras cosas

Todo esta implementado en `lib.rs`, `main.rs` solo inicializa
el programa y corre un loop de forma indefinida.

# Ejecutar
Asegurate de tener `cargo` instalado,

## Iniciar `nerve`

Inicializa nerve desde un entorno virtual en python:
```bash
python -m venv alenia-env

Linux   -> source alenia-env/bin/activate
Windows -> ./alenia-env/bin/activate

(alenia-env) pip install alenia-nerve
(alenia-env) nerve start --verbose
```

`nerve` debe estar ejecutandose para usar el programa.

## Ejecutar
```bash
cargo run
```
## Correr Tests
```bash
cargo test
```
