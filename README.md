# **Integración continua I - Testeo**

## **Tareas a realizar**

Utilizando como base uno de los repositorios de ejemplo propuestos en la [teoría de GitHub Actions](https://github.com/FormacionCloud/CursoEspecializacion/blob/main/teoria/integracion-continua-testeo.org) ([Node con GitHub Actions](https://github.com/curso-github-cefire/tdd-node-sample-actions) o [Python con GitHub Actions](https://github.com/curso-github-cefire/tdd-python-sample)), crea un repositorio en tu cuenta de GitHub. Dicho repositorio debe contener:

* **Una función** que compruebe **si un número dado es par**.
* **Un test** que realice **pruebas con varios números** para comprobar que la función está correctamente diseñada.
Puedes utilizar cualquier lenguaje de programación soportado por GitHub Actions.

Deberás configurar el archivo en la carpeta `.github/workflows/` para el flujo que hayas decidido utilizar.

>[!IMPORTANT]

>Si haces un fork de algún repositorio que tenga activada alguna acción (es decir, que tenga algún archivo en la carpeta `.github/workflows`), tu repositorio copia **no las activará por defecto**, sino que deberás ir a la pestaña Actions y activarlas manualmente. Esto es así porque las Actions consumen recursos (minutos de ejecución) que se descuentan de tu cuenta. Una vez activadas podrás comprobar que sucesivos envíos sí que activan dichas acciones.
