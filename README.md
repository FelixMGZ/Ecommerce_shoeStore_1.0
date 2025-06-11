# ShoeStore E-Commerce

ShoeStore es una tienda en línea de calzado desarrollada con HTML, CSS, JavaScript y Bootstrap. Permite a los usuarios navegar, buscar y comprar productos, así como a los administradores gestionar productos, usuarios y pedidos.

## Requisitos

- Python 3.10+
- Cuenta y proyecto en Supabase

- Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
- Crea un archivo `.env` en la raíz del proyecto y agrega tus claves de Supabase:
   ```
   SUPABASE_URL=tu_url_de_supabase
   SUPABASE_KEY=tu_key_de_supabase

## Estructura del Proyecto

```
app/
  admin/           # Panel de administración (productos, usuarios, pedidos)
  assets/          # Imágenes y recursos estáticos
  public/
    css/           # Hojas de estilo
    js/            # Scripts JavaScript
  user/            # Dashboard de usuario
  views/           # Vistas públicas (inicio, tienda, contacto, login, registro)
```

## Funcionalidades

- **Catálogo de productos** con filtros y paginación.
- **Carrito de compras** persistente en localStorage.
- **Registro e inicio de sesión** de usuarios.
- **Panel de administración** para gestionar productos, usuarios y pedidos.
- **Dashboard de usuario** con resumen de pedidos y gestión de tarjeta.
- **Responsive** y diseño moderno con Bootstrap.

  # Shoe Store Backend

Backend para una tienda de zapatos, construido con **FastAPI** y **Supabase**.

## Estructura del Proyecto

```
app/
├── api/
│   ├── products.py
│   ├── users.py
│   └── orders.py
├── core/
│   ├── config.py
│   └── security.py
├── db/
│   └── supabase.py
├── models/
│   └── order.py
├── main.py
└── requirements.txt
```

## Uso

Ejecuta el servidor de desarrollo con:
```sh
uvicorn main:app --reload
```
