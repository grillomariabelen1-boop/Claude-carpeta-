# Tarea: subir las tablas de talles Hechter a la web de Village Polo Club

Sitio: villagepoloclubstore.com.ar (panel de Tiendanube). Ya tengo la sesión iniciada en el panel.

## Qué hacer en cada producto

1. En el panel de Tiendanube, ir a **Productos** y buscar el producto por nombre.
2. Entrar a editarlo y bajar hasta **Descripción**.
3. Pasar el editor a **modo código** (botón `<>`).
4. Ir **al final** de la descripción actual, dejar una línea en blanco y pegar el HTML que corresponde (ver abajo).
   **No borrar ni modificar el texto que ya existe.**
5. Salir del modo código, revisar que la tabla se vea y **guardar**.
6. Pasar al siguiente producto.

Si un producto ya tiene una tabla de talles, no pegar otra: anotarlo y seguir.

## Productos y qué tabla lleva cada uno

**Tabla A · Ambos** (12 productos):
- Ambo Liverpool Visón Hechter
- Ambo Liverpool Blue Hechter
- Ambo Liverpool Grey Hechter
- Ambo Liverpool Blue Cintura Elástica Hechter
- Ambo Liverpool Cintura Elástica Visón Hechter
- Ambo Preston Navy Sarga Hechter
- Ambo Leeds Grey Sarga Hechter
- Ambo Leeds Black Sarga Negro Hechter
- Ambo Leeds Navy Sarga Hechter
- Ambo Arlington Marino Hechter
- Ambo Arlington Hechter Visón
- Ambo Arlington Gris Hechter

**Tabla B · Sacos** (2 productos):
- Saco Sport Vison Hechter
- Saco Triota Navy Azul Marino Hechter

**Tabla C · Camisas** (1 producto):
- Camisa Saint German Hechter Blanca

**No tocar:** Ambo Lavable Negro y Ambo Lavable Marino (no son Hechter), chinos Budapest, pantalón de corderoy y campera Copenhague.

## Tabla A · Ambos

```html
<p><strong>Tabla de talles Hechter</strong></p>
<p><strong>Saco</strong></p>
<div style="overflow-x:auto;">
<table border="1" cellpadding="6" style="border-collapse:collapse;font-size:13px;">
<tr><th>Talle</th><th>46</th><th>48</th><th>50</th><th>52</th><th>54</th><th>56</th><th>58</th><th>60</th></tr>
<tr><td>Equivalencia aproximada</td><td>S</td><td>M</td><td>L</td><td>XL</td><td>XXL</td><td>3XL</td><td>4XL</td><td>5XL</td></tr>
<tr><td>1/2 pecho (a 1 cm de la sisa)</td><td>49</td><td>51</td><td>53</td><td>55</td><td>57</td><td>60</td><td>62</td><td>63</td></tr>
<tr><td>Ancho de hombros</td><td>43.6</td><td>44.8</td><td>46</td><td>47.2</td><td>48.4</td><td>49.6</td><td>50.8</td><td>52</td></tr>
<tr><td>Ancho de espalda</td><td>42.6</td><td>43.8</td><td>45</td><td>46.2</td><td>47.4</td><td>48.6</td><td>49.8</td><td>51</td></tr>
<tr><td>Largo de manga</td><td>64</td><td>64.5</td><td>65</td><td>65.5</td><td>66</td><td>66.5</td><td>67</td><td>67.5</td></tr>
<tr><td>Largo de espalda</td><td>71</td><td>72</td><td>73</td><td>74</td><td>75</td><td>76.5</td><td>77</td><td>78</td></tr>
</table>
</div>
<p><em>La equivalencia con S-XL es orientativa.</em></p>
<p><strong>Pantalón</strong></p>
<div style="overflow-x:auto;">
<table border="1" cellpadding="6" style="border-collapse:collapse;font-size:13px;">
<tr><th>Talle</th><th>40</th><th>42</th><th>44</th><th>46</th><th>48</th><th>52</th><th>54</th><th>56</th></tr>
<tr><td>1/2 cintura</td><td>41</td><td>43</td><td>45</td><td>47</td><td>49</td><td>53</td><td>55</td><td>57</td></tr>
<tr><td>1/2 cadera</td><td>49</td><td>51</td><td>53</td><td>55</td><td>57</td><td>61</td><td>63</td><td>65</td></tr>
<tr><td>1/2 rodilla (a 35 cm de la entrepierna)</td><td>21.3</td><td>21.7</td><td>22.1</td><td>22.5</td><td>23.7</td><td>24.5</td><td>24.9</td><td>25.3</td></tr>
<tr><td>Tiro delantero (con cintura)</td><td>24.5</td><td>25</td><td>25.5</td><td>26</td><td>26.5</td><td>27.5</td><td>28</td><td>28.5</td></tr>
<tr><td>Tiro trasero (con cintura)</td><td>40.5</td><td>41</td><td>41.5</td><td>42</td><td>42.5</td><td>43.5</td><td>44</td><td>44.5</td></tr>
</table>
</div>
<p><strong>Cómo usar la tabla:</strong> son medidas de la prenda en centímetros, tomadas con la prenda estirada sobre una mesa. Buscá una prenda tuya que te quede bien, apoyala igual y compará. ¿Dudás entre dos talles? Escribinos por WhatsApp y te asesoramos.</p>
```

