# Teoría: El Cadenero y la Billetera 🕶️

Para mostrar tu pase VIP a un servidor, no lo gritas a los cuatro vientos. Lo entregas de manera discreta. 

En Internet, esta "billetera" donde guardas tus pases secretos se llama **Headers** (Cabeceras). Las cabeceras son información oculta que viaja junto con tu petición, y el usuario normal de Internet nunca las ve.

### 1. Preparando la Billetera
¡Buenas noticias! Una billetera (Headers) en Python no es más que un simple **Diccionario** que ya conoces desde el Módulo 3.

```python
mi_billetera = {
    "Authorization": "Bearer mi_codigo_secreto_123"
}
```
*Anatomía:*
- `"Authorization"`: Es el compartimento de la billetera diseñado para credenciales.
- `"Bearer"`: Significa "Portador". Le dice al cadenero: *"Soy el portador de este código"*. Es el estándar más usado en la industria.

### 2. Mostrando la Billetera al Cadenero
Cuando usamos `requests.get()`, podemos pasarle nuestra billetera usando una instrucción especial llamada `headers=`.

```python
respuesta = requests.get("https://api.privada.com", headers=mi_billetera)
```
El símbolo `=` aquí no guarda una variable, sino que le dice a la herramienta `get`: *"Oye, cuando viajes a esa URL, llévate esta billetera contigo"*.

---

## ¿Qué pasa si me equivoco? (El Panel de Errores)

Al lidiar con autenticación, los errores no hacen que Python explote. En su lugar, el servidor te responde amablemente con un **Código de Estado** (status_code) de rechazo.

**Error 1: `status_code 401 (Unauthorized)`**
- **Qué significa:** ¡No Autorizado! (El cadenero te detuvo).
- **Por qué pasa:** Olvidaste mandar tu diccionario `headers`, enviaste una API Key incorrecta, o escribiste mal la palabra `"Bearer "`.

**Error 2: `status_code 403 (Forbidden)`**
- **Qué significa:** ¡Prohibido!
- **Por qué pasa:** Sí enviaste un pase VIP válido, pero tu pase es de "categoría bronce" y estás intentando entrar a la zona "platino". (No tienes permisos para esa URL en específico).

**Éxito: `status_code 200 (OK)`**
- ¡El cadenero revisó tu billetera, vio la pulsera correcta y te abrió la puerta!
