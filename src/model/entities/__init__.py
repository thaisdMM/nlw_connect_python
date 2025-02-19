#a tabela de inscritos depende da tabela de eventos, essa é uma forma de associálas, pois os arquivos __init__.py sãos o primeiros a rodar no python3

from .eventos import Eventos
from .inscritos import Inscritos
