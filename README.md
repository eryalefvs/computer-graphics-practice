# Práticas de Computação Gráfica com OpenGL  

Este repositório contém atividades práticas de Computação Gráfica utilizando OpenGL com a biblioteca Glumpy em Python, equivalentes à segunda etapa da matéria Computação Gráfica, 6º período.  

## 📌 Prática 2

### 🎯 Objetivo  
A prática explora o uso da biblioteca Glumpy, que facilita a utilização do OpenGL em Python. Os códigos mesclam Python e C++ para trabalhar com primitivas gráficas como pontos, linhas e triângulos.  

### 🔍 Principais conceitos abordados  
- Definição de vértices e fragmentos  
- Configuração de cores e tamanhos de pontos  
- Criação de uma janela gráfica com Glumpy  
- Uso de shaders com `gl_Position` e `gl_FragColor`  
- Habilitação de blend de cores para suavizar transições  

### 📝 Exercícios  
1. Alterar as primitivas gráficas para linhas e triângulos, ajustando o tamanho dos pontos.  
2. Modificar as cores das primitivas.  
3. Implementar a função `on_init` para ativar blend de cores e criar um gradiente suave entre os vértices dos triângulos.  

---

## 📌 Prática 2  

### 🎯 Objetivo  
Nesta prática, exploramos interações do usuário com elementos gráficos na tela, utilizando eventos do mouse para modificar a posição dos vértices dos triângulos.  

### 🔍 Principais conceitos abordados  
- Normalização das coordenadas da tela (-1 a 1)  
- Identificação da posição do clique do mouse e movimentação dos vértices  
- Manipulação da cor dos fragmentos  
- Configuração do tamanho dos pontos gráficos  
- Habilitação de blend de cores  

### 📝 Exercícios  
1. Modificar o código da Prática 1 para exibir apenas um triângulo.  
2. Criar a função `on_mouse_press(x, y, button)` para atualizar a posição do triângulo com base no clique do mouse.  
3. Detectar o vértice mais próximo do clique e permitir movimentá-lo com `on_mouse_drag(x, y, dx, dy, button)`.  
4. Diferenciar ações entre os botões do mouse:  
   - Botão esquerdo move apenas um vértice.  
   - Botão direito move o triângulo inteiro.  

---

## 🚀 Tecnologias Utilizadas  
- **Python**  
- **OpenGL**  
- **Glumpy**  
- **C++ (primitivas gráficas)**  
