# Instalar rpy2 para fazer ponte entre R e Python (Windows)

- Instalar R
- [Baixar](https://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2) o binário de acordo com a sua versão do python e colocar na pasta onde o python está instalado no seu computador
    - Exemplo: **C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python37**
- Dentro da pasta de onde o seu python está instalado, rodar o comando `````pip install rpy2[sua-versao]`````
    - Exemplo: para o binário **rpy2-2.9.5-cp37-cp37m-win_amd64.whl**, o comando será `````pip install rpy2-2.9.5-cp37-cp37m-win_amd64.whl`````
- Criar duas variáveis de ambientes: **R_HOME** e **R_USER**
    - **R_HOME** terá o caminho de onde o R está instalado
    - **R_USER** terá o caminho de onde a lib rpy2 está instalada no seu python
        - Exemplo: **C:\Users\SEU_USUARIO\AppData\Local\Programs\Python\Python37\Lib\site-packages\rpy2**
- Também colocar binário baixado no anteriormente na pasta do seu projeto
- Dentro do projeto, rodar o comando `````pip install rpy2[sua-versao]`````
    - Exemplo: para o binário **rpy2-2.9.5-cp37-cp37m-win_amd64.whl**, o comando será `````pip install rpy2-2.9.5-cp37-cp37m-win_amd64.whl`````
