# Projeto de Processamento de Imagens - Classificação de Raios-X

## Detector de Covid
Detecção de COVID-19 em Raios-X Torácicos

## Equipe
- [Carlos Eduardo Nogueira de Freitas Veiga](https://github.com/cenfv)
- [Samuel Pereira Porto](https://github.com/smlporto)
- [Welyson Carlos](https://github.com/welyson1)

## Descrição do(s) Descritor(es) Implementado(s)
Para este projeto, foram implementados dois descritores de características diferentes:
1. **Histograma de Hu Moments**
   - Descrição: Este descritor captura as características de forma de uma imagem, proporcionando informações sobre a geometria global da mesma.
   
2. **Histograma de Textura LBP (Local Binary Pattern)**
   - Descrição: Este descritor destaca padrões locais de textura na imagem, tornando-se útil para a detecção de texturas específicas.

## Repositório do Projeto
[Link do Repositório no GitHub](https://github.com/smlporto/classificacao-imagens)

## Video
[Link do Video](https://youtu.be/sighWM-pjxo)

## Classificador e Acurácia LBP
### Parâmetros
- Número de pontos da vizinhança: 24
- Raio da vizinhança: 8

### MLP (Multilayer Perceptron)
- Classificador utilizado: MLPClassifier do scikit-learn
- Acurácia obtida: 100,00% 
### Random Forest
- Classificador utilizado: RandomForestClassifier do scikit-learn
- Acurácia obtida: 73,21% 
### SVM (Support Vector Machine)
- Classificador utilizado: SVM do scikit-learn
- Acurácia obtida: 96,43%

## Classificador e Acurácia HU Moments
### MLP (Multilayer Perceptron)
- Classificador utilizado: MLPClassifier do scikit-learn
- Acurácia obtida: 50% 
### Random Forest
- Classificador utilizado: RandomForestClassifier do scikit-learn
- Acurácia obtida: 58,93% 
### SVM (Support Vector Machine)
- Classificador utilizado: SVM do scikit-learn
- Acurácia obtida: 53,57%

## Estrutura de Pastas
```plaintext
/projeto_processamento_imagens
    /features_labels: Contém os arquivos de características e rótulos extraídos das imagens.
    /images_full: Diretório original contendo todas as imagens.
        /covid: Imagens de raio-X classificadas como COVID.
        /normal: Imagens de raio-X classificadas como normais.
    /images_split: Diretório para imagens divididas em conjuntos de treino e teste.
        /train
            /covid
            /normal
        /test
            /covid
            /normal
    /results: Contém os resultados do projeto, como matrizes de confusão e gráficos de desempenho.
    data_splitting.py: Script para dividir as imagens em conjuntos de treino e teste.
    grayHistogram_FeatureExtraction.py: Script para extrair características usando o histograma em escala de cinza.
    mlp_classifier.py: Script para treinar e testar um classificador MLP (Multilayer Perceptron).
    rf_classifier.py: Script para treinar e testar um classificador Random Forest.
    run_all_classifiers.py: Script para executar todos os classificadores e comparar os resultados.
    svm_classifier.py: Script para treinar e testar um classificador SVM (Support Vector Machine).
```

## Instruções de Uso
1. Instale o Miniconda ou Anaconda
- [Miniconda: Miniconda Installers](https://docs.conda.io/projects/miniconda/en/latest/index.html)
- [Anaconda: Anaconda Installers](https://www.anaconda.com/download/)

2. Crie um novo ambiente com Conda
```bash
conda env create -f "diretorio_do_projeto"\environment.yml
```
Substitua diretorio_do_projeto pelo endereço do diretório do seu projeto.

3. Ative o ambiente conda.
```bash
conda activate projetofinal
```

4. Navegue até o diretório do projeto e execute o código
```bash
cd "diretorio_do_projeto"
python init_window.py
```

5. Use a interface gráfica para executar os scripts.
