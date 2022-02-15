<blockquote>
<center>

# Flask 🌶 | Restful API

![](./1.png)

</center>

## About:

- This is an flask api for first project in Arvan | Chellekhune

## 🔧 Set your configuration ⚙

- Creating .env file and write below fields on that

```sh
MYSQL_URI="mysql+pymysql://<USERNAME>:<PASSWORD>@<HOST>/<DATABASE>"
LABLE="<TITLE>"

# Change <USERNAME> to your database username
# Change <PASSWORD> to your database password
# Change <HOST>     to your server   IP
# Change <DATABASE> to your database name that you're created on MySql
# LABLE is optional
```

## 🚀 Running

- Installing libraries

```shell
/REST#> ls
 __pycache__/  api.http  example.env  model.py  README.md  requirements.txt  server.py  wsgi.py
/REST#> pip install -r requirements.txt
/REST#> flask run
 * Environment: production
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

## ⛓ Routes

>| Route        | Methods             | Parameter |
>| ------------ | ------------------- | --------- |
>| /            | GET                 |           |
>| /phonenumber | GET,POST,PUT,DELETE | /ID       |

## 🧪 Examples

> - GET /

```json
// Response:
{
  "Arvan": "~Sistan~"
}
```

> - GET /phonenumber

```json
// Response:
{
  "Result": [
    {
      "id": 3,
      "name": "Hasti",
      "phone": "+29346533e72894",
      "description": "This is Hasti"
    },
    {
      "id": 5,
      "name": "Mohammad",
      "phone": "+2934652894",
      "description": "This is Mohammad"
    }
  ],
  "length": 2
}
```

> - POST /phonenumber

```json
//RequestBody:
Content-Type: application/json

{
    "name":"Mohammad",
    "phone":"+2934652894",
    "description":"This is Mohammad"
}
```

```json
// Response:
{
  "staus": "OK",
  "msg": "New record created successfully",
  "name": "Mohammad",
  "phone": "+29346532894",
  "desc": "This is Mohammad"
}
```

> - PUT /phonenumber/5

```json
//RequestBody:
Content-Type: application/json

{
    "name":"MohammadJavad",
    "phone":"+1111111"
}
```

```json
// Response:
{
  "msg": "Record updated successfully",
  "status": "OK"
}
```

> - DELETE /phonenumber/5

```json
// Response:
{
  "msg": "Record removed successfully",
  "status": "Ok"
}
```

## 🚀 Running in production (with Gunicorn 🦄)

- Gunicorn is a Python WSGI HTTP Server for UNIX. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.

```shell
/REST#> pip install gunicorn
/REST#> gunicorn -w 4 --bind 0.0.0.0:5000 wsgi:app

## -w       = The number of worker processes for handling requests.
## --bind   = The flask socket to bind.
## wsgi:app = <Your application file without .py>:<Callable function in your application file>

```

- Next, create the systemd service unit file. Creating a systemd unit file will allow Ubuntu’s init system to automatically start Gunicorn and serve the Flask application whenever the server boots.

```shell
/#> sudo nano /etc/systemd/system/flask-gunicorn.service
/#> sudo chmod 755 /etc/systemd/system/flask-gunicorn.service
```

- Write blow fields on that

```yaml
[Unit]
Description=Gunicorn for serving flask app
After=network.target

[Service]
User=<yourUser>
WorkingDirectory=<path>
ExecStart=gunicorn -w 4 --bind 0.0.0.0:<port> "wsgi:app"

[Install]
WantedBy=multi-user.target

# <yourUser> = Your linux username with permission for running service
# <path>     = Path to the flask api directory
```

- Then

```shell
# Start the flask-gunicorn service:
/REST#> systemctl start flask-gunicorn
# Enable it so that it starts at boot:
/REST#> systemctl enable flask-gunicorn
# Status:
/REST#> systemctl status flask-gunicorn
```
<center>

## Good Luck 
</center>

<br>
</blockquote>
<br>
