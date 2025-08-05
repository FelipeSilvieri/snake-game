# Snake Game RL

Jogo da cobrinha com aprendizado por reforço profundo. O agente utiliza uma rede neural para aprender a jogar e é treinado com visualização em tempo real dos resultados.

## Requisitos
- Python 3.10+
- Dependências listadas em `requirements.txt`

## Instalação
```
pip install -r requirements.txt
```

## Execução
Para iniciar o treinamento contínuo do agente:
```
python train.py
```

Para executar um teste rápido de uma quantidade finita de jogos (por exemplo 2 episódios):
```
python train.py --episodes 2
```
Durante o treinamento, uma janela Pygame mostrará o jogo e um gráfico exibirá a evolução das pontuações em tempo real.
