
OCR Image Text Extractor

Este projeto realiza a extração de texto de imagens usando a biblioteca EasyOCR e salva os resultados em uma planilha CSV.

- Funcionalidades
- 📷 Extração de texto de imagens via OCR
- 📄 Exportação dos dados extraídos para uma planilha `.csv`
- 🧩 Suporte a múltiplos idiomas

- Requisitos
Antes de executar, instale as dependências com:
pip install easyocr

- Como usar

1. Importar a função principal
Você pode usar as duas funções fornecidas:
from your_script import extractToList, data_sps

Ou executar diretamente o script editando os valores de entrada.

2. Extrair texto da imagem
# Parâmetros:
# - Idioma (ex: 'en' para inglês, 'pt' para português)
# - Caminho para a imagem (ex: 'imagens/foto.png')

data = extractToList('en', 'path/to/your/image.png')

3. Gerar a planilha
header = ['Texto Detectado']  # Cabeçalho da planilha
data_sps(data, header)

Isso criará o arquivo spreadsheet.csv no mesmo diretório do script.

- Estrutura das funções

extractToList(language, imagePath)
- Lê a imagem e retorna uma lista com os textos detectados.
- Utiliza EasyOCR para reconhecer os caracteres.

data_sps(data, header)
- Gera um arquivo spreadsheet.csv com os dados extraídos.
- Codificação UTF-8 e separação por vírgula.

-Exemplo de uso completo
from easyocr import Reader
import csv

data = extractToList('pt', 'minha_imagem.png')
data_sps(data, ['Texto Detectado'])

- Observações
- O caminho da imagem deve usar / (barra normal) mesmo no Windows.
- A função extractToList retorna apenas os textos detectados, sem coordenadas ou score de confiança.

