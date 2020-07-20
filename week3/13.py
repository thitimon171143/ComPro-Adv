<body>
    <div class="container theme-showcase" role="main">
        <div class="jumbotron">
            <h1>Guest Book</h1>
            <a type="button" class="btn btn-link" href="{{ url_for('sign') }}">Sign the Guest Book</a>
        </div>
        {% for r in result %}
        <div class="page-header">
            <h1>{{ r.name }}</h1>
        </div>
        <div class="well">
            <p>{{ r.comment }}</p>
        </div>
        {% endfor %}
    </div>
</body>