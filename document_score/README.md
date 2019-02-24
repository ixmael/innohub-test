# Puntuación de un documento XML
Este ejercicio calcula la puntuación de un documento XML. La puntuación es el número de atributos que existen en el documento XML.

La entrada de este programa es a través de la *entrada estándar* del sistema operativo. El formato de entrada consta una línea inicial indicando la cantidad de líneas del documento XML, y después cada línea del documento XML.

Ejemplo:
```bash
6
<feed xml:lang='en'>
   <title>EnvioClick</title>
   <subtitle lang='en'>Programming test</subtitle>
   <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
   <updated>2019-02-08T12:00:00</updated>
</feed>
```

El resultado del programa sólo se escribe la puntuación del documento XML.

Ejemplo:
```bash
5
```

## Ejecución
```bash
python calculate_score.py
```

```bash
cat fuente.txt | python calculate_score.py
```
