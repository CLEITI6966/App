[app]

title = MeuApp
package.name = meuapp
package.domain = org.meuapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = INTERNET

# Usa o ícone padrão do Android
icon.filename = 

# Arquivo principal
entrypoint = main.py

# Suporte a arquitetura arm64-v8a
android.archs = arm64-v8a

# Para compilar offline, deixe desativado (opcional)
android.update_build_requirements = False

[buildozer]

log_level = 2
warn_on_root = 1

[android]

# Usa build-tools mais recentes automaticamente
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.gradle_dependencies =

[toolchain]

[python]

[hostpython]

[hooks]

