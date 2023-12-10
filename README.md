# Projeto de Processamento de Imagens - Classificação de Raios-X

## Título do Projeto
Detecção de COVID-19 em Raios-X Torácicos

## Equipe
- [Carlos Eduardo Nogueira de Freitas Veiga](https://github.com/cenfv)
- [Samuel Pereira Porto](https://github.com/cenfv)
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
[Link do Video](https://github.com/seu_usuario/nome_do_repositorio)

## Classificador e Acurácia
### MLP (Multilayer Perceptron)
- Classificador utilizado: MLPClassifier do scikit-learn
- Acurácia obtida: [Inserir Valor]% 

### Random Forest
- Classificador utilizado: RandomForestClassifier do scikit-learn
- Acurácia obtida: [Inserir Valor]% 

### SVM (Support Vector Machine)
- Classificador utilizado: SVM do scikit-learn
- Acurácia obtida: [Inserir Valor]%

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
1. Clone o repositório para sua máquina local.
2. Certifique-se de ter todas as dependências instaladas, incluindo o Python e as bibliotecas necessárias (scikit-learn, numpy, opencv, matplotlib).
3. Execute o script `data_splitting.py` para organizar as imagens em conjuntos de treino e teste.
4. Em seguida, execute o script `grayHistogram_FeatureExtraction.py` para extrair as características de histograma de tons de cinza.
5. Utilize os scripts `mlp_classifier.py`, `rf_classifier.py` e `svm_classifier.py` para treinar e avaliar os classificadores MLP, Random Forest e SVM, respectivamente.
6. Para executar todos os classificadores de uma vez, utilize o script `run_all_classifiers.py`.
7. Os resultados, incluindo as matrizes de confusão e a acurácia, serão salvos na pasta `/results`.
