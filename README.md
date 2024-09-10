# Programacion-avanzada
tareas y proyectos del ramo de programacion avanzada

1) ¿Qué es un paradigma de la programación?

Un paradigma de programación es una forma particular de abordar la construcción y organización de programas en informática. Define un conjunto de principios y estilos que guían cómo estructurar el código y resolver problemas. Los paradigmas proporcionan un marco para pensar en cómo un programa debe comportarse, qué estructura debe seguir, y cómo interactúan sus componentes. En clases profundizamos acerca de uno de estos paradigmas conocidos como programación orientada a objetos donde estudiamos conceptos como el de clase, método, atributos etc.


2) ¿En qué se basa la programación orientada a objetos?

La programación orientada a objetos es un paradigma de programación que organiza el software en torno a "objetos" en lugar de funciones o procedimientos como se suele hacer. Los objetos son instancias de clases, que son plantillas que definen las características y comportamientos de esos objetos. Este enfoque se utiliza para representar entidades del mundo real de manera estructurada, lo que facilita el desarrollo de software reutilizable. Además, según lo visto en clases, la programación orientada a objetos, por naturaleza, posee una serie de propiedades como la abstracción y la herencia que son de suma utilidad a la hora de modelar problemas y optimizar modelos.


3) ¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación
big 𝑂?

Por un lado, la recursividad es un procesor en el que una función se llama a sí misma para resolver subproblemas más pequeños del mismo problema hasta llegar a una condición base que detiene la recursión dando el problema por solucionado. Por otro lado, la iteración (o iteratividad como se vio en clases) utiliza bucles (como for o while) para repetir una serie de instrucciones hasta que se cumpla una condición específica.

En cuanto a la relación con la notación Big O, la eficiencia de la recursividad y la iteración depende de la tarea en la que se apliquen. Sin embargo, en términos generales, debido a la naturaleza de la recursividad, es común que los algoritmos recursivos tengan una complejidad mayor que los algoritmos iterativos. Por ejemplo, en el cálculo de los términos de la sucesión de Fibonacci, la versión recursiva simple tiene una complejidad O(2^n), ya que realiza múltiples llamadas redundantes para calcular el mismo valor. En cambio, el enfoque iterativo tiene una complejidad O(n), ya que solo itera una vez por cada número de la sucesión.

Es importante destacar que cualquier algoritmo recursivo puede, en principio, transformarse en una versión iterativa, aunque en algunos casos la recursión es más natural o fácil de expresar. Sin embargo, en muchos problemas, la versión iterativa resulta más eficiente en cuanto a tiempo y memoria y esto se puede verificar con la notación Big O.


4) Explicar la diferencia de rendimiento entre 𝑂(1) y 𝑂(𝑛)

Un algoritmo con complejidad O(1) es independiente del tamaño de la entrada. Esto significa que siempre toma la misma cantidad de tiempo o recursos para ejecutarse, sin importar cuán grande sea la entrada. Por otro lado, un algoritmo de complejidad O(n) posee un comportamiento lineal lo que quiere decir que el tiempo de ejecución aumenta linealmente con el tamaño de los datos que le entreguemos. Es por las explicaciones anteriores que el rendimiento de los algoritmos de complejidad O(1) es mejor que el de los algoritmos de complejidad O(n) especialmente cuando se trabaja con grandes volúmenes de datos.

5) ¿Cómo se calcula el orden en un programa que funciona por etapas?

Para calcular el orden de un programa que funciona por etapas, primero se descompone el programa en cada una de sus etapas o partes. Luego, se determina la complejidad de cada etapa por separado, ya sea O(1), O(n), O(log n), etc., dependiendo de las operaciones que realicen. Si las etapas se ejecutan secuencialmente, las complejidades se suman, y se considera únicamente el término de mayor crecimiento. Si las etapas están anidadas (como los for dentro de otros for), sus complejidades se multiplican. Finalmente, el orden global del programa será la complejidad de la etapa más costosa en términos de crecimiento conforme el tamaño de la entrada aumenta

-Por ejemplo si un problema recorre una sola lista iterativamente: O(n)

-Si se aplica un bucle for dentro de otro bucle for: O(n) * O(n) = O(n^2)

-Si se se recorre una lista iterativamente pero en otra etapa se aplica un bucle for dentro de otro bucle for se considera complejidad O(n^2) por lo explicado antes.

6) ¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?

Como aún no hemos visto el Teorema Maestro, explicaré mi manera intuitiva de determinar la complejidad temporal de un algoritmo recursivo (cabe destacar que es más utilizaod en el cálculo de complejidades de algoritmos más orientados a la matemática): primero debemos escribir su relación de recurrencia, que describe cómo el problema original se divide en subproblemas más pequeños. Luego, expandimos esta relación (desenrollar la recursión), lo que significa ver cuántas veces el algoritmo se llama a sí mismo y cuánto tiempo toma en cada paso. Si el problema se reduce a la mitad en cada llamada recursiva, normalmente el número de niveles es log n, y si en cada nivel se realiza un trabajo que toma tiempo n, entonces el tiempo total del algoritmo será O(n*log n). Este análisis nos permite comprender cuántas operaciones realiza el algoritmo en total y, por lo tanto, su complejidad temporal. Un caso en el que es fácil determinar la complejidad temporal es cuando tenemos ciclos for dentro de otros. De esta manera, si tenemos un ciclo for dentro de otro, tenemos una complejidad temporal de O(n^2) y tenemos un ciclo for dentro de otro ciclo for que a su vez está dentro de otro ciclo for entonces la complejidad será O(n^3) y así sucesivamente.

