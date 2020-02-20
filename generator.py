import pandas as pd
import rpy2.robjects as ro

from features import Function


def generate_diverse_ts(q, frequency, components, size):
    """
    Gera um CSV de séries temporais juntamente com os coeficientes SARIMA usados em cada componente de mixing (modelo
    MAR) e os pesos de mixing correspondentes.
    https://github.com/ykang/gratis/

    :param q: quantidade de séries temporais a serem geradas
    :param frequency: período sazonal das séries temporais a serem geradas
    :param components: número de componentes de mixing ao gerar as séries temporais usando o modelo MAR
    :param size: tamanho das séries temporais
    """

    path = "output/diverse-ts.csv"
    ro.r('write.csv(generate_ts(n.ts = {}, freq = {}, nComp = {}, n = {}), "{}")'.format(q, frequency, components, size,
                                                                                         path))
    df = pd.read_csv(path)
    df = df.drop(df.columns[0], axis=1)

    if q > 1:
        dictionary = {}
        for i in range(q):
            key = "N{}.x".format(i + 1)
            dictionary[key] = "data{}".format(i + 1)

        df = df.rename(columns=dictionary)
    else:
        df = df.rename(columns={"N1.x": "data"})

    df.to_csv(path, index=False, sep=";", encoding="utf-8")

    return df


def generate_multi_seasonal_ts(seasonal_periods, size, components):
    """
    Gera um CSV com uma série série temporal com vários períodos sazonais
    https://github.com/ykang/gratis/

    :param seasonal_periods: uma lista de períodos sazonais da série temporal a ser gerada.
    :param size: tamanho da série temporal
    :param components: número de componentes de mixing ao gerar as séries temporais usando o modelo MAR
    """

    path = "output/multi-seasonal-ts.csv"
    ro.r('write.csv(generate_msts(seasonal.periods = c({}), n = {}, nComp = {}), "{}")'.format(
        str(seasonal_periods)[1:-1], size, components, path))

    df = pd.read_csv(path)
    df = df.drop(df.columns[0], axis=1)
    df = df.rename(columns={"x": "data"})
    df.to_csv(path, index=False, sep=";", encoding="utf-8")

    return df


def generate_ts_with_controllable_features(q, size, frequency, seasonal, features, target):
    """
    Gera um CSV com uma série temporal com features controláveis
    https://github.com/ykang/gratis/

    :param q: quantidade de séries temporais a serem geradas
    :param size: tamanho das séries temporais
    :param frequency: período sazonal das séries temporais a serem geradas
    :param seasonal: 0 para dados não sazonais, 1 para dados com um período sazonal e 2 para vários períodos sazonais
    :param features: um vetor com nome das features a serem controladas
    :param target: valores das features alvo
    """

    functions_values = []
    features_values = []

    for f in features:

        if isinstance(f, Function):
            functions_values.append(f.name)
        else:
            if f.get_name() not in functions_values:
                functions_values.append(f.get_name())

        features_values.append(f.value)

    path = "output/controllable-ts.csv"
    ro.r('write.csv(generate_ts_with_target(n = {}, ts.length = {}, freq = {}, seasonal = {}, features = c({}), '
         'selected.features = c({}), target = c({})), "{}")'
         .format(q, size, frequency, seasonal, ','.join('"{0}"'.format(w) for w in functions_values),
                 ','.join('"{0}"'.format(w) for w in features_values), str(target)[1:-1], path))

    df = pd.read_csv(path)
    df = df.drop(df.columns[0], axis=1)

    if q > 1:
        dictionary = {}
        for i in range(q):
            key = "Series {}".format(i + 1)
            dictionary[key] = "data{}".format(i + 1)

        df = df.rename(columns=dictionary)
    else:
        df = df.rename(columns={"x": "data"})

    df.to_csv(path, index=False, sep=";", encoding="utf-8")
    return df
