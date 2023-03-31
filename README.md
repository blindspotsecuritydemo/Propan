<p align="center">
    <a href="https://pypi.org/project/propan" target="_blank">
        <img src="https://img.shields.io/pypi/v/propan?label=pypi%20package" alt="Package version">
    </a>
    <a href="https://pepy.tech/project/propan" target="_blank">
        <img src="https://static.pepy.tech/personalized-badge/propan?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads" alt="downloads"/>
    </a>
    <a href="https://pypi.org/project/propan" target="_blank">
        <img src="https://img.shields.io/pypi/pyversions/propan.svg" alt="Supported Python versions">
    </a>
    <a href="https://github.com/Lancetnik/Propan/blob/main/LICENSE" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/github/license/Lancetnik/Propan?color=%23007ec6">
    </a>
</p>

# Propan

Propan is a modern framework for building Applications based on <a href="https://microservices.io/patterns/communication-style/messaging.html" target="_blank">Messaging Architecture</a>.

The key features are:

* **Easy**: Designed to be easy to use and learn.
* **Intuitive**: Great editor support. Autocompletion everywhere.
* **Dependencies management**: Minimize code duplication. Multiple features from each argument and parameter declaration.
* **Greate to develop**: cli tool provides great development expireince:
    * framework-independent way to rule application environment
    * application code hot reloading

---

## Quickstart

Install using `pip`:

```shell
$ pip install "propan[async_rabbit]"
```

### Basic usage

Create an application with the following code at `serve.py`:

```python
from propan.app import PropanApp
from propan.brokers import RabbitBroker


broker = RabbitBroker("amqp://guest:guest@localhost:5672/")

app = PropanApp(broker)


@broker.handle("test")
async def base_handler(body):
    '''Handle all default exchange messages with `test` routing key'''
    print(body)
```

And just run it:

```shell
$ propan run serve:app
```

---

### Project template

Also **propan cli** is able to generate production-ready application template:

```shell
$ propan create [projectname]
```

*Notice: project template require* `pydantic[dotenv]` *installation.*

Run created project:

```shell
# Run rabbimq first
$ docker compose --file [projectname]/docker-compose.yaml up -d

# Run project
$ propan run [projectname].app.serve:app --env=.env --reload
```

Now you can enjoy a new development experience!

---

## Examples

To see more framework usages go to `examples/`

