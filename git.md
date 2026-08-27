# Guía para subir tu código a GitHub

Antes de empezar, asegúrate de tener tu terminal abierta exactamente en la carpeta de tu proyecto que quieres subir. Puedes verificar tu ruta actual con:
`pwd`

## Inicializa Git y configura la rama principal:
```bash
git init
git branch -M main
git config user.name "Tu Nombre o Usuario"
git config user.email "tu_correo@ejemplo.com"

git remote add origin <TU_LINK_DE_GITHUB.git>  
#Ejemplo: git remote add origin [https://github.com/andyPlazaCardenas/AnalisisDeAlgoritmos.git]

# Primer commit:

git add .
git commit -m "Primer commit: subida inicial"
git push -u origin main

# Futuros cambios:

git status                                      # (Opcional) Ver qué archivos han cambiado
git add .                                       # Prepara todos los cambios nuevos
git commit -m "Mensaje explicando el cambio"    # Guarda el cambio con un mensaje claro
git push                                        # Sube los cambios a GitHub