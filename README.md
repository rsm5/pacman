# pacman

 Pac-Man, o famoso "joguinho do come-come" (como é conhecido no Brasil) é um dos maiores clássicos dos videogames. Lançado em maio de 1980 no Japão, Pac-Man chegaria aos Estados Unidos em outubro de 1980. E foi lá que ele realmente explodiu, tornando-se posteriormente um sucesso mundial. [4]
 
 O objetivo deste repositório é criar agentes para a versão clássica do Pacman, incluindo fantasmas utilizando algoritmos clássicos em inteligência artificial tais como Reflex Agent, Alpha-Beta Pruning e Expectimax [3]. 

---
## Configuração do Anaconda e virtual environment para a versão 2.7
---

Requirements [1]
 - Anaconda Python distribution installed and accessible

1 - Check conda is installed and in your PATH: conda -V
2 - Check conda is up to date: conda update conda
3 - Create a virtual environment for your project: conda create -n ambiente_pacman_berkeley python=2.7 anaconda
   -> Digite a opção 'y' (yes) para baixar as libs.
   -> OBS: environment location: /home/<SEU_USUARIO>/anaconda3/envs/ambiente_pacman_berkeley
4 - Activate your virtual environment: conda activate ambiente_pacman_berkeley
[OPCIONAL] 5 - Install additional Python packages to a virtual environment: conda install -n ambiente_pacman_berkeley [package]
6 - Deactivate your virtual environment: conda deactivate
7 - Delete a no longer needed virtual environment: conda remove -n ambiente_pacman_berkeley -all

---
## Rodando o Pacman
---

1 - First, play a game of classic Pacman: python pacman.py

2 - Your agent should easily and reliably clear the testClassic layout: python pacman.py -p ReflexAgent -l testClassic

3 - Now, run the provided ReflexAgent in multiAgents.py: 
    python pacman.py --frameTime 0 -p ReflexAgent -k 1

    python pacman.py --frameTime 0 -p ReflexAgent -k 2
    
    
---
## Código para resolver as questões
---

* Para Fazer as questões propostas acesse "multiAgents.py".
* Questões a serem feitas [3]:
  * Question 1 (4 points): Reflex Agent => Pacman ganha
  * Question 3 (5 points): Alpha-Beta Pruning => Fantasminha ganha
  * Question 4 (5 points): Expectimax => Fantasminha ganha


---
## Referências:
---
       [1] eResearch cookbook - 2 minute recipes for scientists. Create virtual environments for python with conda. Disponível em: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
       [2] LIMA, Cloves. Multi-agentes - PACMAN. Disponível em: https://drive.google.com/file/d/1stEVjqcCrpc_DDMrlhmXpV0n-b-nKMMy/view
       [3] UC Berkeley. Project 2: Multi-Agent Search. Disponível em: http://ai.berkeley.edu/multiagent.html       
       [4] Tecmundo. 42 anos de Pac-Man: conheça tudo sobre o game. Disponível em: https://www.tecmundo.com.br/voxel/237159-42-anos-pac-man-conheca-tudo-game.htm

