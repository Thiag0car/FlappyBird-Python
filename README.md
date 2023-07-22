# Como Funciona FlappyBird

<img align="right" src="pics/Flappy2.png" width="27%" >
Flappy Bird é um popular jogo eletrônico casual em que o jogador controla um pequeno pássaro, desafiado a voar por entre os canos sem colidir. O objetivo é avançar o máximo possível para alcançar a maior pontuação. Para jogar no computador, você pode pressionar a tecla de espaço para fazer o pássaro voar e soltar a tecla para fazê-lo descer. A precisão no timing dos saltos é fundamental para evitar obstáculos e progredir no jogo. A simplicidade do Flappy Bird o torna viciante e desafiador para jogadores de todas as idades.

# Como Começar?
Simples! Siga os seguintes passos:

1.  Clone esse repositório no seu computador
2.  pip install pygame (caso ainda não tenha)
3.  Rodar o caderno 'FlappyBird.py'
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

# Tela de Game Over e Recorde

Adicionei uma tela de Game Over para que o jogador não precise rodar o código novamente toda vez que morrer, basta precionar a tecla ENTER que o jogo recomeça. Além disso,
também foi Adicionado um sistema de recorde para deixar o jogo mais interessante. O seu record vai ficar salvo no seu computador então não se preocupe com isso. Caso queira reiniciar o seu recorde basta ir no arquivo 'recorde.txt' e alterar o número que esta lá para zero

# Novos Personagens Jogaveis
<img  align= "right" src="pics/Personagens Jogaveis.png" width="25%" >

Logo no começo do jogo você tera a chance de escolher com qual personagem você quer jogar, basta apertar a tecla '1','2' ou '3' do seu computador e seguir com o personagem escolhido.

Segue adiante as descrições dos personagens:


| Personagem |  Largura | Altura | Descrição | 
| -- | -- | -- | -- | 
| Pássaro | 34 | 24 | Se você quer apenas jogar o jogo normalmente essa é a escolha perfeita para você |
| Bob esponja | 34 | 24 | Escolha divertida, apesar de sua movimentação um pouco estranha o que pode atrapalhar na gameplay |
| Deteu | 34 | *60* | (Desafio) Jogar com Deteu é um Desafio por causa de sua Hitbox consideravelmente maior do que as outras. |






