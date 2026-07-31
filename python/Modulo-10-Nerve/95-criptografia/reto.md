# Reto 95: El Guardián de la Bóveda 🛡️

Has sido asignado como el Jefe de Seguridad de la empresa. Tu deber es tomar los archivos confidenciales de la computadora y cifrarlos antes de enviarlos por correo electrónico.

## Instrucciones Paso a Paso

1. Para empezar, crea manualmente (usando tu teclado y el ratón) un archivo de texto llamado `codigos_nucleares.txt` en esta misma carpeta y escribe cualquier cosa adentro.
2. Crea un archivo nuevo de Python llamado `reto.py`.
3. Importa `pack_nrv` de la librería `nerve`.
4. Imprime `"Iniciando protocolo de seguridad..."`.
5. Usa la herramienta `pack_nrv` para empaquetar el archivo `"codigos_nucleares.txt"`.
6. La caja fuerte resultante DEBE llamarse `"boveda.nrv"`.
7. La contraseña DEBE ser `"alenia_secreto"`.
8. Imprime `"Archivos encriptados con éxito en boveda.nrv"`.
9. *Opcional (si te sientes valiente)*: Importa el módulo `os` y usa `os.remove("codigos_nucleares.txt")` al final de tu script para borrar la evidencia.

## 📜 Reglas de la Misión

**🟢 Conceptos Permitidos:**
- `import`
- `print()`
- `pack_nrv()`
- Textos entre comillas dobles `""`.
- Variables para guardar tu contraseña o nombres de archivo.

**🔴 Prohibido:**
- Usar funciones `def` o bucles `while`/`for` (este programa es un ejecutor directo, se corre de arriba a abajo y termina).
- Usar contraseñas vacías.

## 🏆 Resultado Esperado en la Terminal

Al ejecutar `reto.py`, el proceso será invisible pero poderoso. En la consola verás:

```text
Iniciando protocolo de seguridad...
Archivos encriptados con éxito en boveda.nrv
```

Si revisas tu carpeta después de ejecutarlo, deberías ver un archivo nuevo llamado `boveda.nrv`. ¡Si intentas abrirlo con el Bloc de Notas, solo verás símbolos raros e ilegibles! Has protegido la información con éxito.
