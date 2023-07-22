# Como Funciona FlappyBird

<img align="right" src="pics/Flappy2.png" width="27%" >
Flappy Bird é um popular jogo eletrônico casual em que o jogador controla um pequeno pássaro, desafiado a voar por entre os canos sem colidir. O objetivo é avançar o máximo possível para alcançar a maior pontuação. Para jogar no computador, você pode pressionar a tecla de espaço para fazer o pássaro voar e soltar a tecla para fazê-lo descer. A precisão no timing dos saltos é fundamental para evitar obstáculos e progredir no jogo. A simplicidade do Flappy Bird o torna viciante e desafiador para jogadores de todas as idades.

# Como Começar?
Simples! Siga os seguintes passos:

1.  Clone esse repositório no seu computador
2.  pip install pygame (caso ainda não tenha)
3.  Rodar o caderno FlappyBird
4.  Jogar

# Como o Código Foi Criado

Comecei seguindo o passo a passo do curso da hashtag de como fazer o FlappyBird. Os videos tutoriais se encontram nesse link https://pages.hashtagtreinamentos.com/minicurso-python-criacaojogos-obrigado?blog=1n4033rer&video=3dep762tr e o gabarito (resultado final) desses videos está no arquivo 'FlappyBird_gabarito.py' caso queira testar.

Entretanto achei o jogo incompleto e sem graça e decidi adicionar algumas mudanças e features novas. Então segue uma lista das alterações que eu fiz no jogo do FlappyBird:
- Aumentei a distância do cano do topo em relação ao cano da base de 200 para 217
- O jogo não fecha sozinho mais quando você perde (ou continua rodando mesmo morto), agora ele mostra uma tela de game over e você aperta ENTER se quiser continuar jogando
- Sistema básico de recorde, o seu recorde aparece no canto superior esquerdo e também na tela de game over
- Adicionei o bob esponja como jogável e o DETEU
- Criei uma mini interface para escolher o seu personagem antes de começar o jogo
- Crie um sistema que a cada 20 canos uma nova cor de cano começa a aparecer (ultima cor nova desbloqueada depois do ponto 80)


