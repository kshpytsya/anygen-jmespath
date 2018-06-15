# anygen-jmespath

A [jmespath](https://github.com/kshpytsya/anygen-jmespath) plugin for [anygen](https://github.com/kshpytsya/anygen)

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
