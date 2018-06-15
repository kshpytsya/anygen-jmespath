# anygen-jmespath

A [jmespath](https://github.com/kshpytsya/anygen-jmespath) plugin for [anygen](https://github.com/kshpytsya/anygen)

Require from `some.anygen.yml`:

```
py_requires:
- anygen-jmespath
```

(Note: this is not strictly necessary, but will make `anygen` check for this plugin being installed and optionally installing it if executed from a venv)

Use from `yaql`:

```
jmespath("a", {a=>1})
```

Use in `Jinja` templates:

```
{{ data | jmespath("expr") }}
```

and

```
{% for i in jmespath("expr", data) %}
{{ i }}
{% endfor %}
```
