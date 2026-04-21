# Generar consola

## 1. Obtener el TOKEN

- Ingresar al aplicativo

```
http://192.168.17.11:3000
```

- Ir a ajustes

    <img src="images/step_01.png" width="400"/>

- Generar el TOKEN

    <img src="images/step_02.png"/>


## 2. Probar desde consola

```

curl -X POST "https://192.168.17.11:3000/api/chat/completions" \
     -H "Authorization: Bearer COPIAR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "ministral-3:14b",
       "messages": [
         {
           "role": "user",
                  "stream": true,

           "content": "Dame un programa en Python que imprima Hola, mundo!"
         }
       ]
     }'

```

## 3. Probar desde aplicaciones con Python

```
\ src
   |
   |-- list_models_ia.py       # Listar modelos de IA disponibles
   |-- test_model_api_rest.py  # Invocar a un model o de IA para consulta

```
