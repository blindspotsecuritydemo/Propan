---
run_docker: To working with project start a test broker container
---

# QUICK START

Install using `pip`:

{% import 'getting_started/index/install.md' as includes with context %}
{{ includes }}

## Basic usage

Create an application with the following code at `serve.py`:

{! includes/getting_started/index/01_base.md !}

And just run it:

<div class="termy">
```console
$ propan run serve:app

2023-04-10 23:39:41,145 INFO     - Propan app starting...
2023-04-10 23:39:41,151 INFO     - `base_handler` waiting for messages
2023-04-10 23:39:41,152 INFO     - Propan app started successfully! To exit press CTRL+C
```
</div>

---

## Project template

Also, **Propan CLI** is able to generate a production-ready application template:

<div class="termy">
```console
$ propan create async [broker] [projectname]
Create Propan project template at: /home/user/projectname
```
</div>

!!! note
    Project template requires `pydantic[dotenv]` installation to run

Just run the created project:

<div class="termy">
```console
### Run broker first
$ docker compose --file [projectname]/docker-compose.yaml up -d [broker]

### Run project
$ propan run [projectname].app.serve:app --env=.env --reload

2023-04-10 23:39:41,140 INFO     - Started reloader process [115536] using WatchFiles
2023-04-10 23:39:41,145 INFO     - Propan app starting...
2023-04-10 23:39:41,151 INFO     - `base_handler` waiting for messages
2023-04-10 23:39:41,152 INFO     - Propan app started successfully! To exit press CTRL+C
```
</div>

Now you can enjoy a new development experience!

??? tip "Don't forget to stop test broker container"
    ```bash
    docker container stop test-mq
    ```
