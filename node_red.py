import os
import subprocess

# Criar diretório C:\npmglobal
npmglobal_dir = r'C:\npmglobal'
os.makedirs(npmglobal_dir, exist_ok=True)

# Configurar o prefixo do npm
subprocess.run(['npm', 'config', 'set', 'prefix', npmglobal_dir])

# Criar diretório C:\npmglobal-cache
npmglobal_cache_dir = r'C:\npmglobal-cache'
os.makedirs(npmglobal_cache_dir, exist_ok=True)

# Configurar o cache global do npm
subprocess.run(['npm', 'config', 'set', 'cache', npmglobal_cache_dir, '--global'])

# Instalar node-red globalmente
subprocess.run(['npm', 'install', '-g', '--unsafe-perm', 'node-red'])

# Instalar npm@10.7.0 globalmente
subprocess.run(['npm', 'install', '-g', 'npm@10.7.0'])

# Adicionar C:\npmglobal ao PATH
os.environ['PATH'] += os.pathsep + npmglobal_dir

# Configurar a política de execução
subprocess.run(['Set-ExecutionPolicy', 'Unrestricted', 'LocalMachine'], shell=True)
