import os
import subprocess

# Diretório de instalação do npm
npm_installation_dir = r'C:\Program Files\nodejs'

# Obtém o PATH atual
current_path = os.environ.get('PATH', '')

print(current_path)

# Adiciona o diretório de instalação do npm ao PATH se ainda não estiver presente
if npm_installation_dir not in current_path:
    os.environ['PATH'] = npm_installation_dir + os.pathsep + current_path

# Criar diretório C:\npmglobal
npmglobal_dir = r'C:\npmglobal'
os.makedirs(npmglobal_dir, exist_ok=True)


## Criar diretório C:\npmglobal-cache
#npmglobal_cache_dir = r'C:\npmglobal-cache'
#os.makedirs(npmglobal_cache_dir, exist_ok=True)
#
## Configurar o cache global do npm
#subprocess.run(['npm', 'config', 'set', 'cache', npmglobal_cache_dir, '--global'])
#
## Instalar node-red globalmente
#subprocess.run(['npm', 'install', '-g', '--unsafe-perm', 'node-red'])
#
## Instalar npm@10.7.0 globalmente
#subprocess.run(['npm', 'install', '-g', 'npm@10.7.0'])
#
### Adicionar C:\npmglobal ao PATH
##os.environ['PATH'] += os.pathsep + npmglobal_dir
##
## Configurar a política de execução
#subprocess.run(['Set-ExecutionPolicy', 'Unrestricted', 'LocalMachine'], shell=True)
#
