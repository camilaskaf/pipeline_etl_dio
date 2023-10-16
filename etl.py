# import pandas as pd

# dados_originais = pd.read_csv("dados.csv")

# dados_transformados = dados_originais.copy()
# dados_transformados["Idade"] = dados_transformados["Idade"] + 5

# dados_transformados.to_csv("dados_transformados.csv", index=False)

# print("Processo ETL concluído com sucesso.")

import pandas as pd
import numpy as np

dados_originais = pd.read_csv("dados.csv")


idade_media = np.mean(dados_originais["Idade"])
print(idade_media)

dados_transformados = pd.DataFrame({
    "Estatística": ["Média"],
    "Idade": [idade_media]
})


dados_transformados.to_json("dados_transformados.json", orient="records",
                            lines=True, force_ascii=False, default_handler=str)

print("Processo ETL concluído com sucesso.")