## Tabla B · Sacos

```html
<p><strong>Tabla de talles Hechter</strong></p>
<p><strong>Saco</strong></p>
<div style="overflow-x:auto;">
<table border="1" cellpadding="6" style="border-collapse:collapse;font-size:13px;">
<tr><th>Talle</th><th>46</th><th>48</th><th>50</th><th>52</th><th>54</th><th>56</th><th>58</th><th>60</th></tr>
<tr><td>Equivalencia aproximada</td><td>S</td><td>M</td><td>L</td><td>XL</td><td>XXL</td><td>3XL</td><td>4XL</td><td>5XL</td></tr>
<tr><td>1/2 pecho</td><td>49</td><td>51</td><td>53</td><td>55</td><td>57</td><td>60</td><td>62</td><td>63</td></tr>
<tr><td>1/2 cintura</td><td>45</td><td>47</td><td>49</td><td>51</td><td>54</td><td>57</td><td>59.5</td><td>61</td></tr>
<tr><td>1/2 bajo</td><td>50</td><td>52</td><td>54</td><td>56</td><td>59</td><td>63</td><td>66</td><td>69</td></tr>
<tr><td>Ancho de hombros</td><td>43.6</td><td>44.8</td><td>46</td><td>47.2</td><td>48.4</td><td>49.6</td><td>50.8</td><td>52</td></tr>
<tr><td>Espalda (a 15 cm del cuello)</td><td>42.6</td><td>43.8</td><td>45</td><td>46.2</td><td>47.4</td><td>48.6</td><td>49.8</td><td>51</td></tr>
<tr><td>Largo de manga</td><td>64</td><td>64.5</td><td>65</td><td>65.5</td><td>66</td><td>66.5</td><td>67</td><td>67.5</td></tr>
<tr><td>Largo total de espalda</td><td>71</td><td>72</td><td>73</td><td>74</td><td>75</td><td>76</td><td>77</td><td>78</td></tr>
</table>
</div>
<p><em>La equivalencia con S-XL es orientativa.</em></p>
<p><strong>Cómo usar la tabla:</strong> son medidas de la prenda en centímetros, tomadas con la prenda estirada sobre una mesa. Buscá una prenda tuya que te quede bien, apoyala igual y compará. ¿Dudás entre dos talles? Escribinos por WhatsApp y te asesoramos.</p>
```

## Tabla C · Camisas

```html
<p><strong>Tabla de talles Hechter</strong></p>
<p><strong>Camisa</strong></p>
<div style="overflow-x:auto;">
<table border="1" cellpadding="6" style="border-collapse:collapse;font-size:13px;">
<tr><th>Talle</th><th>S</th><th>M</th><th>L</th><th>XL</th><th>XXL</th></tr>
<tr><td>1/2 pecho</td><td>54</td><td>56</td><td>58</td><td>60</td><td>62</td></tr>
<tr><td>1/2 cintura</td><td>51</td><td>53</td><td>55</td><td>57</td><td>59</td></tr>
<tr><td>Bajo</td><td>54</td><td>56</td><td>58</td><td>60</td><td>62</td></tr>
<tr><td>Sisa</td><td>23.5</td><td>24.5</td><td>25.5</td><td>26.5</td><td>27.5</td></tr>
<tr><td>Largo de manga</td><td>64.5</td><td>65.5</td><td>66.5</td><td>67.5</td><td>68.5</td></tr>
<tr><td>Hombro</td><td>45</td><td>46.5</td><td>48</td><td>49.5</td><td>51</td></tr>
</table>
</div>
<p><strong>Cómo usar la tabla:</strong> son medidas de la prenda en centímetros, tomadas con la prenda estirada sobre una mesa. Buscá una prenda tuya que te quede bien, apoyala igual y compará. ¿Dudás entre dos talles? Escribinos por WhatsApp y te asesoramos.</p>
```

## Al terminar

Pasame una lista con:
- Los productos donde se pegó la tabla
- Los que no encontraste o donde algo falló
- Los que ya tenían tabla de talles
