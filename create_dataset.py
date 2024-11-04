import pandas as pd

data_path = 'dados_filiacoes.csv'
dataset_columns = ['IDLattes',
                    'DuracaoDoutorado',
                    'Genero',
                    'ExclusividadeDoutorado',
                    'Publicacoes',
                    'IdadeAcademica',
                    'HistoricoInternacional']

# Arquivo origem
data_filiacoes = pd.read_csv(data_path)
data_filiacoes.dropna(subset=dataset_columns, inplace=True)
#data_filiacoes.apply(format_value)

# Gerando dataset com as colunas relevantes para regressão logística
data_set = data_filiacoes[dataset_columns]
data_set.to_csv('dataset_filiacoes.csv', index=False)
