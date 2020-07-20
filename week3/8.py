<body>
    <div class="container theme-showcase" role="main">
        <div class="jumbotron">
            <h1>Guest Book</h1>
            <a type="button" class="btn btn-link" href="{{ url_for('sign') }}">Sign the Guest Book</a>
        </div>
        <div class="page-header">
            <h1>{{ name }}</h1>
        </div>
        <div class="well">
            <p>{{ comment }}<p>
        </div>
    </div>
</body>