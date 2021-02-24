# Creador_de_canciones
Por un lado crea una Spider que toma todas las canciones de determinada banda de interent y las alamcena en un excel (en mi caso canciones de damas gratis)

Despues con el parse songs las limpia y acomoda de forma de que sea posible alimentarlas al modelo

Por ultimo esta el modelo con una RNN que se entrena con las canciones y "predice" una cancion en base a alguna palabra inicial

El modelo esta lejos de estar terminado. Los pasos que le faltarian seria en primer lugar introducir un valor de finalizacion de la cancion para que la red sepa diferenciar una de otra.
Luego de finalizacion de frase para que tambien diferencie eso.
