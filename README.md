# Prova Prática - Fundamentos de Programação

Nome do aluno: Nícolas Passos Guimarães

Descrição:
Sistema simples para registro de vendas de uma loja.

Como executar:
python main.py

# Lista de comandos no git executados

# No repositório local:
# Comandos git utilizados:

git init
# Iniciei um novo repositório .git na máquina local, no diretório C:\Users\nicolas.guimaraes\Documents\workspace

git config user.name Nicao-ps
git config user.email nps.guimaraes@gmail.com
# Registrei o usuário que estará trabalhando no repositório .git da máquina local informando o seu nome e e-mail já previamente registrados no github.

git remote add origin https://github.com/Nicao-ps/prova-fundamentos-programacao.git
#  Adicionei o link do repositório web do projeto no github para conectá-lo com o repositório local .git.

git branch -m master main
# Alterei o branch padrão de master para main, para mitigar possíveis inconsistências futuras que poderiam ser geradas pela diferença no branch no momento em que fosse dar os commit, principalmente da máquina local para o repositório do projeto no github.

git pull origin main --allow-unrelated-histories
# Solicitei uma busca com o comando pull e forcei com o comando --allow-unrelated-hitories a permitir a captura de inconsistências entre os arquivos presentes no repertório web do github com a máquina local