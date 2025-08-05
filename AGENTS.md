# AGENTS

## Scope
Este arquivo governa todo o repositório `snake-game`. Qualquer alteração deve seguir estas diretivas.

## Padrões
- Utilize Python 3.10+.
- Adote convenções PEP8 e type hints quando aplicável.
- Use o módulo `snake_rl` para lógica de jogo e aprendizado.
- Execute `python train.py --episodes 1` como verificação rápida após alterações relevantes.

## Estrutura
- `snake_rl/`
  - `game.py`: motor do jogo Snake com Pygame.
  - `agent.py`: agente de aprendizado por reforço e laço de treinamento.
  - `model.py`: rede neural e rotinas de treinamento.
  - `plotter.py`: funções de visualização de métricas em tempo real.
- `train.py`: ponto de entrada para treinar o agente.
- `requirements.txt`: dependências do projeto.

Para adicionar novas features ou arquivos, atualize esta lista de índices para facilitar a navegação dos próximos desenvolvedores ou agentes.
