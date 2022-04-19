# LC_Challenge

**Lemon Challenge - DEMO ‘Space & Beyond’**
1. Los flujos claves y los casos de prueba se encuentran en el archivo ‘Lemon_Challenge_sgrimmer_TCs_S&BDEMO’
2. El test exploratorio de las funcionalidades CORE se encuentra en el archivo ‘Lemon_Challenge_sgrimmer_ExploratoryTest_S&BDEMO’
3. El reporte de bugs y posibles mejoras para el sitio se encuentra en el archivo ‘Lemon_Challenge_sgrimmer_S&BDEMO_BugReport’
4. Se decidió automatizar el flujo crítico de Checkout utilizando Selenium IDE con Python. El archivo de Selenium se encuentra bajo el nombre ‘Lemon_Challenge_sgrimmer_CheckoutTest’ y el archivo conteniendo las pruebas en Python se encuentra bajo el nombre ‘test_lemonChallengesgrimmerCheckoutTest’

**Preguntas a responder:**
1. ¿Sería necesario verificar todos los flujos para el lanzamiento? ¿Por qué? - No sería necesario todos los flujos ni escenarios ya que hay algunas funcionalidades que no se consideran críticas para un lanzamiento, dado que el objetivo de la compañía es ‘Hacer las cosas complejas simples’. Siendo este el caso y dado que la meta principal del cliente es lograr ventas accesibles para los usuarios, hay ciertos casos de prueba que podrían prescindir a la hora de realizar un lanzamiento del sitio y así concentrar al equipo en el objetivo de venta
2. Si tuvieras que planificar una regresión, ¿qué casos de prueba elegirías para que integren la misma? - Dado que el objetivo de una regresión es la validación correcta de las funcionalidades luego de un cambio en el código, evaluaria los escenarios que incluyan la selección y filtro de destinos, el proceso de checkout y la carga correcta de la homepage y sus elementos
3. Se tiene que realizar una entrega de una funcionalidad nueva a producción de forma urgente, esta funcionalidad afecta al core de sistema ¿En qué se enfocaría para que la entrega tenga la mayor calidad posible? - Selección de destino y proceso de checkout (si las ventas siguen funcionando, se puede resolver todo lo demás) 
